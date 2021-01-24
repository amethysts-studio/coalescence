label ending_solitaire:
    # erwin vs lise, on se cache par défaut
    j "Il faut se cacher. Quand Erwin apprendra les résultats, il va vouloir nous tuer plutôt que de faire ce qu'il devrait."
    p "Mais ce n'est pas les Règles !"
    p "Il n'est pas censé nous tuer : le Bourreau nous défendra, non ?"
    #TODO choix dire ça (confiance ---) ou go se cacher
    j "Pas vraiment, je ne pense pas."
    j "Tu fais plus confiance au Bourreau ou à m...{w=0.5}{nw}"
    erw "{b}Putain de MERDE !!!{/b}" with sshake
    narr "Johann me regarda, inquiet."
    j "Il a compris."
    p "On va où ?"
    #TODO choix dire d'aller se cacher en archives OU autre part (confiance ---) ou go se cacher ou confiance Bourreau (protège d'Erwin !) ce qui est mal accueilli par Johann (exemple d'Isaac)
    j "Dans la salle d'archives"
    j "J'ai préparé de quoi la barricader."
    $ sauvegarder("continuer")
    nvl clear
    #TODO sound boom
    n "{nw}" with sshake
    nvl clear
    narr "Erwin cognait contre la porte des archives."
    narr "Il se lançait de toutes ses forces contre la porte."
    j "Il n'arrivera jamais à la casser."
    j "Et même si c'est le cas..."
    j "On va partir."
    p "Hein ?"
    j "Tu sais, dans l'aile droite, il y a une salle dans laquelle on ne peut pas rentrer."
    p "Et tu sais comment y rentrer ?"
    narr "Il hocha de la tête."
    j "Dans un des livres, il y a un bouton qui permet de débloquer un passage sous-terrain."
    narr "J'étais abasourdi."
    j "Il permet au Bourreau de se cacher pendant les folies meurtrières de sa bête."
    narr "Johann me tournait le dos, la main sur l'étagère."
    p "Et c'est quel livre ? Comment tu l'as découvert ?"
    j "Chhht, ne pose pas de questions idiotes."
    narr "J'entendis un clic, à peine perceptible à travers le bruit d'Erwin."
    narr "L'étagère s'enfonça dans le mur, et Johann recula de deux pas. Une échelle en bois apparaissait là où se trouvait la bibliothèque."
    j "Il y a un ordinateur pour faire des recherches, je l'ai juste utilisé avec la bonne recherche."
    j "Maintenant dépêche-toi, l'étagère se replace après 2 minutes. Passe en premier."
    narr "Une fois Johann descendu, l'étagère se replaça."
    narr "Le noir complet, et le silence."
    narr "Je commençai à marcher de l'autre côté du couloir, quand quelque chose me toucha la main."
    j "Kurt, non."
    #TODO insister pour y aller
    j "Le Bourreau est certainement là-dedans. C'est dangereux."
    p "Mais... c'est pas un de nous 4 ?"
    narr "Johann ricana."
    j "Peuh, non..."
    j "T'as pas encore compris, petit innocent..."
    narr "Johann resta silencieux."
    p "Mais est-ce que..."
    narr "Il mit son doigt devant sa bouche, en signe de silence."
    narr "Erwin avait réussi à rentrer dans la salle d'archives."
    erw "{b}RAAAAH{/b}" with sshake
    narr "Des bruits de chute."
    narr "Des étagères qui tombent."
    narr "Un grand fracas au dessus de nos têtes."
    narr "Les minutes passèrent sans qu'Erwin ne calme sa rage."
    narr "Soudain, le silence."
    j "Il est partit."
    p "Il va essayer d'enlever sa bombe." #TODO Kurt dit ça s'il est au courant ofc
    j "Si la bombe explose avant l'heure prévue, ça veut dire que le Bourreau est juste là..."
    narr "Il montra le bout du couloir."
    j "De l'autre coté."
    narr "Nerveux, Johann toucha ses lunettes."
    #TODO bruit boom
    narr "Les bombes d'Erwin et de Lise avaient explosé."
    narr "Johann sourit."
    narr "Il avait l'air fier de lui, et son rire sonnait plus comme de la démence que du bonheur."
    j "Il ne reste que toi, Kurt !"
    j "Ou bien Klaus ?"
    narr "Johann s'approcha fièvreusement de moi."
    narr "Je courus vers l'échelle et appuya sur le bouton intérieur pour ouvrir le passage."
    j "Faisons un deal."
    j "Il me manque une seule information, Kurt. Pourquoi es-tu là ?"
    narr "Je montai à l'échelle."
    j "Si tu me le dis, je te révèle le nom du Bourreau."
    narr "J'étais dans la salle d'archives."
    narr "Lui, dans le tunnel secret, 2 mètres en dessous."
    j "DIS-MOI !"
    $ countdown_time = 12.0
    menu:
        "\"Je ne sais honnêtement pas pourquoi je suis là\"":
            p "Honnêtement, Johann, je ne sais pas pourquoi je suis là."
            p "Vraiment pas."
            p "Maintenant, monte."
            jump ending_solitaire_with_johann
        "Bloquer Johann dans le passage secret":
            p "Non."
            narr "J'agrippai la bibliothèque, et la renversa sur l'entrée du tunnel."
            narr "Des centaines de livres tombèrent sur Johann, et la bibliothèque obstruait le passage."
            narr "Je poussai la bibliothèque centrale et la fit tomber sur la première bibliothèque."
            narr "Ça allait retenir Johann un bon moment, j'avais le temps de fuir."
            narr "Un bruit sourd retentit dans la prison. C'était ouvert."
            narr "La Grande Salle baignait dans la lumière."
            if amour > 15:
                jump ending_solitaire_with_executioner
            else:
                jump ending_solitaire_alone
        "\"Sortons de la prison d'abord\"":
            p "On a plus important que ça à faire, Johann."
            p "Foutons le camp d'ici d'abord."
            jump ending_solitaire_with_johann
        "Ne rien dire" ("default"):
            jump ending_solitaire_say_nothing

label ending_solitaire_say_nothing:
    j "Tu ne veux pas me le dire ?"
    narr "Il secoua la tête de gauche à droite."
    j "Sortons d'ici. On verra bien au commissariat. Tu seras interrogé de toute manière."
label ending_solitaire_with_johann:
    narr "Johann passa devant moi, et nous sortîmes de la salle d'archives."
    narr "Pas de traces d'Erwin ni de Lise."
    narr "La Grande Salle était illuminée d'un blanc qui perçait les yeux."
    p "Enfin, la lumière..."
    narr "Nous étions libres."
    j "Il est temps de partir, Kurt !"
    narr "Il replaça ses lunettes dans un sourire et disparut dans la lumière."
    $ fin = 2
    jump game_over
label ending_solitaire_with_executioner:
    narr "Une silhouette capuchée m'attendait au milieu de la salle."
    b "Tu as réussi !"
    b "Tu es le seul survivant..."
    b "Ca n'a pas été facile, Klaus, mais on l'a fait !"
    narr "Le Bourreau enleva sa capuche."
    isa "Et ben dit donc, Kurt, pourquoi cette tête ?"
    isa "J'ai réussi à le faire, après ces dix horribles jeux."
    isa "Mais tu sais, il fallait que je le fasse."
    isa "Il fallait que je corrige certaines choses."
    isa "Tu sais, tous ceux qui t'ont fait du mal."
    isa "J'ai tué tout le monde !"
    narr "Isaac sourit béatement."
    isa "Tu es fier de moi, mon amour ?"
    isa "Je t'ai construit un nouveau monde, un monde gentil et rempli d'amour."
    isa "Plus personne n'embêtera Klaus."
    isa "Viens avec moi, on sort de cet endroit répugnant..."
    narr "Isaac me prit par la main et sortit dehors."
    narr "Il faisait beau, et les oiseaux chantaient."
    isa "Tu entends, ce chant, Kurt ?"
    isa "C'est une colombe..."
    $ fin = 1
    jump game_over
