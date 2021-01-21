#==================================#
#====== Acte IV : Exploration =====#
#==================================#

label map1_acte4:
    label map1_acte4_:
        nvl clear
        if persistent.language == "english":
            show carte_completeEN:
                xalign 0.0
                linear 0.2 alpha 1.0
        else:
            show carte_completeFR:
                xalign 0.0
                linear 0.2 alpha 1.0
        show go_right:
            linear 0.2 alpha 1.0
        show quit_map:
            linear 0.2 alpha 1.0
        call screen screen_carte1(carte_revelee=True, bonus=False, acte_carte = "4")
        $ salle = _return
        if salle != "go_right":
            if persistent.language == "english":
                show carte_completeEN:
                    linear 0.2 alpha 0.05
            else:
                show carte_completeFR:
                    linear 0.2 alpha 0.05
            show go_right:
                linear 0.2 alpha 0.05
            show quit_map:
                linear 0.2 alpha 0.05
    if salle == "salle_vote":
        narr "Johann était seul dans la salle de vote."
        narr "Il observait attentivement les tablettes tactiles."
        if une_entrevue_johann:
            $ une_entrevue_johann = False
            narr "Il débordait de confiance en lui et savait manifestement quelque chose."
            j "Ah, Kurt, tu es là ?"
            j "Tu te demandes certainement pourquoi j'ai crié pendant la dernière intervention du Bourreau."
            j "Ne t'inquiète pas, je ne suis pas fou. Je voulais juste avoir une confirmation de l'identité du Bourreau."
            j "Maintenant, je sais {i}qui{/i} il est !"
            j "Il suffit de réfléchir un peu."
            j "Explore les archives, aussi. Des choses réellement importantes y sont cachées..."
            j "Maintenant, je réfléchis à {i}comment{/i} le tuer..."
            j "Mais il y a un petit problème : à cause de mon intervention de tout à l'heure, il sait que je connais tout de lui."
            j "Donc il va tout faire pour me tuer..."
            j "Heureusement, j'ai un plan !"
            if johann["confiance"] >= 19:
                j "Je te fais assez confiance. Alors écoute :"
                j "Au prochain vote, je vais voter pour toi. Pour que tu sois élu comme Bourreau, d'accord ?"
                j "Il faudra me faire confiance et comprendre rapidement ce qu'il se passe."
                j "Je te ferai un signe discret quand il faudra agir."
                narr "Il replaça ses lunettes... de la main gauche ?"
                j "Je vois à ton froncement de sourcil que tu as compris."
                j "J'ai un petit tic, remettre mes lunettes de la main droite, parce qu'elles tombent toutes seules..."
                j "Mais là, je le ferai de la main gauche, d'accord ?"
                j "Quand ça arrivera... Il faudra agir !"
                j "Je compte sur toi !"
            else:
                j "Il faut que je sois élu au prochain vote..."
                j "Et je pourrai changer les choses !"
            narr "Je m'attendais à ce qu'il m'en dise plus, mais il garda le silence et détourna le regard."
        else:
            j "T'es encore là ? Laisse-moi tranquille, je dois me préparer..."
        $ sauvegarder("continuer")
    elif salle == "salle_archives":
        narr "Dans un coin de la salle, entre deux étagères poussiéreuses, un très vieil ordinateur diffusait une lumière bleutée."
        narr "Les lettres capitales formaient le mot {b}Index{/b}."
        narr "Il semblait ne pas avoir bougé depuis la dernière fois, comme s'il attendait sereinement que l'on perce les secrets de ce lieu oppressant."
        nvl clear
        jump explore_archives
    elif salle == "salle_chambres":
        narr "Il y a 3 chambres numérotées 1, 2 et 3."
        narr "Les numéros sont écrits en grand et en rouge sur la porte."
        narr "Rosalind, qui avait été élue comme Bourreau, était enfermée dans la chambre 2."
        menu:
            "Parler à Rosalind à travers la porte":
                if rosalind_silent:
                    narr "Elle ne répondait plus."
                else:
                    p "Rosalind ? On peut parler ?"
                    narr "Rosalind grommela derrière la porte"
                    r "Qu'est-ce que tu veux ?"
                    label speak_rosa_acte4:
                        menu:
                            "Informations sur le Jeu":
                                p "Rosalind, tu pourrais me renseigner sur le Jeu ?"
                                if rosalind["confiance"] >= 12:
                                    r "Oui, oui, bien sûr !"
                                    r "J'ai participé aux trois premiers jeux."
                                    r "C'était horrible, et bien différent : le Bourreau ne nous parlait pas."
                                    r "Il laissait juste un mot : {i}Tuez-vous tous{/i}."
                                    r "Ensuite, il nous laissait s'entretuer. Comme nous maintenant."
                                    r "Il n'y avait pas de votes, ni d'élections, ni de Règles..."
                                    r "On aurait pu s'entendre, tous s'allier contre lui, mais il faisait toujours en sorte qu'il y ait un élément perturbateur."
                                    r "Tous les jeux ont dégénéré en bain de sang..."
                                    r "Tout ça, à cause de {i}moi{/i}"
                                    r "Tout ça, à cause de {i}K{/i}..."
                                    narr "Rosalind ne fit plus un bruit"
                                    $ rosalind_silent = True
                                else:
                                    r "Tu rigoles ? J'ai pas confiance en toi..."
                                    r "Tu veux juste me soutirer des informations comme ça ?..."
                                    r "Les jeunes... Aucun respect pour leurs aînés"
                                    $ modif_confiance([rosalind, erwin, lise, johann, leonhard], 
                                                      [-1      ,  0   , 0   , 0     , 0       ], montrer_conf)
                            "Informations sur son neveu" if rosalind["confiance"] >= 11:
                                p "Désolé de vous demander ça mais..."
                                p "...vous avez piqué ma curiosité tout à l'heure, en parlant de votre neveu."
                                p "Vous pouvez m'en dire plus ?"
                                r "Non."
                                r "J'ai trop souffert à cause de lui..."
                            "Lui remonter le moral" if une_entrevue_rosalind:
                                $ une_entrevue_rosalind = False
                                $ modif_confiance([rosalind, erwin, lise, johann, leonhard], 
                                                  [2      ,  0   , 0   , 0     , 0       ], montrer_conf)
                                p "Je... Je ne suis pas d'accord avec les autres."
                                p "Je ne crois pas que vous soyez méchante."
                                p "Et les autres ont eu tort de vous enfermer"
                                r "J'aurais fait la même chose à leur place..."
                                r "Mais tu as m'as l'air sympathique, jeune homme."
                                r "En fait, on avait déjà prévu, avec Erwin et Lise, de t'élire comme le prochain Bourreau..."
                                r "Je pense que tu es le plus innocent d'entre nous, et assez intelligent pour faire quelque chose de bien."
                                narr "Ils ont prévu de m'élire comme Bourreau ? Les enflures..."
                                narr "Si ça arrive vraiment, je vais devoir tuer quelqu'un... Ou mourir..."
                                p "Merci de votre confiance, mais c'est un rôle difficile à porter..."
                                r "C'est le rôle que je porte actuellement. Mais je vais me laisser mourir."
                                r "Toi, il faudra que tu te battes, et que tu fasses les bon choix."
                                narr "Les bon choix ? Facile à dire..."
                                jump speak_rosa_acte4
            "Partir":
                narr "Je passai mon chemin sans rien dire."
        $ sauvegarder("continuer")
    elif salle == "salle_exec":
        narr "La salle d'armes est en fait une cellule de prison dont les murs ont été repeints à la peinture blanche"
        narr "Le mur du fond est tapissé d'armes blanches..."
        if (inventaire["knife"]["nb"] == 1):
            menu:
                "Reposer le couteau":
                    narr "{i}Vous avez reposé le couteau{/i}"
                    $ update_inventory(inventaire["knife"], balance = -1)
                "Partir":
                    pass
        elif (inventaire["knife"]["nb"] == 0):
            narr "Un couteau brillait plus que les autres. Il avait l'air parfaitement affûté, idéal pour se défendre... Ou attaquer."
            menu:
                "Prendre le couteau":
                    $ update_inventory(inventaire["knife"], balance = 1)
                    narr "{i}Vous possédez désormais un couteau{/i}"
                "Partir":
                    pass
        $ sauvegarder("continuer")
    elif salle == "salle_reserve":
        narr "Une colombe rouge remplaçait maintenant l'amas de corps et de sang créé par le Bourreau."
        narr "La tête d'Isaac avait aussi disparu."
        narr "La corde était toutefois restée en plein milieu de la pièce."
        narr "Des lambeaux de chairs étaient toujours incrustée dans la corde."
        narr "Isaac a dû souffrir avant de mourir..."
        narr "Sur les murs à gauche et à droite il y avait de grandes étagères remplies de nourriture et d'objets de toutes sortes"
        narr "Il y avait manifestement assez de conserves pour survivre au moins trois mois."
        narr "Plusieurs objets pouvaient être utiles pour plus tard."
        if not inventaire["lampe"]["connu"]:
            $ inventaire["lampe"]["connu"] = True
            narr "Il y avait notamment une lampe torche..."
            $ update_inventory(inventaire["lampe"], balance = 1)
            narr "Et une batterie même pas à moitié chargée..."
            $ update_inventory(inventaire["battery"], balance = 40)
            $ inventaire["battery"]["connu"] = True
            p "Je prends la batterie, ça peut toujours servir."
        $ sauvegarder("continuer")
    elif salle == "salle_sanitaires":
        narr "Les toilettes étaient toujours aussi sales"
        if len(elus_vote[1]) > 1:
            narr "Le corps d'Emmy n'y était plus..."
        if une_entrevue_leonhard:
            $ une_entrevue_leonhard = False
            narr "Leonhard sortait des toilettes"
            l "Oh, Kurt."
            l "Je pensais justement à vous."
            l "Je me suis fait une petite liste, et j'aimerais avoir votre avis."
            l "En qui faites-vous le moins confiance, ici?"
            menu:
                "Johann":
                    p "Johann. Je pense qu'il cache quelque chose"
                    l "Ah oui ? Intéressant..."
                    $ modif_confiance([rosalind, erwin, lise, johann, leonhard], 
                                      [0       ,  0   , 0   , 0     , 1       ], montrer_conf)
                    l "Je ne lui fais plus autant confiance qu'avant."
                    l "Même si il dégage beaucoup de bonne volonté et d'entrain à essayer de découvrir ce qu'il se passe..."
                    l "... rien n'avance concrètement."
                    l "Nous sommes toujours coincés dans ce {i}putain de Jeu{/i}"
                    l "Il doit jouer un double jeu..."
                "Rosalind":
                    p "Rosalind évidemment."
                    $ modif_confiance([rosalind, erwin, lise, johann, leonhard], 
                                      [0       ,  0   , 0   , 0     , 1       ], montrer_conf)
                    p "Elle a été élue comme Bourreau, alors si elle ne veut pas que sa bombe explose, elle va devoir tuer quelqu'un..."
                    l "Bien. Savais-tu que je la soupçonne ?"
                    l "Je l'ai observée se déplacer"
                    l "Elle marche droit, sans se prendre de murs. Un peu comme si elle voyait"
                    l "Je le sais car c'est moi qui l'ai enfermée dans la chambre 2"
                    l "Elle ne s'est pas débattue, au contraire, elle y est allée, et a ouvert et fermé la porte toute seule..."
                    l "C'est beaucoup trop louche..."
                "Lise ou Erwin":
                    p "Le couple de chimistes."
                    l "Je suis d'accord aussi."
                    l "Ils ont déja leur propre laboratoire, qui peut leur servir d'arme : ce sont des chimistes..."
                    l "C'est étrange d'ailleurs : pourquoi y a-t-il un laboratoire ici ?"
                    l "C'est trop gros pour ne pas y penser..."
                    l "Et puis, regardez dans la Grande Salle."
                    l "C'est vraiment important. Allez-y."
                    l "Ils ne m'inspirent pas confiance..."
        else:
            narr "Leonhard notait quelque chose sur un carnet."
    elif salle == "go_right":
        hide go_right
        hide quit_map
        if persistent.language == "english":
            show carte_completeEN:
                easeout 0.5 xalign 0.25 alpha 0.5
                easein 0.5 xalign 0.5 alpha 1.0
        else:
            show carte_completeFR:
                easeout 0.5 xalign 0.25 alpha 0.5
                easein 0.5 xalign 0.5 alpha 1.0
        $ renpy.pause(1.0, hard=True)
        jump map2_acte4
    elif salle == "quit":
        jump finCarteActe4
    jump map1_acte4
    
