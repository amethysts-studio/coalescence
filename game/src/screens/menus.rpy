screen menu_background():
    zorder 10
    button:
        xysize (720, 1280) at fade_away(0.5)
        image "fondacte/fondfinacte.png"
        action NullAction()
screen menu_title_coal(time = 0.5, initi=False, red=False):
    zorder 11
    default texte = "Coalescence "+config.version
    if red:
        add "fondacte/frame_red.png":
            at smooth_title(time = 1.5, transp = 0.5, dist_y = 0)
            alpha 0.8
    else:
        add "fondacte/frame.png":
            at smooth_title(time = 1.5, transp = 0.5, dist_y = 0)
            alpha 0.8
    button:
        xysize(600,300)
        xpos 65 ypos 80
        if initi:
            at smooth_main_title(time = time, transp = 1.0, dist_y = 80)
        else:
            at smooth_title(time = time, transp = 1.0, dist_y = 80)
        image "Ecran titre/title_coal_reduit.png" at truecenter
        if texte == "Coalescence "+config.version:
            action SetScreenVariable("texte", "CXVL"+romain(persistent.jeu_actuel))
        else:
            action SetScreenVariable("texte", "Coalescence "+config.version)
    text texte xalign 0.5 ypos 1250 color "#444" size 24

screen in_game_menu(acte=0, dico_info=persistent.sauvegarde_info):
    style_prefix "coal"
    zorder 12
    key "rollback" action [Hide("in_game_menu"), Hide("menu_background"), Hide("menu_title_coal"), SetVariable('quick_menu', True)]
    window:
        at fade_away()
        ypos 400
        background "#0000"
        text _("- partie en cours -") italic True color "#2b2" xalign 0.5
    if acte == 0:
        button:
            at xslide(x_depart=-120, x_final=360)
            ypos 500
            action [Hide("in_game_menu"), Hide("menu_background"), Hide("menu_title_coal"), SetVariable('quick_menu', True)]
            hbox:
                image "icons/icon_play.png"
                text _("Reprendre") xpos 50
    else:
        button:
            at xslide(x_depart=-120, x_final=360)
            ypos 500
            action [Hide("in_game_menu"), Hide("menu_background"), Hide("menu_title_coal"), SetVariable('quick_menu', True), Jump("acte"+str(acte+1))]
            hbox:
                image "icons/icon_play.png"
                text _("Passer à l'acte suivant") xpos 50

    hbox:
        at xslide(x_depart=720, x_final=60)
        pos (60,700)
        button:
            xsize 298
            action [Hide("in_game_menu"), Show("liste_personnages", transition=None, acte=acte, situation = "in_game_menu")]
            hbox:
                image "icons/icon_persos.png"
                text _("Sujets") xoffset 15
        if plan_available:
            button:
                xsize 298 xoffset 4
                action [Hide("in_game_menu"), Hide("menu_title_coal"), Show("carte", transition=None, acte=acte, revelee=False)]
                hbox:
                    image "icons/icon_map.png"
                    text _("Carte") xoffset 30
        else:
            window:
                xsize 298 xoffset 4
                hbox:
                    image "icons/icon_map.png"
                    text _("Carte") xoffset 30 color "#888"

    hbox:
        at xslide(x_depart=-120, x_final=60)
        pos (60,800)
        button:
            xsize 298
            action [Hide("in_game_menu"), Show("inventaire", acte=acte)]
            hbox:
                image "icons/icon_items.png"
                text _("Objets") xoffset 15
        button:
            xsize 298 xoffset 4
            action [Hide("in_game_menu"), Show("recap", acte=acte)]
            hbox:
                image "icons/icon_recap.png"
                text _("Résumé") xoffset 30
    

    hbox:
        at xslide(x_depart=720, x_final=60)
        pos (60,1000)
        button:
            xsize 298
            action [Hide("in_game_menu"), Jump("menu_principal")]
            hbox:
                image "icons/icon_menu.png"
                text _("Quitter") xoffset 30
        button:
            xsize 298 xoffset 4
            action [Hide("in_game_menu"), Show("plus_de_menus", transition=None, acte=acte, situation = "in_game_menu")]
            hbox:
                image "icons/icon_bonus.png"
                text _("Plus") xoffset 30