label ending_solitaire_alone:
    narr "J'étais enfin libre."
    narr "J'avançai, sans trop y croire, vers la lumière."
    narr "Il ne restait plus que moi seul, au final..."
    $ fin = 3
    jump game_over

#   if fin_vote_4 != "leonhard_mort":
#       l "Vous avez vu dans la Grande Salle ?"
#       l "À coté de la porte,"
#       l "{i}Love is what SUCKERS elaborate{/i}"
#       l "Il y a aussi cela :"
#       l "{i}Executioner's reward is worth it, Mr. NIGHTINGALE{/i}"
#       l "Avez-vous une idée de ce que cela signifie ?"
#       l "Erwin ?"
#       erw "Euh, non, je ne vois pas..."
#       l "Lise ?"
#       li "Non, vraiment, je ne sais pas..."
#       l "Kurt, tu as une idée ?"
#       l "Et bien tout d'abord, je suis allé me renseigner dans les Archives, et j'ai obtenu des réponses..."
#       l "Le Nightingale, Rossignol en français..."
#       l "...était le surnom d'un membre d'une organisation homophobe américaine, Faithful Word Baptist Church"
#       l "Ce dernier n'aimait pas vraiment les homosexuels..."
#       l "Et afin de leur faire comprendre, il les castrait..."
#       l "Le Rossignol était un malade qui aimait faire souffrir les homosexuels..."
#       r "Un vrai psychopathe..."
#       l "Un psychopathe de la même trempe que le Bourreau !"
#       narr "Leonhard s'expliqua :"
#       l "{i}Executioner's reward is worth it, Mr. NIGHTINGALE{/i}..."
#       l "En prenant les premières lettres de chaque ligne..."
#       l "... on obtient E. R. W. I. N"
#       narr "Tout le monde regarda en sa direction"
#       erw "Quoi ? Vous m'accusez d'être le Rossignol ?"
#       l "Arrête de faire l'innocent, Erwin. J'ai beaucoup trop de preuves contre toi..."
#       narr "Après un silence, Erwin avoua"
#       erw "Très bien, tu as découvert mon secret."
#       erw "Je n'ai jamais intoxiqué de villages !"
#       erw "La vrai raison pour laquelle je suis ici..."
#       erw "... c'est parce que le Bourreau veut punir le Rossignol"
#       erw "C'est pour ça que le Bourreau veut me tuer."
#       l "Oh non, je ne crois pas !"
#       l "Le texte est en anglais, car c'est votre pays natal, n'est-ce-pas ?"
#       narr "Erwin recula d'un pas"
#       erw "Certes..."
#       l "Le texte dit clairement :\n\n{i}La récompense du Bourreau vaut le coup, Mr. Nightingale{/i}\n\nsommes-nous d'accord ?"
#       narr "Erwin grommela :"
#       erw "Oui..."
#       erw "Je vois où vous voulez en venir. Et c'est faux."
#       l "Vous n'êtes pas, comme nous tous, {i}victime{/i} du Bourreau..."
#       narr "Erwin regarda partout autour de lui, paniqué"
#       l "...vous êtes son {i}associé{/i}."

#TODO faire une fin "repeat" en mode 1 jour sans fin


# ======== FINS ==========================================================================================================

