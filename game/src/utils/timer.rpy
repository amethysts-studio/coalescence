init -99 python in _game_runtime_setting:

    import datetime
    import threading
    import store
    from store import (
        config,
        persistent,
        Null,
        NoRollback,
        DynamicDisplayable,
        Text
    )

    """

    API doc:

        :current_runtime.TextFormat(text_format, **text_kwargs):

            It works like a normal 'Text',
            but replaces the data inside "[]" with time values
            corresponding to the current game time.

            Data will be represented by those elements
            that are present in the text.

            For example, the game time is 26 hours:

            If the query looks like: "[day] days [hour] hours.",
            it will show: "1 days 2 hours",

            And if it looks like this: "[hour] hours.",
            it will show "26 hours".

            etc.

            Available values:
                "second"
                "minute"
                "hour"
                "day"
                "week"
                "century"

        :current_runtime.strf(text_format):
            Logic is similar to the previous function, but returns a string.

        :current_runtime.Formatter(expressed_as=None, result_handler=None):

            Returns an object that has properties presented above
            in the "Available values" list.

            :expressed_as:
                Which properties to use to describe the time value.
                Read more in the description "_TimeFormatter.__init__".

            :result_handler:
                (Callable)
                Property will be called with this object, before returning.


        :current_runtime.seconds():
            Returns game time in seconds.

        :current_runtime.get_timedelta():
            Returns 'datetime.timedelta' object
            initialized with the current game time.

        #################################################################

        :total_runtime.TextFormat(text_format, **text_kwargs):
        :total_runtime.strf(text_format):
        :total_runtime.Formatter(expressed_as=None, result_handler=None):
        :total_runtime.seconds():
        :total_runtime.get_timedelta():

            Similar to the functions of the same name,
            but returns values for the total game time (for all saves).

        #################################################################

        :tformat.TextFormat(user_input, text_format, **text_kwargs):
        :tformat.strf(user_input, text_format):
        :tformat.Formatter(user_input, expressed_as=None, result_handler=None):
        :tformat.seconds(user_input):
        :tformat.get_timedelta(user_input):

            Functions are similar to those of the same name,
            but as the first argument should pass value in seconds
            (or "datetime.timedelta" object)
            with which the interaction will be performed.

    """

    class _TimeFormatter(NoRollback):

        __author__ = "Vladya"

        time_values_in_seconds = {
            "second":  (1.),  # It makes sense, doesn't it?
            "minute":  (60.),
            "hour":    (60. * 60.),
            "day":     (60. * 60. * 24.),
            "week":    (60. * 60. * 24. * 7.),
            "century": (((60. * 60. * 24.) * 365.25) * 100.)
            # Month and year do not have permanent value.
        }

        def __init__(
            self,
            time_data,
            expressed_as=None,
            _result_handler=None,
            _timer_mode="current"
        ):

            """
            :time_data:
                An initialized object of class "_PlayTimer",
                numeric value (in seconds),
                datetime.timedelta object
                or "_TimeFormatter" object.

            :expressed_as:
                Iterable object whose elements should be text time values
                in which the result will be expressed.
                (or None)

                For example:
                    (Let "time_data" be 123456789 seconds)
                    ########################################
                    expressed_as = ("second",)
                    Values will look like this:
                        century == 0
                        week    == 0
                        day     == 0
                        hour    == 0
                        minute  == 0
                        second  == 123456789
                    ########################################
                    expressed_as = ("minute", "hour")
                    Values will look like this:
                        century == 0
                        week    == 0
                        day     == 0
                        hour    == 34293
                        minute  == 33.15
                        second  == 0
                    ########################################
                    expressed_as = ("week", "day")
                    Values will look like this:
                        century == 0
                        week    == 204
                        day     == 0.9
                        hour    == 0
                        minute  == 0
                        second  == 0
                    ########################################
                    expressed_as = None
                    Values will look like this:
                        century == 0
                        week    == 204
                        day     == 0
                        hour    == 21
                        minute  == 33
                        second  == 9
                    etc.
            :_result_handler:
                Callable object or None.
                If callable, this will be called for the returned value.
                If None, value will be adapted to the situation.
            :_timer_mode:
                It is used only if "time_data" is "_PlayTimer" instance.
                Can take two values: "current" and "total".
                if _timer_mode == "current":
                    The time value for the current playthrough will be used.
                if _timer_mode == "total":
                    The common time for all games will be used.
            """

            self.__timer_mode = None
            if isinstance(time_data, _PlayTimer):
                self.__time_data = time_data
                if _timer_mode is None:
                    _timer_mode = "current"
                if _timer_mode not in ("current", "total"):
                    raise ValueError("Incorrect '_timer_mode' value.")
                self.__timer_mode = _timer_mode
            elif isinstance(time_data, datetime.timedelta):
                self.__time_data = time_data.total_seconds()
            elif isinstance(time_data, _TimeFormatter):
                self.__time_data = time_data._get_timedata_object()
            else:
                self.__time_data = float(time_data)

            self._set_expressed_as(expressed_as)

            if not ((_result_handler is None) or callable(_result_handler)):
                raise ValueError("Incorrect '_result_handler' value.")
            self.__result_handler = _result_handler

        def __getstate__(self):
            return {
                "time_data": self.__time_data,
                "expressed_as": self.__expressed_as,
                "_timer_mode": self.__timer_mode
            }

        def __setstate__(self, init_kwargs):
            self.__init__(**init_kwargs)

        @staticmethod
        def _default_handler(value):
            value = float(value)
            if value.is_integer():
                return int(value)
            return round(value, 2)

        @property
        def total_seconds(self):
            if isinstance(self.__time_data, _PlayTimer):
                self.__time_data._update_time(True)
                if self.__timer_mode == "current":
                    delta = self.__time_data._total_playtime_current
                else:
                    delta = self.__time_data._total_playtime_global
                return delta.total_seconds()
            return self.__time_data

        @property
        def timedelta(self):
            return datetime.timedelta(seconds=self.total_seconds)

        def _get_timedata_object(self):
            return self.__time_data

        def _set_expressed_as(self, new_expressed_as):

            if new_expressed_as is None:
                new_expressed_as = self.time_values_in_seconds.iterkeys()

            new_expressed_as = frozenset(
                map(lambda x: x.strip().lower(), new_expressed_as)
            )

            for value in new_expressed_as:
                if value not in self.time_values_in_seconds:
                    raise ValueError("{0} is incorrect value.".format(value))

            self.__expressed_as = new_expressed_as

        def __contains__(self, key):
            if key in self.time_values_in_seconds:
                return True
            return False

        def __getitem__(self, key):
            if key not in self:
                raise KeyError(key)
            value = self._get_value(key)
            _handler = (self.__result_handler or self._default_handler)
            return _handler(value)

        def __getattr__(self, name):

            try:
                value = self.__getitem__(name)
            except KeyError as ex:
                raise AttributeError(*ex.args)
            else:
                return value

        def _get_value(self, name):

            assert (name in self)
            if name not in self.__expressed_as:
                return .0

            _as_dict = dict(
                map(
                    lambda val: (val, self.time_values_in_seconds[val]),
                    self.__expressed_as
                )
            )
            values = tuple(sorted(_as_dict.iteritems(), key=lambda x: x[-1]))

            _size = len(values)
            min_unit = None
            for i, (current_unit, in_seconds) in enumerate(values):

                if min_unit is None:
                    min_unit = current_unit

                if current_unit == name:

                    next_unit = next_unit_in_seconds = None
                    if i < (_size - 1):
                        next_unit, next_unit_in_seconds = values[(i + 1)]

                    result = self.total_seconds
                    if next_unit is not None:
                        result %= next_unit_in_seconds

                    if current_unit == min_unit:
                        result /= in_seconds
                    else:
                        result //= in_seconds

                    return result

            raise Exception("Unknown error.")

    class _PlayTimer(Null, NoRollback):

        __author__ = "Vladya"

        _json_value_name = "game_runtime_save_value"
        _persistent_value_name = "total_game_runtime_value"

        single_instance = None

        def __new__(cls):
            if cls.single_instance is None:
                cls.single_instance = super(_PlayTimer, cls).__new__(cls)
                cls.single_instance._already_init = False
            return cls.single_instance

        def __init__(self):

            if self._already_init:
                return

            super(_PlayTimer, self).__init__()
            self.reset_time()
            self.__update_lock = threading.Lock()
            self.__last_update_persistent = None
            self._already_init = True
            self._is_enabled = False

        def __getstate__(self):
            #  This is not necessary for a singleton.
            return None

        def __setstate__(self, value):
            self.__init__()

        @property
        def _total_playtime_global(self):
            """
            Not only for a specific save.
            """
            if getattr(persistent, self._persistent_value_name) is None:
                _start_delta = datetime.timedelta(seconds=.0)
                setattr(persistent, self._persistent_value_name, _start_delta)
            return getattr(persistent, self._persistent_value_name)

        @_total_playtime_global.setter
        def _total_playtime_global(self, new_playtime):
            setattr(persistent, self._persistent_value_name, new_playtime)

        @property
        def _total_playtime_current(self):
            """
            For a specific save.
            """
            return self.__current_store_runtime

        @classmethod
        def turn_on(cls):

            assert renpy.is_init_phase()
            timer_object = cls()
            if timer_object._is_enabled:
                return

            config.start_callbacks.append(timer_object.reset_time)
            config.save_json_callbacks.append(timer_object._save_callback)
            config.overlay_functions.append(timer_object._add)

            timer_object._create_api()

            # Decorate 'renpy.load' so that it loads time from the save file.
            renpy.load = timer_object._load_func_decorator(renpy.load)

            timer_object._is_enabled = True

        def _create_api(self):

            stores = {
                "current_runtime": "current",
                "total_runtime": "total",
                "tformat": "user_input"
            }

            def _get_mode_decorator(mode):
                def _mode_decorator(func):
                    if mode == "user_input":
                        def _new_func(user_input, *args, **kwargs):
                            return func(mode, user_input, *args, **kwargs)
                    else:
                        def _new_func(*args, **kwargs):
                            return func(mode, None, *args, **kwargs)
                    _new_func.__doc__ = func.__doc__
                    return _new_func
                return _mode_decorator

            for store_name, mode_name in stores.iteritems():
                store_name = "store.{0}".format(store_name)
                renpy.ast.create_store(store_name)
                namespace, _special = renpy.ast.get_namespace(store_name)
                _decorator = _get_mode_decorator(mode_name)

                namespace.set("TextFormat", _decorator(self._get_dynamic_text))
                namespace.set("strf", _decorator(self._substitute))
                namespace.set("Formatter", _decorator(self._get_formatter))
                namespace.set("seconds", _decorator(self._get_total_seconds))
                namespace.set("get_timedelta", _decorator(self._get_timedelta))

        def reset_time(self):
            self.__current_store_runtime = datetime.timedelta(seconds=.0)
            self.__last_update_time = None

        def _save_callback(self, save_dict):
            self._update_time(True)
            _runtime_in_sec = self.__current_store_runtime.total_seconds()
            save_dict[self._json_value_name] = _runtime_in_sec

        def _load_func_decorator(self, function):

            def _new_func(filename):
                _json_dict = renpy.slot_json(filename)
                if _json_dict:
                    value = _json_dict.get(self._json_value_name, .0)
                    self.__current_store_runtime = datetime.timedelta(
                        seconds=value
                    )
                    self.__last_update_time = None
                return function(filename)

            _new_func.__doc__ = function.__doc__

            return _new_func

        # API methods. #####################################################

        def _get_formatter(
            self,
            mode,
            user_input,
            expressed_as=None,
            result_handler=None
        ):
            # API name: 'Formatter'
            if mode == "user_input":
                return _TimeFormatter(user_input, expressed_as, result_handler)
            return _TimeFormatter(self, expressed_as, result_handler, mode)

        def _get_total_seconds(self, mode, user_input):
            # API name: 'seconds'
            _formatter = self._get_formatter(mode, user_input)
            return _formatter.total_seconds

        def _get_timedelta(self, mode, user_input):
            # API name: 'get_timedelta'
            _formatter = self._get_formatter(mode, user_input)
            return _formatter.timedelta

        def _get_time_formatter_for_text(self, mode, user_input, text_format):
            # API function without name.
            values = set()
            for val in renpy.substitutions.formatter.parse(text_format):
                _literal, value, _format, _conversion = val
                if value is None:
                    continue
                if value in _TimeFormatter.time_values_in_seconds:
                    values.add(value)

            return self._get_formatter(mode, user_input, values)

        def _substitute(self, mode, user_input, text_format):
            # API name: 'strf'
            scope = self._get_time_formatter_for_text(
                mode,
                user_input,
                text_format
            )
            result = renpy.substitutions.substitute(
                text_format,
                scope=scope,
                force=True
            )
            if isinstance(result, basestring):
                return result
            return result[0]

        def _get_dynamic_text(self, mode, user_input, text_format, **kwargs):
            # API name: 'TextFormat'
            scope = self._get_time_formatter_for_text(
                mode,
                user_input,
                text_format
            )

            if kwargs.get("scope", None) is not None:
                scope = renpy.substitutions.MultipleDict(
                    scope,
                    kwargs["scope"],
                    store.__dict__
                )
            kwargs.update({"scope": scope, "substitute": True})

            def _f(*_args, **_kwargs):
                return (Text(text_format, **kwargs), .0)

            return DynamicDisplayable(_f)

        # ##################################################################

        def _add(self):
            ui.add(self)

        def _update_time(self, force=False):

            with self.__update_lock:

                _current = datetime.datetime.today()

                if self.__last_update_time:
                    _delta = _current - self.__last_update_time
                    self.__current_store_runtime += _delta
                self.__last_update_time = _current

                if self.__last_update_persistent:
                    _delta = _current - self.__last_update_persistent
                    if (_delta.total_seconds() < 5.) and (not force):
                        # Overwriting persistent is an expensive operation,
                        # as the hard disk is being accessed.
                        return
                    self._total_playtime_global += _delta
                self.__last_update_persistent = _current

        def render(self, *args, **kwargs):
            self._update_time()
            renpy.redraw(self, .0)
            return super(_PlayTimer, self).render(*args, **kwargs)

    _PlayTimer.turn_on()