#=========================================================================================================================
screen confirm_newgame(dico_info=persistent.sauvegarde_info):
    $ continue_acte = persistent.sauvegarde_info["continuer"][0]
    style_prefix "coal"
    zorder 20
    key "rollback" action Hide("confirm_newgame")
    button:
        at smooth()
        ysize 600 ypos 500 hover_background "#0000"
        action NullAction()
    window:
        ysize 396 background "#000f"
        at special_confirm_newgame()
        vbox:
            pos (20, 20) xysize (560, 356)
            text _("Attention, si vous commencez un nouveau jeu, la partie en cours sera oubliée.\n") size 28
            text _("Êtes-vous sûr de vouloir commencer un nouveau Jeu ?\n") size 28
            text _("Les succès et la plupart des éléments 'débloqués' seront conservés.") size 28
    button:
        at yslide(500, 900, 0.5)
        action [Hide("menu_alternatif"), Hide("confirm_newgame"), Hide("menu_background"), Hide("menu_title_coal"), Jump("initialisation_debut_partie")]
        hbox:
            image "icons/icon_play.png"
            text _("Nouveau Jeu") xpos 50 yalign 0.5
    button:
        at yslide(600, 1000, 0.5)
        action [Hide("menu_alternatif"), Jump("charger_partie")]
        hbox:
            yalign 0.5
            image "icons/icon_resume.png"
            vbox:
                xpos 50 ypos 10
                hbox: 
                    ysize 38 
                    text _("Continuer l'acte ") 
                    text romain(continue_acte)
                hbox:
                    ysize 38
                    text _("(Partie du ")
                    text (persistent.sauvegarde_info["continuer"][1])+")" xalign 0.0 yalign 0.5
    button:
        ypos 1100
        at smooth()
        text _("Retour") at truecenter
        action Hide("confirm_newgame")

screen menu_alternatif(dico_info=persistent.sauvegarde_info,):
    $ continue_acte = persistent.sauvegarde_info["continuer"][0]
    style_prefix "coal"
    zorder 12
    button:
        at fade_away()
        ypos 500
        if continue_acte != 0 and (persistent.loadable) != False:
            action Show("confirm_newgame")
        else:
            action [Hide("menu_alternatif"), Hide("menu_background"), Hide("menu_title_coal"), Jump("initialisation_debut_partie")]
        hbox:
            image "icons/icon_play.png"
            text _("Nouveau Jeu") xpos 50 yalign 0.5 
    if continue_acte != 0 and (persistent.loadable) != False:
        button:
            at fade_away()
            ypos 600 ysize 120
            action [Hide("menu_alternatif"), Jump("charger_partie")]
            hbox:
                yalign 0.5
                image "icons/icon_resume.png"
                vbox:
                    xpos 50 yalign 0.5
                    hbox: 
                        ysize 38
                        text _("Continuer l'acte ")
                        text romain(continue_acte)
                    hbox:
                        ysize 38
                        text _("(Partie du ")
                        text (persistent.sauvegarde_info["continuer"][1])+")" xalign 0.0 yalign 0.5

    hbox:
        pos (60,800)
        at fade_away()
        button:
            xysize (298, 96)
            action If(_preferences.language == "english",
                    true = Language(None),
                    false = Language("english"))
            hbox:
                at truecenter
                if _preferences.language == None:
                    image "icons/fr.png" yalign 0.5
                    text "     " yalign 0.5
                    image "icons/gb.png" yalign 0.5 alpha 0.3
                elif _preferences.language == "english":
                    image "icons/fr.png" yalign 0.5 alpha 0.3
                    text "     " yalign 0.5
                    image "icons/gb.png" yalign 0.5 
        button:
            xysize (298, 96)
            xoffset 4
            action [Hide("menu_alternatif"), Show("plus_de_menus", transition=None, situation = "menu_principal")]
            hbox:
                image "icons/icon_bonus.png"
                text _("Plus") xoffset 30 yalign 0.5