label ending_bomb:
    narr "Erwin était mort."
    narr "Lise, traumatisée."
    $ sauvegarder("continuer")
    nvl clear
    narr "Lise était enfermée dans le Laboratoire depuis maintenant 15 minutes."
    narr "La chimiste sombrait dans la folie..."
    narr "Elle en voulait à tout le monde."
    narr "On entendait du bruit dans le labo."
    narr "Des bruits de liquides, mais aussi des râles de Lise."
    narr "Ce qu'elle faisait dans le laboratoire..."
    l "Une bombe."
    narr "Elle allait tous nous tuer."
    l "Elle construit une bombe."
    l "Elle s'en fout de tout, elle va tout faire péter... Même elle."
    $ annonce_importante(leonhard, _("Elle va tout détruire."))
    narr "Johann hocha la tête."
    j "C'est bon, ça !"
    p "Pardon ?"
    j "On va pouvoir s'en sortir, grâce à elle !"
    l "Comment ça ?"
    narr "Johann leva les yeux au ciel."
    j "Vous êtes {i}stupides{/i} ou quoi ?"
    j "Si la bombe explose, tout le monde meurt !"
    j "Tout le monde... {i}même le Bourreau{/i} !"
    j "Je vous rappelle qu'il est toujours parmi nous."
    p "Tu es sûr de ça ?"
    narr "Johann ne prit même pas le temps de relever ma remarque et continua."
    j "Donc, il va devoir la tuer avant qu'elle ne le tue."
    j "Et c'est {i}là{/i} qu'on peut le piéger."
    j "Le Bourreau a toutes les clés : il peut même ouvrir les portes verrouillées."
    j "À un moment ou un autre, il va devoir rentrer dans le labo !"
    j "Et si Lise lui prépare une surprise..."
    $ annonce_importante(johann, _("On pourra lui régler son compte."))
    narr "Leonhard restait dubitatif."
    l "Mais si le Bourreau tue Lise, il restera trois personnes !"
    l "Nous pourrions le laisser faire... Et nous serons libres !"
    p "Qui vous dit qu'il ne nous as pas menti ? Êtes-vous sûrs qu'il va tenir sa parole et nous libérer une fois arrivés à 3 ?"
    j "Tu n'as pas tort. Mais cette fois, il va la tenir."
    j "Je te le promets."
    narr "Il se tourna vers Leonhard."
    j "On ne peut pas juste le laisser faire et partir..."
    j "Il faut le piéger !"
    j "J'ai vraiment envie de savoir {i}qui{/i} il est."
    l "Justement. Tu ne joues pas à son Jeu. Tu vas te faire avoir..."
    l "En plus, il faudra beaucoup de chance pour que tout marche..."
    l "En premier, il faut convaincre Lise de se retourner contre le Bourreau, et pas contre le monde entier."
    l "Ensuite... C'est quoi ton plan ?"
    narr "Le sourire de Johann était aussi rassurant qu'inquiétant."
    j "On va laisser Lise se débrouiller. Si on la force à ouvrir la porte, elle aura peur et elle refusera."
    j "Il faut lui montrer qu'on lui fait confiance !"
    j "Le Bourreau peut rentrer et tuer Lise, de n'importe quelle manière. Il va falloir se préparer à toutes les éventualités."
    j "Je ne sais pas si vous avez regardé ce qu'il y a dans le labo. Il y a énormément de matière première. Et il y a aussi des équipements !"
    j "Il y a de quoi renverser une baignoire d'acide chlorhydrique sur le Bourreau."
    l "Et c'est ce que tu veux faire ?"
    j "Parfaitement."
    narr "Leonhard n'avait pas l'air convaincu."
    j "Rapide, efficace... Tu as une meilleure idée, peut-être ?"
    narr "Il grimaça."
    l "Ça va pas être facile..."
    l "Mais bon, c'est mieux que rien."
    l "Qui veut se charger de la négociation avec Lise ?"
    #TODO : Absolument pas Kurt si c'est lui qui a tué Erwin ...
    j "Kurt s'entend mieux que moi avec Lise. Je peux tenter quelque chose en dernier recours, mais je ne garantis rien."
    p "Je vais m'en charger."
    $ sauvegarder("continuer")
    nvl clear
    # discussions pour augmenter la confiance de Lise : l'amadouer. Ca peut ressembler à un dating sim sur le principe
    narr "Je frappai à la porte."
    narr "Rien. Aucun bruit."
    p "Lise ?"
    narr "Des bruits venaient du laboratoire. Lise était en pleine effervescence."
    $ annonce_importante(kurt, _("J'ai un deal à te proposer"))
    li "..."
    narr "Elle avait arrêté de bouger."
    narr "C'était déjà du temps de gagné."
    p "Arrête de construire ta bombe."
    li "Pourquoi ?"
    narr "Elle parlait entre ses dents. Sa voix était tremblante. Elle se retenait de hurler."
    p "Tu vois, le Bourreau..."
    menu:
        "On va découvrir qui il est":
            p "... on peut savoir qui c'est, si tu es avec nous."
            p "Tu ne veux savoir qui a tué ton mari ?"
            p "Ou tu préfères partir sans connaître la Vérité ?"
            narr "Lise resta silencieuse pendant un moment."
            li "Je jure de détruire toute sa famille."
            p "Je prends ça pour un oui."
            $ modif_confiance([lise], [1])
            narr "Je fis signe à Johann. Tout se passait bien."
        "On va le tuer":
            p "... on a réfléchit à un moyen de le tuer."
            li "Ce que je prépare va déjà tuer tout le monde..."
            li "Va te faire voir."
            $ modif_confiance([lise], [-2])
            p "Non, attends, Lise."
    p "On a besoin de toi."
    p "Johann a un plan."
    p "Je peux continuer ?"
    li "..."
    p "Je prends ça pour un oui..."
    li "Balance."
    li "BALANCE TON FOUTU PLAN !!!"
    narr "Je lui expliquai le plan."
    $ sauvegarder("continuer")
    nvl clear
    li "Maintenant, dégage."
    narr "Johann, Leonhard et moi attendions dans la Grande Salle."
    l "Elle a accepté ?"
    p "On ne sait pas. Elle n'a jamais refusé, en tout cas. Et elle a écouté le plan en entier."
    l "Putain..."
    l "Si vous me cherchez, je serai dans la salle d'archive. Il faut absolument que j'explore certaines pistes avant... que ça ce finisse."
    narr "Il partit vers l'aile gauche."
    $ sauvegarder("continuer")
    nvl clear
    narr "Quelques minutes s'était écoulées depuis ma discussion avec Lise."
    narr "Leonhard était introuvable."
    narr "Alors que je retournai dans la Grande Salle, un tintement vint rompre le silence."
    narr "Près du laboratoire, des clés rebondirent sur le sol."
    narr "Le Bourreau."
    narr "Sa silhouette se détachait de l'obscurité, assez claire pour que je puisse la voir tenir un pistolet, mais trop sombre pour deviner son identité."
    unk "Je suis le Bourreau."
    p "Je sais."
    b "Ne me regarde pas."
    narr "Sa voix me semblait familière"
    if persistent.fin_bombe_lise == None:
        $ persistent.fin_bombe_lise = True
        b "Ceci ne fait plus partie du Jeu."
        b "Je dois tuer Lise..."
        b "Sinon, elle nous tuera tous."
        b "Une fois que ça sera fait, le Jeu s'arrêtera. Je te le promets."
        b "Laisse-moi m'approcher du Laboratoire."
        narr "Je reculai et me tournai."
        narr "C'est ce qu'il fallait faire."
        narr "Il fallait qu'il tombe dans notre piège."
        narr "La pression montait."
        narr "Notre seule chance de survie reposait sur Lise."
        narr "Le Bourreau allait-il tomber dans le piège ?"
        narr "Je l'observais discrètement."
        narr "Le temps passait au ralenti."
        narr "Le silence régnait dans la salle"
        narr "Le bruit des clés dans la serrure était assourdissant."
        narr "Le Bourreau attendit une seconde avant de passer à l'action..."
        narr "...puis poussa violemment la porte."
        narr "Le flingue à la main, prêt à tirer."
        narr "Lise l'attendait, les bras croisés..."
        narr "Un seau de liquide bleuâtre tomba du plafond."
        narr "Le Bourreau recula de surprise."
        narr "Trop tard."
        narr "Les yeux exorbités."
        narr "Lise cria."
        narr "Elle balança un fumigène."
        narr "Une balle partit du revolver."
        narr "Vacarme dissonant."
        narr "Lise, touchée en pleine tête."
        narr "Le Bourreau, baigné d'acide."
        narr "Il hurla de rage."
        narr "Lise s'effondra."
        narr "Le Bourreau tituba."
        b "{b}VOUS ALLEZ ME LE PAYER !!!{/b}"
        narr "Il trébucha."
        narr "Son visage commençait à fondre."
        narr "Il tenait sa tête entre ses mains..."
        narr "...puis tomba à genoux."
        narr "Il avait perdu."
        narr "Dans son désespoir, il saisit son revolver."
        narr "Il le pointa vers moi."
        b "{b}RAAAAAAAAAAH !!!{/b}" with sshake
        narr "La douleur l'aveuglait."
        narr "Il tira au hasard une seule fois avant de s'effondrer à son tour."
        narr "Loin de moi."
        narr "Il rampait, agonisant."
        narr "Sa tête rebondit contre le sol une dernière fois."
        narr "{i}Mort{/i}."
        $ sauvegarder("continuer")
        nvl clear
        narr "Johann et moi avançâmes cérémonieusement."
        narr "Deux corps gisaient sur le sol."
        j "C'est la fin..."
        narr "Il installa Lise sur la table du laboratoire, et lui ferma les yeux."
        narr "Pendant ce temps, je me penchai vers le Bourreau."
        j "N'y touche pas, Kurt."
        j "Il est encore plein d'acide. Laisse-moi faire."
        narr "Les mains gantées, il écarta la capuche du visage du Bourreau."
        p "Non..."
        narr "Les larmes aux yeux, je me levai."
        j "Je le savais."
        narr "Encore sous le choc, Johann prit le trousseau de clés qui pendait à la ceinture du Bourreau."
        narr "Nous nous dirigeâmes vers la grande porte, tremblants."
        narr "En quittant la prison, je repensais à tous ce qui s'était passé."
        narr "Ce qui était derrière nous allait me hanter à vie."
        narr "Le Bourreau... pourquoi fallait-il que ce soit lui ?"
        $ annonce_importante(johann, "Isaac...")
        $ persistent.know_isaac = True
        $ fin = 2
        jump game_over
    else:
        unk "J'ai entendu ton accord avec Lise."
        narr "Je frissonnai malgré la chaleur."
        narr "Il avait gagné."
        unk "Tu vas jouer à un dernier jeu:"
        unk "Prends les clés et ouvre la porte"
        p "..."
        narr "J'étais condamné."
        menu:
            "Obéir":
                narr "Je m'approchai de la porte lentement"
                narr "Alors que je me penchai pour attraper les clés du laboratoire, je vis un sourire carnassier se dessiner sur la silhouette du Bourreau"
                narr "Je pris les clés sur le sol et les mis dans la serrure"
                narr "Le bourreau avait un doigt sur les lèvres, en signe de silence"
                narr "J'ouvris la porte, et tout se passa en une fraction de seconde"
                narr "J'entrai dans le laboratoire."
                narr "Lise me balança un liquide rougeâtre sur le visage et, surprise, poussa un cri strident"
                narr "L'acide me brûlait le visage"
                narr "Le Bourreau, riant aux éclats, avança, pointa son pistolet vers Lise, et tira"
                narr "Lise était étendue, à terre"
                narr "Mon visage commençait à fondre"
                narr "Lise, agonisant, exulta dans un dernier souffle :"
                li "Fils de..."
                narr "Alors que mon visage se décomposait, je vis à travers le liquide..."
                narr "...un visage blond, autrefois angélique et maintenant démoniaque, me regardait en train de périr sur le sol."
                narr "J'étais si près du but..."
                unk "Adieu !"
                narr "Isaac riait aux éclats..."
                $ persistent.know_isaac = True
                $ fin = -5
                jump game_over
            "Fuir":
                narr "Il n'était pas question que j'obéisse au Bourreau"
                narr "Pas question que je tombe dans mon propre piège"
                narr "Je reculai, d'abord doucement, puis courrai vers l'aile gauche, mon dernier refuge"
                narr "Peut-être qu'avec Leonhard, on réussirait à se défendre ?"
                narr "Peut-être qu'on réussirait à tuer le Bourreau ?"
                narr "Peut-être qu'on sortirait vivants ?"
                narr "Peut-êtr...{w=0.5}{nw}"
                narr "Il avait tiré."
                narr "Je m'effondrai."
                narr "Quelle fin décevante..."
                narr "Qu'est-ce que je raconte ? Ça n'est pas la fin..."
                narr "Je rampai en direction de l'aile gauche"
                p "Leon..."
                p "{b}LEONHARD !{/b}" with sshake
                narr "Le Bourreau s'approchait lentement."
                narr "Sa voix me rappelait quelqu'un.. Mais qui ?"
                unk "Oh non, ça n'est pas la fin pour toi..."
                narr "Il me tira dans le pied gauche, en riant aux éclats."
                unk "Adieu !"
                narr "Une lumière blanche m'entoura soudain, puis..."
                narr "...{i}plus rien{/i}."
                $ fin = -5
                jump game_over

