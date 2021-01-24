screen message_important(name, important_sentence, color = "#a0a0a0", unknown=False):
    zorder 10
    timer 5.0 action Hide("message_important")
    button:
        xysize(720, 1280)
        background "#0003"
        action Hide("message_important")
    window:
        at xslide(x_depart=-120, x_final=360)
        background "#000d"
        xalign 0.5
        if unknown:
            ypos 700
        else:
            ypos 150
        xsize 600
        vbox:
            xalign 0.5
            xsize 560
            text name:
                xalign 0.5
                yoffset 40
                color color
                size 44
                id name
            text important_sentence:
                justify True
                xalign 0.5
                yoffset 120
                size 36
                id important_sentence


screen scr_achievement_get(title, a_text, icon):
    zorder 18
    timer 6.0 action Hide("scr_achievement_get")

    button:
        action Hide("scr_achievement_get")
        at achievement_transform
        background "#000d"
        xalign 0.5
        yalign 0.9
        xysize (720, 140)
        hbox:
            xysize (600, 120)
            at truecenter
            vbox:
                yalign 0.5 xpos 20 xysize(120, 120)
                image icon at truecenter
            vbox:
                xoffset 10
                xsize 460
                text title:
                    size 34
                    id title
                text a_text:
                    size 26
                    id a_text


screen scr_conf_update(liste_persos, liste_modif):
    timer 6.0 action Hide("scr_conf_update")
    zorder 8
    vbox:
        at confiance_transform
        window:
            background "#000d" xsize 720 ysize 100
            text _("Confiance :") size 36 at truecenter
        for perso, balance in zip(liste_persos, liste_modif):            
            if balance != 0:
                $ phrase = _("a apprécié") if balance > 0 else _("n'a pas aimé")
                frame:
                    background "#000d" xsize 720 ysize 60
                    hbox xpos 120:
                        text perso["nom"] color perso["color"]
                        text phrase xoffset 20
        frame:
            background "#000d" xsize 720 ysize 30