#=========================================================================================================================
screen plus_de_menus(acte=0, situation = "menu_principal"):
    zorder 12
    style_prefix "coal"
    if situation == "menu_principal":
        key "rollback" action [Hide("plus_de_menus"), Show("menu_alternatif")]
    else:
        key "rollback" action [Hide("plus_de_menus"), Show("in_game_menu", acte=acte)]
    window:
        at xslide(x_depart=720, x_final=360)
        xysize (600,96)
        ypos 400
        xalign 0.5
        hbox:
            image "icons/icon_bonus.png"
            text _("Plus") size 42 xoffset 40 yalign 0.5
    hbox:
        at xslide(x_depart=-120, x_final=60)
        pos (60,500)
        button:
            xysize (298, 96)
            action [Hide("plus_de_menus"), Show("affiche_succes", transition=None, acte=acte, obtenu=compte_succes(), total=len((persistent.achievements_dict)), situation = situation)]
            hbox:
                image "icons/icon_success.png"
                text _("Succès") xoffset 30 yalign 0.5
        button:
            xysize (298, 96)
            xoffset 4
            action [Hide("plus_de_menus"), Show("affiche_fins", transition=None, acte=acte, obtenu=compte_fins(), total=len((persistent.fins)), situation = situation)]
            hbox:
                image "icons/icon_cxvl.png"
                text _("Fins") xoffset 30 yalign 0.5

    hbox:
        at xslide(x_depart=720, x_final=60)
        pos (60,600)
        button:
            xysize (298, 96)
            action [Hide("plus_de_menus"), Show("affiche_stats", transition=None, acte=acte, situation = situation)]
            hbox:
                image "icons/icon_stats.png"
                text "Stats" xoffset 30 yalign 0.5
        button:
            xysize (298, 96) xoffset 4
            action [Hide("plus_de_menus"), Show("credits", transition=None, acte=acte, situation = situation)]
            hbox:
                image "icons/icon_credits.png"
                text _("Crédits") xoffset 30 yalign 0.5
    hbox:
        at xslide(x_depart=-120, x_final=60)
        pos (60,700)
        button:
            xysize (298, 96)
            action [Hide("plus_de_menus"), Show("options", transition=None, acte=acte, situation = situation)]
            hbox:
                image "icons/icon_options.png"
                text "Options" xoffset 30 yalign 0.5
        button:
            xysize (298, 96) xoffset 4
            action [Hide("plus_de_menus"), Show("help_plz", transition=None, acte=acte, situation = situation)]
            hbox:
                image "icons/question_mark.png"
                text _("Aide") xoffset 30 yalign 0.5

    button:
        at xslide(x_depart=720, x_final=360)
        xysize (600, 94) xalign 0.5 ypos 800
        text _("Retour") at truecenter
        if situation == "menu_principal":
            action [Hide("plus_de_menus"), Show("menu_alternatif")]
        else:
            action [Hide("plus_de_menus"), Show("in_game_menu", acte=acte)]

screen affiche_succes(obtenu, total, acte=0, situation = "menu_principal"):
    zorder 12
    style_prefix "coal"
    $ succes_obtenus = compte_succes()
    key "rollback" action [Hide("affiche_succes"), Show("plus_de_menus", transition=None, acte=acte, situation = situation)]
    window:
        at xslide(x_depart=-120, x_final=360)
        ysize 116 ypos 380
        vbox:
            hbox:
                ysize 96
                image "icons/icon_success.png"
                text _("Succès") size 42 xoffset 50
                text "[obtenu]/[total]" size 28 xoffset 250 yalign 1.0
            bar value StaticValue(succes_obtenus, len((persistent.achievements_dict))) ysize 12
    viewport:
        at xslide(x_depart=720, x_final=360)
        xysize (600, 620)
        xalign 0.5
        ypos 500
        draggable True
        mousewheel True
        scrollbars "vertical"
        vbox:
            spacing 8
            for i in persistent.achievements_dict:
                $ (nom, texte, is_obtenu, val) = get_info_achievement(i, cache = True)
                window:
                    xsize 580 ysize 110
                    hbox:
                        yalign 0.5
                        if is_obtenu:
                            if val == "Ultime":
                                image "icons/achievement_diamand.png"
                            elif val == "Difficile":
                                image "icons/achievement_or.png"
                            elif val == "Moyen":
                                image "icons/achievement_argent.png"
                            else:
                                image "icons/achievement_bronze.png"
                        else:
                            image "icons/achievement_locked.png"
                        vbox:
                            xoffset 10 yalign 0.5
                            if is_obtenu:
                                text nom size 30
                                text texte size 24 color "#ddd"
                            else:
                                text nom size 30 color "#bbb"
                                text texte size 24 color "#888"
                        
    button:
        at xslide(x_depart=-120, x_final=360)
        xysize (600, 94)
        xalign 0.5
        ypos 1120
        text _("Retour") at truecenter
        action [Hide("affiche_succes"), Show("plus_de_menus", transition=None, acte=acte, situation = situation)]

