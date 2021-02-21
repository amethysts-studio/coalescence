#==================================#
#====== Acte II : Exploration =====#
#==================================#
label sec_map:
    label sec_map_: # renpy-graphviz: IGNORE
        nvl clear
        show carte_incomplete:
            linear 0.2 alpha 1.0
        if elus_vote[1] == ["emmy"]:
            call screen screen_carte1(acte_carte = "2-1")
        elif elus_vote[1] == ["alan"]:
            call screen screen_carte1(acte_carte = "2-4")
        else:
            call screen screen_carte1(acte_carte = "2-23")
        $ salle = _return
        show carte_incomplete:
            linear 0.2 alpha 0.05
    if salle == "salle_vote":
        narr "La salle était grande et simple."
        narr "Comme toutes les salles, elle était mal éclairée, par une unique ampoule qui diffusait une faible lumière jaunâtre"
        narr "Le seul mobilier était une table ronde sur laquelle reposait 6 tablettes tactiles"
        narr "L'une d'elle, celle d'Emmy, était recouverte de sang"
        if simple_visit_salle_vote_acte2:
            $ simple_visit_salle_vote_acte2 = False
            narr "Johann et Leonhard discutaient violemment."
            narr "Ils s'interrompirent en me voyant approcher, et semblaient embarrassés."
            j "Alors, Kurt, des idées pour se sortir de cette situation ?..."
            j "Moi, je suis perdu..."
            narr "Cela semblait étrange de la part de Johann, toujours si sûr de lui d'habitude."
            j "... enfin non, pas perdu, plutôt surpris de ma réflexion !"
            narr "Johann tout craché."
            j "Pour tout te dire..."
            j "Je pense que le Bourreau est un de nous six."
            if len(elus_vote[1]) > 1:
                j "Enfin de nous cinq, (désolé Emmy)."
            narr "Leonhard, nullement surpris, réprimanda Johann."
            l "Johann, arrête de faire ton intéressant."
            l "Montrer son intelligence n'est pas forcément une bonne idée ici, et tu le sais !"
            l "Si le Bourreau se sent menacé, il va s'occuper de ton cas."
            l "Mène ton enquête en silence, comme moi !"
            narr "Il prit Johann à part et chuchota à son oreille."
            menu:
                "Tenter d'écouter discrètement":
                    narr "J'approchai sans bruit, en tendant l'oreille."
                    l "(Et tiens moi informé de ce que tu sais, mais sans le dire à tout le monde, d'accord ?)"
                    narr "Johann me surpris"
                    $ modif_confiance([johann, leonhard], [-1, -1])
                    j "Vraiment, Kurt ?"
                    l "On ne peut pas te faire confiance ?..."
                    j "C'est bon, laisse tomber, Leonhard."
                    narr "Ce dernier grimaça."
                    j "Revenons à nos moutons, veux-tu ?"
                    
                "Les laisser parler seuls" ("default", 8.0):
                    narr "Johann reprit à haute voix :"
                    j "Je ne peux pas me contenir. Ce jeu est trop excitant !"
                    j "Désolé, Leonhard, mais c'est plus fort que moi..."
            j "J'ai l'impression d'être en duel à mort face à un ennemi inconnu..."
            narr "Il remit ses lunettes en souriant"
            j "...comme L contre Kira !"
            narr "Johann dégageait vraiment une aura impressionnante."
            narr "Il était prétentieux, mais cela n'était pas juste de la vantardise..."
            narr "...il était {i}vraiment{/i} un génie"
            $ sauvegarder("continuer", montrer = False)
            jump sec_map
    elif salle == "salle_archives":
        narr "Elle est fermée à clé."
        menu:
            "Regarder par le trou de la serrure":
                p "(C'est trop sombre, on ne voit rien...)"
                if inventaire["lampe"]["nb"] == 1 and inventaire["battery"]["nb"] >=10:
                    menu:
                        "Utiliser la lampe torche":
                            narr "Je sortis la lampe torche de ma poche, et regardai à travers la serrure."
                            $ update_inventory(inventaire["battery"], balance = -10)
                            narr "Il y avait juste des étagères remplies de papiers, et au centre, une bibliothèque..."
                            if first_time_see_archives:
                                $ first_time_see_archives = False
                                narr "Derrière la bibliothèque, il y avait une forme vaguement humaine..."
                                narr "... qui me regardait.{nw}"
                                show jumpscareZoomArchives with None
                                pause 0.1
                                hide jumpscareZoomArchives with None
                                narr "Surpris, je reculai et tombai à la renverse."
                                narr "La lumière de la lampe torche se mit à vaciller, puis s'éteint."
                                p "(Je ne vais plus jamais remettre les pieds ici...)"
                            else:
                                narr "Mais il n'y avait plus rien d'autre."
                                narr "Rien d'effrayant, rien qui bougeait"
                                narr "C'était une hallucination ?"
                                narr "..."
                        "Partir":
                            pass
            "Ne rien faire":
                pass
        $ sauvegarder("continuer", montrer = False)
        jump sec_map
    elif salle == "salle_chambres":
        narr "Il y avait peint en rouge les numeros 1, 2 et 3 sur les portes des chambres"
        narr "2 lits étaient collés aux parois, et un grand placard recouvrait le mur du fond"
        if elus_vote[1] == ["emmy"]:
            narr "Emmy s'était enfermée dans la chambre 2"
        else:
            narr "Alan s'était enfermé dans la chambre 2"

        if not simple_visit_salle_chambre_acte2:
            if elus_vote[1] == ["emmy"]:
                narr "Elle ne voulait plus parler."
            else:
                narr "Il sifflottait tranquillement."
            $ sauvegarder("continuer", montrer = False)
            jump sec_map
        else:
            $ simple_visit_salle_chambre_acte2 = False
            menu:
                "Parler":
                    if elus_vote[1] == ["emmy"]:
                        p "Emmy ?"
                        e "..."
                        e "Quoi ?"
                        p "Je... je suis désolé... que tu aie été désignée, tout à l'heure."
                        e "..."
                        p "De toute façon, c'est peut-être juste une blague, tout {i}ça{/i} !"
                        e "Non mais tu as entendu Leonhard ?"
                        e "Tu sais très bien que je vais mourir avant demain midi."
                        e "C'est...{w} beaucoup trop...{w} je sais pas...{w} {i}bizarre{/i}..."
                        narr "Emmy sanglotait derrière la porte."
                        p "Ça va aller, ne t'inquiète pas."
                        p "Johann est intelligent, et Leonhard pourra l'aider, avec les informations qu'il a l'air d'avoir..."
                        p "Ensemble, ils trouveront une solution !"
                        e "..."
                        p "Tout... tout ira bien, je te le promets."
                        narr "Emmy ricana"
                        e "{i}Vraiment{/i} ?"
                        e "Tu te moques de moi ?"
                        $ renpy.vibrate(1.0)
                        e "{b}TU TE MOQUES DE MOI ?{/b}" with sshake
                        e "JOHANN, LEONHARD ET TOI, VOUS AVEZ TOUS LES TROIS VOTÉ CONTRE MOI, ET TU DIS QUE TOUT IRA BIEN ???"
                        $ renpy.vibrate(1.0)
                        e "{b}DÉGAGE !{/b}" with sshake
                        narr "Emmy se remit à pleurer"
                        $ sauvegarder("continuer")
                        jump sec_map
                    else:
                        p "Alan ?"
                        ala "..."
                        if elus_vote[1] == ["alan"]:
                            p "Je... je suis désolé... que tu aie été désigné, tout à l'heure."
                            ala "..."
                            p "De toute façon, c'est peut-être juste une blague, tout {i}ça{/i} !"
                            ala "Non mais tu as entendu Leonhard ?"
                            ala "Tu sais très bien que je vais mourir avant demain midi."
                            ala "Mais c'est pas ça, le plus grave."
                            ala "Après tout, je mérite peut-être vraiment de mourir."
                            p "Mais non, ne dis pas ça !"
                            ala "..."
                            ala "Peu importe."
                            ala "Tu as entendu ce que j'ai dit aux deux intellos, tout à l'heure ?"
                            ala "Je le pense vraiment."
                            p "Mais... pourquoi ?"
                            ala "Dans pas mal de films, on découvre à la fin que le tueur est parmi les victimes."
                            ala "Ces deux cons ont l'air assez cultivés pour connaître ce genre de films, et assez intelligents pour mettre en place ce genre de bail."
                            ala "Si ça leur permet de casser de la {i}racaille{/i}, ça doit pas leur causer de problèmes."
                            p "..."
                        else:
                            ala "Ça tombe bien que tu viennes."
                        ala "J'ai quelque chose à te dire. C'est important que tu saches ça."
                        p "Quoi ?"
                        ala "Tu sais, je vendais de la drogue."
                        p "Oui, pourquoi ?"
                        narr "Il fit une pause de cinq secondes, et me posa une question en retour."
                        ala "Tu t'y connais, en drogue ?"
                        menu:
                            "Oui":
                                ala "Tu préfères quoi ?"
                                menu:
                                    "Cannabis (résine) ":
                                        ala "T'es sérieux ? C'est plein de merde, ça..."
                                    "Cannabis (herbe)":
                                        $ modif_confiance([alan], [1])
                                        ala "Ouaaais mon pote !"
                                        ala "Check ça !"
                                        narr "Il ouvrit la porte et me tendit son poing"
                                        ala "Dépêche !"
                                        narr "Je lui rendit son check, et il s'enferma de nouveau dans sa chambre."
                                    "Cocaïne":
                                        ala "T'es sérieux ? C'est un vrai truc de {i}junkie{/i}..."
                                        $ modif_confiance([alan], [-1])
                            "Non":
                                ala "D'ac, faut que je t'explique."
                                ala "La drogue, c'est pas comme dans les films."
                                ala "C'est pas les pauvres, les racailles, ni les junkies qui en consomment le plus."
                                ala "C'est {i}mainstream{/i}. Même les bobos fument ! Tout le monde fume. Et ça détruit {i}{b}pas{/b}{/i} le cerveau d'en prendre une fois."
                                ala "Après, ça dépend des drogues."
                                ala "Le {i}shit{/i}, c'est une drogue douce, apaisante, pour les pauvres, ça fait trois fois rien, et c'est en général plein de merde pour la santé."
                                ala "Y a littéralement de la merde dedans. C'est dans le nom, putain, les gens sont cons de prendre ça..."
                                ala "La {i}beuh{/i}, a.k.a la weed, c'est aussi une drogue douce, c'est aussi du cannabis, mais c'est beaucoup plus {i}pur{/i}, parce que c'est pas coupé."
                                ala "C'est aussi beaucoup plus cher, et du coup c'est privilégié par les bobos."
                                ala "Par contre, la {i}coke{/i}, c'est un vrai truc de {i}junkie{/i}. Une drogue dure."
                                ala "Ça coûte une blinde, et ça rend accro..."
                        ala "Mais revenons à ce que je voulais te dire"
                        ala "Comme l'a dit Leonhard, après la weed..."
                        ala "...j'avais commencé à faire mon business de coke."
                        ala "Pourquoi ?"
                        ala "Plus d'argent en jeu, tu comprends bien !"
                        narr "Alan prit une grande inspiration"
                        ala "YO SOY PABLO ESCOBAAARRR !!!"
                        narr "Il partit dans un fou rire."
                        ala "Enfin bref."
                        ala "Tout ça pour te dire..."
                        narr "Il avait l'air de s'amuser dans sa chambre."
                        ala "Mon client."
                        ala "Pour la coke."
                        ala "..."
                        ala "C'était {i}Johann{/i}."
                        $ sauvegarder("continuer", montrer = False)
                        jump sec_map
                "Laisser tranquille":
                    $ sauvegarder("continuer", montrer = False)
                    jump sec_map
    elif salle == "salle_exec":
        narr "Cette salle était spéciale : il n'y avait pas vraiment de porte mais des barreaux en acier"
        narr "L'intérieur était effrayant."
        narr "La pièce, peinte en blanc, semblait plus claire que les autres"
        narr "On se serait cru dans {i}American Psycho{/i}"
        narr "Au centre trônait une guillotine"
        narr "Des couteaux recouvraient les murs"
        narr "Ils étaient soigneusement, régulièrement disposés, de manière que l'on pouvait remarquer..."
        if inventaire["knife"]["nb"] == 1:
            narr "...qu'il en manquait deux..."
        else:
            narr "...qu'il en manquait un..."
        if simple_visit_salle_exec_acte2:
            narr "Isaac, qui était resté discret jusque là, pris la parole"
            isa "Tu as remarqué ? J'en ai pris un..."
            narr "Face à ma surprise, il se défendit"
            isa "Quoi ? Tu as vu mon gabarit ? Faut bien que je puisse me défendre contre le Bourreau..."
            narr "Il jeta un regard effrayé dehors"
            isa "... et contre les autres..."
            isa "Tu penses qu'on a une chance de s'en sortir ?"
            narr "Je hochais la tête, incertain."
            isa "Fais comme moi, Kurt. Prend un couteau. On ne sait pas ce qui peut arriver..."
            menu:
                "Prendre un couteau":
                    $ update_inventory(inventaire["knife"], balance = 1)
                    narr "J'espère que les autres ne remarqueront pas ça..."
                    narr "Ça peut m'être utile en cas de danger mais également préjudiciable si on me surprend avec..."
                "Ne rien faire":
                    pass
        if (inventaire["knife"]["nb"] == 1) and (not simple_visit_salle_exec_acte2):
            menu:
                "Reposer le couteau":
                    narr "{i}Vous avez reposé le couteau{/i}"
                    $ update_inventory(inventaire["knife"], balance = -1)
                "Partir":
                    pass
        elif (inventaire["knife"]["nb"] == 0) and (not simple_visit_salle_exec_acte2):
            menu:
                "Prendre le couteau":
                    $ update_inventory(inventaire["knife"], balance = 1)
                    narr "{i}Vous possédez désormais un couteau{/i}"
                "Partir":
                    pass
        $ simple_visit_salle_exec_acte2 = False
        $ sauvegarder("continuer")
        jump sec_map
    elif salle == "salle_reserve":
        narr "Sur les murs à gauche et à droite il y avait de grandes étagères remplies de nourriture et d'objets de toutes sortes"
        narr "Il y avait manifestement assez de conserves pour survivre au moins trois mois"
        narr "Plusieurs objets pouvaient être utiles pour plus tard"
        if not inventaire["lampe"]["connu"]:
            $ inventaire["lampe"]["connu"] = True
            narr "Il y avait notamment une lampe torche..."
            $ update_inventory(inventaire["lampe"], balance = 1)
            narr "Et une batterie même pas à moitié chargée..."
            $ update_inventory(inventaire["battery"], balance = 40)
            $ inventaire["battery"]["connu"] = True
            p "Je prends la batterie, ça peut toujours servir."
        $ sauvegarder("continuer")
        jump sec_map
    elif salle == "salle_sanitaires":
        narr "A gauche, il y avait 4 toilettes, et de l'autre coté 3 douches avec des lavabos"
        if len(elus_vote[1]) > 1:
            narr "Emmy gisait ici dans une mare de sang..."
            narr "Alan l'avait complètement battue à mort..."
            narr "L'os de son bras doit était cassé, et dépassait de sa peau à travers le coude."
            narr "Le Bourreau avait vraiment mis une bombe dans le bras d'Emmy..."
            narr "En regardant de près, on pouvait voir que ça n'était pas une simple bombe."
            narr "Il y avait plein de capteurs étranges dessus... Bizarre."
        elif elus_vote[1] == ["emmy"]:
            narr "Alan était enfermé dans une douche, mais l'eau ne coulait pas."
            narr "Qu'est-ce qu'il était en train de faire ?"

        else:
            narr "Emmy était en train de prendre une douche."
            narr "Comment peut elle être aussi sereine ? Ça semblait inapproprié de faire ça maintenant..."
            narr "C'était peut-être une maniaque de la propreté !"
        $ sauvegarder("continuer")
        jump sec_map
    else:
        $ quick_menu = True
        return
