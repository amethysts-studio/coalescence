#==================================#
#============== Maps ==============#
#==================================#
screen screen_carte1(carte_revelee=False, bonus=False, acte_carte=None, explorable=True, quitter=True):
    imagemap:
        if acte_carte == "1":
            ground carte1explore0
        elif acte_carte == "2-1":
            ground carte1explore2
        elif acte_carte == "2-23":
            ground "cartes/carte1explore2.png"
        elif acte_carte == "2-4":
            ground "cartes/carte1explore.png"
        elif acte_carte == "4":
            ground "cartes/carte1exploreacte.png"
        else:
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
            hotspot (177, 1030, 354, 150) action Return("quit")
        if bonus:
            hotspot (158, 1190, 22, 28) action Return("bonus")

screen screen_carte2(bonus=False, acte_carte=None, explorable=True):
    imagemap:
        ground "cartes/transparent.png"
        hover "cartes/carte2_hover.png"

        alpha False

        hotspot (0, 117, 132, 895) action Return("go_left")
        if explorable:
            hotspot (136, 123, 447, 886) action Return("grande_salle")
        hotspot (585, 119, 140, 891) action Return("go_right")

        hotspot (177, 1030, 354, 150) action Return("quit")
        if bonus:
            hotspot (158, 1190, 22, 28) action Return("bonus")

screen screen_carte3(bonus=False, acte_carte=None, explorable=True):
    imagemap:
        if acte_carte == "4":
            ground "cartes/carte3exploreacte.png"
        else:
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
        hotspot (177, 1030, 354, 150) action Return("quit")
        if bonus:
            hotspot (158, 1190, 22, 28) action Return("bonus")