screen affiche_fins(obtenu, total, acte=0, situation = "menu_principal"):
    zorder 12 
    style_prefix "coal"
    $ fins_obtenues = compte_fins()
    key "rollback" action [Hide("affiche_fins"), Show("plus_de_menus", transition=None, acte=acte, situation = situation)]
    window:
        at xslide(x_depart=720, x_final=360)
        ysize 116 ypos 380
        vbox:
            hbox:
                ysize 96
                image "icons/icon_cxvl.png"
                text _("Fins") size 42 xoffset 50
                text "[obtenu]/[total]" size 28 xoffset 280 yalign 1.0
            bar value StaticValue(fins_obtenues, len((persistent.fins))) ysize 12
    viewport:
        at xslide(x_depart=-120, x_final=360)
        xysize (600, 616)
        xalign 0.5
        ypos 500
        draggable True
        mousewheel True
        scrollbars "vertical"
        vbox:
            spacing 8
            for i in persistent.fins:
                window:
                    xsize 580
                    hbox:
                        yalign 0.5
                        if persistent.fins[i][1]:
                            if i[0] == "-":
                                image "icons/cxvlineblood.png" xoffset 10
                            else:
                                image "icons/cxvline.png" xoffset 10
                        else:
                            image "icons/cxvline_locked.png" xoffset 10
                        text crypte_fin(i) yalign 0.5 xoffset 20

    button:
        at xslide(x_depart=720, x_final=360)
        xysize (600, 100)
        xalign 0.5
        ypos 1120
        text _("Retour") at truecenter
        action [Hide("affiche_fins"), Show("plus_de_menus", transition=None, acte=acte, situation = situation)]

screen affiche_stats(acte=0, confiance_persos=persistent.confiance, situation = "menu_principal"):
    zorder 12
    style_prefix "coal"
    key "rollback" action [Hide("affiche_fins"), Show("plus_de_menus", transition=None, acte=acte, situation = situation)]
    python:
        #text read
        texte_pourcentage, texte_lu, texte_total = avancement()

        #achievements and endings
        succes_obtenus = compte_succes()
        fins_obtenues = compte_fins()
    window:
        at xslide(x_depart=-120, x_final=360)
        ypos 400
        hbox:
            image "icons/icon_stats.png"
            text _("Statistiques") size 42 xoffset 40 yalign 0.5
    window:
        xysize (600, 616) ypos 500
        at xslide(x_depart=720, x_final=360)
        viewport:
            xysize (580, 616) xpos 20
            draggable True
            mousewheel True
            scrollbars "vertical"
            vbox:
                spacing 30
                vbox:
                    text _("Temps de jeu total : ")
                    text total_runtime.TextFormat("[hour] h [minute] min [second] s", font="DejaVuSans.ttf", color="#bbb" ) 
                    
                vbox:
                    text _("Texte lu (toutes parties confondues)")
                    hbox:
                        bar value StaticValue(texte_lu, texte_total) ysize 12 xsize 400 yalign 0.5
                        text "  "
                        text str(texte_pourcentage) color "#bbb"
                        text "%" color "#bbb"
                vbox:
                    text _("Succès obtenus")
                    hbox:
                        bar value StaticValue(succes_obtenus, len((persistent.achievements_dict))) ysize 12 xsize 400 yalign 0.5
                        text "  "
                        text str(succes_obtenus) color "#bbb"
                        text " / " color "#bbb"
                        text str(len((persistent.achievements_dict))) color "#bbb"
                vbox:
                    text _("Fins atteintes")
                    hbox:
                        bar value StaticValue(fins_obtenues, len((persistent.fins))) ysize 12 xsize 400 yalign 0.5
                        text "  "
                        text str(fins_obtenues) color "#bbb"
                        text " / " color "#bbb"
                        text str(len((persistent.fins))) color "#bbb"
                text _("Confiance min/max atteinte")
                grid 3 8:
                    for perso in sorted(confiance_persos):
                        $ mini,maxi,affiche = confiance_persos[perso][0]*5, confiance_persos[perso][1]*5, confiance_persos[perso][2]
                        if affiche:
                            text perso color "#bbb" xalign 1.0
                            text "   [mini]%" color "#bbb"
                            text "[maxi]%" color "#bbb"
                        else:
                            text ""
                            text ""
                            text ""

    button:
        at xslide(x_depart=-120, x_final=360)
        ypos 1120
        text _("Retour") xalign 0.5
        action [Hide("affiche_stats"), Show("plus_de_menus", transition=None, acte=acte, situation = situation)]