label map2_acte4:
    label map2_acte4_:
        nvl clear
        if persistent.language == "english":
            show carte_completeEN:
                xalign 0.5
                linear 0.2 alpha 1.0
        else:
            show carte_completeFR:
                xalign 0.5
                linear 0.2 alpha 1.0
        show go_left:
            linear 0.2 alpha 1.0
        show go_right:
            linear 0.2 alpha 1.0
        show quit_map:
            linear 0.2 alpha 1.0
        call screen screen_carte2(bonus=False, acte_carte=4, explorable=True)
        $ salle = _return
        if salle != "go_right" and salle != "go_left":
            if persistent.language == "english":
                show carte_completeEN:
                    linear 0.2 alpha 0.05
            else:
                show carte_completeFR:
                    linear 0.2 alpha 0.05
            show go_left:
                linear 0.2 alpha 0.05
            show go_right:
                linear 0.2 alpha 0.05
            show quit_map:
                linear 0.2 alpha 0.05
    if salle == "go_left":
        hide go_left
        hide quit_map
        if persistent.language == "english":
            show carte_completeEN:
                easeout 0.5 xalign 0.25 alpha 0.5
                easein 0.5 xalign 0.0 alpha 1.0
        else:
            show carte_completeFR:
                easeout 0.5 xalign 0.25 alpha 0.5
                easein 0.5 xalign 0.0 alpha 1.0
        $ renpy.pause(1.0, hard=True)
        jump map1_acte4
    elif salle == "go_right":
        hide go_right
        hide quit_map
        if persistent.language == "english":
            show carte_completeEN:
                easeout 0.5 xalign 0.75 alpha 0.5
                easein 0.5 xalign 1.0 alpha 1.0
        else:
            show carte_completeFR:
                easeout 0.5 xalign 0.75 alpha 0.5
                easein 0.5 xalign 1.0 alpha 1.0
        $ renpy.pause(1.0, hard=True)
        jump map3_acte4
    elif salle == "grande_salle":
        narr "La salle centrale était entièrement vide."
        narr "Des traces de sang recouvraient le sol, les murs et même le plafond."
        narr "Ces traces formaient une colombe rouge, les ailes déployées."
        narr "Au fond de la salle, il y avait une porte monumentale, barricadée par des barres de métal cadenassées."
        narr "Cette fois ci, c'est vraiment la porte de sortie..."
        label porte_gauche_droite:
            narr "À gauche et à droite de la porte, il y a deux petits enfoncements sombres."
            if inventaire["lampe"]["nb"] == 1 and inventaire["battery"]["nb"] >=10:
                menu:
                    "Éclairer le côté gauche":
                        $ update_inventory(inventaire["battery"], balance = -10)
                        narr "En éclairant du côté gauche de la porte, on pouvait voir un message, sûrement écrit par le Bourreau..."
                        nvl clear
                        $ quick_menu = False
                        show MessagePorteGauche with dissolve
                        n ""
                        hide MessagePorteGauche with dissolve
                        $ quick_menu = True
                    "Éclairer le côté droit":
                        $ update_inventory(inventaire["battery"], balance = -10)
                        narr "A droite de la porte, il y avait ce message..."
                        nvl clear
                        $ quick_menu = False
                        show MessagePorteDroite with dissolve
                        n ""
                        hide MessagePorteDroite with dissolve
                        $ quick_menu = True
                    "Ne rien faire":
                        jump map2_acte4
                jump porte_gauche_droite
            else:
                jump map2_acte4
            $ sauvegarder("continuer", montrer = False)
    elif salle == "bonus":
        jump bonus
    elif salle == "quit":
        jump finCarteActe4
    jump map2_acte4
    
