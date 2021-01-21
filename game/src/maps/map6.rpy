#==================================#
#====== Acte VI : Exploration =====#
#==================================#
label map1_acte6:
    label map1_acte6_:
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
        call screen screen_carte1(carte_revelee=True, bonus=False, acte_carte = "6")
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
        narr "La salle de vote était vide."
        narr "Sur les 6 écrans sur la table, seuls deux étaient bleus."
        if leonhard["statut"] == "Vivant":
            $ var = "Leonhard"
        elif johann["statut"] == "Vivant":
            $ var = "Johann"
        narr "Celui de [var], et le mien."
        narr "Les autres étaient écarlates. Une colombe flottait au centre des écrans."
        $ sauvegarder("continuer")
    elif salle == "salle_archives":
        if johann["statut"] == "Vivant":
            narr "Johann était dans la salle d'archives, en train de feuilleter un livre."
            if une_entrevue_johann:
                if johann["confiance"] < 13:
                    j "Dégage."
                    j "T'as tué Leonhard, tu veux que je te fasse confiance ?"
                    j "Le pire, c'est que j'ai besoin de toi."
                else:
                    j "Salut, Kurt !"
                    j "Je demande pas ça souvent, mais je vais avoir besoin de ton aide."
                    j "Plus besoin de tuer le Bourreau maintenant."
                    j "On va essayer de s'en sortir à trois, comme il avait annoncé au début."
                    p "Tu es sûr qu'il tiendra sa parole ?"
                    j "Oh, oui. Il est trop fier pour transgresser ses propres règles."
                    j "Je pourrai m'occuper de lui une fois qu'on sera sortis de cette prison de merde..."
                    narr "Il me regarda malicieusement."
                    j "Il faut que je t'explique mon plan."
                $ annonce_importante(johann, _("On va tenter un coup de poker."))
                j "J'explique :"
                j "Lise et Erwin vont voter tous les deux pour Erwin. Puisque que c'est une brute, il a plus de chances de gagner que Lise, en combat."
                j "Surtout que j'ai l'impression qu'ils se préparent un arsenal chimique."
                j "Que ce soit contre moi ou contre toi, on perdra."
                j "Par contre, ils ne s'attendent pas à ce qu'on vote tous les deux..."
                j "...pour {i}Lise{/i}."
                narr "Il affichait un sourire carnassier."
                j "Une égalité entre Lise et Erwin, ça te tente ?"
                j "Ils vont devoir s'entre-tuer... C'est {i}tellement cruel{/i} !"
                narr "Il avait l'air aux anges."
                j "De toute façon, tu n'as pas trop le choix."
                narr "Il replongea dans son livre."
                j "Si tu votes pour quelqu'un d'autre, Erwin se battra contre un de nous deux, en on perdra..."
                narr "Sans attendre de commentaires de ma part, il s'éloigna et se mit à fouiller dans les étagères à la recherche d'informations."
            else:
                j "Tu as compris le plan ? Vote pour Lise !"
                narr "Il replongea dans son livre."
        narr "Il y avait peut-être encore quelque chose d'intéressant à trouver parmi tous ces documents."
        narr "Dans un coin de la salle, entre deux étagères poussiéreuses, un très vieil ordinateur diffusait une lumière bleutée."
        narr "Les lettres capitales formaient le mot {b}Index{/b}."
        narr "Il semblait ne pas avoir bougé depuis la dernière fois, comme s'il attendait sereinement que l'on perce les secrets de ce lieu oppressant."
        nvl clear
        jump explore_archives
    elif salle == "salle_chambres":
        label chambres_gauche_acte4:
            nvl clear
            menu:
                "Regarder chambre 1":
                    narr "Les murs de la chambre étaient abîmés, comme si quelqu'un avait gratté le mur..."
                    jump chambres_gauche_acte4
                "Regarder chambre 2":
                    narr "Des traces rouges tachent les quatre murs, et même le plafond."
                    jump chambres_gauche_acte4
                "Regarder chambre 3":
                    narr "Un mot était glissé dans le placard."
                    narr "{i}Protège Kurt. C'est mon élu.{/i}"
                    narr "Moi ? Mais pourquoi ?"
                    narr "Et à qui est destiné ce mot ?"
                    jump chambres_gauche_acte4
                "Partir":
                    pass
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
        jump map2_acte6
    elif salle == "quit":
        jump finCarteActe6
    jump map1_acte6
    
label map2_acte6:
    label map2_acte6_:
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
        call screen screen_carte2(bonus=False, acte_carte=6, explorable=True)
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
        jump map1_acte6
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
        jump map3_acte6
    elif salle == "grande_salle":
        narr "La salle centrale était entièrement vide."
        narr "Des traces de sang recouvraient le sol, les murs et même le plafond."
        narr "Ces traces formaient une colombe rouge, les ailes déployées."
        narr "Au fond de la salle, il y avait une porte monumentale, barricadée par des barres de métal cadenassées."
        narr "Cette fois ci, c'est vraiment la porte de sortie..."
        label porte_gauche_droite_acte6:
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
                        jump map2_acte6
                jump porte_gauche_droite_acte6
            else:
                jump map2_acte6
            $ sauvegarder("continuer", montrer = False)
    elif salle == "bonus":
        jump bonus
    elif salle == "quit":
        jump finCarteActe6
    jump map2_acte6
    
