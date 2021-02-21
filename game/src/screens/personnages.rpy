screen liste_personnages(liste_persos=liste_persos, acte=0, situation = "en_vote"):
    zorder 12
    style_prefix "coal"
    if situation == "en_vote":
        window:
            at xslide(x_depart=720, x_final=360)
            xysize (600,97) ypos 400 xalign 0.5
            hbox:
                image "icons/icon_persos.png"
                text _("Votez") size 42 xoffset 100 yalign 0.5
    else:
        window:
            at xslide(x_depart=720, x_final=360)
            xysize (600,97) ypos 400 xalign 0.5
            hbox:
                image "icons/icon_persos.png"
                text _("Personnages") size 42 xoffset 100 yalign 0.5

    viewport:
        at xslide(x_depart=-120, x_final=360)
        if situation == "en_vote":
            xysize (600, 697)
        else:
            xysize (600, 597)
        xalign 0.5 ypos 500
        draggable True
        mousewheel True
        scrollbars "vertical"
        vbox:
            for i in liste_persos:
                if i["statut"][:7] != "Inconnu" and (i["statut"][:6]=="Vivant"):
                    window:
                        xysize (580, 100) ymargin 2
                        text i["nom"] color i["color"] xpos 40
                        button:
                            xysize(160, 60) xpos 450 yalign 0.5
                            idle_background "#5555"
                            if situation == "en_vote" and (i in persos_joueurs) and (i["statut"][:6]=="Vivant"):
                                text _("Choisir") at truecenter
                            else:
                                text _("Infos") at truecenter
                            action [Hide("liste_personnages"), Hide("menu_title_coal"), Show("bio_perso", transition=None, perso=i, situation=situation, acte=acte)]
            for i in liste_persos:
                if i["statut"][:7] != "Inconnu" and not (i["statut"][:6]=="Vivant"):
                    window:
                        xysize (580, 100) ymargin 2
                        if i["statut"][:4] == "Mort":
                            image "icons/icon_skullhead.png" xpos 50 alpha 0.2
                            text i["nom"] color "#aaa" italic True xpos 40 #strikethrough True
                        else:
                            text i["nom"] color i["color"] xpos 40
                        button:
                            xysize(160, 60) xpos 450 yalign 0.5
                            idle_background "#5555"
                            if situation == "en_vote" and (i in persos_joueurs) and (i["statut"][:6]=="Vivant"):
                                text _("Choisir") at truecenter
                            else:
                                text _("Infos") at truecenter
                            action [Hide("liste_personnages"), Hide("menu_title_coal"), Show("bio_perso", transition=None, perso=i, situation=situation, acte=acte)]
                        #hbox:
                        #    xpos 300 xysize(250, 96)
                        #    if i["statut"][:4] == "Mort":
                        #        text i["statut"][:5] color "#aaa" italic True yalign 0.5
                        #    elif i["nom"] in ["Bourreau", "Klaus", "Rossignol"] and situation == "en_vote":
                        #        text "Vote impossible" color "#aaa" italic True yalign 0.5
                        #    elif i["nom"] not in ["Bourreau", "Kurt", "Klaus", "Rossignol"]:
                        #        bar value StaticValue(i["confiance"], 20) ysize 12 xsize 200 yalign 0.5
                            
    if situation != "en_vote":
        button:
            at xslide(x_depart=720, x_final=360)
            ypos 1100
            text _("Retour") at truecenter
            action [Hide("liste_personnages"), Show("in_game_menu", acte=acte)]