# ======== ERWIN vs JOHANN ====================================================================================================
label fight_final_erwin_johann_begin:
    narr "Erwin riait aux éclats."
    erw "Alors, Johann, prêt à te battre ?"
    narr "Johann tremblait de peur."
    j "À cause de toi..."
    narr "J'avais condamné Johann."
    erw "Bouge-toi, Kurt. Il ne doit rester qu'un entre moi et lui. Ne te mets pas sur mon chemin"
    $ alliance_finale = "Nobody"
    $ countdown_time = 15.0
    menu:
        "Rejoindre Johann (contre Erwin)":
            $ alliance_finale = "Johann"
            p "Je peux t'aider à le tuer."
            narr "Johann leva les yeux, surpris."
            #$ modif_confiance([johann], [-1])
            j "Mais à quoi tu joues ?"
            narr "Il était visiblement confus, mais accepta mon aide."
            jump fight_final_erwin_johann_active
        "Rejoindre Erwin (contre Johann)":
            $ alliance_finale = "Erwin"
            p "Je vais rejoindre Erwin."
            narr "Johann leva la tête, médusé."
            $ modif_confiance([johann], [-5])
            j "Mais à quoi tu joues ?"
            narr "Je le laissai dans la pièce et marchai vers la grande salle."
            jump fight_final_erwin_johann_active
        "Ne rien dire" ("default"):
            jump fight_final_erwin_johann_passive
        #"Proposer de faire la paix":
        #    $ alliance_finale = "Both"
        #    p "Faites la paix."
        #    narr "Johann et Erwin me dévisagèrent, perplexes."
        #    $ modif_confiance([johann], [-5])
        #    j "Mais à quoi tu joues ?" #TODO
        #    jump fight_final_erwin_johann_active

label fight_final_erwin_johann_passive:
    narr "Et je n'allais pas l'aider contre Erwin."
    narr "Il allait devoir se débrouiller seul..."
    narr "Erwin allait être sans pitié."
    if johann["arme"]:
        j "Je n'ai pas dit mon dernier mot..."
        narr "Il sourit en replaçant ses lunettes."
    else:
        narr "Johann n'avait plus la lame qui était cachée dans ses lunettes..."
        narr "Il tremblait imperceptiblement."
    $ sauvegarder("continuer")
    nvl clear
    narr "Erwin et Johann se toisaient du regard, au centre de la grande salle."
    narr "Moi et Lise étions au fond de la salle, en train de les regarder."
    li "On va vraiment les regarder s'affronter ?"
    narr "Je chuchotai :"
    p "J'ai pas envie de me mêler à tout cela..."
    if johann["arme"]:
        narr "Johann débordait de confiance."
        j "Je vais le faire..."
        narr "Il sourit en replaçant ses lunettes."
        jump final_johann_kills_erwin
    else:
        narr "Maintenant, Johann tremblait clairement de peur."
        jump final_erwin_kills_johann
    

label fight_final_erwin_johann_active:
    narr "Erwin et Johann se regardaient, au centre de la grande salle."
    narr "Moi et Lise étions au fond de la salle, en train de les regarder."
    li "On va vraiment les regarder s'affronter ?"
    narr "Je hochai la tête."
    if alliance_finale == "Johann":
        narr "Je n'allais pas lui dire maintenant que j'allais aider Johann à tuer son mari..."
        jump final_johann_kills_erwin
    elif alliance_finale == "Erwin":
        p "Oh, non !"
        narr "Je lui fis un clin d'oeil."
        jump final_erwin_kills_johann
    else:
        narr "This is a bug or a wip" #TODO demands peace ?
        $ fin = 3
        jump game_over

label final_johann_kills_erwin:
    narr "Johann s'approcha agressivement d'Erwin"
    narr "Surpris, Erwin recula."
    erw "Bah alors, Johann, d'habitude tu ouvres plus ta grande gueule !"
    erw "Tu fous quoi là ?"
    if alliance_finale == "Johann":
        j "J'ai plus d'un tour dans mon sac, Erwin."
        narr "Il allait essayer de gagner du temps. Il fallait que je l'aide, mais comment ?" #TODO: choix
        li "Qu'est-ce qu'il essaye de faire ?..."
        narr "En regardant Lise, j'eus une idée."
        narr "Je me mis en retrait, essayant de me faire le plus discret possible."
    else:
        j "Je suis là pour te tuer, Erwin."
        narr "Johann avait un grand sourire."
        narr "Erwin, toujours impressionnant, était perturbé."
        narr "Ce n'était pas le style de Johann. Il bluffait ?"
    narr "Johann avança vers Erwin, en position de garde."
    erw "Oh, tu sais boxer ? Ça ne va pas t'aider, contre moi..."
    narr "Erwin enleva son T-shirt, révélant des muscles surpuissants."
    narr "Johann lui donna un violent coup de pied latéral dans le ventre."
    narr "Erwin ne broncha pas, mais commençait à s'énerver."
    erw "Johann !!!"
    narr "Rouge de colère, il faisait aussi peur que la créature"
    narr "L'appareil métallique dans sa gorge soulignait encore plus cette ressemblance..."
    erw "N'importe quelle technique de boxe ne suffira pas contre moi."
    narr "Il avait décidé de contre-attaquer."
    narr "N'importe quel coup pouvait tuer Johann, il n'était pas assez entrainé."
    narr "Lise avait les yeux rivés sur Erwin, et marmonnait des paroles inintelligibles."
    li "Allez, allez..."
    if alliance_finale == "Johann":
        narr "La frappe d'Erwin était imminente."
        p "{b}ERWIN !{/b}" with sshake
        narr "Je frappai Lise dans la tempe."
        narr "Prise par surprise."
        narr "Elle s'effondra par terre"
    else:
        narr "Quand Erwin frappa, Johann esquiva agilement..."
        narr "...et baissa la tête, se prenant un coup dans les lunettes."
        narr "Pourquoi ?"
        narr "Il prit très rapidement ses lunettes cassées et en sortit une lame."
        narr "Erwin recula rapidement, mais pas assez pour esquiver la lame de Johann."
