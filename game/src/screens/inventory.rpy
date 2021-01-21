screen inventaire(acte=0, situation = "menu_principal"):
    zorder 12
    style_prefix "coal"
    key "rollback" action [Hide("inventaire"), Show("in_game_menu", acte=acte)]
    window:
        at xslide(x_depart=720, x_final=360)
        ypos 400
        hbox:
            image "icons/icon_items.png"
            text _("Inventaire") size 42 xoffset 40 yalign 0.5
    button:
        at xslide(x_depart=-120, x_final=360)
        ypos 500
        if inventaire["usb_key"]["connu"]:
            text "Clé USB" xoffset 40 yalign 0.5
            action [Hide("inventaire"), Show("inventory_item", acte=acte, situation=situation, item="usb_key")]
        else:
            text "???" color "#888" xoffset 40 yalign 0.5

    button:
        at xslide(x_depart=720, x_final=360)
        ypos 600
        if inventaire["lampe"]["connu"]:
            hbox:
                yalign 0.5
                text "Lampe torche : " xoffset 40 yalign 0.5
                bar value StaticValue(inventaire["battery"]["nb"], 100) ysize 12 xsize 200 xoffset 40 yalign 0.5
                text " "+str(inventaire["battery"]["nb"])+"%" xoffset 60
            action [Hide("inventaire"), Show("inventory_item", acte=acte, situation=situation, item="lampe")]
        else:
            text "???" color "#888" xoffset 40 yalign 0.5

    button:
        at xslide(x_depart=-120, x_final=360)
        ypos 700
        if inventaire["knife"]["connu"]:
            text "Couteau : "+str(inventaire["knife"]["nb"])+"/1" xoffset 40 yalign 0.5
            action [Hide("inventaire"), Show("inventory_item", acte=acte, situation=situation, item="knife")]
        else:
            text "???" color "#888" xoffset 40 yalign 0.5

    button:
        at xslide(x_depart=720, x_final=360)
        ypos 800
        if inventaire["poison"]["connu"]:
            text "Fiole de poison : "+str(inventaire["poison"]["nb"])+"/1" xoffset 40 yalign 0.5
            action [Hide("inventaire"), Show("inventory_item", acte=acte, situation=situation, item="poison")]
        else:
            text "???" color "#888" xoffset 40 yalign 0.5
    button:
        at xslide(x_depart=720, x_final=360)
        ypos 900
        if inventaire["mp3"]["connu"]:
            text "mp3" xoffset 40 yalign 0.5
            action [Hide("inventaire"), Show("inventory_item", acte=acte, situation=situation, item="mp3")]
        else:
            text "???" color "#888" xoffset 40 yalign 0.5
    
    button:
        at xslide(x_depart=-120, x_final=360)
        xysize (600, 94) ypos 1000
        text "Retour" at truecenter
        action [Hide("inventaire"), Show("in_game_menu", acte=acte)]


screen inventory_item(acte=0, situation = "menu_principal", item):
    zorder 12
    style_prefix "coal"
    key "rollback" action [Hide("inventory_item"), Show("inventaire", acte=acte, situation = situation)]
    window:
        at xslide(x_depart=720, x_final=360)
        xysize (600,96) ypos 400
        hbox:
            image "icons/icon_items.png"
            text inventaire[item]["title"] size 42 xoffset 40 yalign 0.5
    window:
        at xslide(x_depart=-120, x_final=360)
        if inventaire[item]["nb"] >= 1:
            xysize (600, 514)
        else:
            xysize (600, 614)
    
        ypos 500
        vbox:
            align (0.5,0.5)
            if inventaire[item]["nb"] >= 1:
                xysize (560, 474)
            else:
                xysize (560, 574)
            text inventaire[item]["text"]
    if inventaire[item]["nb"] >= 1:
        button:
            at xslide(x_depart=720, x_final=360)
            xysize (600, 94) ypos 1020
            text inventaire[item]["act_word"] at truecenter
            if item == "mp3":
                action [Play("music", "music/kingofthedead.ogg", loop=False), Show("inventory_item_detail", acte=acte, situation = situation, item=item)]
            action [Show("inventory_item_detail", acte=acte, situation = situation, item=item)]
    button:
        at xslide(x_depart=-120, x_final=360)
        xysize (600, 94) ypos 1120
        text "Retour" at truecenter
        action [Hide("inventory_item"), Show("inventaire", acte=acte, situation = situation)]


screen inventory_item_detail(acte=0, situation = "menu_principal", item):
    zorder 20
    style_prefix "coal"
    key "rollback" action [Hide("inventory_item_detail"), Show("inventory_item", acte=acte, situation = situation, item=item)]
    button:
        at smooth()
        background "#000f"
        xysize (600, 614) ypos 500
        action NullAction()
    window:
        at smooth()
        xysize (600, 594) ypos 500
        vbox:
            align (0.5,0.5)
            xysize (560, 564)
            text inventaire[item]["text_inspect"]
    button:
        xysize (600, 94) ypos 1120
        text "Retour" at truecenter
        action [Hide("inventory_item_detail"), Show("inventory_item", acte=acte, situation = situation, item=item)]