label map3_acte4:
    label map3_acte4_:
        nvl clear
        if persistent.language == "english":
            show carte_completeEN:
                xalign 1.0
                linear 0.2 alpha 1.0
        else:
            show carte_completeFR:
                xalign 1.0
                linear 0.2 alpha 1.0
        show go_left:
            linear 0.2 alpha 1.0
        show quit_map:
            linear 0.2 alpha 1.0
        call screen screen_carte3(bonus=True, acte_carte = "4")
        $ salle = _return
        if salle != "go_left":
            if persistent.language == "english":
                show carte_completeEN:
                    linear 0.2 alpha 0.05
            else:
                show carte_completeFR:
                    linear 0.2 alpha 0.05
            show go_left:
                linear 0.2 alpha 0.05
            show quit_map:
                linear 0.2 alpha 0.05
    if salle == "salle_vote":
        narr "La salle de vote est similaire à la nôtre"
        narr "Sur la salle centrale étaient disposées 6 tablettes aux noms suivants :"
        narr "Rosalind, Lise, Erwin, Stéphanie, Ukichiro et Sophie."
        $ sophie["statut"] = "Morte"
        $ stephanie["statut"] = "Morte"
        $ ukichiro["statut"] = "Mort"
        $ renpy.notify("Informations obtenues : Sophie, Stéphanie, Ukichiro")
        narr "Un coffre était au centre de la pièce."
        narr "Il était ouvert."
        narr "Le cadenas détruit, visiblement à l'acide"
        narr "Dedans, un mot, probablement du Bourreau :"
        narr "{i}Vous avez sûrement triché pour ouvrir ce coffre.{/i}"
        narr "{i}Rentrez ceci sur l'une des tablettes de vote : 29-01-2013{/i}"
        narr "{i}Pour la suite, vous ne pourrez plus tricher.{/i}"
        #narr "Il fallait un code à 6 chiffres pour ouvrir le cadenas."
        #narr "Je n'avais aucune idée du code. Et pas le temps pour tester le million de combinaison possible..." #TODO
        narr "Je rentrai le code dans la tablette de Ukichiro."
        narr "Elle semblait charger à l'infini... Ca ne marche pas ? Il faudrait peut-être revenir plus tard."
        $ sauvegarder("continuer")
    elif salle == "salle_labo":
        narr "Le Laboratoire était rempli de matériel de chimie :"
        narr "Des étagères entières de flacons de toutes les couleurs, de livres, de pierres..."
        narr "Des lavabos, des éprouvettes, des hottes..."
        narr "Tout ce dont il fallait pour n'importe quelle expérience !"
        narr "Il y avait même une table d'opération..."
        if une_entrevue_lise:
            $ une_entrevue_lise = False
            li "On pense que c'est ici que le Bourreau nous a implanté nos bombes !"
            erw "Et c'est ici que nous avons désactivé celle de Lise..."
            narr "Un moyen de désactiver la bombe ? Il fallait que j'en sache plus."
            p "Comment ça ?"
            erw "Le Bourreau avait greffé la bombe de Lise {i}sur{/i} son bras..."
            narr "Lise montra une cicatrice sur son bras"
            li "L'enlever a laissé des traces..."
            narr "Lise avait le regard dans le vide"
            p "Vous avez réussi à enlever la bombe de Lise ???"
            erw "Oui."
            erw "Mais je ne suis pas sûr que ça sois efficace."
            p "C'est à dire ? Je ne comprends pas, enlever la bombe, ça nous libère du Bourreau non ?"
            erw "Oui, mais la bombe est bourrée de capteurs..."
            erw "C'est comme ça que le Bourreau sait si on est vivants, et où on est."
            erw "Donc, puisqu'il est parmi nous, il sait que Lise est vivante et qu'on a enlevé sa bombe !"
            li "Je pense qu'il va essayer de m'en remettre une... de force."
            erw "C'est pour ça qu'il ne faut pas les enlever. Du moins, il ne faut pas les enlever bêtement."
            erw "Il faut duper les capteurs."
            narr "Il me fit un clin d'oeil..."
            narr "Puis Lise et lui partirent dans un coin, lire des livres de chimie."
        if not inventaire["poison"]["connu"]:
            $ inventaire["poison"]["connu"] = True
            narr "Sur les étagères il y avait un tube à essai fermé avec un bouchon en liège sur lequel il y avait écrit \"{i}Toxine botulique accélérée{/i}\""
            narr "A en juger le logo rouge, ça m'avait tout l'air d'être du poison..."
        else:
            narr "Et une armoire remplie de poisons en tout genres."
        if inventaire["poison"]["nb"] == 1:
            menu:
                "Reposer la fiole de poison":
                    $ update_inventory(inventaire["lampe"], balance = -1)
                    narr "Je posais la fiole."
                "Ne rien faire":
                    narr "Mieux vaut la garder"
        elif not inventaire["poison"]["used"]:
            menu:
                "Prendre la fiole de poison":
                    narr "Ça pourra être utile"
                    $ update_inventory(inventaire["poison"], balance = 1)
                    narr "Je pris la fiole, en espérant que les chimistes ne le remarquent pas..."
                "Ne pas la prendre":
                    narr "Ça ne me servira à rien"
        $ sauvegarder("continuer")
    elif salle == "salle_chambres":
        narr "Des chambres similaires aux nôtres, numérotée de 4 à 6."
        label chambres_acte4:
            nvl clear
            menu:
                "Regarder chambre 4":
                    narr "La chambre 4 est en désordre. Et encore, le mot est faible. L'armoire est tombée sur le sol, la couette éventrée recouvrant le tiers du lit rougeoyant, gorgé d'un sang qui avait viré au pourpre."
                    $ chambre_acte4_seen_once = True
                    jump chambres_acte4
                "Regarder chambre 5":
                    narr "La chambre est très propre, les lits faits. Sûrement la chambre de Lise et Erwin. Elle est même {i}trop{/i} propre... Dorment-ils carrément dans leur laboratoire ?"
                    jump chambres_acte4
                "Regarder chambre 6":
                    narr "La chambre 6 semblait normale à première vue."
                    jump chambres_acte4
                "Partir":
                    pass
        $ sauvegarder("continuer")
    elif salle == "salle_torture":
        narr "La salle de torture est le symétrique de notre salle d'armes."
        narr "Toujours les mêmes armes alignées aux murs, blancs et immaculés."
        narr "Il y avait beaucoup de sang, mais pas de cadavres."
        if une_entrevue_creature and persistent.glitched:
            $ une_entrevue_creature = False
            narr "Au centre de la pièce, la Créature était enchaînée."
            narr "Enfin, je pouvais la voir."
            nvl clear
            show jumpscare1bis with speedinkdissolve:
                alpha 0.5
            $ renpy.pause(0.2)
            nvl clear
            hide jumpscare1bis with speedinkdissolve
            $ renpy.block_rollback()
            narr "Elle me fixait."
            narr "C'était une hybride entre humain et machine..."
            narr "Je ne sais pas pourquoi, mais sa vue me troublait."
            narr "J'étais absorbé par ce que je voyais. Je ne voyais plus qu'{i}elle{/i}."
            narr "Plus qu'elle."
            narr "{i}Plus qu'elle.{/i}"
            narr "{i}{b}PLUS QU'ELLE.{/b}{/i}"
            nvl clear
            narr "{cps=8}{i}{b}PLUS{w=0.5}{/b}{/i}{/cps}{nw}" with megashake
            narr "{cps=8}{i}{b}QUE{w=0.5}{/b}{/i}{/cps}{nw}" with megashake
            narr "{cps=8}{i}{b}ELLE{w=0.5}{/b}{/i}{/cps}{nw}" with megashake
            nvl clear
            unk "{cps=30}Kurt... Tu dois nous libérer. Tu es le seul à pouvoir briser le cycle.{/cps}{w=0.2}{nw}"
            nvl clear
            $ renpy.block_rollback()
            show black with dissolve
            pause 1.0
            hide black with dissolve
            narr "Je repris conscience, les mains serrées aux barreaux de la salle de torture, une veine sur le front."
            $ renpy.block_rollback()
            narr "Au centre, il y avait la Créature enchaînée."
            narr "Que s'était-il passé ?"
            narr "La créature avait parlé, je ne rêve pas ?"
            narr "Elle semblait maintenant endormie, et affichait une infinie tristesse sur son visage."
            narr "{i}Qui{/i} était-elle ?"
            $ sauvegarder("continuer")
        else:
            narr "La Créature était au centre de la pièce, silencieuse."
            narr "Même en l'observant de loin, elle était effrayante."
            narr "Toute blanche, avec des boulons et des lames incrustées dans les mains..."
            narr "Le plus effrayant, c'était de savoir que ce monstre avait autrefois été humain..."
            $ sauvegarder("continuer")
    elif salle == "salle_mystere":
        narr "Il n'y avait rien."
        narr "Si la prison était symétrique, il aurait du y avoir une pièce."
        narr "Mais là, juste un mur : pas de porte."
        narr "Une colombe était taguée en rouge sur le mur, qui avait l'air d'être repeint."
        narr "Je frappai contre le mur."
        narr "Rien."
        narr "Pourtant, mon instinct me disait qu'il y avait quelque chose derrière."
        narr "Mais comment y accéder ? Et c'était {i}quoi{/i}, derrière ?"
        narr "Je collai l'oreille."
        narr "Il n'y avait pas de bruit, rien..."
        narr "L'oreille sur le mur, et le regard en l'air, quelque chose retint mon attention"
        narr "Au fond du couloir, en haut du mur, il y avait cette inscription :"
        narr "{i}Essaye de rentrer,\n{b}Sherlock{/b}...\nJe t'attends.{/i}"
        narr "Le mot Sherlock était mis en valeur."
        narr "Le Bourreau m'attendait ? Est-ce réellement destiné à moi ?"
    elif salle == "salle_sanitaires":
        narr "Des sanitaires"
        narr "Les portes semblent toutes avoir été enfoncées."
        narr "Un combat avait eu lieu ici."
        narr "Du papier traînait partout."
        narr "Un miroir était brisé, révélant un objet en plastique bleu."
        narr "Je m'approchai et enlevai un fragment du miroir abimé."
        $ update_inventory(inventaire["mp3"], 1)
        narr "Il s'agissait d'un MP3. Comment a-t-il pu arriver là ?"
        $ sauvegarder("continuer")
    elif salle == "go_left":
        hide go_left
        hide quit_map
        if persistent.language == "english":
            show carte_completeEN:
                easeout 0.5 xalign 0.75 alpha 0.5
                easein 0.5 xalign 0.5 alpha 1.0
        else:
            show carte_completeFR:
                easeout 0.5 xalign 0.75 alpha 0.5
                easein 0.5 xalign 0.5 alpha 1.0
        $ renpy.pause(1.0, hard=True)
        jump map2_acte4
    elif salle == "bonus":
        jump bonus
    elif salle == "quit":
        jump finCarteActe4
    jump map3_acte4