label erwin_killed:
    narr "Tout se passa très rapidement"
    narr "Erwin, surpris, resta immobile une seconde fatale."
    if leonhard["statut"] == "Vivant":
        narr "Leonhard se rua sur lui, les mains vers sa gorge."
    else:
        narr "Johann se rua sur lui, les mains vers sa gorge."
    narr "Il prit l'appareil de métal et lui arracha de la gorge."
    narr "Un mélange de sang et de glaires s'éjecta du corps d'Erwin."
    narr "Lise était comme une statue."
    narr "Les yeux rivés vers Erwin qui s'étouffait dans ses propres chairs."
    narr "Le sifflement de sa respiration était morbide."
    erw "Lise..."
    narr "La voix d'Erwin était quasiment inaudible, et étonnament aigüe."
    narr "La gorge d'Erwin se bloqua soudainement."
    narr "Ses yeux se révulsèrent."
    if leonhard["statut"] == "Vivant":
        narr "Leonhard l'avait tué."
    else:
        narr "Johann l'avait tué."
    $ erwin["statut"] = "Mort"
    $ sauvegarder("continuer")
    nvl clear
    jump ending_decision

label final_erwin_kills_johann:
    narr "Erwin s'approcha de Johann."
    narr "Monumental."
    narr "Johann n'avait vraiment aucune chance."
    narr "Il recula."
    j "Non..."
    narr "Le désespoir noyait de larmes les yeux de Johann."
    j "C'est moi l'innocent, tu peux pas me tuer !"
    if alliance_finale == "Erwin":
        p "Non, Johann. C'est moi."
        narr "Il me regarda, une flamme de haine brûlant dans ses yeux."
        erw "Kurt dit vrai."
    else:
        erw "Non."
    narr "Il frappa Johann au ventre, sans émotion."
    narr "Son poing pesait comme un marteau."
    narr "La frappe était tellement forte que Johann recula jusqu'au mur, estomaqué."
    narr "Il n'arrivait plus à respirer."
    if alliance_finale == "Erwin":
        narr "Alors qu'il commençait à fuir, je lui coupai la route."
        j "Traître..."
    else:
        narr "Johann essaya de fuir mais fut arrêté par Lise."
    narr "Il se retourna."
    narr "Erwin hurla, le poing levé."
    narr "Je détournai le regard."
    narr "Un cri."
    narr "Les dents de Johann atterrirent devant mes yeux."
    narr "Il était mort."
    $ johann["statut"] = "Mort"
    $ sauvegarder("continuer")
    nvl clear
    jump ending_chemist

# ======== ERWIN vs LEONHARD ==================================================================================
label fight_final_erwin_leonhard_begin:
    narr "Erwin riait aux éclats."
    erw "Alors, Leonhard, prêt à te battre ?"
    l "C'était certain..."
    narr "J'avais condamné Leonhard."
    erw "Bouge-toi, Kurt. Il ne doit rester qu'un entre moi et lui. Ne te mets pas sur mon chemin"
    $ alliance_finale = "Nobody"
    $ countdown_time = 15.0
    menu:
        "Rejoindre Leonhard (contre Erwin)":
            $ alliance_finale = "Leonhard"
            p "Je peux t'aider à le tuer."
            narr "Leonhard leva les yeux, surpris."
            l "Vraiment ? Pourquoi pas..."
            narr "Il était visiblement confus, mais accepta mon aide."
            jump fight_final_erwin_leonhard_active
        "Rejoindre Erwin (contre Leonhard)":
            $ alliance_finale = "Erwin"
            p "Je vais rejoindre Erwin."
            narr "Leonhard leva la tête, médusé."
            $ modif_confiance([leonhard], [-5])
            l "Pourquoi faites-vous ça, Kurt ?"
            narr "Je le laissai dans la pièce, sans répondre, et marchai vers la grande salle."
            jump fight_final_erwin_leonhard_active
        "Ne rien dire" ("default"):
            jump fight_final_erwin_leonhard_passive

label fight_final_erwin_leonhard_passive:
    narr "Et je n'allais pas l'aider contre Erwin."
    narr "Il allait devoir se débrouiller seul..."
    narr "Erwin allait être sans pitié."
    if leonhard["arme"]:
        l "Je n'ai pas dit mon dernier mot..."
        narr "Il sourit en mettant les mains dans ses poches"
    else:
        narr "Leonhard n'avait plus son stylo plume aiguisé..."
    $ sauvegarder("continuer")
    nvl clear
    narr "Erwin et Leonhard se regardaient, au centre de la grande salle."
    narr "Moi et Lise étions au fond de la salle, en train de les regarder."
    li "On va vraiment les regarder s'affronter ?"
    narr "Je chuchotai :"
    p "J'ai pas envie de me mêler à tout cela..."
    if leonhard["arme"]:
        j "Je ne suis pas aussi inoffensif que vous le pensez, Erwin..."
        narr "Il sourit malicieusement"
        jump final_leonhard_kills_erwin
    else:
        narr "Leonhard avait l'air désemparé..."
        jump final_erwin_kills_leonhard
    

label fight_final_erwin_leonhard_active:
    narr "Erwin et Leonhard se regardaient, au centre de la grande salle."
    narr "Moi et Lise étions au fond de la salle, en train de les regarder."
    li "On va vraiment les regarder s'affronter ?"
    narr "Je hochai la tête."
    if alliance_finale == "Leonhard":
        narr "Je n'allais pas lui dire maintenant que j'allais aider Leonhard à tuer son mari..."
        jump final_leonhard_kills_erwin
    elif alliance_finale == "Erwin":
        p "Oh, non !"
        narr "Je lui fis un clin d'oeil."
        jump final_erwin_kills_leonhard
    else:
        narr "This is a bug or a wip" #TODO demands peace ?
        $ fin = 3
        jump game_over

label final_leonhard_kills_erwin:
    narr "Leonhard commença à parler à Erwin, confiant."
    l "Erwin, je vais te tuer."
    narr "La scène avait l'air ridicule, absurde."
    l "Je te laisse l'occasion de mourir dignement."
    l "Il y a plein de strychnine, de cyanure, dans ton laboratoire."
    l "Toi-même, tu connais ces poisons mieux que moi."
    l "Suicidez-vous, et gardez votre honneur."
    narr "Erwin était désarçonné."
    if alliance_finale == "Leonhard":
        p "Je profitai de son inattention pour m'approcher de lui."
        narr "En me voyant approcher l'air menaçant, il repris ses esprits..."
        erw "Et toi, tu me veux quoi ?"
        narr "...mais avait arrêté de regarder Leonhard."
        narr "Je lui fis un clin d'oeil."
        narr "Il n'eut pas le temps de comprendre."
    else:
        erw "Tu dis n'importe quoi."
        narr "Leonhard s'approcha de lui, confiant."
        narr "Il mit sa main dans la poche et en sortit un stylo plume."
        l "Oh, non."
        narr "Leonhard lança son bras d'un mouvement fluide."
        narr "Son stylo, dans l'oeil d'Erwin."
    jump erwin_killed

label final_erwin_kills_leonhard:
    narr "Erwin s'approcha de Leonhard."
    narr "Monumental."
    narr "Leonhard n'avait vraiment aucune chance."
    narr "Il recula."
    l "Vous faites une grave erreur..."
    narr "La détresse se lisait dans les yeux de Leonhard."
    l "Le Bourreau est caché ici. Détruisez le mur de la salle mystère."
    l "Il ne sert à rien de jouer le jeu du Hibou."
    l "Je sais beaucoup de choses sur lui."
    l "Je peux tout vous dire."
    l "On peut s'allier !"
    erw "Non, pas besoin."
    narr "Sa voix était grave et impressionnante."
    erw "Le Bourreau, je crois deviner qui il est."
    narr "Leonhard reculait petit à petit."
    erw "Mais ça n'a pas d'importance."
    erw "Moi, je veux juste jouer son jeu et m'en sortir."
    if alliance_finale == "Erwin":
        narr "Leonhard avait reculé jusque moi."
        p "Désolé Leonhard."
        narr "Je me jetai sur lui et lui fis une clé de bras."
    narr "Erwin sourit, révélant de grandes dents blanches."
    narr "Sans parler, il prépara sa frappe."
    narr "Je lâchai Leonhard au moment ou le poing du géant frappa son crâne."
    narr "Il le frappa encore une fois."
    narr "Un cri."
    narr "Je détournai les yeux."
    narr "Encore une fois."
    narr "Boom."
    narr "Un gémissement."
    narr "Une dernière fois."
    narr "Leonhard était mort."
    $ sauvegarder("continuer")
    nvl clear
    $ leonhard["statut"] = "Mort"
    jump ending_chemist