screen credits(acte=0, situation = "menu_principal"):
    zorder 12
    style_prefix "coal"
    key "rollback" action [Hide("credits"), Show("plus_de_menus", transition=None, acte=acte, situation = situation)]
    window:
        at xslide(x_depart=720, x_final=360)
        xysize (600,94) ypos 400 xalign 0.5
        hbox:
            image "icons/icon_credits.png"
            text _("Crédits") size 42 xalign 0.5
    window:
        ysize 516 ypos 500
        at xslide(x_depart=-120, x_final=360)
        viewport:
            xysize (580, 616) xpos 20
            draggable True
            mousewheel True
            scrollbars "vertical"
            vbox:
                spacing 30
                hbox:
                    text "Version "+config.version+" \""
                    text persistent.version_name
                    text "\""
                hbox:
                    text _("Mis à jour le ")
                    text persistent.version_date color "#bbb"
                text _("\n{i}par Ewen Q.{/i}\n") xalign 0.5
                grid 2 6:
                    xspacing 15
                    yspacing 5
                    text _("Portraits") xalign 1.0
                    text "A-L. Loubière" color "#bbb"
                    text _("Traduction") xalign 1.0
                    text "Juliette Chastel" color "#bbb"
                    text _("Relecture") xalign 1.0
                    text "Houda Rida" color "#bbb"
                    text _("Site Web") xalign 1.0
                    text "Julien Garcia" color "#bbb"
                    text _("Illustration Menu") xalign 1.0
                    text "Joke" color "#bbb"
                    text _("Musique") xalign 1.0
                    text "Marius Prével" color "#bbb"
                text _("Un grand merci à Tom 'PyTom' Rothamel pour le moteur Ren'Py.")
                text _("À tous ceux qui m'ont soutenu dans ce projet qui m'a beaucoup tenu à cœur ces dernières années.")
    button:
        at xslide(x_depart=720, x_final=360)
        ypos 1020
        text _("Licenses") at truecenter
        action [Hide("credits"), Show("licenses", transition=None, acte=acte, situation = situation)]
    button:
        at xslide(x_depart=-120, x_final=360)
        ypos 1120
        text _("Retour") at truecenter
        action [Hide("credits"), Show("plus_de_menus", transition=None, acte=acte, situation = situation)]

screen licenses(acte=0, situation = "menu_principal"):
    zorder 12
    style_prefix "coal"
    key "rollback" action [Hide("credits"), Show("plus_de_menus", transition=None, acte=acte, situation = situation)]
    window:
        at xslide(x_depart=720, x_final=360)
        xysize (600,94) ypos 400 xalign 0.5
        hbox:
            image "icons/icon_license.png"
            text "Licences" size 42 xalign 0.5
    window:
        ysize 616 ypos 500
        at xslide(x_depart=-120, x_final=360)
        viewport:
            xysize (580, 616) xpos 20
            draggable True
            mousewheel True
            scrollbars "vertical"
            text _("Conçu avec {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")
    button:
        at xslide(x_depart=720, x_final=360)
        ypos 1120
        text _("Retour") at truecenter
        action [Hide("licenses"), Show("credits", transition=None, acte=acte, situation = situation)]

