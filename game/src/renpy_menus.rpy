#===== INITIALISATION =====#
label menu_principal:
    nvl clear
    $ quick_menu = False
    n "\n\n\n\n\n\n\n\n\n\n{nw}"
    $ situation = "menu_principal"
    if not persistent.first_play:
        $ persistent.first_play = True
        $ persistent.glitched = False
        #$ nouvelle_simulation() mis dans le splashscreen de fin. Sinon, le screen est pré-chargé sans l'initialisation (valeur=None)
        $ persistent.fins = {
          "-9" : ["Convergence", False],
          "-8" : ["Négligence", False],
          "-7" : ["Imprudence", False],
          "-6" : ["Pestilence", False],
          "-5" : ["Différence", False], #nom, obtenu
          "-4" : ["Urgence", False],#TODO fin pas attribué dans le jeu
          "-3" : ["Violence", False],
          "-2" : ["Démence", False],
          "-1" : ["Dégénérescence", False],
          "0"  : ["Providence", False],#TODO fin non attribuée dans le jeu
          "1"  : ["Connivence", False],
          "2"  : ["Clémence", False],
          "3"  : ["Omnipotence", False],
          "4"  : ["Impatience", False],
          "5"  : ["Conséquence", False],
          "6"  : ["Ultraviolence", False],
          "7"  : ["Dissidence", False],
          "8"  : ["Confluence", False],
          "9"  : ["Existence", False]
        }
        $ persistent.confiance = {
          "Emmy" : [10, 10, False],
          "Isaac" : [10, 10, False],
          "Alan" : [10, 10, False],
          "Johann" : [10, 10, False],
          "Leonhard" : [10, 10, False],
          "Rosalind" : [10, 10, False],
          "Erwin" : [10, 10, False],
          "Lise" : [10, 10, False]          
        }
        $ persistent.partie_actu = "continuer" #acte (partie_désactivée = 0) / texte info / dernier_actif
        
        $ renpy.save("continuer")

    $ partie_actuelle = "continuer" #la variable stockée de maniere persistante sert au stockage, non à l'utilisation
    
    $ renpy.call_screen("menu_alternatif")
    


#===== VOTE =====#
label vote:
    $ quick_menu = False
    nvl clear
    $ situation = "en_vote"
    hide haut_de_page at smooth_title
    stop music fadeout 1.0
    show screen menu_background()
    show screen menu_title_coal()
    call screen liste_personnages(liste_persos=liste_persos, situation = "en_vote")
    
label resultatsvote:
    $ vote_contre = perso["nom"].lower()
    if vote_contre == "kurt" :
        $ get_achievement("suicidaire")
    nvl clear
    show black with dissolve
    pause 1.0
    hide black with dissolve
    show text _("{font=fonts/VanHelsing.ttf}{size=100}Résultats{/font}{/size}") as haut_de_page at smooth_title(time=1.5, transp = 1.0, dist_y = 200)
    pause 1.0
    if acte == 2: # A faire varier un peu ?
        $ votes = {"leonhard":0, "johann":0, "isaac":1, "kurt":0, "alan":2, "emmy":2}

    elif acte == 3:
        if vote2 == 8: # A trahi Isaac OU n'a pas dit la vérité
            $ votes = {"leonhard":0, "johann":0, "isaac":0, "kurt":4, "alan":0, "emmy":0}
            $ vote2 = 4
        else: #Sinon, vote normal
            if elus_vote[1] == ["alan"]:
                $ votes = {"leonhard":1, "johann":1, "isaac":0, "kurt":0, "emmy":2}
                if vote_contre == "leonhard":
                    $ vote2 = 7
                elif vote_contre == "johann":
                    $ vote2 = 6
                else:
                    $ vote2 = 5
            elif johann["confiance"] + leonhard["confiance"] >= 28:
                $ votes = {"leonhard":0, "johann":0, "isaac":1, "kurt":0, "alan":3, "emmy":0}
                $ vote2 = 1
            else:
                $ votes = {"leonhard":0, "johann":0, "isaac":0, "kurt":2, "alan":2, "emmy":0}
                if vote_contre == "alan":
                    $ vote2 = 2
                elif vote_contre == "kurt":
                    $ vote2 = 4
                else:
                    $ vote2 = 3
        
    elif acte == 4:
        $ votes = {"leonhard":0, "johann":0, "kurt":0, "erwin":0, "lise":0, "rosalind":6}

    elif acte == 5:
        $ votes = {"leonhard":0, "johann":0, "kurt":0, "erwin":0, "lise":0}
        if leonhard["confiance"] < 12:
            $ votes["johann"] += 1
        if johann["confiance"] < 12:
            $ votes["johann"] += 1
        if erwin["confiance"] < 12:
            $ votes["erwin"] += 1
        if lise["confiance"] < 12:
            $ votes["erwin"] += 1

    elif acte == 6:
        if fin_vote_4 == "leonhard_mort":
                $ votes = {"johann":0, "kurt":0, "erwin":2, "lise":1}
                if vote_contre == "lise":
                    $ vote5 = 3
                else:
                    $ vote5 = 4
        elif fin_vote_4 == "johann_mort_cachée" or fin_vote_4 == "johann_vivant" or fin_vote_4 == "johann_mort":
            $ votes = {"leonhard":1, "kurt":0, "erwin":2, "lise":0}
            if vote_contre == "erwin":
                $ vote5 = 4
            else:
                $ vote5 = 5

    if acte != 4:
        if vote_contre != "kurt":
            $ votes[vote_contre] += 1
        else:
            $ votes["kurt"] += 1

    if acte == 5:
        $ votes["kurt"] = 5 - (votes["erwin"]+votes["lise"]+votes["johann"]+votes["leonhard"]) #le vote de Kurt a déjà été pris en compte !!!

    $ elus_vote[acte-1] = resultat_vote(votes)
    
    play sound "sounds/vote.ogg"
    $ renpy.pause(0.2)
    call screen vote_results(liste_elus=elus_vote[acte-1])
    #call screen vote_details(liste_elus=elus_vote[acte-1])

    hide haut_de_page at smooth_title
    show black with dissolve
    pause 1.0
    hide black with dissolve

    $ sauvegarder("continuer", montrer=False)
    nvl clear
    $ situation == "en_jeu"
    $ quick_menu = True
    if acte == 2:
        jump suite_vote_1
    elif acte == 3:
        jump suite_vote_2
    elif acte == 4:
        jump suite_vote_3
    elif acte == 5:
        jump suite_vote_4
    elif acte == 6:
        jump suite_vote_5
        
        