# ======== ERWIN vs KURT ==================================================================================
label fight_final_erwin_kurt_begin:
    narr "Erwin riait aux éclats."
    erw "Alors, Kurt, prêt à te battre ?"
    narr "Contre Erwin, il était toujours difficile d'être prêt à se battre..."
    narr "Lise se retourna vers moi."
    li "Tu vas mourir."
    narr "Elle sortit de sa poche une fiole, qu'elle lança vers moi."
    narr "J'esquivais facilement."
    narr "Mais elle recommença encore et encore."
    narr "J'esquivais à chaque fois."
    narr "Pas assez rapide."
    narr "Soudain, elle arrêta."
    narr "Souriante."
    narr "Erwin s'approchai vers moi."
    narr "Je reculai d'un pas..."
    narr "Mais touchai le mur."
    narr "J'étais acculé."
    narr "Il me frappa tellement fort que je perdis connaissance immédiatement."
    #TODO alternative pour tuer Erwin
    #if erwin["statut"] == "Mort":
    #    jump ending_decision
    #else:
    $ fin = -9
    jump game_over

# ======== Ending Chemists (K/Er/Li) ==================================================================================
label ending_chemist:
    narr "Moi."
    narr "Et les chimistes."
    narr "Enfin, nous étions trois."
    narr "Trois."
    narr "La fin ?"
    erw "Bourreau."
    erw "Nous sommes trois."
    erw "Laisse nous partir."
    narr "..."
    b "Silence."
    narr "Le Bourreau avait du mal à respecter sa promesse ?"
    narr "Ca n'était pas ce qu'il avait prévu ?"
    b "Je vous laisse partir."
    b "Mais il vous faut faire un dernier sacrifice."
    erw "Absurde. Ca n'a aucun..."
    narr "Avant qu'Erwin puisse finir sa phrase, une ombre l'interrompit."
    b "Asseyez-vous. Sur les chaises derrière vous."
    narr "Le Bourreau était devant nous, caché sous une capuche noire."
    narr "Dans la main droite, un marteau."
    narr "Dans la main gauche, un flingue."
    b "L'un d'entre vous doit se sacrifier. Soyez courageux, et proposez-vous. Je lui infligerai un dernier blâme."
    b "Pas grand chose, comparé à ce que vous venez de vivre, n'est-ce pas ?"
    erw "C'est quand même absurde. Pourquoi vous faites-ça ? Vous ne respectez même pas vos propres règles..."
    b "Si."
    narr "Il avait touché un point sensible."
    b "Je fixe les règles que je veux."
    narr "Il pointa le pistolet vers Erwin."
    b "Décidez."
    $ countdown_time = 8.0
    menu:
        "Se sacrifier":
            jump ending_chemist_sacrifice
        "Ne rien dire" ("default"):
            jump ending_chemist_no_sacrifice
label ending_chemist_no_sacrifice:
    erw "Moi."
    b "Toi, tu veux te sacrifier ?"
    narr "Le ton du Bourreau était à moitié amusé, à moitié menaçant. Et complètement maladif."
    narr "On dirait qu'il n'attendait que ça."
    b "Très bien."
    narr "Il s'avança vers Erwin, toujours le pistolet visant sa tête, et son marteau de la main droite."
    b "Ouvre les jambes."
    narr "Erwin regarda la Bourreau, interloqué."
    b "Oui, c'est {i}ça{/i} que je veux écraser."
    b "Parce que c'est ce que vous faisiez, en tant que Rossignol, je me trompe ?"
    narr "Sans attendre la réponse d'Erwin, le Bourreau arma sa frappe."
    narr "Il fit descendre le marteau avec une force incroyable."
    narr "Mais Erwin ne bougea pas. Pas la moindre esquive, pas le moindre réflexe."
    narr "Par contre, un léger sourire se dessina sur ses lèvres."
    narr "Le marteau frappa la chaise avec un bruit métallique."
    narr "Sans toucher Erwin."
    b "Hein ?"
    if fin_vote_4 == "johann_mort_cachée" or fin_vote_4 == "johann_vivant":
        narr "Tout se passa très rapidement."
        narr "Erwin se leva."
        narr "Le Bourreau recula, inquiété."
        narr "Une main sortit du noir, derrière le Bourreau."
        narr "Elle lui prit le pistolet des mains."
        narr "Il se retourna..."
        narr "Pour se prendre un crochet d'Erwin."
        narr "Le Bourreau tomba par terre."
        $ annonce_importante(johann, _("Je t'ai en joue, Bourreau."))
        j "Ne bouge pas."
        narr "Erwin ne rapprocha du Bourreau."
        erw "Il y a deux choses que tu ne sais pas, Bourreau."
        erw "Je suis castré. Tu n'avais rien à frapper."
        narr "Il avança lentement vers Johann et fit un geste du menton."
        if fin_vote_4 == "johann_mort_cachée":
            erw "Et il n'est pas mort !"
        else:
            erw "Et il n'est pas mort, apparemment."
        j "Alors maintenant tu vas doucement te lever, sinon je tire."
        b "Vous..."
        narr "Le Bourreau rampait au sol, tremblant de rage."
        b "... je me lève, lentement. Ne tire pas."
        narr "Il se leva en un éclair, et balança son marteau vers Erwin."
        narr "Un tir retentit."
        narr "Deux corps qui tombent sur le sol."
        $ annonce_importante(bourreau, _("{b}RAAAAAH !{/b}"))
        narr "Touché au flanc, le Bourreau était maintenant désarmé."
        j "Tiens-toi bien. Je vais devoir te tuer sinon."
        b "Tue-moi."
        narr "Johann esquissa un sourire."
        j "Je préfère te garder en vie, maintenant. Car je sais qui tu es."
        narr "Lise avait le souffle coupé."
        narr "Son mari saignait de la tête, sur le sol."
        j "Et vous aussi, les deux chimistes."
        j "Justice sera faite. Je sais tout."
        j "Kurt, c'est fini."
        narr "Il s'accroupit et prit des clés, à la ceinture du Bourreau, et me les tendit."
        j "Tu vas pouvoir sortir."
        j "Marche vers le Sud pendant un peu moins d'une heure. Arrivé en ville, va au commissariat."
        j "Dis-leur qu'on a coincé le Rossignol, Erwin."
        j "Il a pas supporté sa castration, le pauvre. Il s'est vengé par la suite sur des dizaines de jeunes, dont Klaus."
        j "Sur commande de Lise."
        narr "Il se tourna vers la femme."
        j "Tu leur diras qu'on a aussi coincé Lise, chef de {i}Gesunder Menschenverstand{/i}, une association homophobe de très grande envergure."
        j "Mais surtout..."
        narr "Il avança de quelques pas."
        j "...dis-leur qu'on a capturé le {i}Hibou{/i}, comme on l'appelle à la Police."
        j "Le Bourreau."
        narr "Il mit le pied sur la tête du Bourreau, pour lui enlever sa capuche."
        j "Aussi connu sous le nom de..."
        $ annonce_importante(johann, _("Isaac."))
        n ""
        $ persistent.know_isaac = True
        $ fin = 6
        jump game_over
    else:
        narr "Le Bourreau hésita un instant fatal."
        narr "Erwin se leva."
        narr "Il prit le bras du Bourreau."
        narr "Le Bourreau arracha son bras de l'emprise d'Erwin."
        narr "Erwin prit le Bourreau par le col."
        narr "Clic. Le bruit de la détente."
        narr "Un coup de feu retentit."
        narr "Le chaos laissa place au silence."
        narr "La balle avait touché Lise en pleine tête."
        narr "Erwin regarda sa femme, abasourdi."
        narr "Son blocage laissa le temps au Bourreau de s'échapper vers l'aile gauche."
        narr "Il me regarda, impuissant."
        narr "Sa tête oscillait entre incompréhension et rage, pour finalement basculer vers de la haine pure."
        narr "La voix du Bourreau vint briser le silence, au travers des haut-parleurs."
        b "La sentence a été rendue. Erwin a voulu jouer et enfreindre les règles. Il a été puni. La dernière épreuve est finie. Vous pouvez sortir."
        narr "Un grincement sourd."
        narr "Et la lumière vint nous aveugler."
        erw "Je ne peux pas sortir."
        erw "Je veux ma vengeance."
        erw "Il... ne doit pas rester en vie."
        erw "Je vais le {b}fracasser{/b} !" with sshake
        erw "Toi, sors. Avant que je ne me défoule sur toi."
        narr "Il n'avait pas besoin de me le dire deux fois. J'étais déjà au seuil de la porte, baignant dans une lumière blanche, le sourire au coin des lèvres."
        narr "Libre."
        $ fin = 7
        jump game_over