screen help_plz(acte=0, situation = "menu_principal"):
    zorder 12
    style_prefix "coal"
    key "rollback" action [Hide("help_plz"), Show("plus_de_menus", transition=None, acte=acte, situation = situation)]
    window:
        at xslide(x_depart=720, x_final=360)
        xysize (600,94) xalign 0.5 ypos 400
        hbox:
            image "icons/question_mark.png"
            text _("Aide") size 42 xalign 0.5
    window:
        xysize (600, 616) ypos 500
        at xslide(x_depart=-120, x_final=360)
        viewport:
            xysize (580, 616) xpos 20
            draggable True
            mousewheel True
            scrollbars "vertical"
            vbox:
                text _("Rejoignez la discussion : théories, secrets et résolution de problèmes sur {a=https://discord.gg/wmu2PWA}Discord{/a} !")
                text "_" xalign 0.5
                text _("Le bouton {i}Passer{/i} en bas de l'écran permet de passer les dialogues déjà lus, jusqu'au prochain choix ou phrase encore non lue.")
                text "_" xalign 0.5
                text _("Le bouton {i}Auto{/i} permet de faire défiler automatiquement les dialogues, à votre rythme : vous pouvez en modifier la vitesse dans le menu des options.")
                text "_" xalign 0.5
                text _("Pour réussir à vaincre le Bourreau, connaître la vérité est nécessaire. Mais non suffisant.")
                text "_" xalign 0.5
                text _("Les codes de triche sont à rentrer dans un menu secret. A vous de le trouver...")

    button:
        at xslide(x_depart=720, x_final=360)
        ypos 1120
        text _("Retour") at truecenter
        action [Hide("help_plz"), Show("plus_de_menus", transition=None, acte=acte, situation = situation)]

screen options(acte=0, situation = "menu_principal"):
    style_prefix "coal"
    zorder 12
    key "rollback" action [Hide("options"), Show("plus_de_menus", transition=None, acte=acte, situation = situation)]
    window:
        at xslide(x_depart=720, x_final=360)
        ypos 400
        hbox:
            image "icons/icon_options.png"
            text _("Options") size 42 xoffset 40 yalign 0.5
    window:
        at xslide(x_depart=-120, x_final=360)
        xysize (600, 146) ypos 500
        vbox:
            xysize (520, 106) spacing 20 at truecenter
            text _("Vitesse du texte")
            bar value Preference("text speed")
    window:
        at xslide(x_depart=720, x_final=360)
        xysize (600, 146) ypos 650
        vbox:
            xysize (520, 106) spacing 20 at truecenter
            text _("Volume de la musique") 
            bar value Preference("music volume")
    window:
        at xslide(x_depart=-120, x_final=360)
        xysize (600, 146) ypos 800
        vbox:
            xysize (520, 106) spacing 20 at truecenter
            text _("Volume des effets sonores")
            bar value Preference("sound volume")

    button:
        at xslide(x_depart=720, x_final=360)
        ypos 950
        text _("Retour") at truecenter
        action [Hide("options"), Show("plus_de_menus", transition=None, acte=acte, situation = situation)]


screen carte(localisation_persos={2}, revelee=False, acte=0):
    zorder 12
    style_prefix "coal"
    key "rollback" action [Hide("carte"), Show("menu_title_coal"), Show("in_game_menu", acte=acte)]
    window:
        background "#0000"
        at smooth_title(time = 1.0, transp = 1.0, dist_y = 0)
        xysize (720,1280)
        if carte_complete:
            image "cartes/carte_complete_penche.png"
        else:
            image "cartes/carte_incomplete.png"
    button:
        at fade_away()
        ypos 1120
        text _("Retour") at truecenter
        action [Hide("carte"), Show("menu_title_coal"), Show("in_game_menu", acte=acte)]

