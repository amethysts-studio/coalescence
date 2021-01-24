#==================================#
#====== Acte I : Simple visit =====#
#==================================#

label first_map:
    label first_map_:
        nvl clear
        show carte1explore0:
            linear 0.2 alpha 1.0
        call screen screen_carte1(quitter = False)
        $ salle = _return
        show carte1explore0:
            linear 0.2 alpha 0.05
        n "\n\n\n\n\n{nw}"
    if salle == "salle_vote":
        narr "C'est la salle d'où l'on vient."
        if inventaire["usb_key"]["nb"] == 0:
            narr "Apparemment, le Bourreau l'appelle la \"Salle de vote\"."
            narr "Il ne sert à rien d'y retourner maintenant, il faut trouver la clé USB qu'à caché le Bourreau."
        else:
            narr "Il est temps d'y retourner pour voir le message du Bourreau."
            hide carte1explore0 with Dissolve(1.0)
            $ quick_menu = True
            jump suite_map_0
    elif salle == "salle_archives":
        narr "Il est écrit sur la porte : \"Archives\""
        narr "Cette salle est fermée à clé..."
    elif salle == "salle_chambres":
        narr "Il y a 3 chambres numérotées 1, 2 et 3."
        narr "Les numéros sont écrits en grand et en rouge sur la porte."
        if first_visit_chambres_map1 and inventaire["usb_key"]["nb"] == 0:
            $ first_visit_chambres_map1 = False
            narr "Alan et Johann s'activèrent et fouillèrent les chambres 1 et 2, tandis que moi et Leonhard fouillâmes la chambre restante."
            narr "La chambre n'étant constituée que de deux lits, une chaise et une armoire, la fouille fut rapide."
            l "C'est étrange, ce qu'il se passe, non ?"
            p "Oui, c'est clair... Ça m'inquiète un peu..."
            l "Vous avez raison."
            narr "Leonhard était le seul à vouvoyer tout le monde. Du coup, je me sentais obligé de le vouvoyer aussi."
            narr "Il était très propre sur lui, comme un gentleman anglais, malgré son nom à consonance allemande."
            l "Le Bourreau est un malade mental."
            p "Vous le connaissez ?"
            narr "Leonhard eu un petit rire cynique."
            l "Si je le connaissais, je l'aurais envoyé derrière les barreaux depuis bien longtemps..."
            l "Mais oui, j'ai déjà entendu parler de lui... Et même plus."
            l "Nous avons tout un dossier sur lui."
            l "Mais bon, {i}je{/i} ne crains rien."
            l "Et vous aussi, vous serez en sécurité, si vous me faites confiance."
            p "Pourquoi ?"
            l "Je ne peux pas te le dire maintenant. Mais nous pouvons nous allier."
            l "Johann me fait déjà confiance."
            l "Le Bourreau a dit que trois personnes s'en sortiront !"
            l "Vous comptez nous joindre ?"
            menu:
                "J'y réfléchirai !":
                    p "J'y réfléchirai !"
                    $ modif_confiance([leonhard], [1])
                    l "D'accord."
                    l "Dis moi ta réponse rapidement, les places sont comptées..."
                    narr "Il était assez direct, mais il n'avait pas tort."
                "Johann vous fait déjà confiance ?":
                    p "Johann vous fait déjà confiance ? C'est rapide..."
                    p "Vous vous connaissiez déjà avant ?"
                    l "Non, nous avons juste parlé quand vous étiez en train de dormir."
                    $ modif_confiance([leonhard], [-1])
                    l "Être suspicieux est quelque chose de compréhensible, mais si je vous propose une alliance, c'est parce que je pensais que je pouvais avoir confiance en vous..."
                "Que savez-vous sur le Bourreau ?":
                    p "Vous avez un dossier sur le Bourreau ? Vous pouvez m'en dire plus ?"
                    l "Oh, non. Je ne sais pas ce que nous allons devenir, et j'aimerai me garder un peu d'avance, vous comprenez."
            narr "Nous fûmes interrompus par Alan et Johann"
            ala "C'est vide. Tous les tiroirs sont vides, j'ai rien trouvé..."
            j "Allons chercher plus loin."
    elif salle == "salle_exec":
        narr "La Salle d'armes est en fait une cellule de prison remplie d'armes blanches."
        narr "Elle est tapissée d'une étrange bâche blanche, et au centre trône une guillotine..."
        if inventaire["usb_key"]["nb"] == 0:
            narr "Toujours aucune trace de la clé USB."
    elif salle == "salle_reserve":
        narr "La Réserve est une salle remplie d'étagères."
        narr "Du papier, des vieux livres, des vêtements, de la nourriture en boite... Il y avait de tout !"
        narr "Il y a au moins de quoi tenir un an, en terme de nourriture."
        if inventaire["usb_key"]["nb"] == 0:
            j "Hum, étrange."
            ala "Quoi ?"
            j "Toutes les pièces sont plus ou moins vides, avec le strict minimum..."
            j "...sauf celle-là, qui regorge d'objets inutiles !"
            narr "Leonhard se tourna instantanément vers une étagère, écarta deux canettes de boisson énergisante, et pris un objet dans sa main."
            l "La clé USB. Voici."
            narr "Johann, comme à son habitude, replaça ses lunettes."
            j "Bien vu, Leonhard. Allons voir ce qu'elle contient."
            $ update_inventory(inventaire["usb_key"], +1, montrer = True)
    elif salle == "salle_sanitaires":
        narr "Des toilettes à gauche, des douches à droite..."
        narr "Le Bourreau a vraiment pensé à tout..."
        narr "...sauf à l'hygiène : les toilettes sont pour la plupart bouchées, et le carrelage surplombé d'une bonne couche de poussière, de boue et de... sang ?"
        if inventaire["usb_key"]["nb"] == 0:
            narr "Inutile de chercher la clé USB ici..."
    jump first_map

