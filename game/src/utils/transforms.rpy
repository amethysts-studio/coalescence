transform xslide(x_depart=-120, x_final=60, time=0.5):
    on show:
        xpos x_depart
        alpha 0.0
        linear time xpos x_final alpha 1.0
    on hide:
        linear time xpos (360-x_depart) alpha 0.0

transform yslide(y_depart=-120, y_final=60, time=0.5):
    on show:
        ypos y_depart
        alpha 0.0
        time 0.2
        alpha 0.2
        linear time ypos y_final alpha 1.0
    on hide:
        linear time ypos y_depart alpha 0.2
        alpha 0.0

transform special_confirm_newgame():
    on show:
        alpha 0.0
        ypos -100 alpha 0.0
        linear 0.2 ypos 100 alpha 1.0
        linear 0.5 ypos 500
    on hide:
        linear 0.5 ypos 100 
        linear 0.2 ypos -100 alpha 0.0

transform fade_away(time = 1.0):
    on show:
        alpha 0.0
        linear time alpha 1.0
    on hide:
        linear time alpha 0.0

transform transition_resultat(time=0.5):
    on show:
        alpha 0.0
        time time
        linear 0.2 alpha 1.0
    on hide:
        linear 0.5 alpha 0.0

transform achievement_transform:
    on show:
        xalign 0.5
        yalign -0.1
        alpha 0.0
        easein 2.0 xalign 0.5 yalign 0.45 alpha 1.0
    on hide:
        easeout 1.0 xalign 0.5 yalign 1.1 alpha -0.3
        
transform going_up(zfinal=0):
    on show:
        ypos 1280
        linear 0.5 ypos zfinal
    on hide:
        linear 0.5 ypos -1280

transform scary_zoom:
    on show:
        alpha 0.0
        time 2.5
        linear 0.5 zoom 1.2 alpha 0.8
        linear 0.5 zoom 3.0 alpha 0.0
    on hide:
        linear 0.5 zoom 3.0 alpha 0.0

transform transform_suspense_vote:
    on show:
        xpos 1020
        alpha 0.5
        linear 6.0 xpos 360 alpha 1.0
    on hide:
        linear 2.0 xpos (-600) alpha 0.0

transform confiance_transform:
    on show:
        ypos -500
        alpha 0.0
        easein 2.0 xalign 0.5 ypos 0 alpha 1.0
    on hide:
        easeout 2.0 xalign 0.5 ypos -500 alpha 0.0

transform smooth_title(time = 0.5, transp = 0.5, dist_y = 60):
    on show:
        alpha -transp
        ypos 0
        easein time ypos dist_y alpha transp
    on hide:
        easeout time ypos 0 alpha -transp

transform smooth_main_title(time = 0.5, transp = 0.5, dist_y = 60):
    on show:
        ypos dist_y
        alpha transp
    on hide:
        easeout time ypos 0 alpha -transp

transform smooth(time=0.5, alpha_max=1.0):
    on show:
        alpha 0.0
        linear time alpha alpha_max
    on hide:
        linear time alpha 0.0

transform defiler(alpha_mini = 0.3, alpha_maxi = 1.0):
    on show:
        alpha 0.0
        xpos 0
        ypos -2560 #hauteur = 1280
        linear 3.0 alpha alpha_maxi ypos -2432
        linear 27.0 ypos -1280
        block:
            linear 30.0 ypos 0 alpha alpha_mini
            ypos -2560
            linear 30.0 ypos -1280 alpha alpha_maxi
            repeat
    on hide:
        linear 3.0 alpha 0.0

transform briller:
    alpha 0.0
    ease 5.0 alpha 0.25
    ease 5.0 alpha 0.0
    repeat

transform message_transform:
    on show:
        alpha 0.0
        easein 0.15 alpha 1.0
    on hide:
        easeout 0.3 alpha -0.3