screen recap(acte=0):
    zorder 12
    style_prefix "coal"
    key "rollback" action [Hide("recap"), Show("menu_title_coal"), Show("in_game_menu", acte=acte)]
    window:
        at xslide(x_depart=720, x_final=360)
        ypos 400
        hbox:
            image "icons/icon_recap.png"
            text _("Résumé") size 42 at truecenter
    button:
        at xslide(x_depart=720, x_final=360)
        ysize 50 ypos 500 ymargin 3
        text "⟰" at truecenter
        action Scroll("events_vp", "vertical decrease", 2000)
    viewport id "events_vp":
        at xslide(x_depart=-120, x_final=360)
        xysize (660, 517) xalign 0.5 ypos 550
        draggable True mousewheel True scrollbars "vertical"
        vbox:
            spacing 20
            for i in liste_events[::-1]: # les derniers events en premier, à l'affichage
                if i["actif"]:
                    vbox:
                        xalign 0.5
                        hbox:
                            xalign 0.5
                            text _("Jour ") italic True color "#bbb" size 22
                            text str(i["jour"]) italic True color "#bbb" size 22
                            text " - "+i["heure"] italic True color "#bbb" size 22
                        text i["details"] size 26 text_align 0.5 #justify True
    button:
        at xslide(x_depart=720, x_final=360)
        ysize 50 ypos 1070 ymargin 3
        text "⟱" at truecenter
        action Scroll("events_vp", "vertical increase", "page")
    button:
        at xslide(x_depart=720, x_final=360)
        ypos 1120
        text _("Retour") at truecenter
        action [Hide("recap"), Show("menu_title_coal"), Show("in_game_menu", acte=acte)]

screen archives_search():
    zorder 12
    style_prefix "coal"
    key "rollback" action NullAction()
    window:
        at smooth
        ypos 60
        hbox:
            at truecenter
            text _("- Index -") size 42
    window:
        at smooth
        ypos 160
        hbox:
            xpos 60 ypos 30
            text _("Rechercher : ")
            text majuscule_au_debut(uniformise(text_entry)) color "#88c" xoffset 20
    window:
        at smooth
        ysize 500 ypos 260
        text _("Dernières recherches : ") ypos 30 xalign 0.5
        viewport:
            xpos 20 ypos 80 xysize (580, 420)
            draggable True
            mousewheel True
            scrollbars "vertical"
            vbox:
                spacing 20
                for recherche in liste_recherches:
                    if uniformise(recherche) in archives_dic:
                        button:
                            xsize 300 ysize 50
                            idle_background "transparent"
                            action Return(recherche)
                            text uniformise(recherche).title()
                    else:
                        text uniformise(recherche).title() color "#666"

    hbox:
        pos (0, 800)
        $ up_alphabet = "AZERTYUIOP" if clavier_azerty else "QWERTYUIOP"
        for letter in up_alphabet:
            button:
                at smooth
                xysize (72, 96) xmargin 2
                text letter  at truecenter
                if len(text_entry)>20:
                    action Notify(_("Recherche trop longue"))
                else:
                    action SetVariable("text_entry", text_entry+letter)
    hbox:
        pos (0, 900)
        $ middle_alphabet = "QSDFGHJKLM" if clavier_azerty else "ASDFGHJKLM" 
        for letter in middle_alphabet:
            button:
                at smooth
                xysize (72, 96) xmargin 2
                text letter xalign 0.5
                if len(text_entry)>20:
                    action Notify(_("Recherche trop longue"))
                else:
                    action SetVariable("text_entry", text_entry+letter)
    hbox:
        pos (145, 1000)
        $ down_alphabet = "WXCVBN" if clavier_azerty else "ZXCVBN"
        for letter in down_alphabet:
            button:
                at smooth xysize (72, 96) xmargin 2
                text letter  at truecenter
                if len(text_entry)>20:
                    action Notify(_("Recherche trop longue"))
                else:
                    action SetVariable("text_entry", text_entry+letter)

    button:
        at smooth 
        xysize (140, 98) xmargin 2
        pos (70, 1000)
        if clavier_azerty:
            text "AZ→QW"
        else:
            text "QW→AZ"
        action [ToggleVariable("clavier_azerty", true_value=True, false_value=False), Jump("explore_archives")]
    button:
        at smooth 
        xysize (140, 98) xmargin 2
        pos (650, 1000)
        text "Del" xalign 0.5
        action SetVariable("text_entry", text_entry[:-1])

    button:
        at smooth
        xysize (288, 96) xpos 508 ypos 1120
        text _("Chercher") at truecenter
        if len(text_entry) > 1:
            action Return(text_entry) #Et on ajoute la variable recherchée à la liste des recherches (voir menus_structure)
        else:
            action Notify(_("Recherche trop courte"))
    button:
        at smooth
        xysize (288, 96) xpos 204 ypos 1120
        text _("Partir") at truecenter
        action Return("stop")