label ending_chemist_sacrifice:
    b "Tu veux te sacrifier ?"
    narr "Il rit doucement, presque fraternellement."
    b "Pas question que tu te proposes, Klaus."
    b "Je ne vais pas gâcher ton joli visage !"
    b "Mais j'apprécie beaucoup ton sens du sacrifice et du devoir."
    b "En réalité, cette dernière épreuve n'en était pas une..."
    narr "Il regarda méchemment Erwin."
    b "...comme certains éléments récalcitrants n'hésitent pas à me le faire remarquer !"
    b "C'était un dernier test..."
    b "Et au vu de votre bon comportement, je me dois d'être magnanime."
    narr "Erwin tiquait. Le comportement du Bourreau avait changé du tout au tout, depuis qu'il était devant nous."
    b "Vous êtes donc libres !"
    narr "Un bruit sourd monta dans la prison."
    narr "Le Bourreau disparut sans que nous ayons eu le temps de le remarquer, aveuglés par la lumière blanche qui venait de la porte de sortie."
    narr "J'avançai vers cette lumière éblouissante, sans trop y croire."
    narr "C'était vraiment... la fin ?"
    $ fin = 5
    jump game_over

# ======== Ending xxx (K/Li/LouJ) ==================================================================================
label ending_decision:
    narr "Lise tremblait."
    narr "Elle revoyait Erwin tomber devant ses yeux."
    li "Je vais vous détruire."
    narr "Une voix assourdissante vint couper Lise dans son élan."
    b "Non."
    b "C'est la fin, et vous êtes tous convoqués dans la Salle de vote Droite."
    b "Immédiatement, sinon {i}boom{/i}."
    narr "Nous nous dirigeâmes vers la salle de vote."
    narr "Une silhouette capuchée nous attendait."
    narr "Un pistolet à la main."
    b "Un dernier bonjour à tous."
    b "Ceci est le dernier test, la dernière épreuve. La porte est déjà ouverte."
    b "Une des personnes ici présente a particulièrement bien agi."
    b "Bien supporté les épreuves, comme je les ai prévues."
    b "Et cette personne, c'est Kurt."
    b "C'est pourquoi je vais lui donner le mot de la fin."
    narr "Il me tendit fermement le pistolet, en souriant."
    $ annonce_importante(bourreau, _("Tire sur qui tu veux."))
label ending_decision_hesitation:
    nvl clear
    b "Tire sur qui tu veux."
    $ countdown_time = 30
    menu:
        "Tuer Leonhard" if leonhard["statut"] == "Vivant":
            jump ending_decision_leonhard
        "Tuer Johann" if johann["statut"] == "Vivant":
            jump ending_decision_johann
        "Tuer Lise" if lise["statut"] == "Vivante":
            jump ending_decision_lise
        "Tuer Lise et Johann" if johann["statut"] == "Vivant":
            $ tuer_bourreau = False
            jump ending_decision_everyone
        "Tuer Lise et Leonhard" if leonhard["statut"] == "Vivant":
            $ tuer_bourreau = False
            jump ending_decision_everyone
        "Tirer sur le Bourreau":
            jump ending_decision_executioner
        "Tuer tout le monde":
            $ tuer_bourreau = True
            jump ending_decision_everyone
        "Se suicider" ("default"):
            jump ending_decision_suicide
        

label ending_decision_suicide:
    $ flingue_owned = True
    jump suicide
label ending_decision_leonhard:
    narr "Tirer sur qui je veux ?"
    narr "Leonhard ou Lise ?"
    narr "Je mis en joue Leonhard."
    p "Adieu, Leonhard."
    narr "La détente pesait tellement lourd..."
    #TODO boom
    narr "Leonhard tomba par terre."
    jump ending_decision_talk_lise
label ending_decision_johann:
    narr "Tirer sur qui je veux ?"
    narr "Johann ou Lise ?"
    narr "Je mis en joue Johann."
    p "Adieu, Johann."
    narr "La détente pesait tellement lourd..."
    #TODO boom
    narr "Johann tomba par terre."
label ending_decision_talk_lise:
    narr "Le Bourreau me prit le pistolet."
    b "Tu as fait ton choix."
    b "Vous pouvez partir, la porte est ouverte."
    narr "Je sortis de la salle de vote, Lise sur les talons."
    li "Putain..."
    narr "Elle était en état de choc."
    narr "La Grande Salle était illuminée par lumière du jour."
    narr "Les rayons de lumière venaient carresser le corps sans vie d'Erwin."
    narr "Lise s'agenouilla près de lui."
    narr "Je continuai d'avancer, sans me retourner."
    narr "Enfin, je partais de ce lieu infernal..."
    $ fin = 9
    jump game_over
label ending_decision_lise:
    narr "Tirer sur qui je veux ?"
    narr "Je mis en joue Lise."
    p "Adieu, Lise."
    narr "La détente pesait tellement lourd..."
    #TODO boom
    narr "Lise tomba par terre."
    narr "Le Bourreau me prit le pistolet."
    b "Tu as fait ton choix."
    b "Vous pouvez partir, la porte est ouverte."
    if leonhard["statut"] == "Vivant":
        narr "Leonhard regardait le Bourreau."
        l "Isaac."
        l "Ce que vous avez fait est impardonnable."
        l "Nous nous reverrons."
        narr "Le Bourreau ricana."
        b "Oh, tu es sûr ? Pour toi, ce n'est pas fini, le vieux..."
    elif johann["statut"] == "Vivant":
        narr "Johann regardait le Bourreau, résigné."
        j "Ta vie est incroyablement triste."
        j "J'aurais surement fait la même chose si ma moitié avait subi ce sort..."
        j "Paix à Klaus."
        j "Mais tu n'iras jamais à Shambhala..."
        narr "Il replaça ses lunettes."
        j "On se reverra sûrement."
        j "J'aurais fait la même chose, à ta place."
        narr "Le Bourreau eu un rire nerveux. Il perdait pied."
        j "Mais ça reste impardonnable. On verra ce qu'on fera de toi. J'ai tous les éléments qu'il me faut."
        j "Au revoir, Hibou, ou Bourreau."
        narr "Johann tourna les talons."
    narr "Je le suivis, direction la Grande Salle."
    narr "La Grande Salle était illuminée par lumière du jour."
    narr "Les rayons de lumière venaient carresser le corps sans vie d'Erwin."
    narr "Je continuai d'avancer, sans me retourner."
    narr "Enfin, je partais de ce lieu infernal..."
    $ fin = 9
    jump game_over