label map3_acte6:
    label map3_acte6_:
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
        call screen screen_carte3(bonus=True, acte_carte = "6")
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
        narr "Elles étaient toutes marquées d'une colombe rouge, sauf celles d'Erwin et Lise."
        $ sophie["statut"] = "Morte"
        $ stephanie["statut"] = "Morte"
        $ ukichiro["statut"] = "Mort"
        $ sauvegarder("continuer")
    elif salle == "salle_labo":
        if lise["confiance"]+erwin["confiance"] < 30:
            if une_entrevue_lise:
                $ une_entrevue_lise = False
                erw "Kurt, tu n'es pas le bienvenu ici. Pars."
                narr "Erwin avait l'air assez agacé, et il me claqua la porte au nez."
                narr "Je suppose que je vais devoir les éviter un moment..."
            else:
                narr "La porte était toujours fermé, Erwin et Lise préparant quelque chose..."
        else:
            narr "Le Laboratoire était rempli de matériel de chimie :"
            narr "Des étagères entières de flacons de toutes les couleurs, de livres, de pierres..."
            narr "Des lavabos, des éprouvettes, des hottes..."
            narr "Tout ce dont il fallait pour n'importe quelle expérience !"
            narr "Il y avait même une table d'opération..."
            if une_entrevue_lise:
                $ une_entrevue_lise = False
                li "Kurt ! Salut, qu'est-ce que tu viens faire ici ?"
                p "Je... suis perdu. Je ne sais plus vers qui me tourner, vers qui faire confiance."
                erw "Tu peux nous faire confiance."
                erw "Vote pour moi au prochain tour. On sera les trois à s'en sortir."
                narr "J'hochai la tête, toujours incertain."
                #TODO proposer enlever bombe
                narr "Je partis vers le matériel de Chimie. Il y avait vraiment de quoi tuer quelqu'un avec tout ça..."
            if not inventaire["poison"]["connu"]:
                $ inventaire["poison"]["connu"] = True
                narr "Sur les étagères il y avait un tube à essai fermé avec un bouchon en liège sur lequel il y avait écrit \"{i}Toxine botulique accélérée{/i}\""
                narr "A en juger le logo rouge, ça m'avait tout l'air d'être du poison..."
            else:
                narr "Une armoire remplie de poisons en tout genres attira mon attention."
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
        label chambres_droite_acte6:
            nvl clear
            menu:
                "Regarder chambre 4":
                    narr "La chambre 4 est en désordre. Et encore, le mot est faible. L'armoire est tombée sur le sol, la couette éventrée recouvrant le tiers du lit rougeoyant, gorgé d'un sang qui avait viré au pourpre."
                    if chambre_acte4_seen_once:
                        narr "Les meubles avaient bougé depuis la dernière fois."
                        narr "La poussière sur le sol, ou plutôt le manque de poussière, indiquait qu'on avait déplacé l'armoire."
                        narr "En fouillant à l'intérieur, je trouvai des photos, cachées en dessous d'une des planches."
                        narr "Les photos avaient était prises ici, pendant les premiers Jeux. Rosalind était sur toutes ces photos."
                        narr "Elle avait l'air en grande souffrance."
                        narr "Derrière les photos était écrit : {i}Elle n'a toujours pas expié ses péchés. Je vais la faire tenir encore un peu.{/i}"
                    jump chambres_droite_acte6
                "Regarder chambre 5":
                    narr "La chambre est très propre, les lits faits. Sûrement la chambre de Lise et Erwin. Elle est même {i}trop{/i} propre... Dorment-ils carrément dans leur laboratoire ?"
                    jump chambres_droite_acte6
                "Regarder chambre 6":
                    narr "La chambre 6 semblait normale à première vue."
                    narr "Une bosse suspecte sur le lit attira mon attention."
                    narr "En soulevant le drap du lit, je trouvai un appareil photo."
                    narr "Vieux modèle, argentique. Les lettres R et L sont gravées dessous l'appareil."
                    jump chambres_droite_acte6
                "Partir":
                    pass
            $ sauvegarder("continuer")
    elif salle == "salle_torture":
        narr "La salle de torture est le symétrique de notre salle d'armes."
        narr "Toujours les mêmes armes alignées aux murs, blancs et immaculés."
        narr "Il y avait beaucoup de sang, mais pas de cadavres."
        narr "La créature n'était plus dans la pièce..."
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
        narr "{i}Essaye de rentrer, Sherlock... Je t'attends.{/i}"
        narr "Le Bourreau m'attendait ? Est-ce réellement destiné à moi ?"
        $ sauvegarder("continuer")
    elif salle == "salle_sanitaires":
        narr "Des sanitaires"
        narr "Les portes semblent toutes avoir été enfoncées."
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
        jump map2_acte6
    elif salle == "bonus":
        jump bonus
    elif salle == "quit":
        jump finCarteActe6
    jump map3_acte6