screen archives_show(search, display):
    zorder 12
    style_prefix "coal"
    key "rollback" action Return("chercher")
    window:
        at smooth
        ypos 60
        text _("- Index -") size 42 xalign 0.5
    window:
        at smooth
        ypos 160
        hbox:
            yalign 0.5 xalign 0.5
            if search == "none":
                text uniformise(display).title() color "#BBB"
            elif uniformise(display) == uniformise(search):
                text uniformise(display).title()  color "#88FF88"
            else:
                text uniformise(display).title()  color "#BBB"
                text " → "
                text uniformise(search).title()  color "#88FF88"
    window:
        xysize (660, 852) ypos 260 
        at smooth
        viewport:
            xysize (640, 852) xpos 20
            draggable True
            mousewheel True
            scrollbars "vertical"
            vbox:
                text ""
                text archives_dic[search] justify True
                text ""
    button:
        at smooth
        xysize (288, 96) xpos 508 ypos 1120
        text _("Chercher") at truecenter
        action Return("chercher")
    button:
        at smooth
        xysize (288, 96) xpos 204 ypos 1120
        text _("Partir") at truecenter
        action Return("stop")

screen unlock_code(): #TODO
    zorder 12
    style_prefix "coal"
    window:
        at smooth
        xysize (600, 94) xalign 0.5 ypos 160
        #image perso["image"] xoffset 33 yalign 0.5
        hbox:
            xpos 60 ypos 30
            text _("Code : ")
            text majuscule_au_debut(uniformise(text_entry)) color "#88c" xoffset 20
    hbox:
        pos (0, 800)
        $ numbers = "01234"
        for letter in numbers:
            button:
                at smooth
                xysize (120, 96) xmargin 2
                text letter  at truecenter
                if len(text_entry)>20:
                    action Notify(_("Recherche trop longue"))
                else:
                    action SetVariable("text_entry", text_entry+letter)
    hbox:
        pos (0, 900)
        $ numbers = "56789"
        for letter in numbers:
            button:
                at smooth
                xysize (120, 96) xmargin 2
                text letter  at truecenter
                if len(text_entry)>20:
                    action Notify(_("Recherche trop longue"))
                else:
                    action SetVariable("text_entry", text_entry+letter)

    button:
        at smooth
        xysize (140, 98) xmargin 2
        pos (580, 1000)
        text "Del"  at truecenter
        action SetVariable("text_entry", "")

    button:
        at smooth
        xysize (288, 96) xpos 364 ypos 1120
        text _("Essayer") at truecenter
        action Return(text_entry)
    button:
        at smooth
        xysize (288, 96) xpos 60 ypos 1120
        text _("Quitter") at truecenter
        action Return("stop")

#=====================================================================================================================
init python:
    
    def avancement():
        lu = renpy.count_seen_dialogue_blocks()
        total = renpy.count_dialogue_blocks()
        return min(100*lu//total, 100), min(lu, total), total #Overflow

    def compte_fins():
        nb = 0
        for i in persistent.fins:
            if persistent.fins[i][1]:
                nb += 1
        return nb

    def compte_succes():
        nb = 0
        for i in persistent.achievements_dict:
            if persistent.achievements_dict[i]["obtenu"]:
                nb += 1
        return nb

    def crypte_fin(fin_id):
        if persistent.fins[fin_id][1]:
            return persistent.fins[fin_id][0]
        else:
            fin_cryptee = ""
            for char in persistent.fins[fin_id][0]:
                if renpy.random.random()*len(persistent.fins) < compte_fins():
                    fin_cryptee += char
                else:
                    fin_cryptee += "?"
            return fin_cryptee

label charger_partie:
    stop music fadeout 1.0
    scene black with inkdissolve
    $ renpy.pause(0.5)
    $ renpy.load(partie_actuelle)

label supprimer_partie:
    $ renpy.unlink_save(partie_choisie)
    $ renpy.call("prepare_play")