label ending_decision_executioner:
    narr "Mais pourquoi me donne-t-il un flingue ?"
    narr "Je pointai le pistolet vers le Bourreau."
    narr "Il souriait patiemment."
    b "Tire. Peu importe sur qui."
    narr "Pourquoi était-il aussi confiant ?"
    $ countdown_time = 10.0
    menu:
        "Tirer sur le Bourreau":
            narr "Le tir était parti droit dans sa tête."
            narr "Un jet de sang jaillit de sa tête."
            narr "La force de l'impact l'avait fait reculer d'un mêtre au moins."
            narr "Le Bourreau était au sol."
            narr "Il avait fait une erreur en me passant le flingue, et il avait essayé de se sauver en me faisant douter."
            narr "Mais ça n'a pas marché."
            narr "Pourquoi a-t-il fait ça ?"
            narr "Lise avait les yeux grands ouverts."
            if leonhard["statut"] == "Vivant":
                narr "Leonhard regardait le Bourreau, ébahi."
                narr "Le Bourreau..."
                $ annonce_importante(leonhard, _("Isaac ?"))
            elif johann["statut"] == "Vivant":
                narr "Johann regardait le Bourreau, ébahi."
                narr "Le Bourreau..."
                $ annonce_importante(johann, _("Isaac ?"))
            narr "Nous avançâmes tous trois vers le corps."
            narr "Lise prit les clés sur le trousseau à sa ceinture."
            li "On peut partir, maintenant..."
            narr "C'était incompréhensible."
            narr "Je sortis de la salle de vote, en transe."
            narr "Lise ouvrit la grande porte."
            narr "La lumière de l'extérieur nous obligeait à plisser les yeux."
            if leonhard["statut"] == "Vivant":
                l "Putain..."
                l "Grace avait raison..."
            elif johann["statut"] == "Vivant":
                j "Isaac."
                narr "Johann replaça ses lunettes, pensif."
            $ fin = 8
            jump game_over
        "Hésiter, changer de cible" ("default"):
            jump ending_decision_hesitation

label ending_decision_everyone:
    narr "Tirer sur qui je veux ?"
    narr "C'est tous des pourris."
    narr "Aucun ne mérite de vivre..."
    narr "Je tins Lise en joue."
    li "Non, ne rentre pas dans son j...{nw}"
    narr "Une de moins."
    narr "Je décalai ma visée, et tirai une seconde fois."
    if leonhard["statut"] == "Vivant":
        narr "Leonhard tomba, raide mort."
    elif johann["statut"] == "Vivant":
        narr "Johann tomba, raide mort."
    p "Seul, maintenant."
    narr "Je me tournai vers le Bourreau."
    p "C'est ça que vous vouliez ?"
    b "Oh, non, Klaus. Ce n'est pas du tout ce que je voulais."
    b "Si j'ai fait tout ça, tous ces jeux, c'est pour te venger."
    b "Je voulais construire un monde meilleur."
    b "Bien sûr, tuer tous les parasites comme Leonhard m'intéressait, mais ce n'était pas mon but."
    b "Je voulais simplement vivre heureux avec toi à Shambhala, Kurt."
    b "Mais te voilà devenu sanguinaire..."
    b "Je crois que j'ai encore tout détruit."
    narr "Il baissa sa capuche."
    isa "Pardonne moi..."
    narr "Isaac pleurait."
    if tuer_bourreau:
        narr "Isaac ?"
        narr "Je serrai la machoire."
        narr "J'étais le dernier debout."
        narr "Fallait pas se laisser influencer."
        narr "Je pressai la détente."
        #TODO boom
        narr "Isaac tomba, raide mort."
    else:
        isa "Donne-moi ça."
        narr "Il prit le pistolet de mes mains."
        isa "C'est de la faute de Rosalind."
        isa "Je croyais pouvoir corriger ça, mais..."
        narr "Il leva le pistolet, le doigt sur la détente."
        isa "C'était irréparable..."
        narr "Il tira."
        narr "Suicide."
    narr "Le Bourreau gisait par terre."
    narr "Un filet de sang s'écoulait sur le sol."
    narr "Lorsqu'il atteint mes pieds, je réalisais ce qu'il s'était passé."
    narr "Trois corps étaient à mes pieds."
    narr "Le Bourreau..."
    narr "Putain, c'est dur."
    narr "Je comprends plus rien."
    narr "Le Bourreau..."
    narr "C'était Isaac ?"
    $ countdown_time = 30.0
    menu:
        "Sortir":
            narr "Je marchai vers la porte comme un zombie."
            narr "Je n'arrivais toujours pas à réaliser ce qu'il s'était passé."
            narr "Pourquoi ?"
            narr "Ca colle pas..."
            narr "Shambhala ? Isaac ? Klaus ? Rosalind ?"
            narr "Tout tournait dans ma tête."
            narr "Mais plus je m'approchais de la sortie, plus j'oubliais."
            narr "Il devait y avoir une explication, mais je m'en fichais."
            narr "La lumière de l'extérieur était tellement douce..."
            $ fin = 1
            jump game_over
        "Se suicider" ("default"):
            jump ending_decision_everyone_suicide

label ending_decision_everyone_suicide:
    $ flingue_owned = True
    jump suicide


# ======== Death xxx (Suicide) ==================================================================================
label suicide:
    $ renpy.block_rollback()
    narr "Me suicider ? Réellement ?"
    $ ajoute_instabilite(1)
    narr "Ca réglerait tout ?"
    narr "Peut-être."
    narr "De toute façon, cette histoire ne peut pas bien finir."
    narr "Autant tout gâcher pour tout le monde."
    narr "..."
    narr "Comment {i}le faire{/i} ?"
    if inventaire["poison"]["nb"] > 0:
        narr "J'avais toujours cette bosse dans ma poche."
        narr "Le poison."
        narr "J'ouvris la fiole, et pencha la tête vers le haut."
        narr "Le liquide rougeâtre paraissait bien innocent dans son petit récipient."
        narr "Je collai la fiole contre mes lèvres."
        narr "Et bus le contenu de la fiole."
    elif inventaire["knife"]["nb"] > 0:
        narr "J'avais toujours cette bosse dans ma poche."
        narr "Le couteau."
        narr "J'empoignais mon couteau."
        narr "Le mis sous ma gorge, à la verticale, à côté de ma trachée."
        narr "Couper la carotide."
        narr "J'enfonçais la lame sous ma gorge."
        narr "J'hurlai de douleur."
        narr "Le sang commençait à s'écouler gentiment..."
        narr "...et lorsque la lame trancha la carotide, tout s'emballa."
        narr "L'hémoglobine giclait partout."
    elif flingue_owned:
        narr "J'approchai le flingue vers ma tête, tremblant."
        narr "J'en avais marre de toute cette horreur."
        narr "Même si je sortais vivant de tout ça, la vie n'aurait plus de sens..."
        narr "Je fermai les yeux et comptai jusqu'à trois."
        p "Un, deux..."
        p "Trois."
    else:
        narr "La réserve."
        narr "Il y a une corde dans la réserve."
        narr "Je me mis à marcher solennellement en direction de la réserve"
        narr "Une fois arrivé, je pris la corde et fit un nœud coulant."
        narr "J'attachai solidement la corde en haut de l'étagère, et me passai la corde au cou."
        narr "Tellement simple."
        narr "Je me laissai pendre, dans un coin obscur."
        narr "Je me débattais sans le vouloir."
        narr "Sans succès.."
        narr "...ou plutôt {i}avec succès{/i}."
    narr "..."
    narr "Et puis..."
    narr "Plus..."
    narr "...rien."
    narr "..."
    narr "Le monde se décomposait autour de moi."
    $ ajoute_instabilite(1)
    narr "..."
    narr "Une lumière blanche ?"
    narr "..."
    narr "La fin."
    $ fin = -1
    jump game_over   
    
label fin_jeu:
    
    #crédits, écran de fin etc...
    
    jump end
    