#=========================================================   Persos   =============================================================================================
screen bio_perso(perso, situation, acte=0):
    zorder 12
    style_prefix "coalbio"

    add perso["image"] alpha 0.5 at smooth(1.0)

    if perso["statut"][:4] == "Mort":
        fixed:
            at smooth(1.0)
            add "right_eye" xpos perso['eyes']['right'][0] ypos perso['eyes']['right'][1] anchor (50, 50)
            add "left_eye"  xpos perso['eyes']['left'][0]  ypos perso['eyes']['left'][1] anchor (50, 50)
            add "fondacte/frame_dead.png" alpha 0.6
    window:
        at smooth_title(time = 1.0, transp = 1.0, dist_y = 60)
        xysize (600, 94) xalign 0.5 ypos 60
        hbox:
            at truecenter
            text "- " color perso["color"] size 48
            text perso["nom"] size 48
            text " -" color perso["color"] size 48
    window:
        at xslide(x_depart=720, x_final=360)
        xysize (600, 94) xalign 0.5 ypos 620
        vbox:
            at truecenter
            if perso in persos_joueurs:
                hbox:
                    xalign 0.5
                    text str(perso["age"])
                    text _(" ans - ")
                    text perso["situation"]
            else:
                text "???" xalign 0.5
            text perso["adjectifs"] xalign 0.5
            #if perso["nom"] not in ["Bourreau", "Kurt", "Klaus"]:
            #    text "Relations : "+get_qualificatif(perso["confiance"]) xalign 0.5
    
    window:
        at xslide(x_depart=-120, x_final=360)
        xysize (600, 394)
        xalign 0.5
        ypos 720
        viewport:
            xysize (580, 394) xpos 20
            draggable True
            mousewheel True
            scrollbars "vertical"
            vbox:
                text ""
                for doublet in perso["bio"]:
                    if doublet[0]: #partie de la bio évolutive disponible ?
                        text doublet[1] #si oui, on l'affiche
                        text "" # petit espace bienvenu pour mieux voir
    if situation == "en_vote" and perso["statut"][:6] == "Vivant":
        hbox:
            pos (60,1120) at xslide(x_depart=720, x_final=60)
            button:
                at message_transform
                xysize (294, 100)
                action [SetVariable('perso', perso), Show("confirm_vote", transition=None, perso=perso)]
                text _("Voter") at truecenter

            button:
                at message_transform
                xoffset 4
                xysize (298, 100)
                action [Hide('bio_perso'), Show("menu_title_coal"), Show("liste_personnages", transition=None, acte=acte, situation = situation)]
                text _("Retour") at truecenter
    else:
        button:
            at xslide(x_depart=720, x_final=360)
            ypos 1120
            xysize (600, 100)
            xalign 0.5
            text _("Retour") at truecenter
            action [Hide('bio_perso'), Show("menu_title_coal"), Show("liste_personnages", transition=None, acte=acte, situation = situation)]

screen confirm_vote(perso):
    zorder 20
    style_prefix "coalconfirm"
    button:
        background "#0000"
        xysize(720, 1280) pos(360, 0)
        action NullAction()
    window:
        xysize (600, 94) xalign 0.5 ypos 60
        hbox:
            at truecenter
            text "- " color perso["color"] size 48
            text perso["nom"] size 48
            text " -" color perso["color"] size 48
    window:
        at smooth(0.2)
        xysize(720, 1126) pos(360, 154)
        image "horror/skullheadVote.jpg" alpha 0.05
    window:
        at smooth(0.2)
        xysize(60, 94) pos(30, 60)
    window:
        at smooth(0.2)
        xysize(60, 94) pos(690, 60)
    window:
        at smooth(0.2)
        xysize(720, 60) pos(360, 0)
    window:
        at xslide(x_depart=-120, x_final=360, time = 0.5)
        xysize (540, 108)
        ypos 530
        text _("Êtes-vous sûr ?") size 32 at truecenter
    hbox:
        pos (120,650)# at smooth(0.5)
        at xslide(x_depart=720, x_final=90, time = 0.5)
        button:
            xysize (264, 100)
            text _("Confirmer") at truecenter
            action [Hide('bio_perso'), Hide('confirm_vote'), Hide('menu_background'), Jump("resultatsvote")]
        button:
            xysize (264, 100) xoffset 12
            text _("Annuler") at truecenter
            action Hide('confirm_vote')



screen vote_details(liste_elus, liste_persos=liste_persos):
    zorder 12
    style_prefix "coal"
    window:
        at smooth(time=0.05)
        xysize (600, 96)
        xalign 0.5 ypos 400
        text "Votes :" xalign 0.5
    frame:
        at going_up(zfinal=500)
        background "#0000"
        ysize 716
        vbox:
            spacing 6
            for i in liste_persos:
                if i["statut"][:6] == "Vivant":
                    window:
                        text i["nom"] color i["color"] xpos 30 yalign 0.5
                        text str(votes[i["nom"].lower()]) xpos 450
                        if i["nom"].lower() in liste_elus:
                            image "icons/icon_skullhead.png" xpos 490 yoffset -8
                            
                            
    button:
        at smooth(time=2.0)
        xysize (600, 100)
        xalign 0.5 ypos 1120
        text _("Continuer") at truecenter
        action [Hide("vote_details"), Return()]

screen vote_results(liste_elus):
    zorder 12
    style_prefix "coal"
    window:
        background "#0000"
        image "horror/skullheadMouth.jpg"
        at scary_zoom
    window:
        at smooth(time=0.05)
        xysize (600, 96)
        xalign 0.5 ypos 400
        text _("Élus :") at truecenter
    window:
        at transition_resultat(time=2.5)
        background "#0000"
        ysize 716 ypos 500
        vbox:
            spacing 20
            for i in liste_elus:
                window:
                    text i.capitalize() color (str_to_perso(liste_persos, i)["color"]) size 36 xpos 50
                        
    hbox:
        pos (60,1120) at smooth(0.5)
        button:
            xysize (294, 100)
            text _("Détails") at truecenter
            action [Hide("vote_results"), Show("vote_details", transition=None, liste_elus=liste_elus)]
                            
        button:
            xysize (294, 100) xoffset 12
            text _("Continuer") at truecenter
            action [Hide("vote_results"), Return()]