#===== GAME OVER =====#
label game_over:
    $ nouvelle_simulation()
    $ persistent.glitched = True
    $ persistent.fins[str(fin)][1] = True
    nvl clear
    $ quick_menu = False
    if fin < 0:
        scene black with dissolve
        
        show game_over_bug with None
        $ renpy.pause(10.0)
    scene fin with fade
    $ renpy.pause(1.5)
    $ aux = False
    if fin < 0:
        $ fin = -fin
        $ aux = True
        $ mot = _("Mort")
    else:
        $ mot = _("Fin")
    show text "{size=40}"+mot+" n°[fin]:{/size}" as mot_fin:
        ypos 680
        alpha 0.0
        linear 1.5 alpha 1.0
    if aux:
        $ fin = -fin
    $ renpy.pause(1.5)
    $ name = persistent.fins[str(fin)][0]
    show text "{font=fonts/VanHelsing.ttf}{size=85}"+name+"{/size}{/font}":
        ypos 800
        alpha 0.0
        linear 3.0 alpha 1.0
    $ renpy.pause(5.0, hard=True)
    nvl clear
    scene black with dissolve
    $ persistent.loadable = False
    $ sauvegarder("continuer")
    if fin > 0:
        $ get_achievement("fin_acte6")
    else:
        $ get_achievement("premiere_mort")
    jump end
    
    

#===== ARCHIVES =====#
label explore_archives:
    nvl clear
    $ quick_menu = False
    if not in_archives:
        show archivuitton with dissolve
        $ in_archives = True
    $ text_entry = ""
    call screen archives_search()

    $ book = _return
    $ book_original = book
    $ book = uniformise(book)
    $ book = recherche_flex(book, archives_liste)
    if book_original == "stop":
        $ quick_menu = True
        hide archivuitton with dissolve
        jump exit_archives
    elif book == "gm":
        $ book = "gesundermenschenverstand"
    elif book == "klaus":
        $ info_klaus_archives = True
        $ rossignol["statut"] = "Caché"
    elif book == "rossignol":
        $ rossignol["statut"] = "Caché"
    elif book == "casoar":
        $ casoar["statut"] = "Caché"
    elif book == "hibou":
        $ hibou["statut"] = "Caché"
    elif book == "cxvl":
        pass
    elif book == "coalescence":
        $ get_achievement("bibliothequaire")
    if book == "none":
        $ liste_recherches = [book_original]+liste_recherches
    else:
        $ liste_recherches = [book]+liste_recherches
    $ liste_recherches = list(set(liste_recherches)) # supprimer doublons ...
    $ liste_recherches.sort(key=lambda x:(not x.islower(), x)) #...et trier dans un ordre logique. Tri en place !

    $ sauvegarder("continuer", montrer=False)

    call screen archives_show(search = book, display=book_original)
    $ choice_button = _return
    if choice_button == "chercher":
        jump explore_archives
    else:
        $ quick_menu = True
        hide archivuitton with dissolve
        jump exit_archives

label exit_archives:
    $ sauvegarder("continuer")
    nvl clear
    $ in_archives = False
    if situation == "en_jeu":
        if acte == 3:
            jump suite_explore_archives
        elif acte == 4:
            jump map1_acte4
        elif acte == 6:
            jump map1_acte6

label bonus:
    pass
#===== CODE =====#
label unlock_code:
    nvl clear
    $ quick_menu = False
    $ text_entry = ""
    call screen unlock_code()
    $ code = _return

