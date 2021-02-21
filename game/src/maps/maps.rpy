#==================================#
#============== Maps ==============#
#==================================#
screen screen_carte1(carte_revelee=False, bonus=False, acte_carte=None, explorable=True, quitter=True):
    
    style_prefix "coal"
    
    use repartition_persos_map_1(acte_carte)
    use kurt_position_on_map("left")

    imagemap:
        at smooth(0.5)
        
        ground "cartes/transparent.png"
        hover "cartes/carte1_hover.png"

        alpha False

        if explorable:
            hotspot (90, 120, 204, 361) action Return("salle_vote")
            hotspot (400, 220, 229, 265) action Return("salle_archives")
            hotspot (90, 485, 204, 262) action Return("salle_chambres")
            hotspot (400, 485, 229, 259) action Return("salle_exec")
            hotspot (92, 746, 202, 264) action Return("salle_reserve")
            hotspot (399, 744, 228, 262) action Return("salle_sanitaires")
        if carte_revelee:
            hotspot (633, 124, 87, 888) action Return("go_right")

    if quitter:
        button:
            at smooth()
            ypos 1070
            text _("Arrêter l'exploration") at truecenter
            action Return("quit")

screen screen_carte2(bonus=False, acte_carte=None, explorable=True):

    use kurt_position_on_map("center")

    imagemap:
        ground "cartes/transparent.png"
        hover "cartes/carte2_hover.png"

        alpha False

        hotspot (0, 117, 132, 895) action Return("go_left")
        if explorable:
            hotspot (136, 123, 447, 886) action Return("grande_salle")
        hotspot (585, 119, 140, 891) action Return("go_right")

    button:
        at smooth()
        ypos 1120
        text _("Quitter") at truecenter
        action Return("quit")

screen screen_carte3(bonus=False, acte_carte=None, explorable=True):

    use repartition_persos_map_3(acte_carte)
    use kurt_position_on_map("right")


    imagemap:
        at smooth(1.0)
        
        ground "cartes/transparent.png"
        hover "cartes/carte3_hover.png"

        alpha False
        if explorable:
            hotspot (421, 120, 209, 363) action Return("salle_vote")
            hotspot (90, 222, 227, 263) action Return("salle_labo")
            hotspot (421, 483, 208, 263) action Return("salle_chambres")
            hotspot (90, 485, 227, 261) action Return("salle_torture")
            hotspot (413, 746, 216, 264) action Return("salle_mystere")
            hotspot (90, 747, 230, 268) action Return("salle_sanitaires")

        hotspot (0, 124, 87, 888) action Return("go_left")

    button:
        at smooth()
        ypos 1120
        text _("Quitter") at truecenter
        action Return("quit")
