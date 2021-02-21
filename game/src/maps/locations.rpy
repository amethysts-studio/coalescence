# Location of characters through maps, time & scenarios
screen localisation(perso, coords):
    text perso["nom"][0] color perso["color"] pos coords xanchor 0.5 font gui.default_font

screen kurt_position_on_map(map_position): # map_position is "left", "center" or "right"
    if map_position == kurt["location"]["side"]:
        text _("Moi") color "#f00" pos kurt["location"]["coords"] xanchor 0.5 font gui.default_font

# Map 1 (left)
screen repartition_persos_map_1(acte_carte):
    if acte_carte == "1":
        use localisation(leonhard, (350, 680))
        use localisation(johann, (350, 580))
        use localisation(alan, (350, 480))

        use localisation(emmy, (180, 420))
        use localisation(isaac, (260, 420))


    elif acte_carte == "2-1": # Emmy condamnée
        use localisation(leonhard, (140, 420))
        use localisation(emmy, (110, 630))
        use localisation(johann, (220, 420))
        use localisation(isaac, (560, 690))
        use localisation(alan, (520, 970))

    elif acte_carte == "2-23": # Emmy morte tuee par Alan
        use localisation(leonhard, (140, 420))
        use localisation(emmy, (550, 830))
        use localisation(johann, (220, 420))
        use localisation(isaac, (560, 690))
        use localisation(alan, (110, 630))

    elif acte_carte == "2-4": # Alan condamné
        use localisation(leonhard, (140, 420))
        use localisation(emmy, (440, 970))
        use localisation(johann, (220, 420))
        use localisation(isaac, (560, 690))
        use localisation(alan, (110, 630))

    elif acte_carte == "4":
        use localisation(johann, (220, 420))
        use localisation(rosalind, (110, 630))
        use localisation(leonhard, (550, 780))


screen repartition_persos_map_3(acte_carte):

    if acte_carte == "4":
        use localisation(lise, (140, 420))
        use localisation(erwin, (220, 420))
