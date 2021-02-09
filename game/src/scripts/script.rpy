# A FAIRE AVANT DE FINIR LE PROJET #TODO
# config.developer
# enlever les label/jump test
# mettre des anti-rollback < $ renpy.fix_rollback() > (ne pas changer les choix faits avants)
# ou avec                  < $ renpy.block_rollback() > (ne pas pouvoir remonter avant)
# outlines [ (absolute(1), "#d00", absolute(1), absolute(2)) ] pour un effet glitch (à modifier mais c'est un test) cf. txt style (strikethrough etc)
#TODO idées : exploser la prison et s'en échapper par le haut
label splashscreen:
    scene black
    if not persistent.sauvegarde_info:
        $ persistent.sauvegarde_info = {"continuer": [0, " ", True, 0]}
    
    if not persistent.set_volumes:
        $ persistent.set_volumes = True
        $ _preferences.volumes['music'] *= .75

    if not persistent.first_play:
        $ nouvelle_simulation()

        n "\n\n\n\n\n\n{nw}"
        menu:
            "{image=icons/fr.png} Français":
                $ renpy.change_language(None, force=False)
            "{image=icons/gb.png} English":
                $ renpy.change_language("english", force=False)
                nvl clear
                n "\n\n\n\n\n\nBeware, the game is nut fully translated yet. Help me on Kickstarter !"
                nvl clear
        nvl clear
        show title_coal_reduit with inkdissolve:
            xalign 0.5 yalign 0.3
        show text "{font=fonts/NorthwoodHigh.ttf}{size=44}\n\n\n\n\n\n\n\n\n\n\n\nVersion [config.version] \"[persistent.version_name]\"{/size}{/font}" as text_version with inkdissolve
        $ renpy.pause(0.5)
        hide title_coal_reduit with inkdissolve
        hide text_version with inkdissolve
        nvl clear
        narr "Petite mise au point avant de commencer :"
        n "C'est un jeu \"survival horror\" d'aventure textuelle, donc l'ambiance est primordiale."
        n "Joue {b}seul{/b}, la {b}nuit{/b} et avec des {b}écouteurs{/b} pour des conditions idéales !"
        if is_daylight():
            n "Je sais qu'il fait encore jour, attend un peu !"
        narr "N'hésite pas à signaler toutes les erreurs, que ça soit des {b}bugs{/b}, des {b}fautes d'orthographe{/b} ou des {b}incohérences{/b}, à {a='mailto:amethystsstudio@gmail.com?body=Mon message'}amethystsstudio@gmail.com{/a} ou sur la conversation {a=https://discord.gg/wmu2PWA}Discord{/a}."
        n "Tu peux aussi envoyer des {b}suggestions{/b} et idées en tout genre."
        narr "Enfin, tu peux aussi me faire part de ton soutien, ce projet est super important pour moi et ça fait toujours plaisir !"
        n "Bon jeu !"
        if is_daylight():
            n "(vraiment, attends la nuit stp !)"
        show clouds with speedinkdissolve
        nvl clear
        pause 0.5
        show text _("{font=fonts/Centaur.ttf}{size=72}{color=#000}Prologue\n\nRêve{/color}{/font}{/size}") as title at truecenter with dissolve
        pause 1.0
        hide title with dissolve
        $ quick_menu = True
        show text _("{font=fonts/Centaur.ttf}{size=32}{color=#000}Prologue : Rêve{/color}{/font}{/size}") as haut_de_page at smooth_title
        n "\n\n\n\n\n\n     {w=1.5}{color=#aaaaaa}{i}Touchez l'écran pour faire avancer les dialogues{/i}{/color}"
        nvl clear
        nar "Je flotte dans les airs, libre."
        nar "Autour de moi, le monde est blanc, cotonneux."
        nar "Je rêve."
        nar "Un nuage s'écarte, et une silhouette familière se dessine devant moi."
        nar "J'ai déjà connu cette personne, mais je n'arrive plus à m'en souvenir."
        nar "Était-ce un ami, un ennemi ? Un proche, ou un adversaire ?"
        menu:
            "Lui parler":
                p_white "Hé ! Hé ! Je suis là !"
                nar "L'inconnu(e) se tourne vers moi."
                bunk_white "Je sais."
                bunk_white "C'est moi qui t'ai fait venir ici."
                $ countdown_time = 8.0
                menu:
                    "Ici ?":
                        p_white "Ici ? C'est où, ici ? Qu'est-ce que je fais là ?"
                        bunk_white "{i}Ici{/i}, c'est nulle part. Ça n'existe pas."
                        bunk_white "Je suis désolé de t'imposer ça."
                    "Toi ?":
                        p_white "Toi, tu es qui ? Je te connais ?"
                        bunk_white "Oh, oui. Mais tu m'auras bientôt oublié."
                    "Ne rien dire" ("default"):
                        bunk_white "Et tu n'es pas ici pour rien."
                        bunk_white "Tu t'es juste réveillé trop tôt..."
                bunk_white "Tu n'étais pas censé te réveiller {i}maintenant{/i}."
                bunk_white "À présent..."
            "S'éloigner":
                nar "Je préfère m'éclipser discrètement. Je me tourne de l'autre côté, et avance quelques mètres..."
                nar "... avant de le voir réapparaître derrière un nuage."
                bunk_white "Tu ne t'échapperas pas si facilement, {i}traître{/i}."
                p_white "Qu'est-ce qu...{w=1.0}{nw}"
        play sound "sounds/small_crescendo.ogg" 
        bunk_white "Endors-toi.{w=1.0}{nw}"
        play music "music/Main_theme.ogg" fadein 5.0
        scene new_main_screen_fond with griffesdissolve
        nvl clear
        show head with dissolve
    else:
        scene new_main_screen_fond with griffesdissolve
        show head with dissolve
        play music "music/Main_theme.ogg" fadein 5.0
    nvl clear
    $ renpy.pause(0.5, hard=True)
    return
    
label start:
    $ playtime_enter = datetime.datetime.now()
    $ quick_menu = False
    scene new_main_screen_fond
    show head with None
    # show title_coal_reduit with None:
    #     xpos 65
    #     ypos 204 #114
    show screen menu_title_coal(time = 1.0, initi=True)
    show moving at defiler
    #show glittering at briller
    hide head with inkdissolve
    nvl clear
    jump menu_principal

#================================================#
#================     Acte I     ================#
#================================================#
label acte1:
    $ persistent.sauvegarde_info[partie_actuelle][0] = 1
    $ acte = 1
    nvl clear
    hide screen menu_title_coal
    pause 0.5
    scene fondacte1 with fade
    show moving at defiler
    play music "music/Theme_acte_1.ogg" fadeout 3.0 fadein 5.0
    pause 0.5
    show text _("{font=fonts/Centaur.ttf}{size=72}Acte I\n\nPrisonniers{/font}{/size}") as title at truecenter with dissolve
    pause 1.0
    hide title with dissolve
    $ quick_menu = True
    show text _("{font=fonts/Centaur.ttf}{size=32}Acte I : Prisonniers{/font}{/size}") as haut_de_page at smooth_title
    n "\n\n\n\n\n\n     {w=1.5}{color=#aaaaaa}{i}Touchez l'écran pour faire avancer les dialogues{/i}{/color}"
    nvl clear
    $ sauvegarder("continuer", montrer = False)
    $ renpy.block_rollback()
    #================================ Intro : in medias res, 1ere video === choix : 1 ============================================
    bunk "Je vois que tout le monde est réveillé !"
    narr "Une douleur atroce me traversait le crâne"
    if persistent.glitched:
        narr "Je n'avais aucun souvenir récent..."
    p "Qu'est-ce que ?..."
    narr "Autour de moi, 5 autres personnes."
    narr "Tout le monde était assis sur une chaise, autour d'une grande table ronde."
    narr "La voix provenait des écrans placés devant chacun d'entre nous."
    bunk "Vous devez vous poser quelques questions légitimes :"
    bunk "Qui sont ces personnes autour de vous ?"
    bunk "Où êtes-vous ?"
    bunk "Qui suis-je ?"
    narr "Sa voix était grave et puissante, peut-être modifiée."
    bunk "Je crois que je vous dois quelques réponses !"
    narr "Tout le monde semblait être hypnotisé par ce visage."
    bunk "Tout d'abord..."
    narr "Un sourire narquois s'esquissa sur ses lèvres"
    bunk "Sachez qu'on m'appelle..."
    $ annonce_importante(bourreau, _("...le {i}Bourreau{/i}."))
    $ bourreau["statut"] = "Masqué"
    narr "Des regards d'incompréhension,{w=0.1} d'inquiétude{w=0.1} et de peur{w=0.1} s'échangèrent dans la salle"
    b "Je vous ai réunis ici..."
    b "...afin de vous faire expier vos péchés."
    narr "L'écran s'éteint."
    narr "{i}Fin de la première transmission{/i}"
    $ sauvegarder("continuer")
    nvl clear
    #================================ Scene 1 : présentation des personnages === choix : 2 ======================================================================
    narr "Le court instant de silence pesant fut rapidement cassé par l'intervention d'un jeune homme à l'air blasé."
    $annonce_importante(johann, _("On nage en plein délire là."), True)
    narr "Tout le monde se tourna vers lui."
    narr "Il était jeune, devait avoir environ 20 ans. Il portait des lunettes et avait tout l'air d'un intellectuel."
    junk "Excusez-moi, je ne me suis même pas présenté"
    narr "Il avait le tic de remettre ses lunettes de la main droite environ toutes les 15 secondes, comme si elles étaient trop lourdes."
    junk "Je m'appelle Johann"
    $ persistent.confiance["Johann"][2] = True
    $ johann["statut"] = "Vivant"
    $ modif_bio(johann, 0, notify=False)
    j "Je suppose que personne ne sait ce qu'il se passe. Je suppose également que cette pièce est ferm..."
    narr "Il fut interrompu par un adolescent, plutôt beau mais incroyablement frêle. Il avait l'air farouche, effrayé par les paroles du Bourreau"
    $annonce_importante(isaac, _("Oui, c.. c'est fermé, j.. j'ai vérifié quand vous étiez évanouis tout à l'heure"), True)
    narr "Il baissa la tête"
    isaunk "P.. Pardon de vous avoir interrompu."
    narr " Johann n'aimait visiblement pas être interrompu."
    narr "Il était certes un intellectuel à lunettes, mais pas le genre craintif. Il dégageait une aura imposante, et inspirait le respect"
    j "Comment tu t'appelles ?"
    isaunk "Je.. Je m'appelle Isaac..."
    $ persistent.confiance["Isaac"][2] = True
    $ isaac['statut'] = "Vivant"
    $ modif_bio(isaac, 0, notify=False)
    j "Tu es sûr que la porte est bien fermée ?"
    isa "Oui !"
    narr "Était-il sincère ?{nw}"
    $ verif_porte_acte1 = False
    $ faire_confiance_isaac_porte = False
    $ countdown_time = 18.0
    menu:
        "Faire confiance à Isaac":
            $ faire_confiance_isaac_porte = True
            $ renpy.fix_rollback()
            $ get_achievement("premier_choix")
            p "Je pense qu'on peut lui faire confiance."
            $ modif_confiance([isaac], [1])
            j "Si tu le dis..."
            narr "Un des inconnus hésitait, mais resta silencieux et son hésitation fut coupée par Johann."
        "Vérifier que la porte est bloquée":
            $ verif_porte_acte1 = True
            $ renpy.fix_rollback()
            $ get_achievement("premier_choix")
            $ modif_confiance([isaac], [-1])
            narr "Je me levai et mis la main sur la poignée."
            p "La porte est bien fermée !"
            j "Très bien !"
        "Ne rien dire" ("default"):
            $ verif_porte_acte1 = False
            $ renpy.fix_rollback()
            narr "Johann hésitait, mais personne ne prenait la parole."
            j "Bon, je vais te faire confiance."
            alaunk "Pas moi. Je vais vérifier."
            narr "L'inconnu se leva et mit la main sur la poignée."
            alaunk "La porte est bien fermée !"
            j "Très bien !"
label suite_premier_choix:
    j "Je résume. On est tous enfermés ici par quelqu'un qui a l'air de vouloir jouer les justiciers."
    $ modif_resume(101)
    j "Il nous a traînés ici et a mis les moyens, à en juger l'équipement."
    j "On a tous une sorte de tablette devant soi, avec des informations personnelles."
    j "En plus d'être équipé, il a un objectif : il nous a pas choisis au hasard."
    j "Donc soit c'est une gigantesque caméra cachée, soit..."
    $annonce_importante(alan, _("...on est dans la merde."), True)
    narr "Un jeune homme au visage anguleux se racla la gorge."
    alaunk "Yo, c'est Alan."
    $ alan["statut"] = "Vivant"
    $ persistent.confiance["Alan"][2] = True
    $ modif_bio(alan, 0, notify=False)
    narr "Il avait l'air d'un petit caïd, le genre de gars à problèmes que tout le monde détestait et dont ses camarades avait peur à l'école."
    ala "D'ailleurs, ça serait cool de savoir qui est qui, hein ?"
    narr "Un vieil homme en costume ajouta :"
    $annonce_importante(leonhard, _("D'autant plus que nous allons rester ici longtemps, je le crains."), True)
    narr "Il parlait bien mieux qu'Alan, mais avec un léger accent allemand."
    lunk "Je suis le Haut Juge Newer, mais vous pouvez m'appeler par mon prénom, Leonhard."
    $ persistent.confiance["Leonhard"][2] = True
    $ leonhard["statut"] = "Vivant"
    $ modif_bio(leonhard, 0, notify=False)
    narr "Il était clairement le doyen du groupe, et devait avoir la cinquantaine ou soixantaine, c'était difficile à dire."
    l "Le Bourreau n'en est pas à son premier coup d'essai."
    l "Il est déjà connu de la Justice et des services secrets, mais nous n'avons jamais pu l'attraper."
    narr "Il dégageait une aura imposante et inspirait le respect."
    narr "Alors que l'audience était captivée, le regard du juge était las"
    l "Nous ne connaissons de lui que sa passion pour les jeux macabres..."
    $ annonce_importante(leonhard, _("...et quelque chose me dit que nous allons être témoins de sa prochaine folie..."))
    narr "La petite assemblée était comme glacée par la révélation du Juge."
    $annonce_importante(emmy,_("Non... C'est pas possible ?!"), True)
    narr "Une fillette, la seule fille du groupe, semblait au bord de la crise d'angoisse."
    eunk "Je.. je m'appelle Emmy."
    $ persistent.confiance["Emmy"][2] = True
    $ emmy['statut'] = "Vivante"
    $ modif_bio(emmy, 0, notify=False)
    e "C'est injuste d'avoir été amenée ici, j'ai toujours été une fervente chrétienne !"
    e "Je n'ai jamais péché, moi ! Qu'est-ce qui m'arrive ???"
    narr "Elle s'effondra en sanglots et Isaac vint la consoler"
    isa "Emmy... Tu étais dans mon lycée, c'est bien ça ?"
    isa "Je crois t'avoir déjà vu quelque part..."
    narr "L'intello à lunettes s'approcha."
    j "Le même lycée ? Ce n'est certainement pas une coïncidence..."
    narr "Il replaça ses lunettes avec confiance"
    j "Je vais mener ma propre enquête."
    j "Avec {i}moi{/i}, ne craignez rien, vous allez sortir de ce merdier."
    j "Pourquoi ? {w=0.1}Parce que je suis un des meilleurs étudiants en droit de ce pays, et sincèrement, je suis l'un des plus grands cerveaux de notre époque."
    p "(Quelle modestie)"
    narr "Des sourires moqueurs s'échangèrent et Isaac soupira."
    j "Qu'est-ce qu'il y a, toi ?"
    narr "Isaac détourna le regard. Il avait l'air facilement intimidable."
    isa "Rien, rien..."
    narr "Il me regarda d'un air entendu. Johann se tourna lui aussi vers moi."
    j "Et toi, tu ne t'es pas présenté ?"
    p "Ah, désolé ! Je m'appelle Kurt..."
    ala "(Mimant une réunion des alcooliques anonymes) Bonjoooour Kuuuurt !"
    narr "La blague n'avait pas l'air de passer et un silence gênant s'installa plusieurs longues secondes, donc je me décidai à continuer ma présentation."
    p "...Mes parents étaient fan de Nirvana, comme vous vous en doutez."
    p "J'ai 17 ans, et peu d'amis : en fait, je passe la plupart de mon temps à jouer..."
    p "...ou à poster des blagues sur mon compte twitter"
    p "Je fais beaucoup d'humour noir ! Je trouve ça drôle, mais ça attire quelques {i}haters{/i}..."
    p "Je récolte tous les jours des milliers de retweets, mes followers vont finir par remarquer mon absence !"
    j "Ah, intéressant !"
    isa "Moi aussi, j'ai un devoir de maths important à rendre pour demain ! Quelqu'un va remarquer mon absence !"
    narr "Johann allait parler lorsque les écrans des tablettes s'allumèrent de nouveau."
    $ sauvegarder("continuer")
    nvl clear
    #================================ Scene 2 : La 2e vidéo =========================================================================
    narr "{i}Début de la transmission 2{/i}"
    narr "Le Bourreau avait toujours le même ton narquois"
    b "Maintenant que tout le monde s'est présenté, laissez-moi vous expliquer pourquoi je vous ai amené ici :"
    $ annonce_importante(bourreau, _("Vous êtes tous des criminels."))
    narr "Cette dernière phrase fit l'effet d'une bombe au sein du petit groupe"
    narr "Johann, l'intello à lunettes, criminel ?"
    narr "Isaac, le beau et timide garçon, criminel ?"
    narr "Emmy, la chrétienne, criminelle ?"
    narr "Leonhard, le juge, criminel ? Ce serait un comble..."
    narr "Quant à Alan, il avait beau l'air rebelle, il avait bien loin d'avoir l'air d'un criminel..."
    narr "Et MOI ??? Je passais ma vie au lycée ou sur internet..."
    narr "Tout ce que j'ai réussi dans ma vie, c'est de percer sur Twitter, grâce à de l'humour (très) noir..."
    narr "Mes tweets étaient un peu limite quelquefois..."
    narr "...enfin..."
    narr "...en vrai, ils étaient carrément racistes et homophobes. Mais de là à me traiter de criminel..."
    narr "Le Bourreau avait maintenant le même sourire que le {i}Joker{/i} de {i}Batman{/i}"
    b "Vous êtes tous des criminels restés {i}impunis{/i}."
    b "Vous allez donc devoir payer pour vos crimes !"
    $ modif_resume(102)
    narr "Il éclata de rire, tandis que tout le monde avait l'air effrayé... exceptés Johann et Leonhard"
    narr "Johann souriait, et Leonhard avait toujours l'air impassible"
    $ annonce_importante(bourreau, _("Je vais {i}tuer{/i} certains d'entre vous."))
    b "Seuls {i}3{/i} partiront d'ici vivants..."
    b "Je ne vais pas simplement vous exécuter. J'aurais déjà pu le faire avant, lorsque vous étiez évanouis..."
    b "Vous voyez, ce n'est pas {i}tuer{/i} qui m'intéresse..."
    b "Je veux {i}jouer{/i} avec vous"
    b "Je veux que vous {i}souffriez{/i} avant de mourir"
    b "Car l'espoir de survie vous donne la rage !"
    narr "Il avait un rire diabolique"
    b "Tout d'abord, allez visiter notre magnifique terrain de jeu... J'espère que vous apprécierez !"
    b "J'y ai caché une clé USB contenant la 3ème vidéo"
    b "Préparez-vous à un {b}{i}carnage{/i}{/b} !!!"
    narr "{i}Fin de la transmission 2{/i}"
    $ modif_bio(bourreau, 0)
    narr "Alors, que Emmy, Alan et Isaac étaient terrorisés, Leonhard, nullement impressionné, se leva et ouvrit la porte"
    l "{i}\"Il\"{/i} est passé nous ouvrir la porte pendant que nous regardions sa vidéo"
    j "Quel enfoiré !"
    if not verif_porte_acte1:
        ala "Alors, Isaac, on a des problèmes de mémoire ? Tu disais que c'était fermé, tout à l'heure, non ?"
        if faire_confiance_isaac_porte:
            e "Et Kurt, tu disais faire confiance à Isaac..."
            $ modif_confiance([emmy], [-1])
        narr "Isaac haussa les épaules"
        isa "Il a peut-être ouvert la porte entre temps..."
        isa "On ne sait pas encore dans quoi on est tombés ! Ça commence à me faire peur..."
    else:
        j "Il veut juste nous impressionner..."
    j "Je ne pense pas qu'il soit sérieux."
    j "Il ne va pas {i}vraiment{/i} y avoir un carnage ici..."
    narr "Leonhard le coupa brutalement"
    l "Si."
    l "Je l'ai déjà dit, il est connu pour ses massacres mis en scène..."
    l "Ne le négligez pas :"
    l "Il va {i}vraiment{/i} tuer 3 d'entre nous"
    narr "Isaac avait les yeux exorbités"
    isa "N.. Non, ça doit être une blague, une.. une caméra cachée ! ..."
    e "Si ça en est une, elle n'est pas drôle..."
    j "Ne perdons pas de temps, allons visiter les lieux"
    isa "M.. Mais, si il nous tend un piège ?"
    isa "Il vaudrait mieux rester ici, non ?"
    e "Moi, je reste ici avec Isaac !"
    ala "Peuh, tu vas pas survivre longtemps avec cette trouille, toi !"
    narr "Une lueur de défi brilla dans les yeux d'Isaac"
    isa "C'est cette peur qui va me permettre de survivre, au contraire..."
    isa "Fais ta forte tête si tu veux, mais prendre des risques inutiles ici..."
    narr "Il laissa sa phrase en suspens. Alan avait l'air de prendre conscience de son choix, mais ne pouvait plus reculer."
    ala "Tocard."
    narr "Il se tourna vers la porte, entouré de Johann et Leonhard"
    $ sauvegarder("continuer")
    nvl clear
    #================================ Scene 3 : la visite et la 3e video === choix : 3 3-1 3-2-1 3-2-2 ======================================================================
    narr "Arrivé au niveau de la porte, Johann se tourna vers moi."
    j "Tu fais quoi, toi ?"
    menu:
        "Rester avec {color=#ffd}Emmy{/color} et {color=#5ba7ff}Isaac{/color}":
            $ get_achievement("premier_choix")
            $ acte1_rester = True
            $ modif_confiance([emmy, isaac], [1, 1])
            p "Je reste ici."
            narr "Le groupe se scinda donc en deux."
            narr "Une fois que les bruits de pas furent peine audibles, Isaac exprima son soulagement :"
            isa "Super ! On sera toujours plus en sécurité à 3 que à 2!"
            e "Et puis surtout... les 3 là-bas me font peur..."
            e "Alan est juste une brute épaisse..."
            e "Johann est {i}trop{/i} intelligent pour être inoffensif"
            e "Et Leonhard..."
            narr "Isaac interrompit Emmy, avec un regard entendu"
            isa "Il me fait peur aussi."
            isa "Ces 3 là ne sont pas dignes de confiance, n'est ce pas ?"
            e "Oui, je suis totalement d'accord..."
            e "Il faut vraiment que je parte d'ici."
            narr "Après un instant de silence, Emmy se tourna vers sa tablette."
            e "Il y a sûrement quelque chose à trouver dedans..."
            narr "Je me penchai vers ma tablette. Son contenu était parfaitement banal, mais 2 choses sortaient de l'ordinaire."
            narr "Il y avait un dossier \"Sujets\", et un plan."
            show cursor_menu with dissolve
            $ plan_available = True
            $ renpy.notify("La carte est maintenant accessibles depuis le menu.")
            e "Super ! Une carte !"
            hide cursor_menu with dissolve
            isa "Et bien voilà, pas besoin d'explorer, et on est sûrement plus renseignés qu'{i}eux{/i} maintenant !"
            $ renpy.notify("Ce dossier est accessibles depuis le menu.")
            e "Par contre, regardez dans le dossier \"Sujets\"..."
            p "Quoi ??? On est tous fichés !"
            isa "Ca craint..."
            isa "Et pourquoi il y a écrit {i}Crime{/i} ?"
            narr "Emmy était pensive. Elle y comprenait quelque chose, elle ?"
            p "J'en sais rien..."
            isa "Moi non plus..."
            narr "Il ne restait plus qu'à attendre que Johann, Leonhard et Alan rentrent."
            $ sauvegarder("continuer")
            nvl clear
            narr "Au bout de 15 longues minutes d'attente, Johann, Leonhard et Alan entrèrent de nouveau dans la pièce"
            l "Nous avons trouvé la clé USB. Regardez !"
        "Suivre {color=#9400ce}Alan{/color}, {color=#ff7700}Johann{/color} et {color=#008c3b}Leonhard{/color}":
            $ renpy.fix_rollback()
            $ get_achievement("premier_choix")
            $ acte1_rester = False
            $ modif_confiance([alan, johann, leonhard], [1,1,1])
            p "Rester ici n'avance à rien, je pars avec vous"
            narr "Nous sortîmes de la pièce pour arriver dans un long couloir"
            j "Allez, on y va !"
            $ plan_available = True
            $ first_visit_chambres_map1 = True
            $ sauvegarder("continuer")
            nvl clear
            hide haut_de_page at smooth_title
            pause 0.5
            show text "{font=fonts/Centaur.ttf}{size=40}Carte{/font}{/size}" as haut_de_page at smooth_title(dist_y =60)
            jump first_map
            label suite_map_0:
                nvl clear
                hide haut_de_page at smooth_title
                $ get_achievement("decouvre_carte")
                pause 0.5
                show text "{font=fonts/Centaur.ttf}{size=32}Acte I : Prisonniers{/font}{/size}" as haut_de_page at smooth_title
                pause 1.5
    #================================ Scene 4 : la 3e video === Conf : I+2/-2 J+2/-1 =========================================================================
    narr "Leonhard mit la clé USB dans sa tablette et lança l'enregistrement"
    narr "{i}Début de la troisième transmission{/i}"
    b "Salut à tous, une nouvelle fois..."
    b "Maintenant que vous savez {i}qui{/i} vous êtes et {i}où{/i} vous êtes, il est temps de vous expliquer les règles de mon jeu"
    narr "Le Bourreau prenait manifestement un malin plaisir à étaler ses plans"
    b "Comme je vous l'ai dit, vous êtes {i}tous{/i} coupables de crimes horribles, restés impunis..."
    b "...enfin pas exactement {i}tous{/i} coupables..."
    b "Pour pimenter un peu le jeu..."
    b "...j'ai invité un parfait innocent à la partie !"
    p "(C'est moi ??? Ou alors...)"
    e "C'est injuste !!!"
    b "Le but de mon {i}Jeu{/i} est de punir tous les criminels :"
    b "Vous allez avouer tous vos crimes"
    $ annonce_importante(bourreau, _("Tous les jours, à midi, vous allez voter pour celui d'entre vous que vous jugez {i}le plus coupable{/i}..."))
    b "...et je l'exécuterai avant le prochain vote !"
    $ sauvegarder("continuer")
    nvl clear
    b "Vous {i}devez{/i} jouer à mon jeu."
    b "Il est interdit de {i}refuser de jouer{/i}, ou de {i}tuer l'innocent{/i}..."
    b "De toute façon, vous n'avez pas le choix."
    b "Emmy, regardez votre bras droit. Collez-y l'oreille."
    narr "Emmy s'exécuta."
    narr "Elle retint un cri. Elle avait l'air paniquée, en détresse."
    e "Ça... ça fait tic-tac !"
    b "Pendant votre sommeil prolongé, j'ai placé..."
    narr "Le Bourreau éclata de rire"
    b "...quelques {i}explosifs{/i} dans votre corps !"
    b "Alan, le tien est directement placé à coté de ton cœur..."
    b "Isaac, dans ton bras gauche"
    b "Kurt, sur ton poumon droit"
    b "J'ai placé celui de Leonhard juste au dessus de ses bijoux de famille..."
    b "Et celui de Johann, dans le poignet droit !"
    b "Si vous n'obéissez pas à mes ordres... BOUM!"
    narr "Emmy avait un petit rire nerveux. Isaac avait la tête dans les bras. Le juge fronçait les sourcils."
    narr "Johann et Alan avaient l'air détendus, ne semblaient pas intimidés par le Bourreau"
    b "À l'heure où je vous parle, il doit bientôt être midi :"
    $ annonce_importante(bourreau, _("{i}{b}QUE LE VOTE COMMENCE !!!{/b}{/i}"))
    $ modif_resume(103)
    narr "{i}Fin de la troisième transmission{/i}"
    $ sauvegarder("continuer")
    nvl clear
    hide moving at defiler
    hide haut_de_page at smooth_title 
    $ quick_menu = False
    show screen menu_background()
    show screen menu_title_coal()
    call screen in_game_menu(acte=acte)
#================================================#
#================     Acte II     ===============#
#================================================#
label acte2:
    hide fondfinacte at fade_away
    $ acte = 2
    $ acte_romain = "II"
    $ persistent.sauvegarde_info[partie_actuelle][0] = 2
    n "C'est le dev qui vous parle !"
    n "Est-ce que vous avez aimé le premier acte ?"
    n "Ca serait vraiment cool que vous m'envoyiez vos réactions !"
    n "...et que vous laissez un petit 5 étoiles sur le play store ;) "
    n "N'hésitez pas à m'envoyer vos {b}commentaires{/b}, des {b}bugs{/b}, des {b}fautes d'orthographe{/b} ou des {b}incohérences{/b}, sur {a=https://discord.gg/wmu2PWA}Discord{/a}"
    nvl clear
    play music "music/Theme_acte_2.ogg" fadeout 3.0 fadein 3.0
    scene fondacte2 with fade
    show moving at defiler
    pause 0.5
    show text _("{font=fonts/Centaur.ttf}{size=72}Acte II\n\nLe Vote{/font}{/size}") at truecenter with dissolve
    pause 1.5
    hide text with dissolve
    show text _("{font=fonts/Centaur.ttf}{size=32}Acte II : Le Vote{/font}{/size}") as haut_de_page at smooth_title
    nvl clear
    #================================ Scene 1 : vote1 / fight === choix : 2 ======================================================================
    narr "La table ronde trônait au centre de la salle de vote"
    narr "Nous prîmes place devant notre écran."
    narr "Un d'entre eux, celui d'Emmy, était recouvert de sang"
    narr "Décidément, elle n'était pas impressionnable"
    narr "Tout le monde s'installa"
    l "En tant que juge, j'aimerais présider la séance"
    narr "Comme personne ne s'opposait à cette idée, le juge continua"
    l "Tout d'abord, afin de procéder à un jugement le plus juste possible..."
    narr "On va vraiment tuer l'un d'entre nous ? C'est impossible. Pourquoi personne ne réagit ?"
    l "...chacun doit avouer ses crimes."
    narr "Isaac s'indigna :"
    isa "Vous êtes fous !!! On va pas {i}vraiment{/i} voter pour tuer l'un d'entre nous, quand même ?"
    narr "Il regarda Johann, qui lui sourit"
    isa "Tu es avec moi, Johann ? Tu disais que tu croyais pas à cette histoire !"
    j "J'aimerais vérifier que le Bourreau met bien ses menaces à exécution..."
    ala "C'est peut-être juste une caméra cachée, pas la peine de s'énerver !"
    j "Et puis..."
    narr "Il regarda malicieusement Leonhard"
    j "... j'ai la certitude de ne pas mourir, du moins ce tour-ci !"
    narr "Alan ajouta d'un ton glacial :"
    ala "Isaac, petite fiotte. Si tu refuses de participer, le Bourreau va faire exploser ta bombe..."
    isa "Pourquoi moi ???"
    isa "Il suffit que tout le monde refuse de jouer !"
    isa "Si tout le monde refuse, il ne va pas faire exploser tout le monde ! On peut gâcher son {i}Jeu{/i} en faisant ça, non ?"
    narr "Alors que Johann allait répondre, Leonhard le coupa."
    l "Le meilleur choix est de voter, quoi qu'il arrive :"
    l "Le Bourreau va tout faire pour que son Jeu se déroule selon ses envies..."
    l "Si tu es un obstacle au bon fonctionnement du jeu, tu vas devenir une cible pour le Bourreau..."
    l "Et tu vas mourir peu de temps après."
    narr "Johann chuchota"
    j "Je n'aurais pas dit mieux..."
    narr "Le juge reprit d'une voix forte :"
    l "S'il vous plaît ! J'ai besoin des récits de tout le monde"
    l "Qu'avez vous fait pour attiser la colère du Bourreau ? Quels sont vos {i}péchés{/i} ?"
    $ sauvegarder("continuer")
    nvl clear
    l "Afin de partir sur de bonnes bases, et afin d'encourager les langues à se délier, je vais vous avouer mon crime"
    l "Je suis mêlé à une affaire compliquée de corruption."
    narr "L'assemblée lui lança un regard mauvais."
    l "J'avoue avoir accepté des grosses sommes d'argent en échange de plusieurs services malhonnêtes..."
    l "J'espère que maintenant vous allez être aussi franc que moi."
    $ claim_bystander = False
    l "Qu'as-tu fait, Kurt ?"
    menu:
        "Clamer l'innocence":
            $ renpy.fix_rollback()
            p "Je suis l'innocent. Je n'ai jamais rien fait de mal..."
            p "Du moins, je ne vois pas ce qui a pu provoquer le Bourreau"
            $ claim_bystander = True
        "\"Blagues\" un peu limites sur les réseaux":
            $ renpy.fix_rollback()
            p "Je suis toujours resté dans la légalité."
            p "La seule chose préjudiciable que j'ai faite..."
            p "... ce sont des blagues racistes sur Twitter"
            p "Xénophobes, quelque fois, antisémites et homophobes aussi..."
            p "Mais cela reste de l'humour noir, pour faire rire : je ne pense pas ce que j'écris"
            p "Je me suis déjà fait censurer, ça ne m'étonnerait pas que le Bourreau veuille me faire taire, mais de là à me tuer..."
    $ modif_bio(kurt, 1)
    narr "Alan prit la parole"
    ala "Moi, j'ai déjà tabassé un petit de 10 ans par plaisir."
    narr "Tout le monde le regardait, bouche bée."
    narr "Isaac le regardait différemment. Il savait quelque chose sur cette affaire ?"
    narr "Alan se défendit :"
    ala "J'avais que 14 ans !!!"
    ala "J'ai aussi fait pleurer mes profs..."
    ala "J'en ai frappé un, une fois..."
    narr "Johann leva un œil"
    j "C'est tout ? Je m'attendais à plus, Alan... Tu nous caches quelque chose ?"
    narr "Alan avait l'air indifférent face à la violence de ses actes"
    ala "J'ai été viré de mon collège environ tous les ans, mais ça n'est pas un crime."
    l "Et au lycée ?"
    ala "Je... J'ai déjà acheté et vendu de la drogue..."
    narr "Alan hésita"
    l "Continue !"
    ala "...de la cocaïne"
    $ modif_bio(alan, 1)
    l "Il s'est fait prendre comme un bleu à sa 3ème livraison."
    l "J'ai été mis sur l'affaire, mais ses parents m'ont grassement payé pour lui faire éviter la prison pour mineurs, d'où mon affaire de corruption."
    $ modif_bio(leonhard, 1)
    l "Je ne sais pas si le fait de se revoir ici est une coïncidence ou non..."
    j "Je ne pense pas : je pense que nous sommes tous ici pour une raison particulière !"
    j "Moi, j'ai triché à l'examen d'entrée de mon école."
    $ modif_bio(johann, 1)
    j "Je n'aurais pas pu rentrer à la meilleure école du pays autrement"
    j "Les études de droit sont impitoyables, et tout le monde triche plus ou moins..."
    narr "Il avait un sourire en coin"
    j "C'est une introduction à la justice et à la vie politique moderne !"
    j "Certains y arrivent sans se tâcher les mains..."
    j "... mais la plupart se corrompent déjà à ce stade."
    j "A toi, Isaac !"
    narr "Isaac prit une grande inspiration"
    if claim_bystander:
        isa "Je... Je suis le vrai, le seul innocent ici..."
    else:
        isa "L'innocent... C'est moi..."
    $ modif_bio(isaac, 1)
    narr "Isaac prit sa tête entre ses mains"
    isa "Je vous supplie de me croire..."
    narr "Emmy le regarda avec des yeux exorbités"
    narr "Le silence se fit"
    narr "Emmy articula avec une voix faible, tremblante"
    e "C'est..."
    e "...c'est {i}moi{/i} qui suis innocente..."
    $ modif_bio(emmy, 1)
    e "Je n'ai jamais fait de mal à une mouche..."
    narr "Johann jubilait"
    j "Ça fait beaucoup d'innocents, vous ne trouvez pas ?"
    j "L'un de vous cherche à cacher un crime tellement {i}horrible{/i} que si il l'avouait, tout le monde aurait voté contre lui, je me trompe ?"
    j "Mais le mieux, vous savez, ça n'est pas de cacher ses crimes..."
    j "Ça ne fait que de vous rendre plus suspects !"
    j "Vous {i}devez{/i} avouer vos crimes, comme l'a dit le Bourreau"
    if claim_bystander:
        menu:
            "Clamer l'innocence":
                $ renpy.fix_rollback()
                narr "Je décidai de ne rien dire quant à mes activités sur internet"
            "Avouer":
                $ renpy.fix_rollback()
                $ claim_bystander = False
                p "Je.. Je suis toujours resté dans la légalité"
                p "La seule chose préjudiciable que j'ai faite..."
                p "... ce sont des blagues racistes sur twitter"
                p "Xénophobes, quelque fois, antisémites et homophobes aussi..."
                p "Mais cela reste de l'humour noir, pour faire rire : je ne pense pas ce que j'écris"
                p "Je me suis déjà fait censurer..."
                p "...ça ne m'étonnerait pas que le Bourreau veuille me faire taire une bonne fois pour toutes..."
    narr "Pas un bruit ne se fit entendre du coté d'Isaac et Emmy"
    narr "Johann commença à siffloter"
    j "Très bien, les \"innocents\"..."
    j "Vous êtes ma prochaine cible !"
    j "Il y aura peut-être des dommages collatéraux..."
    $ annonce_importante(johann, _("...mais ceux qui cachent leurs actes sont les pires criminels."))
    $ modif_resume(204)
    l "Bien. Nous allons pouvoir passer au vote..."
    $ quick_menu = False
    $ sauvegarder("continuer")
    nvl clear
    hide haut_de_page at smooth_title
    jump vote
label suite_vote_1:
    $ quick_menu = True
    $ is_voting = False
    $ situation = "en_jeu"
    play music "music/Theme_acte_2.ogg" fadeout 3.0 fadein 3.0
    scene fondacte2 with fade
    show moving at defiler
    show text "{font=fonts/Centaur.ttf}{size=32}Acte II : Le Vote{/font}{/size}" as haut_de_page at smooth_title
    $ get_achievement("premier_vote")
    pause 1.5
    if elus_vote[1] == ["emmy"]:
        narr "Les écran des tablettes se brouillèrent, pour laisser la place au Bourreau"
        narr "Sa voix grave trancha le silence qui avait suivit le vote"
        b "S'il y avait eu égalité, les personnes concernées auraient du s'entre-tuer dans l'heure."
        narr "Johann chuchota"
        j "C'est bon à savoir..."
        b "Mais dans ce cas, les résultats du vote sont clairs."
        b "D'ici 24 heures, Emmy sera exécutée."
        $ modif_resume(205)
        b "Je vous remercie de votre collaboration."
        narr "Le visage du Bourreau disparu, et tout le monde regarda Emmy"
        narr "Elle n'était que pleurs"
        narr "Elle nous dévisagea un à un"
        e "Vous.. vous..."
        $ renpy.vibrate(1.0)
        e "{b}Vous m'avez trahi !{/b}" with sshake
        narr "Elle couru hors de la salle"
        isa "Emmy, attends !"
        narr "Isaac partit avec elle"
        narr "Johann, Leonhard, Alan et moi sortîmes dans le couloir"
        narr "Emmy s'était enfermée dans la chambre 2"
        isa "Emmy, sort ! Je te jure que tu ne vas pas mourir !"
        ala "On est pas encore sûrs que le Bourreau soit sérieux... Sois pas trouillarde !"
        l "Alan ! Tu veux absolument voir une personne mourir de ses mains pour en avoir la preuve ?..."
        l "Je {i}sais{/i} que le Bourreau est sérieux..."
        l "Il a déjà tué et va {i}encore{/i} tuer..."
        l "Ne jouons pas avec lui."
        j "Leonhard, tais-toi ! On essaye de rassurer Emmy..."
        narr "Isaac resta auprès d'Emmy, pour essayer de la rassurer."
        narr "Celle-ci préféra rester enfermée quand même."
    elif elus_vote[1] == ["alan"]:
        narr "Les écran des tablettes se brouillèrent, pour laisser la place au Bourreau"
        narr "Sa voix grave trancha le silence qui avait suivit le vote"
        b "S'il y avait eu égalité, les personnes concernées auraient du s'entre-tuer dans l'heure."
        narr "Johann chuchota"
        j "C'est bon à savoir..."
        b "Mais dans ce cas, les résultats du vote sont clairs."
        b "D'ici 24 heures, Alan sera exécuté."
        $ modif_resume(206)
        b "Je vous remercie de votre collaboration"
        narr "Le visage du Bourreau disparu, et tout le monde regarda Alan"
        narr "Il avait le visage plus crispé que jamais"
        ala "Je vois. Vous préférez tuer le \"Bad boy\", la vermine, le gars violent..."
        ala "Vous n'avez pas compris que ce sont les intellectuels les plus dangereux ?"
        narr "Il regarda Johann et Leonhard"
        ala "Ce sont {i}eux{/i}, les Bourreaux."
        narr "Sur cette accusation, il quitta calmement la pièce"
        narr "Le silence régnait dans la salle"
        narr "Johann se leva à la poursuite de Alan, puis revint"
        j "Il... il s'est enfermé dans la chambre 2..."
        narr "Nous nous déplaçâmes dans le couloir"
        isa "Alan, sort ! Je te jure que tu ne vas pas mourir"
        e "On est pas encore sûrs que le Bourreau soit sérieux"
        l "Emmy ! Tu veux absolument voir une personne mourir de ses mains pour en avoir la preuve ?..."
        l "Je {i}sais{/i} que le Bourreau est sérieux..."
        l "Il a déjà tué et va {i}encore{/i} tuer..."
        l "Ne jouons pas avec lui."
        j "Leonhard ! On essaye de mettre Alan en confiance..."
        narr "Johann resta auprès d'Alan, pour essayer de le rassurer."
        narr "Celui-ci préféra rester enfermé quand même."
    elif elus_vote[1] == ["alan", "emmy"]:
        narr "Les écran des tablettes se brouillèrent, pour laisser la place au Bourreau"
        narr "Sa voix grave trancha le silence qui avait suivi le vote"
        b "Intéressant, il y a égalité..."
        b "Vous savez que j'ai placé des explosifs dans votre corps..."
        narr "Le visage du Bourreau se figea"
        b "Emmy, Alan..."
        b "...vous allez donc devoir vous battre."
        narr "Il sourit"
        b "A mort !"
        b "Si personne ne meurt d'ici une heure, je fais exploser les bombes des personnes concernées"
        $ modif_resume(207)
        narr "Emmy regarda son bras"
        $ annonce_importante(bourreau, _("Que le combat commence."))
        narr "Elle regarda chacun d'entre nous,{w} tour à tour,{w} lentement,{w} pour finir sur Alan"
        narr "Son regard s'orienta vers son bras de nouveau"
        narr "Une flamme s'alluma dans ses yeux"
        narr "Subitement, elle courut hors de la salle"
        $ renpy.vibrate(1.0)
        ala "{b}Toi, reviens !!!{/b}" with sshake
        ala "Qu'est-ce que t'as derrière la tête, sale {b}pute{/b} ?"
        narr "Il courut à sa poursuite"
        $ sauvegarder("continuer")
        nvl clear
        narr "Après un temps d'hésitation, tout le monde se leva"
        narr "Johann, Leonhard, Isaac et enfin moi sortîmes dans le couloir"
        narr "Vide."
        narr "Silencieux."
        $ renpy.vibrate(1.0)
        unk "{b}AAAAAAAHHHH{/b}" with sshake
        narr "Le cri de détresse résonna plusieurs fois..."
        narr "...puis laissa place au silence."
        narr "Je décidai d'avancer"
        narr "1ère chambre.{w} Vide."
        narr "2ème chambre.{w} Vide."
        narr "Salle d'armes.{w} Vide."
        narr "3ème chambre.{w} Toujours vide."
        narr "Sanitaires.{w} Une porte était brisée, par terre."
        play music "music/Theme_meurtre.ogg" fadeout 2.0 fadein 2.0
        narr "En face, Alan en sang"
        narr "Mais ça n'était pas {i}son{/i} sang."
        narr "C'était le sang d'{i}Emmy{/i}."
        narr "Elle gisait par terre, dans une mare de sang."
        narr "Sans vie."
        $ emmy["statut"] = "Morte"
        narr "Alan se leva"
        narr "Il se tourna vers moi, l'air enragé"
        narr "Il se précipita sur moi..."
        narr "...puis me bouscula et courut s'enfermer dans la chambre 2."
        $ sauvegarder("continuer")
        nvl clear
        narr "Tout le monde s'attroupa autour de la chambre où s'était enfermé Alan"
        isa "{b}Tu l'as tuée ! Tu l'as tuée !{/b}"
        narr "Il prit sa tête entre ses mains"
        isa "Pourquoi ???"
        l "Pourquoi tant de violence, de cruauté ?..."
        j "Tu viens de tuer un humain, Alan..."
        menu:
            "L'encourager à parler":
                $ renpy.fix_rollback()
                $ modif_confiance([alan], [1])
                p "Dis nous, pourquoi as-tu fais ça ?.."
            "Lui crier dessus":
                $ renpy.fix_rollback()
                $ modif_confiance([alan], [-1])
                p "Espèce d'ordure, tu n'as pas de cœur ???"
        narr "Alan garda le silence"
        narr "Isaac frappa de toutes ses forces, par désespoir, sur la porte"
        $ renpy.vibrate(1.0)
        isa "{b}Pourquoi ???{/b}" with sshake
        narr "Alan hurla"
        ala "J'avais pas le choix !"
        isa "Tu avais parfaitement le choix !!!"
        narr "Johann fut frappé par quelque chose, replaça nerveusement ses lunettes, puis sourit."
        play music "music/Theme_acte_2.ogg" fadeout 2.0 fadein 2.0
        j "Non, il était dans une impasse."
        l "Alan, tu n'avais pas besoin de la tuer..."
        ala "Vous comprenez pas. Elle allait me tuer si je la butais pas !!!"
        narr "Johann prit la parole, confiant."
        j "Si, je te comprends. Et je sais même comment elle allait te tuer !"
        narr "Johann regarda autour de lui"
        j "Je suis le seul à comprendre pourquoi Alan a tué Emmy ?"
        j "Je suis le seul à savoir ce qu'avait prévu Emmy ?"
        $ countdown_time = 8
        menu:
            "Ne pas parler" ("default"):
                $ renpy.fix_rollback()
                $ modif_confiance([johann], [-1])
                narr "Johann avait l'air désespéré"
                j "Vous êtes tous stupides ou quoi ?"
            "Elle attendait la fin du compte à rebours":
                $ renpy.fix_rollback()
                $ modif_confiance([johann], [1])
                narr "Johann sourit"
                j "Exact."
            "Elle avait caché une arme là-bas":
                $ renpy.fix_rollback()
                narr "Johann avait l'air désespéré"
                j "Pas du tout..."
                $ modif_confiance([johann], [-1])
        j "Emmy voulait s'enfermer dans les toilettes pendant une heure, pour attendre la sentence du Bourreau"
        j "Elle était intelligente :"
        j "Cela aurait permis de voir si le Bourreau met à exécution ses menaces..."
        l "Tu veux absolument voir une personne mourir de ses mains pour en avoir la preuve ?..."
        l "Je {i}sais{/i} que le Bourreau est sérieux..."
        l "Ne jouons pas avec lui !"
        j "Laissons ce débat de coté, veux-tu ? Bon, je reprends."
        j "Mais {i}surtout{/i}, cela aurait tué Alan, dont la bombe est près du cœur, mais pas forcément Emmy, sa bombe étant placée dans son avant-bras..."
        narr "Alan prit la parole"
        ala "C'est ça. Elle faisait l'innocente, mais elle cachait bien son jeu."
        ala "Vous auriez vu ses yeux... Une sauvage..."
        ala "Et puis..."
        ala "Elle... Elle aurait été dangereuse pour la suite..."
        ala "C'est mon instinct."
        narr "Johann et Leonhard se regardèrent, surpris"
        
    else:
        narr "Les écran des tablettes se brouillèrent, pour laisser la place au Bourreau"
        narr "Sa voix grave trancha le silence qui avait suivi le vote"
        b "Intéressant, il y a égalité..."
        b "Vous savez que j'ai placé des explosifs dans votre corps..."
        narr "Le visage du Bourreau se figea"
        b "Emmy, Alan, Isaac..."
        b "...vous allez donc devoir vous battre."
        narr "Il sourit"
        b "A mort !"
        b "Si personne ne meurt d'ici une heure, je fais exploser les bombes des personnes concernées."
        $ modif_resume(208)
        $ annonce_importante(bourreau, _("Que le combat commence."))
        isa "Alan."
        isa "Ce combat va se jouer d'homme à homme."
        ala "D'homme à {i}mauviette{/i}."
        narr "Alan avait l'air confiant. Il se permettait de provoquer Isaac..."
        narr "C'était compréhensible, Alan devait faire deux fois le poids de son adversaire."
        narr "Isaac s'élança vers Alan."
        narr "Il prépara son poing..."
        narr "...et frappa Alan de toutes ses forces."
        narr "Ce dernier le stoppa net."
        ala "Pathétique."
        narr "Frappe d'Alan."
        narr "Il avait la force d'une presse hydraulique."
        narr "50 tonnes dans le visage d'Isaac."
        narr "Isaac tomba à terre immédiatement, assommé."
        e "{b}ISAAC !{/b}" with sshake
        narr "Emmy se précipita vers Isaac, et tourna la tête vers Alan, hargneuse."
        ala "K.O."
        ala "En un coup."
        narr "Il éclata de rire."
        ala "En {i}un coup{/i} ! La tapette !!!"
        narr "Emmy se jeta vers Alan, les mains crispées."
        ala "Hey, qu'est-ce que..."
        narr "Elle lui lacéra le visage."
        narr "Ses ongles étaient plus affutés qu'une lame."
        ala "{b}WOOOOOOH{/b}" with sshake
        ala "Sale {i}pute{/i} !"
        narr "Emmy s'enfuit dans le couloir."
        narr "Il courut à sa poursuite"
        $ sauvegarder("continuer")
        nvl clear
        narr "Après un temps d'hésitation, tout le monde se leva"
        narr "Johann, Leonhard et enfin moi sortîmes dans le couloir"
        narr "Vide."
        narr "Silencieux."
        narr "Isaac s'était relevé péniblement de l'attaque d'Alan."
        $ renpy.vibrate(1.0)
        unk "{b}AAAAAAAHHHH{/b}" with sshake
        narr "Le cri de détresse résonna plusieurs fois..."
        narr "...puis laissa place au silence."
        narr "Je décidai d'avancer"
        narr "1ère chambre.{w} Vide."
        narr "2ème chambre.{w} Vide."
        narr "Salle d'armes.{w} Vide."
        narr "3ème chambre.{w} Toujours vide."
        narr "Sanitaires.{w} Une porte était brisée, par terre."
        play music "music/Theme_meurtre.ogg" fadeout 2.0 fadein 2.0
        narr "En face, Alan en sang"
        narr "Mais ça n'était pas {i}son{/i} sang."
        narr "C'était le sang d'{i}Emmy{/i}."
        narr "Elle gisait par terre, dans une mare de sang."
        narr "Sans vie."
        $ emmy["statut"] = "Morte"
        narr "Alan se leva"
        narr "Il se tourna vers moi, l'air enragé"
        narr "Il se précipita sur moi..."
        narr "...puis me bouscula et courut s'enfermer dans la chambre 2."
        $ sauvegarder("continuer")
        nvl clear
        narr "Tout le monde s'attroupa autour de la chambre où s'était enfermé Alan"
        isa "{b}Tu l'as tuée ! Tu l'as tuée !{/b}"
        narr "Il prit sa tête entre ses mains"
        isa "Pourquoi ???"
        l "Pourquoi tant de violence, de cruauté ?..."
        j "Tu viens de tuer un humain, Alan..."
        $ countdown_time = 8.0
        menu:
            "L'encourager à parler":
                $ renpy.fix_rollback()
                $ modif_confiance([alan], [1])
                p "Dis nous, pourquoi as-tu fais ça ?.."
            "Lui crier dessus":
                $ renpy.fix_rollback()
                $ modif_confiance([alan], [-1])
                p "Espèce d'ordure, tu n'as pas de cœur ???"
            "Ne rien dire" ("default"):
                $ renpy.fix_rollback()
        narr "Alan garda le silence"
        narr "Isaac frappa de toutes ses forces, par désespoir, sur la porte"
        $ renpy.vibrate(1.0)
        isa "{b}Pourquoi ???{/b}" with sshake
        narr "Alan hurla"
        ala "J'avais pas le choix !"
        isa "Tu avais parfaitement le choix !!!"
        $ emmy["statut"] = "Morte"
        
    if "emmy" in elus_vote[1] and "alan" in elus_vote[1]:
        ala "Pour l'instant, je préfère rester enfermé dans la chambre, si ça ne vous dérange pas..."
        ala "Déjà parce que j'ai pas envie de me battre contre vous tous."
        ala "Aussi, je pense que j'ai pas réellement besoin de vous."
        isa "Et bien reste enfermé, {i}tocard{/i}, j'ai bien envie de te tuer..."
        narr "Alan eut un petit rire moqueur"
        ala "Oh, la victime se rebelle ?"
        ala "Tu veux que je sorte, pour te botter le cul ?"
        isa "Quand tu veux. Je t'en veux encore pour ce que tu m'as fait endurer au collège..."
        narr "Alan ricana"
        ala "Je sortirai pas."
        ala "Tu m'auras pas à la provoc', petite fiotte."
        ala "Et puis, je compte bien détruire le Bourreau."
        narr "Johann intervint, pour calmer le jeu entre Alan et Isaac"
        j "Alan, reste caché. Et Isaac, calme-toi."
        l "Mieux vaut réduire au maximum les meurtres au sein de notre petit groupe."
        l "Restons solidaires..."
        isa "{b}Mais il vient de tuer Emmy ! C'était mon amie !{/b}"
        j "On ne peut plus rien y faire, Isaac. Calme-toi."
        narr "Isaac grimaça"
        isa "Très bien, je sais pour qui je vais voter demain..."
        narr "Leonhard le regarda avec de gros yeux"
        l "Ne fais pas ce genre de menaces."
        l "La situation est beaucoup trop sérieuse pour blaguer avec ça."
        isa "Bah quoi ? Il a raison, je suis trop faible par rapport à lui."
        isa "Le Bourreau va se charger du sale boulot à ma place..."
        $ modif_resume(209)
    $ sauvegarder("continuer")
    nvl clear
    #================================ Scene 2 :  === choix : 2 ======================================================================
    narr "15h"
    narr "Déjà 3h depuis le vote"
    if len(elus_vote[1]) < 2:
        narr "En attendant qu'il se passe quelque chose, je décidai de visiter les lieux en détail"
    else:
        narr "Nous étions tous choqués par la mort d'Emmy"
        narr "Pour me changer les idées, je décidai de visiter les lieux en détail"
    $ simple_visit_salle_vote_acte2 = True
    $ simple_visit_salle_exec_acte2 = True
    $ simple_visit_salle_chambre_acte2 = True
    $ first_time_see_archives = True
    $ sauvegarder("continuer")
    hide haut_de_page at smooth_title
    show text "{font=fonts/Centaur.ttf}{size=32}Exploration{/font}{/size}" as haut_de_page at smooth_title
    nvl clear
    pause 1.5
    jump sec_map
        
label suite_map_1:
    $ get_achievement("decouvre_carte")
    nvl clear
    hide carte_incomplete at carte_fade
    hide carte1explore1 at carte_fade
    hide carte1explore23 at carte_fade
    hide carte1explore4 at carte_fade

    hide haut_de_page at smooth_title
    show text "{font=fonts/Centaur.ttf}{size=32}Acte II : Le Vote{/font}{/size}" as haut_de_page at smooth_title
    pause 1.5
    narr "19h"
    $ modif_resume(210)
    narr "Après avoir visité les lieux, Isaac s'était dévoué pour nous faire à manger"
    isa "Désolé, je n'ai trouvé que ça..."
    narr "Il nous tendit des assiettes de \"raviolis\" verdâtres"
    narr "Nous étions 4 assis autour de la table de la salle de vote :"
    if elus_vote[1] == ["emmy"]:
        narr "Emmy avait refusé de sortir de sa chambre pour manger"
    elif elus_vote[1] == ["alan"]:
        narr "Alan avait refusé de sortir de sa chambre pour manger"
    else:
        narr "La place d'Emmy était désespérément vide..."
        narr "... et Alan avait refusé de sortir de sa chambre pour manger"
    isa "Bon app', les gars !"
    p "Bon appétit, Isaac !"
    narr "Johann regarda son assiette puis Isaac, suspicieux."
    j "J'espère que tu n'as pas mis de poison dans le plat..."
    narr "Il rigola"
    j "Mais non Isaac, je rigole ! Il faut te détendre..."
    narr "Cela sonnait faux."
    j "Bon appétit."
    l "Merci, bon appétit à vous tous..."
    narr "Le repas se déroulait silencieusement, dans un calme presque apaisant"
    if isaac["confiance"] >= 12 and persistent.glitched:
        narr "Isaac rompit ce silence, enjoué."
        isa "Ca vous dirait de jouer à un ni oui ni non ?"
        narr "Leonhard le regarda, surpris"
        isa "Je sais que c'est bizarre, vu la situation, mais ça détendrait tout le monde, non ?"
        narr "Sans attendre la réponse de Leonhard, il demanda à Johann :"
        isa "Tu aimes les pizzas ?"
        j "Bien sûr. J'adore les hawaïennes, avec de l'ananas dessus !"
        narr "Isaac rigola. Il avait un don pour détendre l'atmosphère."
        isa "Quelle ignominie ! Elle ne devraient pas exister, c'est une hérésie !"
        j "Oh, ne t'inquiète pas, j'ai menti."
        j "Un peu comme toi quand tu as proclamé être innocent, n'est-ce pas ?"
        narr "L'ambiance qui commençait à s'installer était redescendue d'un seul coup."
        isa "Je ne pensais pas à ce genre de questions, Johann."
        isa "Le but était de se reposer, de penser à autre chose."
        j "Très bien."
        show black with None
        show text "Menteur." at truecenter as screamer with None
        $ renpy.pause(0.1)
        hide screamer
        hide black
        narr "Mais l'ambiance était retombée."
        narr "Tout le monde se replongea silencieusement dans son repas."
    narr "Lorsque tout le monde eût fini de manger, Johann brisa le silence"
    j "J'ai réfléchi..."
    isa "Ça t'arrive, des fois, de réfléchir ? Waouh."
    j "Très drôle."
    narr "Johann esquissa un sourire"
    j "Non, sérieux."
    j "On ne peut pas juste aller dormir comme ça."
    j "Il faut établir des tours de garde !"
    j "Pour surveiller tout le monde et alerter en cas de présence du Bourreau"
    if len(elus_vote[1]) < 2:
        j "Je rappelle que le Bourreau doit faire son travail ce soir..."
    else:
        narr "Johann se tourna vers Isaac"
        j "Il est possible que quelqu'un veuille se venger d'Alan"
    j "Il faut essayer de passer une nuit sans sang."
    j "Vous êtes d'accord ?"
    isa "Non."
    isa "L'idée d'organiser des tours de garde est mauvaise !"
    isa "Je pense qu'il suffit de bloquer les portes"
    isa "L'idée des tours de garde que tu propose va nous épuiser : mieux vaut passer une bonne nuit afin de garder la forme..."
    isa "... pour être opérationnels au bon moment !"
    j "Tu sais qu'il est inutile de fermer les portes à clé ? Le Bourreau possède sûrement toutes les clés..."
    isa "Il suffirait de les bloquer avec une chaise, ou un lit, par exemple..."
    isa "...et puis faire le garde pourrait nous coûter la vie : il pourrait nous attaquer seul, dans le couloir, sans aucun problème !"
    narr "Les lunettes de Johann brillèrent :"
    j "C'est {i}là{/i} où tu as tort, Isaac !"
    j "Le Bourreau veut {i}jouer{/i}, pas tuer tous les {i}gardes{/i} qui surveillent celui qui doit être exécuté..."
    j "Les gardes, en plus de nous garantir une sécurité, pourront peut-être voir le Bourreau ou autres choses utiles..."
    narr "Isaac n'avait pas l'air convaincu"
    l "Je propose..."
    narr "Isaac et Johann avaient déjà compris la fin de la phrase"
    l "(accompagné d'Isaac et de Johann) ... de faire un {i}vote{/i} !"
    menu:
        "Organiser des tours de garde (Johann)":
            $ renpy.fix_rollback()
            $ modif_confiance([emmy, isaac, alan, johann, leonhard], 
                              [0   , -1   , 0   , 1     , 0       ])
            p "Je suis d'accord avec Johann"
            narr "Tout le monde était de cet avis"
        "Dormir enfermés (Isaac)":
            $ renpy.fix_rollback()
            $ modif_confiance([emmy, isaac, alan, johann, leonhard], 
                              [0   , 1    , 0   , -1    , 0       ])
            p "Je suis d'accord avec Isaac"
            if elus_vote[1] == "emmy":
                narr "Leonhard et Alan n'étaient pas de mon avis"
            elif elus_vote[1] == "alan":
                narr "Leonhard et Emmy n'étaient pas de mon avis"
            else:
                narr "Leonhard n'était pas de mon avis"
                isa "Égalité... Bon, je veux bien te donner raison cette fois, Johann."
    narr "Les tours de garde suivant furent organisés:"
    if len(elus_vote[1]) >= 2:
        narr "Moi, Leonhard, Johann puis Isaac."
        narr "Alan n'allait pas faire de garde."
        narr "Il va faire sa propre garde dans sa chambre..."
        narr "A vrai dire, j'avis peur qu'Isaac se venge sur lui."
        narr "Il avait l'air si proche d'Emmy !"
    elif elus_vote[1]==["emmy"]:
        narr "Alan, moi, Leonhard, Johann puis Isaac."
    elif elus_vote[1]==["alan"]:
        narr "Moi, Leonhard, Johann puis Isaac."
        narr "Emmy ne voulait pas monter la garde, et de toute façon Alan avait crié ne pas lui faire confiance..."
    l "Très bien."
    l "Il y a deux lits individuels par chambre."
    l "Il ne reste plus qu'à choisir avec qui vous voulez partager votre chambre !"
    if elus_vote[1]==["alan"]:
        e "Mais on est 5, et Alan est déjà enfermé dans sa chambre !"
        narr "Johann la regarda avec dédain."
        j "Il y aura un garde, donc on sera seulement 4 à dormir... On tournera."
        j "Kurt, tu choisis qui ?"
    menu:
        "Leonhard":
            $ modif_confiance([leonhard], [1])
            p "Je fais confiance à Leonhard"
            l "Je vous fais confiance à vous aussi, Kurt."
            $ sleep_with = "leonhard"
        "Isaac" if isaac["confiance"] >= 11:
            $ modif_confiance([isaac], [1])
            p "Je fais confiance à Isaac"
            isa "Cool !"
            $ sleep_with = "isaac"
        "Johann" if johann["confiance"] >= 11:
            $ modif_confiance([johann], [1])
            p "Je fais confiance à Johann"
            j "Super !"
            $ sleep_with = "johann"
    $ sauvegarder("continuer")
    nvl clear
    $ modif_resume(211)
    narr "À 21h, je commençai mon tour de garde."
    if sleep_with == "leonhard":
        l "Bon courage, Kurt"
        p "Merci, Leonhard..."
    elif sleep_with == "johann":
        j "Bon courage, Kurt. Tout va bien se passer, ne t'inquiète pas !"
        p "Merci, Johann..."
    else:
        isa "Courage, Kurt ! Si Johann a raison, tu ne risques rien !"
        p "Je l'espère..."
    narr "J'avais quand même une légère appréhension."
    $ sauvegarder("continuer")
    nvl clear
    narr "Tout le monde était parti se coucher."
    narr "J'étais seul dans l'obscurité"
    narr "Je me sentais {i}tellement{/i} vulnérable..."
    narr "Mais je finis par m'habituer aux ténèbres et à la solitude, et à ne plus entendre les bruits discrets et inquiétants venant de derrière la porte de sortie."
    narr "..."
    narr "Mais au fond de moi, cette attente me terrifiait."
    narr "Je finis mon tour de garde vers minuit, sain et sauf."
    $ sauvegarder("continuer")
    nvl clear
    if sleep_with == "leonhard":
         narr "Je réveillai Leonhard assez difficilement, qui partit faire son tour de garde, et me couchai seul."
    elif sleep_with == "isaac": 
        narr "Je réveillai Leonhard assez difficilement, qui partit faire son tour de garde, et rejoignis Isaac pour la nuit."
        isa "Kurt, c'est toi ?"
        p "Oui, c'est moi."
        p "Tu devrais dormir, tu sais ? Profite que les autres montent la garde pour te reposer !"
        isa "Je sais, je sais. Mais je n'y arrive pas."
        isa "J'en ai marre de ce jeu. Trop marre."
        isa "..."
        narr "Isaac semblait réellement dépassé. Il restait silencieux et pensif."
        p "Vas-y !"
        isa "Quoi ?"
        p "Je sens que tu as quelque chose à me dire."
        isa "Je..."
        isa "Je pense me suicider."
        $ modif_bio(isaac, 3)
        isa "J'en peut plus de ma vie. Même dehors de {i}ça{/i}, je veux dire."
        isa "Ma vraie vie est déjà {i}merdique{/i}."
        isa "Et si je me suicide ici, maintenant, ça sauvera l'un d'entre vous."
        $ modif_bio(isaac, 2)
        isa "En plus, ça frustrera ce malade mental, le {i}Bourreau{/i} ou peu importe quel nom il se donne."
        if emmy["statut"] == "Morte":
            isa "Et puis, Emmy est morte..."
            narr "Isaac détourna la tête"
            isa "C'est trop pour moi..."
        else:
            narr "Il secoua la tête."
        $ countdown_time = 8.0
        menu:
            "Le rassurer":
                p "Le Bourreau ne devrait pas exister."
                narr "Isaac releva la tête."
                p "S'il n'avait pas organisé ce truc, là... Tout le monde irait mieux."
                p "On ne devrait pas avoir à vivre cela."
                p "Et si on est tous des criminels, nous aurions du être jugés."
                p "Le Bourreau ne devrait pas exister, et ce Jeu non plus."
                isa "Mais il existe..."
                p "Je pense que le Bourreau va être juste envers nous."
                narr "Isaac hocha la tête, en signe d'approbation."
                $ modif_confiance([isaac], [1], "cacher")
                isa "Tu as raison."
                isa "Il punira ceux qui ne se repentent pas."
            "Rester silencieux" ("default"):
                pass
        narr "Isaac partit se coucher, et pleura en silence pendant un quart d'heure avant de s'endormir."
    elif sleep_with == "johann":
        narr "Je réveillai Leonhard assez difficilement, qui partit faire son tour de garde, et rejoignis Johann pour la nuit."
        narr "Ce dernier sursauta en m'entendant entrer."
        j "Kurt... C'est toi putain ?"
        p "Oui pourquoi ?"
        j "Désolé..."
        j "Je suis sur les nerfs en ce moment."
        j "Ton tour de garde s'est bien passé ?"
        p "Oui, il ne s'est pas passé grand chose."
        j "Normal, entre 21h et minuit, il ne se passe rien... Les choses peuvent bouger vers 4 ou 5 heures du matin, je pense."
        j "C'est pour ça que je me suis proposé pour ces horaires, je ne veux pas imposer du danger à quelqu'un d'autre..."
        j "... d'autant plus qu'organiser des tours de garde était mon idée."
        j "Je ne veux pas être le responsable s'il arrive malheur à l'un de nous..."
        j "Enfin bref. Bonne nuit, Kurt."
        p "Bonne nuit, Johann !"
    narr "Mon sommeil fut profond et ininterrompu pendant toute la nuit..."
    $ sauvegarder("continuer")
    nvl clear
    #================================ Scene 3 :  ===  ======================================================================

    narr "Jour 2, 7h"
    narr "Mon réveil ne sonnait pas la fin du cauchemar mais plutôt son commencement"
    narr "D'un air las, et peu confiant, je me levai et me dirigeai vers la porte"
    narr "Celle-ci s'avéra verrouillée à clé... Il n'y avait aucun moyen de l'ouvrir..."
    narr "Même en ouvrant avec la clé, quelque chose bloquait la porte"
    if sleep_with == "isaac" :
        narr "Isaac avait commencé son tour de garde il y a une heure, et n'était toujours pas là"
    narr "Étrange..."
    play sound "sounds/footsteps.ogg" loop
    narr "Soudain, un bruit."
    stop music fadeout 10.0
    narr "Des bruits de pas."
    narr "Mécaniques."
    narr "{i}Quelqu'un{/i} marchait dans le couloir."
    narr "Ou {i}quelque chose{/i}."
    narr "Les pas se rapprochaient."
    if sleep_with == "johann" :
        narr "Johann dormait toujours."
    elif sleep_with == "leonhard":
        narr "Leonhard dormait toujours."
    narr "Les bruits de pas étaient de plus en plus clairs."
    stop sound
    narr "Et puis, plus rien..."
    play sound "sounds/breathing.ogg"
    narr "...suivi d'une respiration bruyante."
    narr "Qui ou quoi {i}ça{/i} était..."
    narr "{i}Ça{/i} était juste devant la porte."
    menu:
        "Regarder par la serrure":
            $ renpy.fix_rollback()
            $ screamer_nuit1 = True
            narr "J'approchai de la porte."
            narr "Le bruit continuait."
            if sleep_with == "johann" :
                narr "Derrière moi, Johann dormait toujours profondément."
            elif sleep_with == "leonhard":
                narr "Derrière moi, Leonhard dormait toujours profondément."
            narr "J'avançai lentement vers la porte, ..."
            narr "...pris mon courage à deux mains, ..."
            narr "... et regardai par le trou de la serrure."
            narr "C'était une {i}créature{/i} hybride."
            narr "Sanglante."
            stop sound fadeout 10.0
            narr "Un mélange de {i}chair{/i} et de {i}métal rouillé{/i}."
            narr "C'était {i}ça{/i}, le Bourreau ?"
            narr "La {i}créature{/i} recommença à bouger."
            narr "..."
            narr "Je voulais m'enfuir."
            narr "..."
            narr "Mais impossible."
            narr "..."
            narr "J'étais paralysé."
            narr "..."
            narr "Pourquoi ?"
            narr "..."
            narr "Parce que..."
            narr "{i}Ça{/i} me regardait.{w=0.5}{nw}"
            nvl clear
            $ quick_menu = False
            play sound "sounds/jumpscare.ogg" noloop
            show jumpscareNuit1
            $ renpy.vibrate(1.5)
            pause 0.8
            hide jumpscareNuit1
            show black with dissolve
            pause 3.0
            hide black with dissolve
            $ quick_menu = True
        "Bloquer la porte":
            $ renpy.fix_rollback()
            $ screamer_nuit1 = False
            narr "Je pris une chaise dans la chambre, et la coinça sous la poignée..."
            narr "...qui se mit à tourner lentement."
            narr "La porte bougea..."
            narr "Mais ne s'ouvrit pas."
            unk "..."
            unk "k..."
            unk "klAuSSS"
            unk "..."
            unk "KlAauUUsss..."
            unk "..."
            unk "C'est kLAusssSS ?"
            unk "..."
            $ renpy.vibrate(0.5)
            unk "{b}kLAAuuUSSss ?{/b}" with sshake
            unk "..."
            unk "Pas Kllaauss ?"
            unk "..."
            narr "La {i}créature{/i} partit."
            stop sound
    nvl clear
    play music "music/Theme_acte_2.ogg" fadein 5.0
    narr "La créature était partie."
    $ modif_resume(212)
    narr "Plus de peur que de mal..."
    narr "... même si j'étais encore tétanisé."
    narr "Je retournai dans mon lit, sans pour autant réussir à m'endormir."
    $ sauvegarder("continuer")
    nvl clear
    narr "À 9h, une sonnerie retentit violemment"
    narr "Évidemment, la porte était maintenant ouverte..."
    narr "Tout le monde sorti aussitôt dans le couloir"
    if len(elus_vote[1]) < 2:
        $ perso = elus_vote[1][0].title()
        narr "Tout le monde... sauf Isaac et [perso]"
    else:
        narr "Tout le monde... sauf Isaac et Emmy."
    narr "Isaac gisait, inconscient et la tête en sang, derrière les barreaux de la salle d'armes."
    narr "Johann se rua vers la porte, mais..."
    narr "...elle était fermée à clé."
    l "Isaac, ça va ?"
    p "Isaac, réponds-nous ! T'es vivant ???"
    narr "Johann hurla"
    $ renpy.vibrate(1.0)
    j "{b}ISAAC !{/b}" with sshake
    narr "Isaac se leva lentement, tout en tenant sa tête ensanglantée"
    isa "Oui... oui......"
    if len(elus_vote[1]) < 2:
        isa "Mais..."
        isa "Ne...ne faites pas..."
        narr "Il marqua une pause"
        isa "... pas attention à moi"
        isa "Je suis pas... important."
        isa "Regardez..."
        narr "Il tendit faiblement l'index droit devant lui, en larmes"
        narr "Tout le monde suivit son regard"
        narr "La chambre 2 était ouverte..."
        play music "music/Theme_meurtre.ogg" fadeout 4.0 fadein 4.0
        narr "Le Bourreau avait mit à exécution sa menace."
        narr "La pièce était remplie de sang."
        narr "C'était une boucherie..."
        narr "Des membres dispersés un peu partout dans la pièce."
        narr "Du sang mêlé aux draps."
        narr "Une hache vermillon plantée au milieu de la chambre."
        narr "La lame enfoncée dans le sol."
        narr "..."
        if elus_vote[1] == ["emmy"]:
            narr "La tête d'Emmy pendue au manche."
            $ modif_resume(213)
            $ emmy["statut"] = "Morte"
        else:
            narr "La tête d'Alan pendue au manche."
            $ modif_resume(214)
            $ alan["statut"] = "Mort"
        narr "Ses boyaux traînaient sur le sol, en lambeaux."
        narr "Johann eut un mouvement de recul"
        j "Ugh... C'est... c'est pas humain..."
        j "Le Bourreau est un {i}MONSTRE{/i}..."
        narr "Leonhard s'avança calmement."
        narr "Il avait le teint pâle, mais ne semblait pas au bord du vomi comme l'était Johann, ni en pleurs comme Isaac"
        if elus_vote[1] == ["emmy"]:
            narr "Alan avait les yeux exorbités devant ce carnage"
        else:
            narr "Emmy avait les yeux exorbités devant ce carnage"
        narr "Leonhard marcha vers la pièce et referma la porte"
        l "Cela vaut mieux pour nous tous..."
        l "Occupons-nous d'Isaac, plutôt..."
        play music "music/Theme_acte_2.ogg" fadeout 2.0 fadein 2.0
    l "Isaac, que s'est-il passé ?"
    narr "Isaac prit sa tête, toujours douloureuse, dans ses mains"
    isa "Johann m'a réveillé pour mon tour de garde, vers 6 heures..."
    isa "J'ai à peine fait quelques pas et puis ..."
    isa "BAM! Plus rien..."
    isa "{i}Exactement{/i} comme lorsqu'on nous a ramenés ici..."
    isa "Et avant, j'ai vu quelque chose... d'{i}étrange{/i}."
    isa "Quelque chose qui {i}n'était pas humain{/i}."
    isa "Je... je crois que c'était le Bourreau. Mais..."
    isa "Il lui manquait des membres, et il était comme {i}décharné{/i}."
    isa "Il y avait du métal mélangé à sa chair un peu partout."
    isa "C'était vraiment horrible."
    $ modif_resume(215)
    j "C'est impossible."
    narr "Johann n'avait pas l'air de croire Isaac. Il était perturbé."
    $ countdown_time = 8.0
    menu:
        "Je l'ai vu aussi" if screamer_nuit1:
            p "Moi aussi, je l'ai vu, par le trou de ma serrure !"
            p "Isaac a raison... Cette {i}Créature{/i}... Elle est horrible !"
            narr "J'avais des frissons rien que d'y penser."
            p "C'est indescriptible."
            narr "Isaac avait l'air retourné, mais soulagé de savoir que quelqu'un partageait son souvenir cauchemardesque"
            j "Étrange..."
            $ modif_confiance([emmy, isaac, alan, johann, leonhard], 
                          [0   , 1    , 0   , -1     , 0       ])
        "Je l'ai entendu" if not screamer_nuit1:
            p "J'ai entendu quelque chose aussi. Près de ma porte."
            narr "J'avais des frissons rien que d'y penser."
            p "C'est indescriptible."
            p "La {i}chose{/i} hurlait un nom... Elle cherchait quelqu'un."
            p "Mais ce n'étais pas un de nous six qu'elle cherchait."
            j "Étrange..."
        "Ne rien dire" ("default"):
            j "Tu es sûr d'avoir bien vu ?"
            if elus_vote[1] == ["alan"]:
                e "C'est le Démon..."
                narr "Johann ricana."
            else:
                ala "Il est fou. La peur te fais perdre tes sens, Isaac."
            j "C'était sûrement une hallucination."
            isa "Je ne sais pas. Peut-être..."
            isa "Il fait tellement sombre ici... Ne pas voir la lumière du jour me rend malade."
    isa "Mais bon, au moins, je suis en vie..."
    narr "Difficilement, il sourit pour détendre l'atmosphère et montrer qu'il allait bien"
    isa "J'aimerais m'endormir différemment, ça fait 2 jours de suite qu'on m'assomme pour dormir, haha !"
    $ modif_bio(isaac, 4)
    narr "Johann sourit légèrement"
    narr "Les yeux d'Isaac furent attirés par quelque chose sur la porte de la chambre 2"
    isa "Regardez, on dirait un message !"
    narr "{image=documents/parchemin.png}"
    narr "Isaac avait un sourire narquois"
    isa "On va encore voter ? Ce vote là est assez facile ! Choisissez de me libérer et c'est bon..."
    j "Tu n'as rien compris ? Vraiment ? Je te pensais plus malin, Isaac."
    narr "Isaac grommela pour lui-même :"
    isa "J'ai pas eu une nuit facile, s'il te plaît..."
    j "C'est juste une invitation {i}évidente{/i} à se rendre en salle de vote..."
    j "Il doit y avoir un piège, ou une contrepartie à fournir..."
    j "En tout cas, il y a quelque chose là-bas !"
    $ sauvegarder("continuer")
    nvl clear
    narr "La salle de vote était teintée d'une lumière rouge"
    narr "Au centre de la pièce, l'écran d'Isaac était allumé."
    narr "Une vidéo était sur \"Pause\""
    narr "Leonhard appuya sur \"Jouer\" et attendit."
    narr "Rien ne se produisit les 3 premières secondes..."
    narr "Puis la lumière s'éteint."
    $ sauvegarder("continuer")
    nvl clear
    narr "Une voix gronda dans l'obscurité"
    b "Isaac a été puni, pour avoir perturbé le fonctionnement du Jeu."
    b "Mais ça n'est qu'un détail."
    if elus_vote[1] == ["alan"]:
      b "L'un d'entre nous nous a quitté depuis ma dernière intervention..."
      b "Alan était un être violent et feignant."
      b "Il ne valait pas mieux qu'un {i}déchet{/i} !"
      b "Les causes de son exécution sont nombreuses"
      b "Violent envers son entourage, proche ou lointain, il inspirait la peur dans son quartier"
      b "Sa mort entraîne la fin de son trafic malsain de stupéfiants empoisonnant la population"
      b "...et conforte les innocents qu'il maltraitait."
      $ modif_bio(alan, 2)
    else:
      b "L'une d'entre nous nous a quitté depuis ma dernière intervention..."
      b "Emmy, derrière son air innocent, cachait un tempérament colérique, instable, intolérant"
      b "Voici son atroce histoire :"
      b "Elle n'a jamais vu son père. Il est parti avant sa naissance, qui a été un désastre. Des complications à l'accouchement ont mené à la mort de la mère."
      b "Orpheline de naissance, elle a été élevée par 2 hommes..."
      b "...homosexuels."
      b "Raillée par ses \"amies\", elle se mit à détester ses parents"
      b "Elle passa toute son enfance seule, sans amies."
      b "Les filles de sa classe se moquaient d'elle et la rejetaient."
      b "La haine s'accumulait tous les jours sous les remarques blessantes."
      b "Elle devint de plus en plus sèche avec ses pères, et {i}retournait sa rage{/i}, non pas contre ses amis..."
      b "...mais contre ceux qui l'aimaient comme leur vraie fille..."
      b "Après une dizaine de fugues, à 15 ans, elle décida d'en finir."
      b "Elle ne pouvait plus supporter de vivre."
      b "Elle avait {i}trop{/i} souffert."
      b "Elle mit le feu à la maison familiale."
      b "Le feu a tout détruit."
      b "Ses parents, morts."
      b "Elle allait pouvoir recommencer sa vie à zéro."
      b "De toute façon, personne ne pourrait jamais suspecter la petite fille de meurtre :"
      b "Comment une petite fille pourrait tuer 2 hommes robustes, qui l'ont élevée et chérie ?"
      b "Emmy joua la comédie, et cacha le monstre qu'elle était devenue sous un masque innocent d'adolescente perdue"
      $ modif_bio(emmy, 1, set_value=False)
      $ modif_bio(emmy, 2)
      $ modif_bio(emmy, 3)
    b "Réjouissez-vous de sa mort..."
    narr "Un instant se silence suivi cette déclaration morbide"
    b "Mais je n'ai pas fini de jouer avec vous."
    b "Je le rappelle, il doit n'en rester que trois !"
    b "La {i}salle des archives{/i} est désormais ouverte"
    b "De plus, je tiens à vous le dire..."
    play music "music/Theme_meurtre.ogg" fadeout 0.8 fadein 0.6
    narr "Il continua d'un ton enjoué :"
    $ annonce_importante(bourreau, _("Je suis {b}{i}l'un d'entre vous{/i}{/b} !"))
    narr "Il éclata d'un rire hystérique"
    b "Bonne {i}chance{/i} !..."
    $ sauvegarder("continuer")
    nvl clear 
    narr "La lumière revint subitement"
    
    narr "Tout le monde était secoué par l'intervention du Bourreau"
    if elus_vote[1] == ["alan"]:
      narr "Alan était vraiment aussi mauvais que ça ? ..."
      narr "Mais surtout, l'un d'entre nous est le Bourreau ?"
      narr "Emmy ?"
    else:
      narr "Emmy était vraiment une criminelle ? ..."
      narr "Mais surtout, l'un d'entre nous est le Bourreau ?"
      narr "Alan ?"
    narr "Isaac ?"
    narr "Johann ?"
    narr "Ou Leonhard ?"
    narr "Cela semblait irréaliste."
    $ modif_resume(216)
    l "Le Bourreau est parmi nous ? Je m'y attendais."
    j "Mais alors... La créature qui a assommé Isaac cette nuit..."
    j "C'était {b}{i}quoi{/i}{/b} ?"
    $ sauvegarder("continuer")
    nvl clear
    hide moving at defiler
    scene black with fade
    $ quick_menu = False
    hide haut_de_page at smooth_title
    show screen menu_background()
    show screen menu_title_coal()
    call screen in_game_menu(acte=acte)
    
    
#================================================#
#===============     Acte III     ===============#
#================================================#
label acte3:
    $ acte = 3
    $ acte_romain = "III"
    $ persistent.sauvegarde_info[partie_actuelle][0] = 3
    nvl clear
    scene black with fade #at inkdissolve
    n "C'est le dev qui vous parle !"
    n "Est-ce que vous avez aimé les 2 premiers actes ?"
    n "Ca serait vraiment cool que vous m'envoyiez vos réactions !"
    n "...et que vous laissez un petit 5 étoiles sur le play store ;) "
    n "Je code nuit et jour depuis maintenant 2 ans et demi..."
    n "...je veux faire le maximum pour qu'il ait un maximum de succès à sa sortie officielle !"
    n "La grande énigme commencera à l'acte IV du jeu, pour l'instant vous ne pouvez pas vraiment envisager ce qui est en train de se passer."
    n "Vous ne pouvez pas voir le but principal..."
    n "...mais une grande partie des indices se trouve ici, dans les actes I, II et III, ne laissez rien passer à côté ! ;)"
    n "Et n'hésitez pas à m'envoyer vos {b}commentaires{/b}, des {b}bugs{/b}, des {b}fautes d'orthographe{/b} ou des {b}incohérences{/b} !"
    n "Bon jeu !"
    nvl clear
    play music "music/Theme_acte_3.ogg" fadeout 3.0 fadein 3.0
    scene fondacte3 with fade
    show moving at defiler
    $ quick_menu = True
    pause 0.5
    show text _("{font=fonts/Centaur.ttf}{size=72}Acte III\n\nLe Jeu{/size}{/font}") as title at truecenter with dissolve
    pause 1.5
    hide title with dissolve
    show text _("{font=fonts/Centaur.ttf}{size=32}Acte III : Le Jeu{/size}{/font}") as haut_de_page at smooth_title
    nvl clear
    $ sauvegarder("continuer", montrer = False)
    #================================ Scene 1 :  ===  ======================================================================
    narr "Il n'était pas encore 11h."
    narr "Nous avions ouvert la porte à Isaac. Lui aussi avait entendu la sinistre déclaration du Bourreau."
    narr "Il restait du temps avant le second tour, aussi nous avions décidé de visiter la salle débloquée par le Bourreau ..."
    narr "Leonhard, Isaac et Johann me suivaient"
    if elus_vote[1] == ["alan"]:
        narr "Emmy était aussi sortie."
    else:
        narr "Alan était aussi sorti."
    narr "Nous entrâmes donc dans la pièce inconnue"
    narr "Les murs de cette dernière était recouverts de bibliothèques, comme attendu d'une salle d'archives"
    narr "De plus, une bibliothèque était disposée en plein milieu de la pièce, empêchant de distinguer ce qu'il y avait derrière"
    narr "Des minutes de procès et des codes pénaux de différents pays recouvraient les 4 murs"
    narr "Un vieil ordinateur diffusait une lumière froide sur ces livres poussiéreux."
    narr "Sur la bibliothèque centrale étaient disposés des livres bien plus singuliers"
    narr "On y retrouvait nombreux livres de la littérature française, anglaise et américaine."
    narr "Un livre ressortait du lot :"
    narr "Il était intitulé {i}HowtoPunish{/i}, et trônait fièrement, seul, sur l'étagère du haut de cette bibliothèque"
    narr "Je le pris, puis tournai la tête vers Johann"
    narr "Il me répondit par un mouvement de tête, signifiant : 'Vas-y' "
    narr "J'ouvris donc cet inquiétant livre."
    narr "Il était rempli de scènes de massacres et de tueries..."
    if elus_vote[1] == ["alan"]:
        narr "Emmy, qui regardait par dessus mon épaule, eut un mouvement de recul."
        e "C'est... c'est glauque !"
    else:
        narr "Alan, qui regardait par dessus mon épaule, avait l'air fasciné."
        ala "Il rigole pas, lui, wesh..."
    narr "En regardant de plus près, le livre décrivait..."
    narr "...ce qu'il se passe ici même..."
    narr "Leonhard interrompit ma lecture"
    l "Je vous l'avait dit, maintenant en voici une preuve :"
    l "Ce qu'il fait actuellement s'est déjà produit dans le passé"
    l "Il n'en est pas à son premier coup d'essai..."
    l "Cela s'est déjà passé 9 fois pour être précis."
    l "À 2 différences près : il ne s'est jamais mêlé à ses futures victimes..."
    l "...et personne n'a jamais survécu."
    l "Du moins, pas à ma connaissance."
    j "Mais c'est peut être toujours le cas : il nous a peut-être menti tout à l'heure !"
    j "Rien ne nous dit qu'il est {i}vraiment{/i} parmi nous : il veut peut-être juste nous diviser..."
    l "Néanmoins, nous pensons que pour \"fêter\" son 10ème {i}Jeu{/i}, comme il l'appelle, il fera quelque chose de {i}spécial{/i}."
    l "Ces 2 anomalies dans son mode opératoire le prouvent !"
    isa "Mais on ne sait jamais : mieux vaut ne pas prendre pour argent comptant ce que nous a dit le Bourreau !"
    j "Soyons attentifs, et réfléchissons avant d'agir."
    isa "Exact. D'autant plus que le Bourreau... "
    j "... est {i}un de nous 5{/i}."
    isa "Trouver {i}qui{/i} est le Bourreau est facile, il suffit d'un peu de temps et de stratégie..."
    j "Je suis d'accord. Nous sommes assez intelligents pour le trouver !"
    narr "Il regarda malicieusement Leonhard."
    j "Et j'ai déjà des pistes..."
    j "Mais {i}d'abord{/i}..."
    j "...je dois vérifier quelque chose..."
    narr "Johann recula de trois pas."
    narr "Il ferma la porte de la salle à clé, et fit face à Isaac."
    narr "Il s'approcha de lui lentement, et lui susurra à l'oreille :"
    j "{size=-5}Dis-moi, Isaac, as-tu peur du Bourreau ?{/size}"
    narr "Isaac pâlit subtilement."
    isa "Hein ? Pourquoi ?"
    narr "Johann éclata d'un rire fou, avant de reprendre un air sérieux."
    play music "music/Theme_acte_6.ogg" fadeout 0.5 fadein 0.5
    $ renpy.vibrate(1.0)
    j "{b}PARCE QUE JE SUIS LE BOURREAU !!!{/b}" with sshake
    narr "Tout les regards étaient tournés vers Johann."
    j "{b}ET QU'EST-CE QUE TU VAS FAIRE ???{/b}"
    narr "Immédiatement, Isaac courut se cacher."
    if elus_vote[1] == ["alan"]:
        narr "Emmy courut pour rejoindre d'Isaac."
    else:
        narr "Alan craqua ses phalanges, prêt à se battre."
    narr "Leonhard ne bougea pas d'un pouce."
    $ countdown_time = 15.0
    menu:
        "Se cacher avec Isaac":
            narr "Face à cette révélation, je préférai me cacher aux côtés d'Isaac"
            $ revelation_bourreau_couteau = False
        "Coup de couteau" if inventaire["knife"]["nb"] == 1:
            narr "Je brandis mon couteau vers Johann"
            $ revelation_bourreau_couteau = True
        "Rester immobile" ("default"):
            narr "Préférant ne pas attirer l'attention de Johann, je ne bougeai pas d'un pouce"
            $ revelation_bourreau_couteau = False
    if revelation_bourreau_couteau:
        j "{b}Wooow !!!{/b} Calme toi, Kurt." with sshake
        j "Baisse ton couteau."
        j "Mon but était {i}juste{/i} de tester vos réactions."
        narr "Malgré la situation tendue, je décidai de baisser mon arme."
        j "Je voulais voir {i}qui{/i} était capable de se battre contre le Bourreau."
        j "Je suis plutôt déçu d'Isaac. Par contre, toi, Kurt..."
        $ modif_confiance([isaac, johann], [1, 2])
        j "... tu as les tripes pour le vaincre."
        narr "Leonhard balbutia"
        l "Je... je savais que tu nous testais. C'est pour ça que je n'ai pas bougé."
        j "Bien sûr. Et toi, Isaac ?"
    elif not ("alan" in elus_vote[1]):
        narr "Alan, vif, leva son poing."
        j "{b}Wooow !!!{/b} Calme toi, Alan." with sshake
        j "Calme toi."
        j "Mon but était {i}juste{/i} de tester vos réactions."
        narr "Alan stoppa net, mais il restait prêt. "
        narr "La situation était tendue."
        j "Je voulais voir {i}qui{/i} était capable de se battre contre le Bourreau."
        $ modif_confiance([johann], [-2])
        j "Je suis déçu d'Isaac, Leonhard et Kurt. Par contre, toi, Alan..."
        j "... tu as les tripes pour le vaincre."
        narr "Leonhard balbutia"
        l "Je... je savais que tu nous testais. C'est pour ça que je n'ai pas bougé."
        j "Bien sûr. Et toi, Isaac ?"
    else:
        j "{b}RIEN ! TU NE VAS RIEN FAIRE ! ET NI LEONHARD, NI KURT NON PLUS{/b}"
        narr "Johann marqua une pause."
        j "Comment voulez-vous survivre ?"
        narr "Il était triomphant, mais désappointé. Il nous regardait avec pitié."
        j "Si vous n'êtes même pas capable de lutter contre le Bourreau, qu'allez vous faire ?..."
        j "Je ne suis {i}pas{/i} le Bourreau."
        j "Je voulais juste voir si vous aviez le courage de le battre..."
        $ modif_confiance([isaac, johann], [1, -2])
        j "... et je suis déçu..."
    narr "Secoué par la mise en scène de Johann, Isaac se renfrogna"
    isa "Je n'aurai pas la force de le tuer, tu as raison..."
    isa "Mais tu m'as fait peur avec cette mise en scène..."
    isa "Je croyais que tu étais {i}vraiment{/i} le Bourreau..."
    isa "..."
    isa "Mais tu l'es peut-être réellement !"
    narr "Leonhard souriait face à ce retournement de situation"
    l "C'est {i}ça{/i}, le 10ème Jeu du Bourreau..."
    l "Il en a eu marre des bains de sang faciles et défouloirs..."
    l "Il voulait un défi cette fois..."
    l "Il s'est mêlé à nous, afin de {i}jouer{/i} avec nous, et nous perdre..."
    l "Il {i}sait{/i} que nous allons jouer son jeu"
    l "{i}Qui{/i} est le vrai Bourreau ?"
    l "C'est ce qu'il faut découvrir..."
    narr "Leonhard sourit subtilement."
    narr "Même si c'était moins flagrant que pour Johann et Isaac, ce Jeu mortel avait aussi l'air de lui plaire"
    l "Et il compte nous éliminer jusqu'au dernier, sans nul doute..."
    isa "Sauf si nous échappons à son jeu !"
    j "Pour cela, il faudra redoubler de vigilance, car je dois l'avouer..."
    j "...il est malin..."
    narr "La réponse d'Isaac trancha brutalement"
    isa "Oh, non, il est plutôt facile d'échapper à son jeu !"
    isa "Il suffit de se suicider."
    narr "Johann fit de grands yeux"
    j "Pardon ???"
    narr "Isaac sourit, d'un air narquois"
    isa "Ben oui, si tout le monde se suicide, le Bourreau aura perdu car il ne pourra plus {i}jouer{/i}..."
    $ modif_bio(isaac, 3)
    j "Toi aussi tu auras perdu..."
    j "... la {b}{i}vie{/i}{/b}, putain."
    j "C'est stupide ! Ne fais pas ça..."
    narr "Johann prit une grande inspiration"
    j "J'adore ce {i}Jeu{/i}..."
    narr "Il était aux anges"
    j "Enfin un {i}vrai{/i} défi à mon niveau... et avec de {i}vrais{/i} enjeux..."
    narr "Plus réservé, Leonhard semblait aussi prit par le {i}Jeu{/i}"
    l "Pour ma part, je compte bien jouer le jeu... Et le gagner..."
    $ sauvegarder("continuer")
    nvl clear
    play music "music/Theme_acte_3.ogg" fadeout 3.0 fadein 3.0
    $ modif_resume(317)
    narr "Après la visite de cette nouvelle pièce, le groupe semblait plus divisé que jamais"
    narr "L'heure du deuxième vote approchait."
    narr "L'avant-dernier vote."
    narr "Le choix de chacun allait être décisif."
    $ sauvegarder("continuer")
    nvl clear
    narr "Midi. Heure du vote."
    $ vote2 = 0 #initialisation needed
    narr "Tout le monde se réunit en silence..."
    l "On se retrouve, pour le deuxième vote."
    l "Vous avez quelque chose à dire ?"
    menu:
        "Dénoncer Isaac et son couteau" if not simple_visit_salle_exec_acte2:
            $ renpy.fix_rollback()
            $ grosse_balance_sa_mere = True
            p "J'ai quelque chose à dire."
            narr "Johann se tourna vers moi, intéressé"
            p "Isaac. Il a un pris couteau en salle d'armes."
            $ modif_confiance([isaac], [-10])
            narr "Isaac me foudroya du regard"
            isa "Enfoiré..."
            if inventaire["knife"]["nb"] > 0:
                isa "Mais toi aussi, tu en as pris un, {i}connard{/i}."
                narr "Leonhard partit en salle d'armes et constata que deux couteaux manquaient."
                j "Sérieusement ? Kurt, tu oses dénoncer Isaac alors que tu es toi-même fautif ?"
                narr "Il tourna la tête, méprisant"
                j "Tu es ridicule."
                l "Une balance hypocrite."
                if elus_vote[1]==["alan"]:
                    narr "Emmy me sourit"
                    e "Prépare-toi à mourir !"
                else:
                    narr "Alan était plié de rire"
                    ala "Y a pas plus con que toi, mec."
                    ala "T'es mort, gros !"
                $ vote2 = 8
            else:
                narr "Leonhard leva un sourcil"
                l "C'est vrai, ça, Isaac ?"
                narr "Il alla vérifier en salle d'armes, et revint 30 secondes après."
                l "Il manque effectivement un couteau."
                l "Isaac, montre-le nous."
                narr "Isaac le regarda dans les yeux, la tête baissée."
                isa "Évidemment."
                isa "Vous savez très bien que je suis le plus faible d'entre nous tous. Sans couteau, je ne suis rien."
                narr "Isaac serrait les dents."
                isa "Je me ferais tuer en 2 minutes ici !"
                isa "Avec une bande de traîtres comme Kurt..."
                isa "Je ne peux vraiment plus faire confiance à personne."
                isa "Faites attention à Kurt."
                isa "Il vous trahira aussi."
            if elus_vote[1]==["alan"]:
                $ modif_confiance([isaac, emmy, johann, leonhard], 
                                  [-2, -2, -2, -2, -2])
            else:
                $ modif_confiance([isaac, alan, johann, leonhard], 
                                  [-2, -2, -2, -2, -2])
            $ vote2 = 8
        "Avouer mon crime" if claim_bystander:
            $ renpy.fix_rollback()
            p "Je..."
            if elus_vote[1]==["alan"]:
                $ modif_confiance([isaac, emmy, johann, leonhard], 
                                  [-1  , -1   , -1  , -1    , -1      ])
            else:
                $ modif_confiance([isaac, alan, johann, leonhard], 
                                  [-1  , -1   , -1  , -1    , -1      ])
            p "Je vous ai menti."
            $ claim_bystander = False
            p "Je.. Je suis toujours resté dans la légalité"
            p "La seule chose préjudiciable que j'ai faite..."
            p "... ce sont des blagues racistes sur twitter"
            p "Xénophobes, quelque fois, antisémites et homophobes aussi..."
            p "Mais cela reste de l'humour noir, pour faire rire : je ne pense pas ce que j'écris"
            p "Je me suis déjà fait censurer..."
            p "...ça ne m'étonnerait pas que le Bourreau veuille me faire taire une bonne fois pour toutes..."
            j "Et bien enfin, il t'en aura fallu du temps, pour avouer..."
        "Ne rien dire":
            narr "Je préférais ne rien dire."
    narr "Johann replaça ses lunettes."
    if elus_vote[1] == ["alan"] and persistent.glitched:
        j "Emmy, tu joues toujours l'innocente ou tu tiens à nous dire la vérité ?"
        narr "Emmy le regarda, apeurée"
        e "Non, je le jure, je suis innocente !"
        narr "Elle baissait les yeux vers le sol"
        j "Menteuse."
        j "Je vais voter pour toi, tu le sais ?"
        j "{b}AVOUE{/b}" with sshake
        narr "Emmy se renferma encore plus sur elle-même en pleurant"
        isa "Johann. Ne lui parle plus jamais comme ça. Elle {i}est{/i} l'innocente."
        isa "Je suis un criminel."
        narr "Johann avait les yeux pétillants"
        isa "J'avoue. Je suis homosexuel."
        narr "Johann était intrigué. Ce n'était pas la réponse qu'il attendait."
        isa "Le Bourreau est violent. Regarde comment il a tué Alan."
        isa "Je pense que c'est le genre de personne qui prône la virilité etc..."
        isa "Il veut me punir de mon homosexualité, c'est normal."
        narr "Johann hocha la tête et replaça ses lunettes."
        j "Intéressant."
        j "C'est noble de ta part de l'avouer, mais je ne pense pas que le Bourreau considère ça comme un crime."
        j "Au contraire, ça fait de toi quelqu'un..."
        narr "Johann sourit en penchant la tête. Il avait l'air absorbé dans ses réflexions"
        j "... de {i}fascinant{/i}."
        j "Réellement {i}fascinant{/i}."
        narr "Leonhard était en pleine confusion"
        l "Isaac."
        l "Connais-tu..."
        l "...Klaus ?"
        narr "Isaac pâlit subitement"
        isa "Oui."
        isa "Je... Comment...{nw}"
        l "Oubliez ça."
        narr "Johann regardait tour à tour Leonhard et Isaac. Il s'était passé quelque chose entre Isaac et Leonhard, quelque chose d'important."
    else:
        j "Isaac, tu joues toujours l'innocent ou tu tiens à nous dire la vérité ?"
        narr "Isaac lui lança un regard assassin."
        isa "Tu le sais très bien."
        isa "Il y a des gêneurs plus importants à éliminer, ne te concentre pas sur moi..."
        p "(De qui parle-t-il ?)"
    if claim_bystander:
        l "Et toi, Kurt ?"
        j "Tu vas jouer la comédie encore longtemps ?"
        menu:
            "Avouer":
                p "Je..."
                $ modif_confiance([emmy, isaac, alan, johann, leonhard], 
                                  [-2  , -2   , -2  , -2    , -2      ])
                p "J'ai menti."
                $ claim_bystander = False
                p "Je.. Je suis toujours resté dans la légalité"
                p "La seule chose préjudiciable que j'ai faite..."
                p "... ce sont des blagues racistes sur twitter"
                p "Xénophobes, quelque fois, antisémites et homophobes aussi..."
                p "Mais cela reste de l'humour noir, pour faire rire : je ne pense pas ce que j'écris"
                p "Je me suis déjà fait censurer..."
                p "...ça ne m'étonnerait pas que le Bourreau veuille me faire taire une bonne fois pour toutes..."
            "Persister à se prétendre innocent":
                p "Je te dis la vérité depuis le début, Johann."
                p "Arrête de me prendre la tête."
                p "Je. Suis. Innocent."
                $ annonce_importante(bourreau, _("Menteur.{w=0.5}{nw}"))
                $ modif_confiance([emmy, isaac, alan, johann, leonhard], 
                                  [-3  , -3   , -3  , -3    , -3      ], "Cacher")
                narr "La voix avait résonné dans la salle de vote"
                narr "J'étais devenu pale. Un spectre."
                p "Je..."
                p "..."
                p "Il ment. Ne... ne le croyez pas, il... il cherche à nous diviser."
                j "Peuh. Bien sûr."
                narr "Tout le monde me regardait suspicieusement."
                narr "J'avais merdé."
                $ vote2 = 8
    l "Très bien. Passons au vote."
    jump vote

label suite_vote_2:
    play music "music/Theme_acte_3.ogg" fadein 3.0
    scene fondacte3 with fade
    show moving at defiler
    show text "{font=fonts/Centaur.ttf}{size=32}Acte III : Le Jeu{/font}{/size}" as haut_de_page at smooth_title
    pause 1.5
    $ situation = "en_jeu"
    narr "Les résultats du vote venaient de s'afficher."
    narr "Nous attendions tous une déclaration du Bourreau, qui n'arrivait pas."
    narr "Mais nous savions ce qu'il allait se passer :"
    if vote2 <= 2:
        narr "Alan allait mourir."
        $ modif_resume(318)
        narr "Il ne se laissa pas impressionner, et accueillit la nouvelle froidement."
        if elus_vote[1] == ["emmy"]:
            narr "Il savait comment le Bourreau avait tué Emmy, et était prêt à se défendre..."
        else:
            narr "Il avait tué Emmy. Il ne croyait toujours pas le Bourreau capable d'un meurtre..."
        narr "Et même si le Bourreau arrivait devant lui, il se pensait capable de le vaincre."
        narr "Le Bourreau était l'un d'entre nous."
        narr "Mais peu importe qui c'était..."
        narr "Alan pouvait battre n'importe qui !"
        narr "Il se leva et alla chercher la hache ensanglantée du Bourreau dans la chambre 2"
        narr "Mais ne la trouva pas :"
        narr "Elle se trouvait loin, derrière les barreaux de la salle d'armes..."
        narr "...qui était fermée..."
        narr "Il hurla de rage"
        $ renpy.vibrate(1.0)
        ala "{i}{b}PUTAIN DE MERDE !!!{/b}{/i}" with sshake
        narr "Il réfléchit une minute, puis déclara"
        ala "Toutes les armes sont derrière ces barreaux..."
        ala "Et il peut éventuellement y en avoir derrière la porte de sortie..."
        ala "Mais si je ne peux pas en avoir, le Bourreau non plus, puisque c'est l'un d'entre vous !"
        ala "J'ai qu'à me placer devant la salle de vote, vide toute la nuit, jusqu'à demain, et je verrai tout ce qu'il se passe ici..."
        ala "Je vous verrai entrer et sortir des chambres pour les tours de garde..."
        ala "Puisque le Bourreau est l'un d'entre vous, je le verrai..."
        ala "Il ne pourra {i}pas{/i} aller chercher d'arme en salle d'armes ni {i}dehors{/i}..."
        ala "Il devra m'affronter à mains nues, et perdra."
        narr "Alan sourit"
        ala "Échec et mat !"
    elif vote2 == 3:
        $ modif_resume(319)
        narr "Alan et moi allions devoir nous battre à mort."
        narr "Alan se leva, le regard rivé vers moi"
        ala "Désolé, mon {i}pote{/i}, mais c'est toi ou moi !"
        menu:
            "Parler":
                p "Écoute, pas la peine de t'énerver, on peut s'entendre et trouver une solution."
                ala "Une solution à quoi ? Si on attend, les bombes vont exploser."
                ala "Toi, plus de poumons. Et moi..."
                ala "...plus de cœur."
                ala "Et je compte vivre encore un peu, tu vois ?"
            "Fuir":
                pass
        narr "Il fallait fuir."
        narr "Il était beaucoup trop fort pour moi..."
        narr "Une arme. J'ai besoin d'une arme."
        narr "Direction, la salle d'armes."
        narr "Mais elle était fermée..."
        if inventaire["knife"]["nb"] == 1:
            narr "Heureusement, j'ai ce petit couteau..."
            p "(C'est mieux que rien...)"
        else:
            p "{b}PUTAIN !{/b}" with sshake
            narr "J'aurais du y prendre une arme, plus tôt..."
        narr "Alan était sorti."
        narr "Il me regardait en souriant."
        narr "Je reculai."
        ala "T'es déjà {i}mort{/i}, mec."
        narr "J'étais coincé au fond du couloir..."
        narr "Que faire ?"
        menu:
            "Attaquer (poings)":
                $ renpy.fix_rollback()
                narr "Je sautai vers son visage"
                narr "Alan stoppa ma main"
                narr "Il riposta violemment."
                narr "La douleur était trop intense."
                narr "Sous le choc, je m'effondrai sur le sol."
                narr "Il me rua de coups."
                ala "{b}TU VAS CREVER, OUI ?{/b}"
                narr "Ma tête était sur le point d'exploser."
                narr "Je ne voyais plus rien à travers mes yeux injectés de sang."
                narr "5 coups."
                narr "6 coups."
                narr "7 coups."
                narr "..."
                narr "20 coups."
                narr "..."
                narr "40 ?"
                narr "Je perdis connaissance."
                $ fin = -3
                jump game_over
            "Se défendre":
                $ renpy.fix_rollback()
                narr "Alan fonça sur moi."
                narr "Si c'était un taureau, moi j'étais un pathétique {i}toreador{/i} voué à l'échec."
                narr "Je regardai, fasciné et comme paralysé, la machine de muscle se rapprocher de moi à la vitesse de l'éclair."
                narr "Il me projeta de toute ses forces contre le mur."
                narr "Son corps frappa violemment le mien."
                narr "Je sentis mes côtes se briser sous l'impact."
                narr "La douleur était trop intense."
                narr "Sous le choc, je m'effondrai sur le sol."
                narr "Il me rua de coups."
                ala "{b}TU VAS CREVER, OUI ?{/b}"
                narr "Ma tête était sur le point d'exploser."
                narr "Je ne voyais plus rien à travers mes yeux injectés de sang."
                narr "5 coups."
                narr "6 coups."
                narr "7 coups."
                narr "..."
                narr "20 coups."
                narr "..."
                narr "40 ?"
                narr "Je perdis connaissance."
                $ fin = -3
                jump game_over
            "Attaquer (couteau)" if inventaire["knife"]["nb"]==1:
                $ renpy.fix_rollback()
                narr "Alan fonça sur moi."
                narr "Si c'était un taureau, moi j'étais un pathétique {i}toreador{/i} voué à l'échec."
                narr "Je regardai, fasciné et comme paralysé, la machine de muscle se rapprocher de moi à la vitesse de l'éclair."
                narr "Il allait me cogner de toute ses forces."
                narr "Je tins le couteau fermement entre mes mains."
                narr "Il ne le vit que trop tard."
                narr "Ça n'empêcha pas le choc."
                narr "Son corps frappa violemment le mien."
                narr "Le couteau s'enfonça profondément dans sa chair."
                narr "Je sentis mes côtes se briser sous l'impact."
                narr "La douleur était trop intense."
                narr "Sous le choc, je m'effondrai sur le sol."
                $ sauvegarder("continuer")
                nvl clear
                isa "Kurt, ça va ?"
                narr "Clairement pas. J'étais complètement sonné."
                j "Il a l'air de s'être pris un sacré coup, quand même..."
                l "Alan était une brute."
                j "{i}Était{/i}, oui."
                isa "Heureusement pour lui qu'il avait ce couteau sur lui !"
                j "Ouais."
                j "J'aime moyen."
                j "Il peut tuer n'importe qui, quand il veut, avec {i}ça{/i}."
                narr "Je ne pouvais pas protester, j'étais trop mal."
                j "C'est le genre de truc qu'un {i}Bourreau{/i} a toujours sur lui."
                j "Enfin bref. Mettons-le sur un lit, en attendant."
                $ sauvegarder("continuer")
                nvl clear
                isa "Hey, Kurt ! T'as géré !"
                isa "T'as tué ce {i}connard{/i} d'Alan, trop fort !"
                $ modif_resume(320)
                isa "Je sais que c'est mal de souhaiter la mort de quelqu'un, mais bon..."
                if elus_vote[1] == ["emmy"]:
                    isa "Il m'a fait trop de mal quand j'étais petit..."
                else:
                    isa "Il a {i}tué{/i} Emmy, quand même..."
                $ modif_confiance([isaac], [2])
                isa "Merci beaucoup"
            "Flash (lampe torche)" if inventaire["lampe"]["nb"]==1 and inventaire["battery"]["nb"]>=1 and isaac["confiance"] >= 15:
                $ renpy.fix_rollback()
                narr "Alors qu'il s'approchait de moi, je sortis ma lampe torche, et lui braqua droit dans les yeux."
                narr "La lumière étant trop faible pour avoir un quelconque effet, il se mit à rire."
                ala "T'es pas sérieux ?!"
                ala "Tu crains. À deux minutes de ta mort, tu me sors un truc {i}ridicule{/i}."
                ala "Tu voulais faire quoi ? M'éblouir ?"
                ala "Tu es {i}ridicule{/i}."
                ala "Tu es..."
                narr "Ses yeux se révulsèrent."
                ala "Qu'est ce..."
                narr "Derrière lui, Isaac."
                narr "Avec son couteau de chasse cranté."
                $ isaac["arme"] = False
                narr "Il le retira violemment du dos d'Alan."
                isa "Sale {i}enflure{/i}."
                narr "Alan tomba sur le sol, à l'agonie."
                narr "Un filet de sang rougeâtre coulait de son dos."
                isa "Tu méritais pas mieux, {i}connard{/i}."
                isa "C'est la première chose qui me fait plaisir depuis le début de ce foutu Jeu de merde."
                ala "I... Isaac ?"
                narr "Il planta son couteau entre les omoplates d'Alan."
                isa "Ouais, c'est moi."
                narr "Nouveau coup de couteau."
                isa "Il te fait toujours {i}rire{/i}, le premier de la classe ?"
                narr "Encore un."
                isa "Tu le trouves toujours aussi {i}faible{/i}, le premier de la classe ?"
                narr "Encore."
                $ renpy.vibrate(0.5)
                isa "{b}T'AS TOUJOURS ENVIE DE L'HUMILIER, LE PREMIER DE LA CLASSE ?{/b}" with sshake
                narr "Dernier coup."
                narr "Isaac avait les larmes aux yeux."
                narr "Il se tourna vers moi, en marchant sur ce qu'il restait d'Alan"
                isa "Merci..."
                isa "Merci de l'avoir distrait. J'en pouvais plus de lui."
                p "..."
                p "Tu viens de tuer un être humain, Isaac"
                isa "Pff, Alan, un humain ?"
                $ modif_resume(321)
                narr "Il hocha la tête."
        isa "..."
        isa "Tu... tu crois que le Bourreau fait exprès, de nous monter les uns contre les autres ?"
        isa "Il savait que j'avais beaucoup de rancune envers Alan."
        isa "Il voulait qu'on le tue ?"
        p "..."
        isa "Ce jeu est tellement {i}malsain{/i}..."
    elif vote2 == 4:
        narr "J'allais mourir."
        $ modif_resume(322)
        narr "Putain."
        narr "Mais qu'est-ce que j'ai fait pour mériter ça ?"
        narr "Je regrettais chacun de mes choix..."
        narr "À moins qu'il soit encore possible de changer les choses ?"
    elif vote2 == 5:
        narr "Emmy allait mourir."
        $ modif_resume(323)
        narr "Elle ne se laissa pas impressionner, et accueillit la nouvelle froidement."
        narr "Elle savait comment le Bourreau avait tué Alan, et était prête à se défendre..."
        narr "Et même si le Bourreau arrivait devant elle, elle se disait capable de le vaincre..."
        narr "Pourquoi ? Elle refusait de le dire..."
        narr "Le Bourreau était l'un d'entre nous."
        narr "Mais peu importe qui l'était"
        narr "Emmy pouvait battre n'importe qui..."
        narr "Elle se leva et alla chercher la hache ensanglantée du Bourreau dans la chambre 2"
        narr "Mais ne la trouva pas..."
        narr "Elle se trouvait loin, derrière les barreaux de la salle d'armes..."
        narr "...qui était fermée..."
        narr "Elle sourit"
        e "De mieux en mieux..."
        narr "Elle déclara subitement"
        e "Toutes les armes sont derrière ces barreaux..."
        e "Et il peut éventuellement y en avoir derrière la porte de sortie..."
        e "Mais si je ne peux pas en avoir, le Bourreau non plus, puisque c'est l'un d'entre vous !"
        e "Je n'ai qu'à me placer devant la salle de vote vide toute la nuit, jusqu'à demain, et je verrai tout..."
        e "Je vous verrai entrer et sortir des chambres pour les tours de garde..."
        e "Si le Bourreau est l'un d'entre vous, je le verrai !"
        e "Il ne pourra pas aller chercher d'arme en salle d'armes ni {i}dehors{/i}"
        e "Il devra m'affronter à mains nues et perdra."
        narr "Emmy sourit"
        e "Échec et mat !"
    elif vote2 == 6:
        narr "Emmy et Johann allaient devoir se battre."
        $ modif_resume(324)
        narr "Ils l'avaient bien compris"
        narr "Emmy regarda Johann. Une flamme brillait dans ses yeux"
        narr "Johann était assez vif d'esprit pour comprendre qu'Emmy était une menace"
        narr "Pour la première fois, il prit ses lunettes et les enleva."
        narr "Emmy commença à faire le tour de la table."
        narr "Elle avait les mains sur les seins."
        narr "Johann grommela"
        j "Une arme dans le soutien-gorge ? Pathétique..."
        $ emmy["arme"] = False
        $ modif_bio(emmy, 4, notify=False)
        narr "Emmy en sortit une lame et avança sereinement vers Johann"
        e "Ton heure est venue."
        narr "Un pas."
        narr "..."
        narr "Deux pas."
        narr "..."
        narr "Elle s'approchait dangereusement de Johann"
        narr "Trois pas."
        narr "..."
        narr "A 5 mètres de son but, elle s'arrêta net."
        narr "Une aiguille était plantée dans sa poitrine, au niveau du cœur"
        narr "Johann, le bras élancé, la regardait froidement."
        narr "On aurait dit 2 statues."
        narr "Emmy, les yeux grands ouverts, suffoquait."
        narr "Elle tomba sur ses genoux."
        e "C..."
        narr "Elle tremblait de plus en plus fort"
        e "Comment ?..."
        narr "Du sang sortait de sa bouche"
        e "c'est..."
        narr "Johann la regarda, hautain. Il n'avait plus ses lunettes."
        j "Tu m'as sous-estimé ?"
        e "...injuste..."
        narr "Elle tendit faiblement le doigt..."
        narr "... puis s'effondra."
        narr "Morte."
        narr "Le Jeu avait fait sa 2ème victime..."
        narr "Nous étions tous les 4 choqués par la mort brutale d'Emmy."
        narr "En arrière-plan, on pouvait voir une branche de lunette."
        $ johann["arme"] = False
        narr "Johann y cachait une arme ?"
        $ modif_bio(johann, 3, notify=False)
        $ modif_bio(johann, 4)
        narr "C'est pour cela qu'elle étaient lourdes et qu'il les replaçait tout le temps ?"
        narr "Johann se révélait réellement dangereux..."
        narr "Mais ce qui est fait est fait."
        narr "Le Bourreau voulait une victime..."
        $ modif_resume(325)
        narr "...et Emmy était partie."
    else:
        narr "Emmy et Leonhard allaient devoir se battre."
        $ modif_resume(326)
        narr "Ils l'avaient bien compris"
        narr "Emmy regarda Leonhard. Une flamme brillait dans ses yeux"
        narr "Leonhard avait comprit qu'Emmy était une menace"
        narr "Il mit ses mains dans ses poches, sereinement."
        narr "Emmy commença à faire le tour de la table."
        narr "Elle avait ses mains sur ses seins."
        narr "Leonhard grommela"
        l "Une arme dans le soutien-gorge ? Vulgaire..."
        $ emmy["arme"] = False
        $ modif_bio(emmy, 4, notify=False)
        narr "Emmy en sortit une lame et avança lentement vers Leonhard"
        e "Ton heure est venue."
        narr "Un pas."
        narr "..."
        narr "Deux pas."
        narr "..."
        narr "Elle s'approchait dangereusement du Juge"
        narr "Trois pas."
        narr "..."
        narr "A 5 mètres de son but, elle s'arrêta net."
        narr "Leonhard s'était jeté sur elle."
        narr "Il lui avait planté son stylo-plume dans la gorge."
        narr "On aurait dit 2 statues."
        narr "Emmy, les yeux grands ouverts, suffoquait."
        narr "La carotide tranchée"
        narr "Elle tomba sur ses genoux."
        e "Le..."
        narr "Elle tremblait de plus en plus fort"
        e "Je..."
        narr "Du sang sortait de sa bouche"
        e "veux..."
        narr "Leonhard la regarda, froid."
        e "... vivre..."
        narr "Elle tendit faiblement le doigt..."
        narr "... puis s'effondra."
        narr "Morte."
        narr "Le Jeu avait fait sa 2ème victime..."
        narr "Nous étions tous les 4 choqués par la mort brutale d'Emmy."
        $ modif_bio(leonhard, 2, notify=False)
        $ modif_bio(leonhard, 3)
        narr "Johann avait l'air estomaqué par ce qu'avait fait Leonhard"
        narr "Il ne le pensait pas capable d'une telle violence."
        $ leonhard["arme"] = False
        narr "Mais ce qui est fait est fait."
        narr "Le Bourreau voulait une victime..."
        $ modif_resume(327)
        narr "... et Emmy était partie."
    $ sauvegarder("continuer")
    nvl clear
    
    
    #=========================================================================================================
    narr "16h"
    if vote2 == 4:
        narr "Encore 20 heures à vivre..."
        narr "Ou {i}plus{/i} ?"
        narr "Comment allais-je m'en sortir ?"
    elif vote2 == 3:
        narr "Déjà 4 heures que j'avais tué Alan..."
    elif vote2 == 6:
        narr "Déjà 4h que Emmy a été tuée..."
        narr "Leonhard avait jeté la lame secrète de Johann aux toilettes."
    elif vote2 >= 7:
        narr "Déjà 4h que Emmy a été tuée..."
        narr "Johann avait jeté la lame-stylo de Leonhard aux toilettes."
    narr "L'attente était le pire ennemi ici. C'était insoutenable."
    narr "Il n'y avait rien à faire ici, à part attendre les votes et les sentences du Bourreau..."
    narr "Je me suis dit que j'allais fouiller un peu la salle d'Archives."
    narr "Peut-être que la corde de sortie se trouvait dans les livres."
    narr "Il {i}faut{/i} que je comprenne ce qu'il se passe ici !"
    $ sauvegarder("continuer")
    nvl clear
    narr "Maintenant que j'ai le temps, je vais pouvoir un peu plus fouiller la pièce."
    narr "Dans un coin de la salle, entre deux étagères poussiéreuses, un très vieil ordinateur diffusait une lumière bleutée."
    narr "L'écran était très épuré. Y étaient affichés seulement des lettres capitales formant le mot {b}Index{/b}, ainsi qu'une barre de recherche."
    narr "Il y a un outil de recherche recensant les livres et leurs thèmes... Intéressant !"
    nvl clear
    jump explore_archives
    
label suite_explore_archives:
    $ modif_resume(328)
    narr "19h."
    narr "La soirée se passait dans une ambiance tendue"
    narr "Une nouvelle fois, Isaac avait préparé à manger."
    $ modif_bio(isaac, 5)
    narr "Au menu, des épinard en boîte..."
    narr "Pas de quoi ravir Leonhard, qui faisait la moue"
    narr "Johann détendit l'atmosphère"
    j "Alors comme ça, Monsieur le \"Haut Juge\" n'aime pas les épinards ?"
    narr "Isaac rigola, et ajouta :"
    isa "Ma mère me forçait à en manger quand j'étais petit... depuis j'en raffole !!!"
    isa "Par contre je n'ai jamais aimé le fromage..."
    isa "Comment les gens peuvent manger du {i}lait moisi{/i} ???"
    narr "Ce fut au tour de Johann d'éclater de rire"
    j "Mais tu rigoles, c'est tellement bon ! ..."
    narr "Le \"repas\" se finit sur une note détendue et légère, animé par les remarques d'Isaac et Johann sur leurs goûts et préférences culinaires"
    $ sauvegarder("continuer")
    nvl clear
    narr "22 heures"
    narr "L'organisation de la 2e nuit se préparait"
    narr "Il avait été tiré au sort que je dormirais dans la chambre 3"
    $ sleep_with2 = "seul"
    if vote2 == 4:
        narr "Johann avait choisi de dormir dans la chambre 1 avec Leonhard"
        narr "Isaac proposa de me tenir compagnie, que j'acceptai volontiers"
        $ sleep_with2 = "isaac"
    else:
        if isaac["confiance"] >= johann["confiance"]:
            narr "Johann avait choisi de dormir dans la chambre 1 avec Leonhard"
            narr "Isaac proposa de me tenir compagnie"
            menu:
                "Dormir avec Isaac":
                    isa "À deux, on aura moins peur !"
                    $ sleep_with2 = "isaac"
                    if len(elus_vote[1]) < 2:
                        isa "Surtout après ce qu'il s'est passé hier soir..."
                "Dormir seul":
                    narr "Je décidai de dormir seul"
        else:
            narr "Isaac avait choisi de dormir dans la chambre de Leonhard"
            narr "Johann proposa de me tenir compagnie"
            menu:
                "Dormir avec Johann":
                    j "À deux, on aura moins peur !"
                    $ sleep_with2 = "johann"
                    if len(elus_vote[1]) < 2:
                        j "Surtout après ce qu'il s'est passé hier soir..."
                "Dormir seul":
                    narr "Je décidai de dormir seul"
    if vote2 == 1:
        narr "Alan avait décidé rester éveillé toute la nuit afin de lutter contre le Bourreau"
    elif vote2 == 5:
        narr "Emmy avait décidé rester éveillée toute la nuit afin de lutter contre le Bourreau"
    else:
        narr "L'idée de Johann (organiser des tours de garde) n'ayant pas été efficace la première nuit, nous décidions d'adopter l'idée d'Isaac:"
        narr "Nous bloquâmes les portes avec les lits."
        narr "Même si le Bourreau peut contrôler l'ouverture et la fermeture des portes..."
        narr "...il ne pourra pas ouvrir les portes si elles sont bloquées physiquement !"
    narr "Même si tout avait été fait pour que la nuit se passe bien..."
    $ modif_resume(329)
    narr "... tout le monde était nerveux."
    $ sauvegarder("continuer")
    nvl clear
    $ modif_resume(330)
    narr "1h du matin."
    narr "Je ne dormais toujours pas."
    narr "J'étais beaucoup trop anxieux."
    narr "La {i}Créature{/i} n'était toujours pas revenue."
    narr "Pas pour l'instant."
    if vote2 <= 2 :
        narr "Alan veillait toujours dans le couloir, prêt à en découdre avec le Bourreau."
    elif vote2 == 5:
        narr "Emmy attendait toujours dans le couloir, avec toujours le même air espiègle."
        narr "Qu'avait-elle prévu ?..."
    if sleep_with2 == "isaac":
        p "Oh mon Dieu."
        narr "Isaac avait encore disparu."
        narr "Paniqué, je le cherchai dans toute la chambre."
        narr "J'étais tétanisé à l'idée d'ouvrir la porte, donc je restais dans la chambre"
    elif sleep_with2 == "johann":
        narr "Johann non plus ne dormait pas."
    narr "Qu'allait-il se passer cette nuit ?"
    narr "Je me rendormis vers 1h30 du matin..."
    $ sauvegarder("continuer")
    nvl clear
    if vote2 == 4:
        narr "2h30."
        narr "Je cherchai toujours un moyen de survivre à ce que me préparait le Bourreau..."
        narr "Pourtant, rien à craindre : la porte était toujours bien coincée par le lit..."
        if sleep_with2 == "isaac":
            narr "...et je faisais confiance à Isaac, qui dormait toujours tranquillement de l'autre coté..."
            narr "Lui n'a pas la crainte de se faire tuer pendant son sommeil..."
        else:
            narr "Isaac n'était toujours pas revenu..."
            narr "Fallait-il que je sorte le chercher ?"
            narr "Non. C'était trop dangereux. Et si quelqu'un me voyait ? J'imagine bien Johann veiller en regardant à travers la serrure..."
        narr "2h45."
        narr "Le doute m'envahissait."
        narr "Et si Isaac avait raison, dans la salle d'archive ?"
        narr "Perdu pour perdu, devais-je frustrer le Bourreau, et me suicider ?"
        narr "Ou me battre contre lui, donner tout ce que je peux pour protéger ma vie ?"
        menu:
            "Se suicider":
                jump suicide
            "Attendre et se battre":
                $ renpy.fix_rollback()
                $ ajoute_instabilite(-1)
                narr "Il ne fallait pas que je me laisse abattre."
                narr "Je n'étais pas au fond du trou, du moins pas encore."
                narr "Je pouvais encore m'en sortir."
        $ sauvegarder("continuer")
        nvl clear
    $ assomme = False
    narr "3h30."
    narr "Un bruit contre la porte."
    narr "Dans le couloir, un cliquetis métallique résonnait."
    narr "..."
    narr "La {i}Créature{/i} était là."
    if vote2 == 4:
        narr "Pour moi."
    if sleep_with2 == "isaac":
        narr "Et Isaac n'était toujours pas à coté de moi."
        narr "Étrange... il n'a pas été choisi pour la prochaine exécution, pourtant !"
        narr "La dernière fois, il a été assommé par le Bourreau."
        narr "Qu'est ce qui a pu bien lui arriver, cette fois ?..."
    narr "..."
    narr "J'entendais la Chose gémir et grogner."
    narr "Elle ne traînait pas pour rien ici."
    narr "Qu'est-ce qu'il fallait que je fasse ?"
    menu:
        "Sortir":
            narr "Il fallait que je sorte."
            narr "Il {i}fallait{/i} que je voie ce qui se passe."
            if vote2 == 4:
                narr "Pour me défendre"
            elif sleep_with2 == "isaac":
                narr "Pour protéger Isaac."
            else:
                narr "Pour voir la créature, et percer son mystère."
            narr "J'ouvris la porte."
            narr "Fit deux pas dans le couloir."
            narr "..."
            narr "Rien."
            if vote2 <= 2:
                narr "Alan, qui était censé rester veiller, n'était plus là."
            elif vote2 == 5:
                narr "Emmy, qui était censée rester veiller, n'était plus là."
            p "Je le sens pas, là..."
            narr "Un tintement métallique."
            narr "Le cliquetis venait de là où je ne pouvais pas regarder."
            narr "Vers la salle d'archive."
            narr "Isaac était debout dans le couloir, au tournant."
            narr "Il pouvait voir la Créature, mais pas moi."
            narr "Il regardait droit devant lui, absorbé par ce qu'il voyait."
            if not simple_visit_salle_exec_acte2:
                narr "Les yeux exorbités, il tenait son couteau à deux mains."
            else:
                narr "Les yeux exorbités, il tenait un couteau à deux mains."
            narr "Un bruit de pas résonna, et Isaac recula d'un pas."
            isa "Toi..."
            isa "Tu..."
            isa "C'EST TOI ???"
            narr "La créature gémit"
            isa "Mais bordel, toi aussi..."
            narr "Il baissa son arme."
            isa "Qu'est-ce qu'il t'a fait, bordel..."
            $ renpy.vibrate(0.5)
            isa "{b}QU'EST-CE QU'IL T'A FAIT ????{/b}" with sshake
            isa "..."
            narr "Il avait les larmes aux yeux."
            $ renpy.vibrate(0.5)
            isa "{b}JE VAIS LE DÉTRUIRE !!!{/b}" with sshake
            narr "Isaac se tourna et me vit"
            if vote2 == 4:
                isa "Oh, non..."
                $ renpy.vibrate(0.5)
                isa "{b}KURT, FUIS !!!{/b}" with sshake
                narr "Trop tard."
                narr "La créature surgit."
                narr "Elle sauta par dessus Isaac et fondit sur moi."
                narr "Son métal."
                narr "Sa chair."
                narr "{i}Mon sang{/i}."
                narr "Je sentis ses doigts métalliques déchirer ma peau."
                narr "je trébuchai en essayant de m'enfuir."
                narr "Je ne pouvais rien faire."
                narr "Ses lames me percèrent les yeux, qui giclèrent de sang."
                narr "En trente secondes, elle avait fini."
                narr "Mon esprit commençait à s'enfuir."
                narr "Tout se décomposa autour de moi."
                narr "De la lumière blanche."
                narr "..."
                narr "La fin."
                $ fin = -2
                jump game_over
            else:
                isa "Kurt..."
                narr "Il pencha la tête, en transe."
                narr "Il marchait vers moi."
                isa "Fais-moi confiance, sur ce coup..."
                narr "Il s'approcha de moi et me susurra à l'oreille :"
                isa "Johann n'est qu'un manipulateur égocentrique..."
                isa "Avec mon plan, le Bourreau n'a plus aucune chance !"
                isa "Et je me suis préparé..."
                narr "Il avait un air dément"
                isa "... à l'ultime sacrifice !"
                narr "Il courut à la réserve et s'enferma."
                narr "Une sensation désagréable me parcourut la colonne vertébrale."
                narr "C'est alors que je me rendis compte de mon erreur."
                narr "Mon sang se glaça."
                narr "Un souffle sur mon épaule."
                narr "La créature était dans mon dos."
                nvl clear
                show jumpscareNuit2 at truecenter
                play sound "sounds/jumpscare.ogg" noloop
                pause 0.8
                hide jumpscareNuit2
                show black with dissolve
                pause 3.0
                hide black with dissolve
                $ assomme = True
        "Rester enfermé":
            narr "La créature s'approchait."
            if vote2 != 4:
                narr "Rien ne servait de paniquer, elle ne venait pas pour moi."
                narr "Le Bourreau ne veut pas me tuer."
                narr "..."
                $ renpy.vibrate(0.5)
                if vote2 <= 2:
                    isa "{b}ALAN ????{/b}" with sshake
                elif vote2 == 5:
                    isa "{b}EMMY ????{/b}" with sshake
                else:
                    isa "{b}QU'EST-CE QU'IL T'A FAIT ????{/b}" with sshake
                narr "Isaac était dans le couloir."
                $ renpy.vibrate(0.5)
                isa "{b}C'EST QUOI CE BORDEL ?!?{/b}" with sshake
                $ renpy.vibrate(0.5)
                isa "{b}JE VAIS LE DÉTRUIRE !!!{/b}" with sshake
                narr "Des bruits de pas dans le couloir, suivit d'un crissement métallique."
                narr "Qu'est-ce qu'il se passait ???"
                narr "..."
                narr "Plus aucun bruit..."
                narr "..."
                narr "Vraiment, rien."
                narr "Et c'était plus inquiétant que le bruit métallique de la Créature."
                $ sauvegarder("continuer", montrer=True)
                nvl clear
                narr "Impossible de dormir"
                $ sauvegarder("continuer", montrer=False)
                nvl clear
                narr "Je tombai de fatigue vers 5h"
            else:
                if inventaire["knife"]["nb"] > 0:
                    narr "Je sortis mon couteau de sa poche"
                else:
                    narr "Je n'avais que mes mains pour me défendre contre la créature."
                narr "La chose avançait lentement."
                narr "..."
                narr "J'étais tétanisé."
                narr "..."
                narr "Elle était devant la porte."
                narr "Un mécanisme s'enclencha."
                narr "La porte..."
                narr "... s'ouvrait toute seule."
                p "Isaac ?"
                narr "Il était devant la créature et la regardait."
                narr "Il tenait un couteau dans la main droite."
                narr "Plein de sang."
                if elus_vote[1] == ["alan"]:
                    isa "J'ai tué Johann."
                else:
                    isa "J'ai tué Alan."
                isa "Ca fait deux morts."
                isa "La créature doit te tuer, ce soir, Klaus."
                isa "Je veux dire, {i}Kurt{/i}."
                isa "Mais le Bourreau a dit que 3 morts suffiraient."
                isa "Tu vas vivre, Kurt."
                narr "Il se tourna vers moi."
                narr "Il avait l'air dément."
                narr "Il souleva le couteau dans les air..."
                isa "Bonne chance, pour la suite."
                narr "...et le planta dans sa gorge."
                narr "Il se sacrifiait, pour moi ?"
                isa "Je..."
                narr "Du sang giclait de sa carotide"
                isa "...crois..."
                narr "La créature recula."
                isa "...en toi."
                narr "Isaac s'effondra."
                narr "Sans vie."
                narr "Je m'agenouillai près de son corps..."
                narr "...lorsque la créature me planta une lame dans l'œil.{w=0.5}{nw}"
                nvl clear
                play sound "sounds/jumpscare.ogg" noloop
                show jumpscareNuit2alt at truecenter
                pause 0.8
                hide jumpscareNuit2alt
                show black with dissolve
                pause 3.0
                hide black with dissolve
                $ renpy.vibrate(0.5)
                p "{b}{size=30}AAAAAAAHHHH !!!{/size}{/b}" with sshake
                narr "La créature retira sa lame."
                narr "Le monde se décomposa autour de moi."
                narr "Pourquoi ?"
                narr "Je tombai, et ma tête se fracassa contre celle d'Isaac."
                narr "La créature trancha la tête d'Isaac et me lacéra les côtes."
                p "Je..."
                narr "Tout se vaporisa autour de moi."
                narr "..."
                narr "Une lumière blanche..."
                narr "C'était la fin."
                $ fin = -2
                jump game_over
    $ sauvegarder("continuer", montrer=False)
    nvl clear
    $ isaac["statut"] = "Mort"
    $ emmy["statut"] = "Morte"
    $ alan["statut"] = "Mort"
    $ modif_resume(331)
    j "KURT !!!"
    l "Réveillez-vous !"
    narr "Je me réveillais lentement."
    l "Bien dormi ?"
    narr "Je hochai de la tête."
    p "Pas trop, non."
    if assomme:
        j "T'as une bosse énorme."
        l "La créature qui a assommé Isaac hier..."
        l "Elle a recommencé avec toi ?"
        narr "Johann replaça ses lunettes, pensif."
        j "Mais pourquoi fait-elle {i}ça{/i} ?"
        l "Je ne sais pas. Mais bref."
    else:
        l "Dépêchez-vous de retrouver vos esprits."
        l "Il s'est passé quelque chose d'important."
    l "Cette nuit a été..."
    j "...un {i}carnage{/i}."
    if vote2 <= 2:
        j "Le Bourreau a fait son travail."
        l "Alan est mort ce soir."
        l "Il a été démembré."
        l "Il y a des morceaux de son corps partout, c'est répugnant..."
        l "Et... ce n'est pas tout."
    elif vote2 == 5:
        j "Le Bourreau a fait son travail."
        l "Emmy est morte ce soir."
        l "Elle a été démembrée."
        l "Il y a des morceaux de son corps partout, c'est répugnant..."
        l "Et ce n'est pas tout."
    if assomme:
        l "La créature s'est défoulée sur toi..."
        j "... mais surtout..."
    j "Isaac n'est plus parmi nous."
    p "Comment ça ?"
    j "Il s'est..."
    narr "Il regarda Leonhard en grimaçant"
    j "...suicidé. Enfin on pense qu'il s'est suicidé."
    l "On a retrouvé sa tête accroché à une corde, dans la réserve..."
    if vote2 <= 2:
        l "À côté des membres d'Alan."
        $ modif_resume(332)
    elif vote2 == 5:
        l "À côté des membres d'Emmy."
        $ modif_resume(333)
    j "Il y a du sang partout, dans toute les pièces."
    l "Je n'ai jamais vu ça..."
    j "Mais c'est pas ça, le {i}pire{/i}."
    j "Tu veux que je te montre ?"
    p "Oui, vas-y..."
    j "Viens."
    narr "Johann m'amena à la réserve."
    j "Voilà..."
    narr "C'était de la pure horreur."
    narr "Je vomis immédiatement."
    narr "Leonhard détourna le regard."
    narr "La corde était au centre de la pièce."
    j "On savait qu'Isaac voulait se suicider mais là..."
    narr "Seule la tête et le cou d'Isaac étaient encore en place."
    narr "Sa nuque avait été lacérée par les lames de la Créature."
    j "...pendaison puis décapitation..."
    narr "Il détourna la tête."
    j "Mais c'est pas tout."
    j "Le Bourreau est passé par là."
    j "Il nous a laissé un cadeau..."
    narr "Dans un coin de la pièce, affalé sur un tabouret, il y avait un monstre."
    narr "Un mélange de plusieurs chairs."
    narr "Un puzzle humain."
    narr "La tête d'Emmy, les bras et les jambes d'Isaac, le corps d'Alan cousus entre eux."
    narr "Sur le ventre, le Bourreau avait laissé un mot."
    p "\"Le mal incarné\""
    narr "Il n'y avait aucun mot pour décrire... {i}ça{/i}."
    l "C'est..."
    narr "Johann l'interrompit avant qu'il ne fasse de remarque."
    j "Chut."
    j "C'est la fin."
    j "Il ne doit en rester que trois, selon le Bourreau."
    j "S'il tient sa parole, c'est la fin."
    narr "Il remua la tête."
    j "La fin, {i}bordel{/i}..."
    $ modif_resume(334)
    narr "Leonhard se laissa tomber par terre."
    l "La fin, putain, la fin..."
    $ sauvegarder("continuer")
    nvl clear
    b "La fin ?"
    b "Pas du tout..."
    b "Le {i}Jeu{/i}..."
    b "...ne fait que commencer."
    $ modif_resume(335, notify=False)
    b "C'est maintenant l'heure..."
    $ annonce_importante(bourreau, _("...de la {b}Coalescence{/b}."))
    $ sauvegarder("continuer")
    nvl clear
    hide moving at defiler
    scene black with fade
    $ quick_menu = False
    hide haut_de_page at smooth_title
    show screen menu_background()
    show screen menu_title_coal()
    call screen in_game_menu(acte=acte)
    
    
#================================================#
#================     Acte IV     ===============#
#================================================#
label acte4:
    $ acte = 4
    $ acte_romain = "IV"
    $ persistent.sauvegarde_info[partie_actuelle][0] = 4
    nvl clear
    play music "music/Theme_acte_4.ogg" fadein 3.0
    scene fondacte4 with fade
    show moving at defiler
    $ quick_menu = True
    pause 0.5
    show text "{font=fonts/Centaur.ttf}{size=72}Acte IV\n\nCoalescence{/size}{/font}" as title at truecenter with dissolve
    pause 1.5
    hide title with dissolve
    show text "{font=fonts/Centaur.ttf}{size=32}Acte IV : Coalescence{/size}{/font}" as haut_de_page at smooth_title
    nvl clear
    narr "Un grand bruit sourd retentit dans toute la prison."
    narr "Johann me regarda, hésitant."
    l "La porte a dû s'ouvrir..."
    j "On y va ?"
    j "Je le sens pas..."
    l "Kurt, tu passes en premier ?"
    p "D'accord..."
    narr "Nous avançâmes le long du couloir, en marchant lentement et prudemment"
    narr "Arrivé au bout du couloir, au niveau de la salle de vote, je jetai un coup d'œil vers la porte de sortie."
    narr "Je chuchotai :"
    p "La porte de sortie... elle est ouverte..."
    j "Tu vois autre chose ?"
    narr "J'avançai jusqu'à la porte."
    p "Je ne vois rien, tout est noir..."
    p "Soit il fait nuit, soit..."
    p "...nous sommes encore enfermés."
    p "Leonhard et Johann me rejoignirent."
    narr "Soudain, Leonhard bégaya, avec stupeur."
    l "De... Devant..."
    narr "En face, à travers une porte similaire à celle que nous venions de franchir..."
    narr "...brillait deux grands yeux blancs"
    narr "Des yeux étranges. Presque totalement blancs, sans iris..."
    narr "Pendant que nous retenions tous notre souffle, deux autres paires d'yeux apparurent."
    narr "Personne ne bougeait."
    narr "Après quelques instants d'hésitation, Johann ouvrit la bouche, mais fut interrompu par la voix du Bourreau"
    $ sauvegarder("continuer")
    nvl clear
    b "Ceci est ma dernière intervention."
    narr "Son ton était grave et il prit une pause d'une dizaine de secondes"
    narr "Une ampoule s'alluma faiblement, mais nous aveuglait car nous étions habitués à l'obscurité"
    narr "J'en profitai pour observer Johann et Leonhard"
    narr "Johann avait l'air paniqué. Il touchait ses lunettes toutes les secondes"
    narr "Leonhard était impassible, comme à son habitude"
    b "Trois nouvelles recrues vont venir s'ajouter au Jeu."
    narr "Moi, Johann et Leonhard regardâmes les trois nouvelles silhouettes"
    narr "Devant nous, à 15 mètres, se tenait une femme d'environ 60 ans."
    narr "Elle avait les yeux révulsés et avait tout l'air d'une aveugle"
    narr "Il lui manquait aussi un bras..."
    narr "Derrière elle se tenait un homme et une femme qui se tenaient nerveusement la main"
    narr "Le Bourreau reprit"
    b "Vous avez tous les six survécu à la première partie de mon Jeu."
    $ annonce_importante(bourreau, _("Vous êtes les finalistes."))
    b "Mais comme je l'ai dit, il ne doit en rester que trois"
    if johann["confiance"] >= 16:
        narr "Johann me fit un discret signe de la tête, l'air de dire : \"On fait équipe ?\""
    narr "Les trois autres survivants nous dévisagèrent."
    $ modif_resume(436)
    narr "L'ambiance était clairement hostile."
    b "Nous allons {i}changer les règles{/i}."
    b "Vous n'allez plus voter pour ma victime."
    b "À midi, vous allez dorénavant voter..."
    b "... pour le {b}Bourreau{/b}"
    l "Quoi ?"
    b "Celui qui sera élu comme le nouveau Bourreau devra tuer une autre personne dans les 24h, sinon..."
    $ renpy.vibrate(1.0)
    b "... {i}{b}BOOM !!!{/b}{/i}" with sshake
    b "{i}Vous{/i} allez vous-même faire le sale boulot."
    narr "Alors que tout le monde était silencieux, Johann souriait, les yeux brillants"
    b "Pour assurer le bon déroulement du Jeu.."
    $ renpy.vibrate(1.0)
    j "{b}KLAUS !!!{/b}" with sshake
    narr "Le Bourreau fut surpris un moment par le cri de Johann."
    narr "Les autres furent également étonnés, particulièrement la vieille aveugle qui semblait paniquée"
    narr "Le Bourreau continua comme si de rien n'était"
    b "... si votre bombe a déjà explosé, je vous la remplacerai par une autre !"
    narr "Johann semblait dans un autre monde."
    narr " Alors que tout le monde était inquiété par le Bourreau, Johann riait"
    b "Le Jeu continuera..."
    j "{b}JE TE BATTRAI, BOURREAU !!!{/b}"
    narr "Le Bourreau ne fit pas attention à Johann, cette fois"
    b "... jusqu'à la mort de trois d'entre vous."
    b "Et je vous le rappelle : "
    b "Je suis {i}parmi vous{/i}."
    $ modif_resume(437)
    narr "La voix se tut."
    $ sauvegarder("continuer")
    nvl clear
    narr "Alors que Johann affichait un sourire triomphant, Leonhard s'avançait vers le nouveau groupe"
    l "Puisqu'on va encore être longtemps coincés ici, autant se connaître, non ?..."
    $ persistent.confiance["Rosalind"][2] = True
    $ persistent.confiance["Erwin"][2] = True
    $ persistent.confiance["Lise"][2] = True
    $ rosalind["statut"] = "Vivante"
    $ erwin["statut"] = "Vivant"
    $ lise["statut"] = "Vivante"
    narr "Johann avait l'air motivé. Il se présenta en premier, en avouant ce qui lui a valu d'être pris par le Bourreau"
    narr "Leonhard et moi fîmes de même"
    narr "La soixantenaire pris ensuite la parole"
    r "Je m'appelle Rosalind. J'ai 63 ans, j'étais secrétaire dans ma jeunesse. Je suis aveugle, mais j'entends {i}très{/i} bien."
    r "Je... je ne souhaite pas dire pourquoi je suis ici."
    $ modif_bio(rosalind, 0)
    r "Je te laisse te présenter, Erwin"
    narr "Un homme immense et imposant s'avança."
    erw "Je suis Erwin, et voici ma femme Lise."
    narr "Sa voix était grave, vibrante, avec des sonorités métalliques."
    li "Nous sommes chimistes et nous nous sommes rencontrés sur notre lieu de travail."
    narr "Elle était beaucoup plus enjouée, joyeuse, rayonnante que son mari."
    li "Une négligence de notre part à causé l'empoisonnement d'un petit village d'une dizaine d'habitants..."
    erw "Nous ne nous le sommes jamais pardonné."
    $ modif_bio(erwin, 0, notify=False)
    $ modif_bio(erwin, 1)
    li "Le Bourreau non plus, apparemment..."
    $ modif_bio(lise, 0, notify=False)
    $ modif_bio(lise, 1)
    erw "Comme vous, nous sommes les survivants de notre ancien groupe de six..."
    li "Mais {i}nous nous doutions que vous étiez là{/i}."
    narr "Johann fronça les sourcils, intrigué. Erwin s'expliqua :"
    erw "Pour son dernier Jeu, le Bourreau avait forcément préparé autre chose que {i}d'habitude{/i} !"
    j "Que \"{i}d'habitude{/i}\" ???"
    narr "Erwin regarda sa femme, qui répondit, méfiante."
    li "Vous n'avez jamais participé au Jeu, avant ?"
    narr "Leonhard resta de marbre, mais une lumière traversa ses yeux."
    r "J'ai participé aux {i}trois premiers jeux{/i}..."
    r "... c'est là d'où je tire toutes mes blessures..."
    erw "Moi et Lise avons survécu au dernier Jeu, le 9ème..."
    $ modif_resume(438)
    narr "Sa femme remua la tête. Elle se remémorait les évènements du dernier Jeu."
    erw "... nous ne pensions jamais revenir {i}ici{/i}..."
    erw "Mais {i}vous{/i}, c'est votre premier Jeu ?"
    j "Oui..."
    narr "Les tics de Johann semblaient plus fréquents qu'au premier jour."
    j "Si je comprends bien, tous le monde de votre côté à déjà participé à un Jeu."
    j "De notre côté, personne."
    j "C'est bien ça, Leonhard ? Kurt ?"
    narr "Leonhard et moi hochâmes la tête"
    j "Pour son Dernier Jeu, le Bourreau a voulu organiser quelque chose de spécial"
    j "Nous avons vu son livre {i}HowToPunish{/i} : avant le Jeu n'était qu'un bain de sang général..."
    l "Maintenant aussi..."
    j "Oui, mais cette fois, il impose des {i}Règles{/i}, il sépare tout le monde en 2 groupes..."
    narr "Johann prit une grande inspiration et replaça ses lunettes."
    narr "Comment n'avait-il pas de crampe dans le bras droit ? Il faisait ça tout le temps..."
    $ annonce_importante(johann, _("J'ai une théorie."))
    j "Pour son {i}final{/i}, le Bourreau veut faire se rencontrer les meilleurs survivants..."
    j "... et ceux qui ont commis un crime qui le concerne personnellement."
    narr "Leonhard chuchota"
    l "Les meilleurs tueurs..."
    l "... contre ceux qu'il veut voir souffrir..."
    narr "Johann sourit"
    j "On avance bien..."
    narr "Rosalind n'était pas de son avis"
    r "Dis moi, Monsieur Je-Sais-Tout, comment expliques-tu que je sois dans le camp des {i}\"tueurs\"{/i} ? Je suis aveugle et manchot..."
    narr "Johann répliqua"
    j "C'est bien {i}ça{/i} qui m'intrigue..."
    j "Comment as-tu réussi à survivre à {i}trois Jeux ?{/i}..."
    narr "Rosalind garda le silence."
    $ sauvegarder("continuer")
    nvl clear
    narr "Erwin prit la parole, après quelques instants."
    erw "La Créature."
    j "Pardon ?"
    erw "La Créature. Ce n'est pas le Bourreau. Et nous l'avons enchaînée."
    narr "Johann resta bouche bée quelques instants."
    j "C'est... beaucoup d'informations."
    j "La {i}Créature{/i}..."
    j "Je crois que je vois de quoi tu parles."
    j "Nous aussi avons eu à faire à elle."
    j "Elle a assommé un de nos compagnons, une nuit..."
    erw "Pas uniquement."
    narr "Erwin s'exprimait toujours de façon sèche, mais précise et efficace."
    erw "C'est {i}elle{/i} qui était chargée de tuer ceux qui avaient été élus."
    narr "Johann était admiratif."
    narr "Erwin arrivait à faire avancer concrètement les choses."
    narr "Je sentais qu'il allait être important pour la suite."
    j "C'est donc ça qu'Isaac avait vu..."
    erw "Mais nous l'avons emprisonnée, enchaînée."
    erw "Elle ne fera plus rien de mal."
    $ modif_resume(439)
    narr "Leonhard pensa à haute voix"
    l "C'est pour ça qu'il doit changer les Règles..."
    erw "Elle est dans notre salle de torture."
    p "La salle de torture ?"
    li "Oui ! J'ai fait un schéma, si vous voulez."
    narr "Lise nous expliqua rapidement à quoi ressemblait leur coté de la prison."
    narr "Même si je ne l'avais pas entièrement visitée, je savais maintenant qu'elle ressemblait à peu près à ça :"
    $ renpy.notify("Carte mise à jour.")
    nvl clear
    show carte_complete_penchee with dissolve
    $ quick_menu = False
    $ carte_complete = True
    $ renpy.pause(2.0, hard=True)
    n ""
    hide carte_complete_penchee with dissolve
    $ quick_menu = True
    nvl clear
label fincartetotale:
    nvl clear
    narr "Il restait environ une demi-heure avant le début du vote."
    narr "J'avais juste le temps de parler à deux personnes."
    $ nb_parle = 0
    $ talk_to = ""
    $ talk_to2 = ""
label talk_acte4:
    narr "À qui pouvais-je bien parler ?"
    $ nb_parle += 1
    menu:
        "Johann" if not talk_to == "johann":
            if nb_parle == 1:
                $ talk_to = "johann"
            else:
                $ talk_to2 = "johann"
            narr "J'allais vers Johann"
            j "Bon."
            j "On fait quoi, avec {i}eux{/i} ?"
            j "Ils m'ont l'air vraiment dangereux..."
            j "D'après ce que Lise a dit, au lieu d'une salle d'archive, il y a un laboratoire."
            j "Mais Erwin et Lise sont chimistes... C'est une trop grande coïncidence..."
            p "Leonhard est Juge, c'est tout aussi louche !"
            if johann["confiance"] > 17:
                j "Tu n'as pas tort. Et j'ai de moins en moins confiance en Leonhard..."
            else:
                j "Tu n'as pas tort. Mais j'ai confiance en Leonhard."
            j "Enfin bref."
            j "Tu as du me prendre pour un fou, tout à l'heure."
            j "Tu sais, quand j'ai crié {i}Klaus{/i}."
            j "Mon enquête avance bien, et je crois avoir trouvé quelque chose d'important."
            $ choses_apprises_johann = 0
            $ tab_j_4 = [False, False, False]
            label johann_acte_4:
                if choses_apprises_johann == 0:
                    j "Et toi, tu as appris des choses sur Klaus par exemple ?"
                else:
                    j "Autre chose ?"
                menu:
                    "Créature" if not screamer_nuit1 and not tab_j_4[0]:
                        $ tab_j_4[0] = True
                        $ choses_apprises_johann += 1
                        p "La première nuit..."
                        p "La {i}créature{/i} dont parlait Isaac. Je l'ai entendue."
                        p "Elle avait l'air de {i}chercher{/i} Klaus..."
                        j "Intéressant..."
                        jump johann_acte_4
                    "Archives" if info_klaus_archives and not tab_j_4[1]:
                        $ tab_j_4[1] = True
                        $ choses_apprises_johann += 1
                        p "J'ai fouillé dans les archives..."
                        narr "Johann m'interrompit."
                        j "Et Klaus est soit un champion d'apnée, soit un inventeur de génie, c'est ça ?"
                        narr "Il sourit"
                        j "Je suis fier de toi, mais je suis arrivé au même point infructueux..."
                        jump johann_acte_4
                    "Mot d'Isaac" if not tab_j_4[2]:
                        $ tab_j_4[2] = True
                        $ choses_apprises_johann += 1
                        p "Le mot qu'a trouvé Isaac quand il était enfermé..."
                        p "Il est écrit : {i}Klaus hates you{/i}..."
                        j "Oh, bravo, tu sais lire le morse !"
                        j "J'avais trouvé ça aussi."
                        jump johann_acte_4
                    "Non" if choses_apprises_johann == 0:
                        $ modif_confiance([johann], [-2])
                        j "Dommage... Je t'ai surestimé, Kurt."
                    "C'est tout" if choses_apprises_johann != 0:
                        $ modif_confiance([johann], [choses_apprises_johann])
                        j "Tu as fait du bon travail, Kurt, bravo !"
                j "Personnellement, je pense que Klaus et le Bourreau ne font qu'un."
                j "Cela ne reste qu'une théorie, mais..."
                narr "Son regard brillait à travers ses lunettes"
                j "...j'ai rarement tort !"
                j "Je ne préfère pas m'avancer, mais je crois que je connais aussi l'identité du Bourreau."
                j "C'est bientôt la fin du {i}Jeu{/i}, Kurt."
        "Leonhard" if not talk_to == "leonhard":
            if nb_parle == 1:
                $ talk_to = "leonhard"
            else:
                $ talk_to2 = "leonhard"
            narr "Leonhard était debout, en train d'observer les murs de la Grande Salle où nous étions."
            narr "Il fut surpris par mon arrivée"
            l "Oh, Kurt. Vous allez bien ?"
            p "Oui, relativement. Et vous ? Vous regardiez quoi ?"
            l "Rien de précis. En fait, j'avais le regard dans le vide, je réfléchissais."
            narr "Il anticipa ma question sans sourciller."
            l "À quoi je réfléchissais ? C'est plutôt évident."
            l "Pourquoi le Bourreau change-t-il ses règles en milieu de Jeu ?"
            l "Pourquoi Johann a-t-il hurlé \"Klaus\" ?"
            l "Mais surtout..."
            l "Pourquoi ça a déstabilisé le Bourreau, alors que la vidéo était censée être pré-enregistrée ?"
            l "Johann voulait tester cela, j'imagine."
            l "Il est vraiment au dessus de nous."
            l "Trop, peut-être."
            l "..."
            l "En tout cas, le Bourreau est en train de perdre pied."
            l "Il ne pourra pas resister à l'intelligence de Johann."
            l "À moins qu'il avait tout prévu d'avance ?"
            l "Ou encore, que le Bourreau et Johann ..."
            l "..."
            l "Non, impossible."
            p "Impossible que les deux soient de mèche ? Ou soient la même personne ?"
            p "Comment pouvez-vous en être sûr ?"
            narr "Leonhard grimaça"
            l "Il y a des choses qu'il vaut mieux te cacher, désolé..."
        "Rosalind" if not talk_to == "rosalind":
            if nb_parle == 1:
                $ talk_to = "rosalind"
            else:
                $ talk_to2 = "rosalind"
            p "Excusez-moi, Rosalind, j'ai quelques questions à vous poser"
            narr "Rosalind recula vivement"
            r "Cette voix..."
            r "Oh mon Dieu, cette voix..."
            r "J'aurais voulu ne plus jamais l'entendre !"
            p "Pourquoi dites-vous ça ?"
            r "Tu... tu ne me reconnais pas ?"
            p "Et bien, non !"
            r "Ah..."
            r "Pardonne-moi. En fait, tu as la même voix que mon neveu."
            r "Ça a fait ressurgir de mauvais souvenirs dans ma mémoire."
            p "(Ah ? Elle est en froid avec son neveu ?)"
            menu:
                "S'excuser":
                    p "Je suis désolé !"
                    $ modif_confiance([rosalind], [1])
                    r "Mais non voyons, ce n'est pas de ta faute..."
                "Poser des questions sur son neveu":
                    r "Hmph."
                    $ modif_confiance([rosalind], [-1])
                    r "Je n'ai {i}vraiment{/i} pas envie d'en parler ici. Surtout en ce moment."
            r "Kurt, c'est bien ça ?"
            r "Tu as la même voix, et presque le même nom que mon neveu."
            r "C'est assez surprenant. Et ce n'est pas vraiment agréable."
            r "Car si j'ai participé à trois jeux, et que je suis encore là, après avoir été rendue aveugle, et après avoir perdu un bras..."
            $ modif_bio(rosalind, 2)
            r "C'est à cause de {i}lui{/i}."
        "Erwin" if not talk_to == "erwin":
            if nb_parle == 1:
                $ talk_to = "erwin"
            else:
                $ talk_to2 = "erwin"
            narr "Je m'approchai d'Erwin"
            narr "Erwin était froid, glacial."
            narr "Autant Leonhard était stoïque, et n'exprimait pas ses sentiments, autant Erwin était froid dans le sens agressif du terme"
            erw "Que me veux-tu ?"
            erw "Nous avons un Bourreau à démasquer et à vaincre."
            narr "Ses phrases étaient courtes et sèches."
            erw "Je n'ai pas le temps à accorder aux imbéciles..."
            erw "J'espère que tu n'es pas aussi {i}stupide{/i} que le chinois."
            narr "Intrigué, je le coupai."
            p "Le \"chinois\" ? C'est qui ?"
            erw "Hmph."
            erw "Tu crois que je vais te donner des informations gratuitement ?"
            erw "Dis-moi ce qu'il s'est passé de votre coté d'abord."
            menu:
                "Coopérer":
                    p "Très bien..."
                    narr "Je l'informai donc des évènements de l'aile gauche de la prison."
                    narr "Il hocha la tête avec intérêt."
                    erw "Merci beaucoup. Tu es loin d'être stupide. Excuse-moi."
                    $ modif_confiance([erwin], [2])
                    erw "Maintenant, à mon tour."
                    erw "Nous aussi, nous n'avons eu que deux votes à faire."
                    erw "Le chinois, ou japonais, je m'en fous, s'est suicidé."
                    erw "Comme votre \"Isaac\"."
                    erw "Je vais reprendre depuis le début."
                    erw "Nous étions six. Moi, ma femme, Rosalind, le chinois, une mère Stéphanie et sa fille Sophie."
                    erw "La mère a été désignée au premier tour."
                    erw "Durant la nuit, elle s'est faite {i}détruire{/i} par le Bourreau."
                    erw "Enfin, pas par le Bourreau, mais par sa {i}créature{/i}."
                    erw "Sa fille, désespérée, a voté contre elle-même au second tour."
                    erw "Elle voulait se battre contre la {i}créature{/i} et venger sa mère."
                    erw "Elle a {i}failli{/i} réussir."
                    erw "Un bel oxymore."
                    erw "Bref. Elle l'a affrontée."
                    erw "Elle a réussi à assommer la créature, et à l'enchaîner dans la salle de torture..."
                    erw "...mais est morte de ses blessures ce matin."
                    erw "Paix à son âme."
                    erw "Mais revenons au chinois."
                    erw "Grâce à Sophie, nous avons pu observer la {i}créature{/i} qui devait nous tuer."
                    erw "La {i}créature{/i}..."
                    erw "...elle est {i}traumatisante{/i}."
                    erw "C'est une femme."
                    erw "Ça devait être une belle femme, avant."
                    erw "Avant..."
                    erw "... que le Bourreau la charcute."
                    erw "..."
                    erw "Elle est en lambeaux."
                    erw "Ce mélange de chair et d'acier... Ca me dégoûte."
                    erw "Le bourreau lui a coupé les cheveux, et lui a inséré des {i}lames{/i} à la place des mains."
                    erw "Il lui a tailladé les poignets."
                    erw "Presque comme ferait un suicidaire."
                    erw "\"Presque\", car il l'a fait dans le {i}mauvais{/i} sens."
                    erw "Pour la faire saigner sans réellement en mourir."
                    erw "Pour la faire {i}souffrir{/i}."
                    erw "Mais le {i}pire{/i}..."
                    erw "C'est sa mâchoire."
                    erw "Le Bourreau l'a détruite."
                    erw "..."
                    erw "Sa mâchoire pend, {i}{b}fracassée{/b}{/i}, au bout de sa bouche."
                    erw "C'est infâme à voir..."
                    p "..."
                    erw "En découvrant la {i}créature{/i}..."
                    narr "Erwin, le mur de glace, avait l'air ému, ou plutôt dégoûté de ce qu'il décrivait."
                    erw "Le chinois..."
                    erw "..."
                    erw "Il a reconnu sa petite amie."
                    erw "..."
                    erw "Il ne l'a pas supporté."
                    $ modif_bio(ukichiro, 1, notify=False)
                "Refuser":
                    erw "Comme tu voudras, Kurt."
                    $ modif_confiance([erwin], [-2])
                    erw "Nous serons donc ennemis, à défaut de se pouvoir faire confiance."
                    erw "Il est essentiel de se faire confiance ici."
                    erw "Mais puisque seuls trois peuvent s'en sortir..."
                    erw "Il faut faire des choix."
        "Lise" if not talk_to == "lise":
            if nb_parle == 1:
                $ talk_to = "lise"
            else:
                $ talk_to2 = "lise"
            narr "Lise était en train de parler toute seule."
            narr "Elle avait l'air plus extravertie que son mari."
            narr "Ce qui n'était vraiment pas très dur, cela dit."
            narr "Comment des personnes avec des tempéraments aussi différents peuvent-elles s'entendre ?"
            narr "Les opposés s'attirent, j'imagine."
            narr "Elle me fit un grand sourire, un peu inquiétant, à mon arrivée."
            li "Tu es Kurt, je me trompe ?"
            if talk_to == "erwin":
                li "Je suis désolé si mon mari t'a fait peur tout à l'heure."
                li "Il s'est vraiment passé des horreurs..."
            else:
                li "Tu es là pour apprendre ce qu'il s'est passé de notre côté, j'imagine."
                li "Désolée, je ne suis pas assez forte pour t'expliquer tout ce qu'il s'est passé..."
                li "Va voir mon mari, quand tu auras le temps !"
            li "Quand je repense à..."
            narr "Elle grelotta."
            li "Non, je préfère ne pas y penser."
            li "Parlons d'autre choses, veux-tu ? Le passé, est le passé."
            li "Tu as des questions à me poser ? Autre chose que le jeu, s'il te plaît."
            menu:
                "Vie professionnelle":
                    p "Tu es chimiste, c'est bien ce que tu nous as dit tout à l'heure ?"
                    p "Tu peux faire quoi avec ce qu'il y a dans le laboratoire ?"
                    li "..."
                    li "Tout."
                    p "Tout ?"
                    li "À peu près tout ce que je veux, mais en quantité limitée."
                    li "Il y a beaucoup de ressources dans ce laboratoire."
                    li "C'est d'ailleurs surprenant !"
                "Vie privée":
                    p "Où en êtes-vous, avec Erwin ?"
                    li "On s'est mariés il y a deux ans, en France !"
                    p "Oh, {i}félicitations{/i} !{#en français dans le texte}"
                    narr "Lise rougit"
                    li "Merci !"
    $ sauvegarder("continuer")
    nvl clear
    if nb_parle == 1:
        narr "Le temps s'écoulait."
        narr "Je pouvais encore parler à une personne avant le début du vote."
        jump talk_acte4
    narr "Une sonnerie retentit"
    narr "Il était midi."
    narr "L'heure du vote."
    narr "Tandis que Leonhard, Johann et moi étions allés voter à la salle de vote de l'aile gauche, sur nos tablettes respectives, Erwin, Lise et Rosalind votèrent depuis leur salle de vote."
    $ sauvegarder("continuer")
    nvl clear
    jump vote
    
label suite_vote_3:
    play music "music/Theme_acte_4.ogg" fadein 3.0
    $ quick_menu = True
    $ is_voting = False
    $ situation = "en_jeu"
    nvl clear
    scene fondacte4 with fade
    show moving at defiler
    show text "{font=fonts/Centaur.ttf}{size=32}Acte IV : Coalescence{/font}{/size}" as haut_de_page at smooth_title
    pause 0.5
    hide title with dissolve
    narr "Johann me regarda, interloqué"
    j "Je... je n'ai pas voté pour Rosalind."
    narr "A l'issue de ce vote surprenant, tout le monde se rejoignît dans la grande salle"
    narr "Tout le monde semblait étonné, voire suspicieux"
    narr "Nous nous sommes mis en ligne devant Rosalind"
    r "Bon..."
    r "Sachant que je n'ai moi-même pas voté pour moi, le vote a manifestement été truqué..."
    $  modif_resume(440)
    r "Le vrai Bourreau a voulu me désigner comme son successeur  ?"
    r "Soit. Je suis le Bourreau pour une journée."
    r "Mais je ne vais tuer personne."
    r "De toute manière, comment le pourrais-je ? Je suis aveugle et handicapée..."
    r "Je vais simplement attendre l'explosion de la bombe dans ma jambe."
    r "Ne vous inquiétez pas pour moi, je connais bien la douleur, après 3 jeux..."
    r "Je survivrai."
    narr "Leonhard fronça les sourcils"
    l "Je ne vous fais pas confiance."
    l "Le vote a manifestement été trafiqué..."
    l "Vous semblez dire que c'est en votre défaveur, mais cela pourrait être le contraire..."
    l "Vous êtes en position de force pour le moment !"
    l "Vous avez l'approbation, et peut-être même le soutien du vrai Bourreau !"
    l "Et je ne vois pas en quoi le fait que vous soyez handicapée change la donne."
    l "Au contraire, personne ne peut soupçonner une handicapée..."
    l "Et qui nous dit que vous êtes vraiment aveugle ? Personne ne vous connaît..."
    j "Rosalind, nous avons {i}besoin{/i} de vous faire confiance."
    j "Nous {i}devons{/i} savoir comment se sont passés vos derniers jeux, et {i}pourquoi{/i} vous avez été choisie par le Bourreau..."
    j "Dites la vérité, sinon..."
    j "... on vous enferme jusqu'à demain midi"
    narr "Rosalind resta muette quelques instants"
    $ annonce_importante(rosalind, _("Je préfère encore que l'on m'enferme."))
    $ sauvegarder("continuer")
    nvl clear
    narr "14h."
    narr "Rosalind avait été enfermée dans la chambre 2 de l'aile gauche de la prison"
    narr "Tout le monde explorait les nouvelles pièces accessibles"
    $ sauvegarder("continuer")
    nvl clear
    $ book = "begin"
    $ rosalind_silent = False
    $ une_entrevue_johann = True
    $ une_entrevue_lise = True
    $ une_entrevue_leonhard = True
    $ une_entrevue_creature = True
    $ une_entrevue_rosalind = True
    $ first_time_see_arcade = True
    $ piles_supplementaires = False
    $ chambre_acte4_seen_once = False
    jump map2_acte4
    
label finCarteActe4:
    hide carte_complete with dissolve
    hide go_left with dissolve
    hide go_right with dissolve
    hide quit_map with dissolve
    narr "19h."
    narr "Nous étions tous réunis en cercle dans la grande salle centrale."
    narr "D'un coté, Johann et Leonhard. De l'autre, Erwin et Lise."
    narr "Je m'étais mis au milieu, en position de médiateur."
    narr "Isaac n'était plus là pour nous préparer à manger..."
    narr "Johann avait donc ramené de la soupe, froide comme d'habitude"
    j "Bon appétit. Du moins, si vous en avez encore."
    narr "Erwin resta de marbre."
    li "Merci, Johann, à toi aussi !"
    p "Bon ap' !"
    narr "Leonhard souffla, las."
    l "La même chose..."
    narr "Le repas se passait silencieusement."

    narr "Lise rompit le silence"
    li "Comment s'organise-t-on, cette nuit ?"
    narr "Johann répondit immédiatement :"
    j "Étant donné que la Créature est enchaînée et que Rosalind est enfermée, on ne craint rien, non ?"
    l "Le Bourreau rôde toujours ! Et on ne sait pas ce qui peut arriver."
    l "Je ne prendrais pas de risques inutiles. Je dormirai enfermé dans la chambre 3, si vous me cherchez."
    li "D'accord !"
    narr "Elle regarda son mari"
    li "Nous dormirons dans la chambre 5, notre favorite !"
    $ sleep_with3 = "Alone"
    if johann["confiance"] >= 18:
        j "Kurt, ça te dirait qu'on dorme dans la même chambre ?"
        menu:
            "Accepter":
                p "Pas de problème !"
                $ sleep_with3 = "Johann"
                narr "Johann sourit en replaçant ses lunettes."
                $ modif_confiance([johann], [1])
                j "Cool ! Chambre 1 ?"
                p "Pourquoi pas !"
            "Refuser":
                p "Non, désolé, mais je me sens plus en sécurité seul..."
                narr "Johann fit la moue"
                $ modif_confiance([johann], [-1])
                j "Pas grave..."
                j "Je vais dormir seul chambre 1, moi !"
                p "Ce sera chambre 4 pour moi."
    else:
        j "Je vais dormir seul chambre 1, moi !"
        p "Ce sera chambre 4 pour moi."
    $ sauvegarder("continuer")
    nvl clear
    narr "Une heure plus tard, nous allâmes nous coucher"
    narr "La créature et Rosalind étant neutralisées, rien ne devrait se passer, cette nuit !"
    narr "Malgré les morts d'Isaac, Emmy et Alan, je sentais que mon sommeil allait être plus léger cette nuit."
    narr "C'était un peu égoïste, mais je me sentais en sécurité."
    narr "Tant pis pour les autres."
    $ sauvegarder("continuer")
    nvl clear
    narr "Jour 4, 3h"
    narr "Quelque chose me réveilla."
    narr "Je sentais que quelque chose n'allait pas, malgré le silence"
    #TODO insérer son et diminuer musique
    $ renpy.pause(0.5)
    narr "On frappait à ma porte."
    narr "Doucement. Comme si il ou elle ne voulait pas faire de bruit."
    #Rosalind s'est échappée (grâce à la créature mais on ne sait pas comment/pourquoi à ce stade)
    $ spy_rosalind = True
    $ is_kurt_ko = False

label nuit_rosalind:
    menu:
        "Regarder à travers la serrure" if spy_rosalind:
            $ spy_rosalind = False
            narr "Intrigué, je regardai à travers la serrure."
            narr "Une robe à pois. Style vieille."
            narr "Rosalind ?"
            narr "Mais qu'est-ce qu'elle fait là ?"
            jump nuit_rosalind
        "Ouvrir la porte":
            narr "J'ouvris la porte."
            r "Klaus ?"
            narr "Rosalind n'avait pas l'air dans un état normal."
            r "C'est bien toi ?"
            menu:
                "Je suis Kurt, pas Klaus.":
                    p "Je suis Kurt. Pas Klaus."
                    r "Menteur. Je te reconnais bien."
                    $ nie = True
                "Ne rien dire":
                    $ nie = False
            r "Je dois te parler."
            r "Tu... as eu un comportement inacceptable."
            label fight_rosalind:
                r "Je dois..."
                r "{b}TE PUNIR{/b}" with sshake
                narr "Rosalind colla sa main contre moi."
                p "Oh merde..."
                narr "Un taser."
                r "Tu vas rentrer sagement avec moi."
                narr "Elle appuya sur le bouton."
                narr "Je me contractai, anticipant la douleur."
                if piles_supplementaires: #on a piqué la batterie, il n'y en a plus pour rosalind
                    narr "Mais rien ne se passa."
                    narr "Son taser ne marchait pas."
                    r "Comment ça, plus de piles ?"
                    narr "Il fallait réagir vite."
                    narr "Et j'étais seul."
                    menu:
                        "Riposter (couteau)" if inventaire["knife"]["nb"] == 1:
                            narr "Je sortis mon couteau, et lui enfonçai dans le ventre."
                            narr "Rosalind suffoquait."
                            r "Klaus..."
                            if nie:
                                p "JE SUIS PAS KLAUS, PUTAIN !!!"
                            else:
                                p "Meurs."
                            narr "Rosalind cracha du sang..."
                            narr "...et s'effondra."
                            $ rosalind["statut"] = "Morte"
                        "Riposter (poison)" if inventaire["poison"]["nb"] == 1:
                            narr "Je sortis la fiole, pris Rosalind à la gorge, et lui versa le liquide dans la bouche."
                            $ update_inventory(inventaire["poison"], -1)
                            $ inventaire["poison"]["used"] = True
                            narr "Rosalind suffoquait, essayait de cracher le poison."
                            r "Klaus..."
                            if nie:
                                p "JE SUIS PAS KLAUS, PUTAIN !!!"
                            else:
                                p "Meurs."
                            narr "Rosalind commença à se raidir..."
                            narr "...et s'effondra."
                            $ rosalind["statut"] = "Morte"
                        "Riposter (poing)":
                            narr "Je frappai Rosalind de toutes mes forces."
                            narr "Rosalind s'effondra immédiatement."
                            narr "J'y étais peut-être allé un peu fort."
                            narr "Elle était inconsciente, à terre."
                            narr "Un filet de sang s'écoulait de son crâne..."
                        "Appeler à l'aide":
                            narr "J'avais besoin d'aide. C'était urgent."
                            narr "J'hurlai à m'en vriller les cordes vocales."
                            p "{b}À l'aide !!!{/b}" with sshake
                else:
                    narr "La douleur était inimaginable."
                    narr "Je tombai à terre, à peine capable de penser."
                    narr "Rosalind avait l'air choquée par ses propres actes."
                    narr "J'étais seul. Il me fallait de l'aide."
                    narr "J'hurlai à m'en vriller les cordes vocales."
                    p "{b}AAAAAAAHHHH !!!{/b}" with sshake
                    narr "Je n'arrivais pas à articuler {i}\"À l'aide\"{/i}..."
                    $ is_kurt_ko = True
        "Parler":
            p "Qui est là ?"
            r "Klaus ?"
            r "C'est bien toi ?"
            menu:
                "Je suis Kurt, pas Klaus.":
                    p "Je suis Kurt. Pas Klaus."
                    r "Menteur. Je te reconnais bien."
                "Ne rien dire":
                    pass
            r "Je dois te parler."
            r "Tu... as eu un comportement inacceptable."
            r "Laisse-moi rentrer. Je dois te faire rentrer dans le droit chemin."
            r "C'est pour ton bien que je fais ça."
            r "Tu me connais bien. Je veux juste que tout aille bien."
            menu:
                "Comment es-tu sortie ? (méfiance)":
                    r "Comment je suis sortie ?"
                    r "Aucune porte ne peut me retenir."
                    r "Vous êtes tous bien naïfs."
                    r "J'ai survécu à trois jeux..."
                    r "...je survivrai à celui-ci."
                    narr "Son intonation disait le contraire."
                    narr "Essayait-elle de se convaincre elle-même ?"
                    narr "Avec une bombe en elle, un bras et deux yeux en moins..."
                    r "Je vais nous libérer, Klaus."
                    r "Le Bourreau..."
                    narr "Rosalind hésita un long moment. Elle semblait réfléchir."
                    narr "Elle n'était clairement pas dans son état normal."
                    $ annonce_importante(rosalind, _("J'ai tué Leonhard."))
                    p "{b}{i}QUOI ?{/i}{/b}"
                    p "Non, impossible. Tu n'as pas fait {i}ça{/i} ???"
                    narr "Alors que je commençais à m'énerver, j'entendis des bruits de pas"
                "Ouvrir la porte (confiance)":
                    narr "Lentement, j'ouvris la porte à Rosalind."
                    narr "Elle avait le visage pâle, le corps faible."
                    narr "Au bord de la mort."
                    r "Merci."
                    jump fight_rosalind
        "Ne rien faire":
            r "Klaus ?"
            r "Tu es là ?"
            r "Je sais que tu es là."
            r "Arrête de faire semblant."
            r "Je suis aveugle, mais j'entends {i}tout{/i}."
            r "Ton cœur bat fort dans ta poitrine."
            r "Oh ! Erwin..."
            r "Qu'est-ce qu'il...{w=0.2}{nw}"
    nvl clear
    if is_kurt_ko:
        narr "Je reprenais lentement mes esprits."
    narr "Erwin était là, silencieux."
    erw "Rosalind."
    narr "Il parlait entre ses dents, avec sa voix métallique."
    erw "Qu'est ce que tu as fait, {i}{b}putain{/b}{/i} ?"
    narr "Il se tourna vers moi."
    erw "Leonhard est K.O."
    erw "Rosalind l'a planté. Mais il n'est pas mort."

    if rosalind["statut"] == "Vivante":
        r "Il m'a enfermé en prison. C'est lui mon ennemi."
        narr "Erwin pencha la tête."
        erw "Ça va, Rosalind ?"
        erw "T'as pas l'air bien."
        erw "Physiquement, c'est évident."
        erw "Mais mentalement ?"
        erw "Tu en as marre, hein ?"
        erw "Tu n'as pas survécu aux trois jeux auxquels tu as participé."
        $ annonce_importante(erwin, _("Tu es {i}brisée{/i}."))
        narr "Erwin la prit par la gorge..."
        narr "...et la plaqua contre un mur." with sshake #TODO bruitages
        li "Non ! Erwin..."
        narr "Lise arrivait en courant."
        li "Calme-toi !"
        narr "Du sang coula dans les cheveux de Rosalind."
        erw "Elle le mérite. T'as vu ce qu'elle a fait à Leonhard ?"
        erw "Il faut qu'on parle sérieusement..."
        $ sauvegarder("continuer")
        nvl clear
        narr "Lise était partie réveiller Johann pour l'informer de la situation."
        li "Elle ne va pas bien."
        erw "Elle a déjà un bon pied dans la tombe."
        narr "Johann hocha la tête."
        r "Il a raison."
        r "Je vais bientôt mourir."
        narr "Son expression était saccadée. Elle avait du mal à parler."
        r "Alors écoutez-moi."
        r "C'est important..."
        p "Qu'y a-t-il ?"
        narr "Elle toussa bruyamment."
        r "Klaus."
        l "Parle, parle, {i}parle{/i} bordel !"
        r "Klaus est la raison de notre présence ici."
        $ jours = (persistent.jeu_actuel - 1)*5 +4
        r "C'est à cause de lui qu'on s'entre-tue depuis maintenant [jours] jours." #si bug : compter le nombre réel de jours.
        narr "Elle avait capté notre attention."
        r "C'est mon neveu."
        narr "Leonhard regarda Rosalind, interloqué."
        l "Vraiment ? Mais pourquoi ça ?"
        l "Je veux dire, quel est le rapport entre lui et..."
        l "... et {i}ça{/i} ?"
        narr "Rosalind soupira. Elle tremblait de plus en plus."
        r "Le point commun entre nous tous..."
        r "C'est qu'on est responsable de sa mort."
        $ annonce_importante(rosalind, _("On a tué Klaus."))
        narr "Rosalind transpirait à grosses gouttes."
        r "Et le Bourreau veut le venger."
        j "Mais pourquoi ? C'est quoi le lien entre Klaus et le Bourreau ?"
        narr "Il était visiblement déstabilisé. Ses tics reprenaient."
        r "Je ne sais pas... Et il ne le sait peut-être pas lui-même."
        $ annonce_importante(rosalind, _("Il en à {i}rien à foutre{/i} de la Justice."))
        r "Klaus est un prétexte."
        r "Il veut juste {i}se défouler{/i}..."
        narr "Ses yeux se révulsèrent, puis revinrent à la normale quelques secondes."
        r "Je..."
        narr "Elle était de plus en plus faible."
        r "Le Rossignol..."
        r "Ukichiro..."
        r "..."
        r "Klaus..."
        narr "Elle s'évanouit."
        $ sauvegarder("continuer")
        nvl clear
        narr "Lise se précipita sur elle."
        li "Elle... elle n'est {i}pas{/i} morte."
        narr "Elle n'avait pas l'air de croire en ce qu'elle affirmait."
        li "Je vais surveiller son état."
        l "Faites attention, Lise."
        l "Je vous rappelle que c'est officiellement le Bourreau."
        narr "Lise lui jeta un regard noir"
        li "Elle ne ferait pas de mal à une mouche."
        li "Ça se voit, non ? Elle est au bord du décès !!!"
        narr "Leonhard haussa les épaules."
        l "N'en soit pas si sûre."
        narr "Leonhard n'avait pas l'air très inquiété."
        narr "À vrai dire, que Rosalind meure, ou qu'elle tue Lise, ça ne lui était égal..."
        narr "Il ne doit en rester que trois."
        narr "Il n'était pas contre un décès de plus..."
        narr "Johann, lui, était plus préoccupé."
        narr "Rosalind avait encore des choses à dire..."
        narr "On l'enferma de nouveau dans sa chambre, Lise à ses côtés."
    $ sauvegarder("continuer")
    nvl clear
    hide moving at defiler
    scene black with fade
    $ quick_menu = False
    hide haut_de_page at smooth_title
    show screen menu_background()
    show screen menu_title_coal()
    call screen in_game_menu(acte=acte)
#================================================#
#================     Acte V     ================#
#================================================#
label acte5:
    $ acte = 5
    $ acte_romain = "V"
    $ persistent.sauvegarde_info[partie_actuelle][0] = 5
    nvl clear
    stop music
    scene fondacte5 with fade
    show moving at defiler
    $ quick_menu = True
    pause 0.5
    show text "{font=fonts/Centaur.ttf}{size=72}Acte V\n\nKlaus{/font}{/size}" as title at truecenter with dissolve
    pause 1.5
    hide title with dissolve
    show text "{font=fonts/Centaur.ttf}{size=32}Acte V : Klaus{/font}{/size}" as haut_de_page at smooth_title
    nvl clear
    narr "Midi."
    if rosalind["statut"] == "Vivante":
        narr "Le Bourreau allait punir Rosalind."
        narr "Au final, elle n'avait tué personne cette nuit, malgré sa tentative sur Leonhard."
        narr "Sa bombe allait normalement exploser..."
        narr "Immobile, elle se mit à chanter, en transe"
        r "{i}He wakes up early today{/i}"
        r "{i}Throws on a mask that will alter his face{/i}"
        r "{i}Nobody knows his real name{/i}"
        r "{i}But now he just uses one he saw on a grave{/i}{nw}"
        play sound "sounds/explosion.ogg" noloop
        n "{w=1.0}{nw}" with sshake
        $ sauvegarder("continuer")
        nvl clear
        play music "music/Theme_acte_5.ogg" fadein 3.0
        narr "La bombe placée dans sa jambe avait explosé."
        narr "Rosalind était à terre."
        narr "Défigurée de douleur."
        narr "Elle perdait beaucoup trop de sang."
        narr "Elle n'était pas encore inconsciente, et était toujours en plein délire"
        narr "Toutefois, elle semblait articuler quelque chose de cohérent"
        r "{i}...e...ui...olé...lau...{/i}" #je suis désolée Klaus
        narr "Elle n'allait pas survivre à l'explosion."
        r "{i}...e..ne...lai...a...te...tu..{/i}" #je ne voulais pas te tuer
        narr "Puis ses muscles se relâchèrent."
        li "Je vais chercher de quoi la soigner !"
        narr "Lise partit en quête de bandages, de morphine et autres antalgiques"
        l "Tiens bon, Rosalind. Tu dois vivre encore un peu ! Juste le temps du vote..."
        narr "On emmena Rosalind au Laboratoire, sur la table d'opération."
        $ sauvegarder("continuer")
        nvl clear
        narr "Une demi-heure plus tard."
        narr "Lise vint nous voir."
        li "Il est bientôt 13 heures. Il va falloir aller voter."
        l "Et Rosalind ?"
        $ annonce_importante(lise,  _("Elle... elle est morte..."))
        $ rosalind["statut"] = "Morte"
        narr "Erwin arriva derrière sa femme et l'enlaça."
        erw "Nous n'avons rien pu faire pour la sauver, nous somme désolés..."
        narr "Il pris sa tête dans ses mains de géant."
        erw "Nous ne sommes que chimistes, pas médecins... Tu n'as pas à t'en faire, Lise."
        erw "C'est la faute du Bourreau..."
        narr "On la laissa pleurer dans les bras de son mari."
    else:
        narr "Le Bourreau n'avait rien besoin de faire, Rosalind étant morte..."
        l "Bon, Kurt. Il va falloir que tu nous confirmes ce qu'il s'est passé ce soir."
        p "Mais je l'ai déjà dit au moins trois fois ! C'est un interrogatoire ?"
        j "Il a raison de demander. Je préfère être sûr, n'ayant rien vu..."
        erw "Rosalind a voulu tuer Leonhard, puis a commencé à t'attaquer, donc tu l'as tuée, c'est ça ?"
        p "Oui, oui ! C'était de la légitime défense !"
        narr "Johann grogna."
        j "Elle aurait pu être utile..."
    $ sauvegarder("continuer")
    nvl clear
    narr "Il était midi passées de cinquante cinq minutes"
    $ modif_resume(541)
    narr "Johann alla chercher Lise et Erwin afin de participer au vote avant l'échéance, 13h."
    narr "Une fois revenus, Leonhard prit la parole"
    l "Dépêchons."
    l "Nous allons procéder au quatrième vote."
    l "Avez-vous quelque chose à annoncer ?"
    menu:
        "Ne rien dire":
            narr "Je préférais ne rien dire."
            l "Kurt, non ?"
        "Je sais qui est le Bourreau":
            p "Je sais qui est le Bourreau."
            narr "Lise me regarda, surprise."
            narr "C'était bien la seule étonnée."
            erw "Impressionnant."
            narr "Il avait un sourire ironique."
            j "Ça fait longtemps que je sais qui c'est."
        "Message de fraternité":
            p "On est plus que cinq. Mais c'est pas pour autant qu'il faut se séparer et baisser les bras."
            p "Je ne crois pas que le Bourreau soit parmi nous tous."
            p "S'il a changé les règles, c'est pour une raison."
            p "Le Bourreau est à bout ! On peut le vaincre, ensemble !"
            narr "Erwin n'avait pas l'air convaincu."
            erw "Tu cherches à gagner notre confiance ?"
            $ modif_confiance([erwin, lise, johann, leonhard],
                              [-1   , 0   , -1    , -1      ])
            j "Pathétique."
            l "Évidemment, il est impossible de défaire le Bourreau."
            l "Deux personnes vont encore mourir, on est sur le point de désigner le prochain tueur..."
            j "...et tu fais un discours de solidarité ?"
            erw "Pour éviter de t'attirer des ennuis, tu fais ami-ami avec tout le monde ?"
            erw "Ça marchera pas avec moi."
            narr "Après un instant de silence, Johann reprit la parole."
    j "Personne d'autre ne veut ajouter quelque chose ?"
    narr "Leonhard fixa Erwin."
    l "Même pas vous, Monsieur {i}Rossignol{/i} ?"
    narr "Erwin était estomaqué."
    erw "Je..."
    l "Ne faites pas l'innocent."
    l "Je sais tout."
    narr "Leonhard nous regarda tour à tour."
    l "Je peux pas tout vous expliquer tout de suite : il est bientôt 13 heures."
    l "Il faut aller voter {i}maintenant{/i} !"
    l "Dépêchez-vous."
    l "Que le vote commence !"
    $ sauvegarder("continuer")
    nvl clear
    jump vote
    # =============== VOTE 4 =================================================================================
label suite_vote_4:
    $ quick_menu = True
    $ is_voting = False
    $ situation = "en_jeu"
    play music "music/Theme_acte_5.ogg" fadeout 3.0 fadein 3.0
    nvl clear
    show text "{font=fonts/Centaur.ttf}{size=32}Acte V : Klaus{/font}{/size}" as haut_de_page at smooth_title
    narr "Tout le monde se réunit en silence dans la Grande Salle."
    if len(elus_vote[4]) == 1:
        l "Bon, un Bourreau a bien été élu, cette fois ci."
        l "Mais au juste, ça veut dire quoi ?"
        l "C'est quoi, ce statut de Bourreau ?"
        l "Est-on est aidé par le vrai Bourreau ?"
        l "Ou est-ce juste une tâche à remplir ?"
        j "Je ne pense pas que le vrai bourreau aide le nouveau."
        j "À mon avis, il veut juste observer ce que quelqu'un ferait à sa place."
        erw "Mais si il est effectivement parmi nous, il se met en danger, non ?"
        j "Je ne pense pas."
        j "Il a du tout prévoir..."
        narr "Il hésita."
        l "À moins ?"
        j "...à moins qu'il ait prévu de mourir pour son dernier Jeu."
    else:
        l "Personne n'a été élu. Il y a égalité."
        li "Encore des meurtres... Je n'en peux plus."
    narr "Le silence était glaçant."
    narr "L'attention de l'assemblée se recentra sur les résultats du vote."
    if elus_vote[4] == ["kurt"]:
        narr "J'avais été élu..."
        #Kurt : peut tuer n'importe qui sauf Lise protégée par son mari
        $ annonce_importante(kurt, _("Je suis... le Bourreau ?"))
        $ modif_confiance([erwin, lise, johann, leonhard], 
                          [-2   , -2  , -2    , -2      ])
        narr "Un sentiment étrange m'envahit."
        narr "Tellement de puissance..."
        narr "Mais autant d'appréhension."
        if inventaire["knife"]["nb"] == 1 or inventaire["poison"]["nb"] == 1:
            narr "Au moins, j'étais armé."
        else:
            narr "Je n'étais même pas armé..."
        narr "Tous me dévisagèrent."
        erw "Parle. Qui vas tu tuer ?"
        $ temporiser = True
        label choix_important:
            narr "Qui allais-je tuer ?"
            menu:
                "Johann":
                    $ kill = "Johann"
                "Leonhard":
                    $ kill = "Leonhard"
                "Erwin":
                    $ kill = "Erwin"
                "Lise":
                    $ kill = "Lise"
                "Me suicider":
                    $ kill = "myself"
                "Temporiser" if temporiser:
                    p "Je préfère attendre un peu..."
                    $ modif_confiance([erwin, leonhard], [-1, 1])
                    p "C'est une décision beaucoup trop importante pour être prise rapidement."
                    erw "Pff."
                    erw "C'est sur que faire ça la nuit, c'est plus pratique, hein ?"
                    erw "Assume tes choix. Choisis."
                    narr "Dos au mur, je n'avais plus vraiment le choix."
                    $ temporiser = False
                    jump choix_important
            after_choice "Êtes-vous sûr de votre choix ?"
            menu:
                "Oui":
                    pass
                "Non":
                    nvl clear
                    jump choix_important
            if kill == "myself":
                narr "Aucun ne méritait de mourir."
                narr "Isaac. Je vais faire comme Isaac."
                narr "Je vais me suicider."
                jump suicide
            elif kill == "Johann":
                p "Johann."
                p "Je vais tuer Johann."
                narr "Johann écarquilla les yeux, et couru vers l'aile gauche."
                $ gibier = "johann"
                jump machination
            elif kill == "Leonhard":
                narr "Leonhard."
                jump fight_leonhard
            elif kill == "Erwin":
                $ vise_lise = False
                p "Erwin."
                narr "Erwin sourit cyniquement."
                erw "Moi ?"
                p "Toi."
                narr "Je ricanai."
                p "Ouais, toi. De toute façon, c'est pas à moi de mourir."
                jump fight_erwin
            elif kill == "Lise":
                $ vise_lise = True
                p "Lise."
                erw "{b}PARDON ???{/b}" with sshake
                narr "Sa voix métallique résonna longtemps dans la salle."
                erw "Tu veux tuer LISE ???"
                narr "Une veine devenait de plus en plus apparente sur son front."
                narr "C'était une bête enragée."
                menu:
                    "Céder et calmer le jeu":
                        p "Calme-toi, je blaguais."
                        p "Lise est la plus innocente, j'allais quand même pas faire ça..."
                        p "(Je le ferai cette nuit)"
                        narr "Erwin ne semblait pas convaincu."
                        narr "Il s'approchait dangereusement de moi."
                        narr "Je ne reculai pas, et le regardai dans les yeux."
                        narr "Il me frappa directement au visage."
                        narr "Je volai, et m'effondrai au sol."
                        erw "{b}TU CROIS QUE JE VAIS ME CALMER ???{/b}" with sshake
                    "Tenir tête":
                        narr "Mais il fallait lui tenir tête. Céder, c'était perdre toute crédibilité."
                        narr "Surtout face à lui."
                        narr "Mais j'allais tuer sa femme..."
                        narr "Putain, j'aurais du y penser avant..."
                narr "Je le fixai agressivement."
                p "Tu veux y passer avant elle, hein ?"
                erw "C'est moi ou rien. Pas elle."
                jump fight_erwin


    elif elus_vote[4] == ["erwin"]:
        narr "Sans surprise, Erwin prit la parole."
        $ annonce_importante(erwin, _("Je suis le nouveau Bourreau."))
        erw "Je doit tuer avant demain midi."
        narr "Sa voix métallique le rendait inhumain."
        erw "Mais je vais le faire maintenant."
        narr "Lise n'eut aucune réaction face aux mots tranchants de son mari."
        narr "Elle ne semblait pas surprise."
        if erwin["confiance"] >= 12:
            erw "Vous m'avez appelé Rossignol, tout à l'heure, Leonhard."
            erw "Vous savez tout ?"
            erw "Dommage."
            erw "Je vais devoir vous tuer."
            narr "Il regarda longuement le juge, qui détourna le regard."
            l "Johann. Je vais peut-être mourir."
            l "Je veux que tu saches qu...{w=0.5}{nw}"
            narr "Erwin le frappa en pleine tête."
            erw "{b}Ta gueule.{/b}"
            narr "Leonhard s'écroula immédiatement sur le sol."
            l "{b}AaAaaaaah{/b}"
            l "{b}PU-TAAAAIN{/b}"
            l "Erwin est le Bourreau."
            li "Hein ?"
            l "Ne fais pas l'innocente, Lise, tu l'es aussi."
            erw "N'importe quoi."
            erw "Voilà pourquoi c'est toi que j'ai décidé de tuer."
            erw "Tu es peut-être juge, tu as peut-être été mis sur l'affaire, mais tu ne vaux rien."
            erw "À lancer de fausses pistes, tu nous embrouilles."
            erw "C'est d'ailleurs ton but."
            narr "Erwin lui assena un deuxième coup."
            erw "Car c'est toi, le Bourreau."
            narr "La tête de Leonhard frappa le sol."
            narr "Violemment."
            narr "Un filet de sang coulait entre ses cheveux."
            narr "Erwin s'agenouilla à coté de Leonhard à demi conscient."
            erw "Bois ça."
            narr "Il lui versa un liquide jaunâtre dans la bouche."
            j "{size=-5}Non, putain...{/size}"
            narr "Leonhard se crispa soudainement, puis se détendit."
            narr "Mort."
            $ leonhard["statut"] = "Mort"
            $ erwin["arme"] = False
            $ fin_vote_4 = "leonhard_mort"
            jump suite_fight_vote4
        else:
            erw "Kurt, comment vas-tu ?"
            narr "Il... m'avait choisi ?"
            erw "Je suis désolé de te l'annoncer, mais tu es celui en qui j'ai le moins confiance."
            narr "Il regarda Leonhard"
            erw "J'ai hésité avec ce fouineur, qui a l'air d'être au courant de mes activités."
            erw "Mais bon, il a une bonne raison de rester en vie."
            erw "Toi, tu es inutile."
            erw "Tu fais quoi de ta vie ? Tu fais quoi, ici ?"
            erw "Rien."
            jump fight_erwin


    elif elus_vote[4] == ["johann"]:
        j "Bon."
        $ annonce_importante(johann, _("Je suis le nouveau Bourreau ?"))
        j "Très bien."
        j "Parfait, même."
        j "Car j'ai déjà choisi ma victime."
        if johann["confiance"] >=18:
            j "Kurt."
            narr "Ces mots résonnaient dans ma tête."
            narr "Moi ?"
            narr "Johann voulait me tuer, {i}moi{/i} ?"
            p "Putain, Johann, tu fais quoi ?"
            j "Je {i}sais{/i} que ni Erwin, ni Lise ne sont les Bourreaux."
            j "À cause de ce qu'il y a écrit sur le mur de la Grande Salle."
            j "Et puisque le Bourreau est encore vivant, il ne reste que toi, Kurt."
            narr "Il avança d'un pas."
            narr "Et replaça ses lunettes."
            narr "De la main gauche ?"
            narr "Quelque chose n'allait pas."
            if inventaire["knife"]["nb"] > 0:
                narr "J'avais un couteau."
                narr "Mais bon."
            else:
                narr "Il fallait que je gagne du temps."
            narr "Je décidai de fuir dans la salle d'armes."
            narr "Un bon lieu de combat, où je pourrai avoir toutes les armes que je souhaite."
            narr "Prions pour qu'elle soit ouverte."
            narr "Je courus aussi vite que je pouvais le faire."
            narr "Johann était parti à ma poursuite."
            jump machination
        else:
            jump erwin_vs_johann
        
    elif elus_vote[4] == ["erwin", "johann"]:
        #fight johann erwin
        #TODO CHOIX (?) : AIDER L'UN OU L'AUTRE
        narr "Johann et Erwin..."
        narr "Allaient devoir s'entretuer."
        jump erwin_vs_johann

        
    elif elus_vote[4] == ["erwin", "kurt"]:
        erw "Quel dommage, Kurt."
        narr "Je vais devoir affronter... ce monstre ?"
        if erwin["confiance"] >= 13:
            erw "J'avais confiance en toi."
            erw "Je voulais tuer Leonhard, mais ce sera au prochain tour, j'imagine."
        jump fight_erwin

    elif elus_vote[4] == ["johann", "kurt"]:
        #TODO vote 4 johann VS kurt
        n ""
        jump machination
    else:
        narr "Erreur #142857. Ceci ne fait pas partie du jeu, veuillez en informer le développeur à amethystsstudio@gmail.com"

label erwin_vs_johann:
    j "Dommage, Erwin. Je te respectais beaucoup."
    erw "Ce combat ne peut que mal finir pour notre groupe."
    erw "Mais avec un peu de chance, je peux tuer le Bourreau..."
    narr "Il mit ses mains dans ses poches."
    j "Choisis bien, Erwin."
    narr "Johann avança d'un pas."
    narr "Et replaça ses lunettes."
    narr "De la main gauche ?"
    narr "Quelque chose n'allait pas."
    erw "{i}{b}Johann.{/b}{/i}" with bigshaq
    narr "Johann s'enfuit vers l'aile gauche."
    narr "Erwin à sa poursuite."
    nvl clear
    narr "Pour ne pas entendre les bruits de lutte, Leonhard avait fermé la porte de la Grande Salle."
    narr "Le silence qui assourdissait la Grande Salle laissait entendre des gémissements et des râles au loin."
    narr "Leonhard essayait de rassurer Lise."
    li "J'ai pas besoin de ton soutien, juge. Je suis forte."
    li "Mon mari en a traversé des plus dures."
    li "Il va surv...{w=0.2}{nw}"
    unk "{b}PUTAIN DE MERDE !!!{/b}"
    narr "Quoi ? Que s'était-il passé ?"
    narr "Je bousculai Leonhard."
    narr "Me précipitai sur les lieux du crime."
    narr "Les sanitaires."
    narr "Le carrelage était rouge de sang."
    narr "Des morceaux de chair jonchaient le sol vermillon."
    narr "Erwin était debout, de dos, au milieu de la pièce."
    narr "Devant lui, une main découpée."
    narr "Il se pencha pour la prendre..."
    narr "...la jeta dans les toilettes..."
    narr "...et tira la chasse."
    narr "Il fit une pause puis se retourna vers nous."
    $ annonce_importante(erwin, _("De Johann, il ne reste {b}rien{/b}."))
    $ johann["statut"] = "Mort ?"
    $ fin_vote_4 = "johann_mort_cachée"
    $ sauvegarder("continuer")
    nvl clear
    l "Putain, Johann..."
    narr "C'était la première fois que Leonhard perdait autant patience."
    l "{i}{b}Johann !!!{/b}{/i}" with sshake
    narr "Il s'approcha d'Erwin, les yeux haineux."
    l "Tu vas le regretter..."
    narr "Erwin le regarda du haut de son mètre 93."
    erw "Je vais vous sauver tous."
    narr "Il s'approcha de Leonhard, déterminé."
    erw "Pour moi, mourir n'est pas une option. Pour toi, une fatalité."
    jump suite_fight_vote4
    #=============================================================================
    # Contient : fight leonhard, machination k/j, fight erwin, (machination k/er)

label fight_leonhard:
    narr "Celui qui méritait de mourir, c'était Leonhard."
    p "Juge."
    p "Ma sentence est tombée. Sur vous."
    l "Très bien."
    if leonhard["arme"]:
        l "Sachez que je suis prêt. Venez."
        narr "Il était beaucoup trop confiant. Du bluff ?"
        if inventaire["knife"] == 1:
            narr "Le couteau était toujours là, dans ma poche."
        elif inventaire["poison"] == 1:
            narr "La fiole de poison était toujours là, dans ma poche."
        else:
            narr "J'étais désarmé. Ca n'allait pas être facile..."
    narr "Une goutte de sueur perla discrètement sur son front."
    narr "Les autres nous regardaient, inquiets."
    narr "J'avais toujours l'air confiant et déterminé."
    narr "Il fallait que je ne laisse aucune trace d'hésitation devant les autres..."
    narr "...et surtout devant Leonhard."
    narr "En réalité, je n'étais pas du tout prêt."
    narr "Leonhard était impressionnant de sang-froid."
    narr "Immobile. Imposant. Il attendait que je l'attaque."
    $ sauvegarder("continuer")
    nvl clear
    narr "Que devais-je faire ?"
    $ passif = True
    $ countdown_time = 15.0
    menu:
        "L'attaquer aux poings":
            $ passif = False
            jump fight_leonhard_rate
        "L'attaquer au couteau" if inventaire["knife"]["nb"] == 1:
            jump fight_leonhard_couteau
        "Jeter le poison au visage" if (inventaire["poison"]["nb"]  == 1) and not inventaire["poison"]["used"]:
            jump fight_leonhard_poison
        "Lui faire boire le poison (s'aider d'Erwin)." if erwin["confiance"] >= 18 and (inventaire["poison"]["nb"]  == 1) and not inventaire["poison"]["used"]:
            jump fight_leonhard_poison_erwin
        "Rester immobile" ("default"):
            jump fight_leonhard_rate

label fight_leonhard_couteau:
    if leonhard["arme"]:
        narr "Il fallait que j'engage le combat."
        narr "Je glissai ma main dans ma poche."
        narr "Le couteau était bien là."
        narr "Le métal était froid."
        narr "Je m'avançai vers Leonhard."
        narr "Sans prévenir il se jeta sur moi, sa main dans sa poche de chemise."
        narr "Un stylo à plume ?"
        narr "Il visa ma gorge."
        narr "Je le bloquai."
        narr "Ripostai avec un coup de couteau."
        narr "Dans le bras."
        narr "Je sentis sa chair se déchirer sous mon poing."
        narr "Je faiblis et failli échapper le couteau."
        narr "Blesser quelqu'un au couteau est quelque chose d'horrible."
        #animation de frappe
        $ renpy.vibrate(0.5)
        narr "Une douleur perçante me traversa l'abdomen." with sshake
        narr "Leonhard retira son stylo ensanglanté de mon ventre."
        narr "L'adrénaline me montait au cerveau."
        narr "Elle noyait mon esprit dans une mare de haine."
        narr "Déchaîné, je frappai Leonhard de toute mes forces."
        narr "Déstabilisé, il trébucha."
        narr "Je le poussai et le planquai contre le mur."
        l "Attends, J..."
        narr "Je lui plantai mon couteau dans le cou."
        p "Adieu, Juge."
        l "Jo..."
        l "{i}Johann.{/i}"
        narr "Il s'effondra sur le sol."
        narr "Mort."
    else:
        l "Vous allez faire quoi ?"
        l "Je n'ai même plus d'arme..."
        l "Vous allez me tuer, maintenant ?"
        narr "Il avait l'air inoffensif, agressé."
        narr "Les autres me regardèrent, agacés."
        narr "Je ne pouvais pas tuer quelqu'un qui avait ce comportement."
        narr "Il... le faisait exprès ?"
        narr "Il avait toujours eu l'air stoïque, et maintenant veut faire de la peine aux autres ???"
        narr "Et puis, il venait de me tutoyer."
        narr "À quoi jouait-il ?"
        erw "Ne te laisse pas attendrir."
        narr "Il donna un coup de pied puissant à Leonhard, qui tomba lourdement sur le sol."
        narr "Alors que je m'approchai de Leonhard, il fuit, courut maladroitement vers la salle d'armes."
        narr "Je le rattrapais facilement."
        p "Juge, toi ?"
        p "Tu as essayé de tous nous influencer tout à l'heure, quand tu as parlé d'un certain \"Rossignol\""
        p "Je ne sais pas si tu es le Bourreau ou pas. Je ne sais pas si tu es un complice."
        p "Mais tu n'es certainement pas de mon côté."
        narr "Je lui plantai mon couteau dans la gorge."
        $ modif_confiance([erwin, lise, johann], [-2, -2, -2], False)
    $ fin_vote_4 = "leonhard_mort"
    $ leonhard["statut"] = "Mort"
    jump suite_fight_vote4

label fight_leonhard_poison:
    narr "J'étais seul contre lui."
    narr "Si je pouvais le tuer, c'était parce que j'avais volé cette fiole de poison du Laboratoire."
    narr "Mais il n'acceptera jamais de boire le poison, même en bluffant."
    narr "Il voulait se battre maintenant."
    narr "Il fallait que je la lui lance dessus, en espérant que l'effet soit assez foudroyant pour le tuer -ou le rendre vulnérable."
    narr "C'était risqué."
    narr "Je devais le prendre par surprise"
    p "Leonhard, pourquoi Erwin t'a...{nw}"
    narr "Je la lui lançai à la tête avant de finir ma phrase." with sshake
    narr "Elle explosa sur son visage sidéré."
    narr "Le poison commençait déjà à faire effet."
    l "{i}Kurt ???{/i}"
    narr "Fou de rage, les yeux injectés de sang."
    narr "Il se rua sur moi."
    if leonhard["arme"]:
        narr "Son poing dans la poche."
        narr "Il en sortit un stylo plume."
        narr "Quoi ?"
        narr "Avant que je réagisse, il me l'avait planté dans le cou."
        narr "Je ne comprenais plus rien."
        narr "Un jet de sang pourpre sortait de mon corps."
        narr "Une lumière blanche..."
        $ sauvegarder("continuer")
        $ fin = -6
        jump game_over
    else:
        narr "Son poing serré fusa vers mon visage."
        narr "Je le bloquai, mais il avait plus de force que moi."
        narr "Je reculai sous le choc."
        narr "Il était recouvert de poison, et n'avait pas l'air d'apprécier."
        narr "Le temps jouait en ma faveur."
        narr "Je fonçai de toutes mes forces vers lui."
        narr "Surpris que je contre-attaque, il n'eut pas le temps d'esquiver."
        narr "Il tomba lourdement sur le sol."
        l "EeuARrhg"
        narr "Il n'arrivait plus à parler."
        narr "La paralysie le défigurait déjà."
        narr "Il ne pouvait même plus se lever."
        narr "Il n'était bientôt plus de ce monde."
        $ fin_vote_4 = "leonhard_mort"
        $ leonhard["statut"] = "Mort"
        jump suite_fight_vote4

label fight_leonhard_poison_erwin:
    narr "Comment était-il possible de l'empoisonner ?"
    narr "Jeter le poison sur lui était trop risqué."
    narr "Le temps que le poison fasse effet... Il allait me tuer."
    narr "Il fallait lui faire boire le poison."
    narr "Heureusement, Erwin n'avait pas apprécié la remarque de Leonhard tout à l'heure."
    narr "Il allait m'être d'une grande aide."
    p "Erwin."
    erw "Oui ?"
    p "Tu te souviens de ce qu'a dit Leonhard ?"
    narr "Je sortis la fiole de poison."
    narr "Erwin ricana."
    erw "Je vois. Désolé Leonhard."
    narr "Il s'approcha de Leonhard et le souleva dans les airs par la gorge."
    erw "À toi de jouer, Kurt."
    narr "Je m'approchai, et lui enfonça la toxine dans l'œsophage."
    narr "Erwin regardait malicieusement Leonhard, qui essayait de se débattre en vain."
    erw "Désolé, Juge, mais tu en savais un peu trop..."
    narr "Leonhard avait des convulsions."
    narr "Il ne contrôlait plus ses muscles."
    narr "En quelques minutes, il se vida de toutes ses forces, suspendu au bras d'Erwin."
    narr "Mort."
    $ fin_vote_4 = "leonhard_mort"
    $ leonhard["statut"] = "Mort"
    jump suite_fight_vote4

label fight_leonhard_rate:
    narr "Seul contre lui."
    if passif:
        l "Tu as peur de moi ?"
        narr "Il sourit."
        l "Quel faible..."
        narr "Une flamme dansait dans son regard."
    else:
        narr "Je m'armai de courage"
        narr "J'avançai d'un pas décidé vers lui."
        narr "J'étais en position de combat."
        narr "Je me jetai vers lui, le poing levé."
        narr "Leonhard esquiva."
    narr "Il se rua sur moi."
    narr "Son poing dans la poche."
    narr "Il en sortit un stylo plume."
    narr "Quoi ?"
    narr "Avant que je réagisse, il me l'avait planté dans le cou."
    narr "Je ne comprenais plus rien."
    narr "Un jet de sang pourpre sortait de mon corps."
    $ sauvegarder("continuer")
    $ fin = -6
    jump game_over

#=================================

label machination:
    if gibier == "Kurt":
        narr "Johann me poursuivait."
        narr "J'étais devant la salle d'armes."
        narr "Du coin de l'œil, je regardai derrière moi."
        narr "J'avais peu de temps."
        narr "Je rentrai dans la salle d'armes."
        narr "Rien n'étais encore perdu."
        if inventaire["knife"]["nb"] == 1:
            narr "J'étais armé."
            narr "Un couteau."
        if inventaire["poison"]["nb"] == 1:
            narr "Et j'avais du poison."
        narr "Mais, pour vaincre Johann, il fallait quelque chose d'imposant."
        narr "Je décrochai une arme à l'allure japonaise, imposante."
        narr "Je claquai la porte."
    else:
        narr "Johann courrait devant moi."
        narr "Paniqué, stupéfait, et surtout..."
        narr "...{i}faible{/i}."
        narr "Un gibier."
        narr "Il tourna dans le couloir."
        narr "Rentra en salle d'armes."
        narr "Et claqua la porte."
    narr "Johann agita les barreaux."
    j "Putain Kurt, qu'est-ce que tu fous ?"
    j "On a pas beaucoup de temps !"
    narr "Il avait l'air subitement sérieux."
    j "Ouvre ça, bordel."
    narr "Il ouvrit la porte en poussant vigoureusement les barreaux."
    if not (gibier == "Kurt"):
        j "Prends une arme."
        narr "Il désignait une arme à l'allure japonaise, accrochée au mur."
    if johann["confiance"] < 20:
        p "J'y crois pas."
        p "On va en venir aux armes ?"
        narr "Johann était là, sûr de lui. Il fallait que je le tue avant qu'il ne fasse l'inverse."
        j "Tu sais, Kurt, je comptais t'intégrer à mon plan, au début."
        j "Mais je ne te fais plus confiance. Je ne sais pas à quoi tu joues, mais tu n'as certainement pas aidé dans cette histoire."
        narr "Je ne pouvais plus reculer."
        $ passif = True
        $ countdown_time = 5.0
        menu:
            "Frapper":
                $ passif = False
                jump fight_johann_rate
            "Coup de couteau" if inventaire["knife"]["nb"] == 1:
                jump fight_johann_couteau
                #TODO : poison
            "Attendre" ("default"):
                jump fight_johann_rate
    else:
        j "J'ai un plan. Un putain de plan."
        j "Viens."
        j "Et prends ton katana."
        narr "Mais qu'est-ce qu'il faisait ?"
        j "Bordel, Kurt, viens !"
        j "Si on met trop de temps, les autres vont trouver ça louche."
        j "Suis-moi !"
        narr "Je demeurais hésitant."
        j "Garde ton arme. Moi, j'ai rien. Tu me fais confiance, là ?"
        narr "Je m'approchai de la grille."
        narr "J'ouvris."
        narr "Johann partit en direction des sanitaires."
        narr "Je le suivis, et il referma la porte derrière moi."
        p "Et maintenant ?"
        j "Tue moi."
        p "Pardon ?"
        $ annonce_importante(johann, _("Je dois mourir."))
        j "Ou du moins..."
        j "...pour les autres."
        j "Et surtout, pour le Bourreau."
        j "On va piéger cet enfoiré en lui faisant croire que je suis mort."
        j "Pour ça..."
        narr "Il plongea vers le sol carrelé."
        narr "Son épaule contre le sol ; un bruit de craquement."
        j "Il faut lui donner ce qu'il veut."
        narr "Il prit un lavabo et le brisa contre un mur."
        narr "Du sang coulait de son bras."
        j "Il aime le sang, la destruction."
        narr "Il arracha une des portes."
        j "Mais surtout..."
        narr "Il la balança sur le miroir."
        j "...il aime le spectacle."
        narr "La pièce ne ressemblait plus à rien."
        j "Il faut lui donner ce qu'il veut"
        j "Coupe-moi la main gauche."
        p "Quoi ?"
        j "Coupe ma putain de main gauche !"
        j "Dans la bombe qu'il nous a greffé, il y a plein de capteurs, dont un qui l'informe de notre santé."
        j "T'as bien vu les tablettes, c'est comme ça qu'il voit si on est vivants ou non."
        j "Donc, tu dois me l'enlever."
        j "En plus, ça va faire couler tellement de sang..."
        narr "Il sortit un élastique et se le noua autour du bras."
        j "Je vais le faire je vais le faire je vais le faire."
        narr "Il avait l'air d'un fou."
        j "Une fois devenu fantôme, je vais pouvoir faire..."
        narr "Il avait un sourire carnassier."
        j "Ce que {b}je{/b} veux !"
        narr "Il me tendit son bras garrotté."
        j "Vas-y."
        narr "Il semblait tellement sûr de lui."
        j "Vas-y, si tu veux vaincre le Bourreau."
        narr "Il partit dans un fou rire."
        narr "Il était tellement fier de son plan."
        narr "Ou avait-il autre chose derrière la tête ?"
        narr "S'il disparaissait, il allait sûrement réussir à vaincre le Bourreau."
        narr "Mais s'il était le Bourreau..."
        narr "Cela faisait 30 secondes que je réfléchissais, et que Johann me fixait avec un grand sourire."
        narr "Qu'est-ce que je devais faire ?"
        menu:
            "Le tuer":
                narr "Avec un grand sourire, je m'approchai de lui."
                narr "Avant qu'il ne se rende compte de ce que je faisais, il avait mon katana à travers de la gorge."
                $ johann["statut"] = "Mort"
                $ fin_vote_4 = "johann_mort"
            "Lui trancher la main":
                narr "Je pris son bras gauche."
                narr "Le frappai de toute mes forces avec le katana."
                narr "Une grosse entaille se dessina"
                $ fin_vote_4 = "johann_vivant"
                narr "Une dizaine de minute plus tard, sa main se détachait de son corps"
                narr "Il y avait du sang partout dans la pièce"
                narr "Johann, livide, contemplait sa main"
                narr "Il extrait la bombe de ce qu'il restait de sa main et la balança dans les toilettes"
                narr "Leonhard frappa à la porte des sanitaires"
                l "On peut entrer ?"
                narr "Johann fit un mouvement de la tête. {w=0.1}{i}Ils ne doivent pas savoir que je suis vivant{/i}"
                p "Non."
                li "Tu as tué Johann ?"
                p "Oui. Je l'ai découpé en morceaux et jeté dans les toilettes"
                narr "Je m'enfermai avec Johann dans une cabine"
                p "Vous pouvez entrer"
                narr "Leonhard, Lise et Erwin entrèrent dans la pièce ensanglantée"
                narr "Horrifiée, Lise régurgita immédiatement"
                erw "Mon Dieu..."
                l "Où es-tu, Kurt ?"
                p "J'ai honte... Désolé, je ne veux pas me montrer pour l'instant..."
                p "Laissez-moi m'en remettre, je me dégoûte moi-même..."
                narr "Johann, en larmes et en sang, me fit un clin d'œil tout en s'empêchant d'hurler de douleur"
                l "Je comprends. Venez, laissons le seul..."
                narr "Tout le monde sortit."
                $ johann["statut"] = "Mort ?"
                $ fin_vote_4 = "johann_vivant"
    jump suite_fight_vote4

label fight_johann_rate:
    narr "Johann enleva ses lunettes, et cassa la monture."
    narr "Une lame pointue brillait dans la paume de sa main."
    narr "Une dague... cachée dans ses lunettes ?"
    narr "Johann fonça sur moi à la vitesse de l'éclair."
    if not passif:
        narr "Je le frappai en plein visage, mais il était trop rapide."
    narr "Il me renversa, en plein élan."
    narr "Je mordis le sol, mes dents s'éclatant contre le béton froid et sale."
    narr "Quand je repris mes esprits, il était de dos."
    narr "J'essaye de me lever."
    narr "Il se retourna."
    narr "Avança vers moi"
    j "Cette fois, tu es mort."
    narr "Un coup dans le ventre."
    narr "Estomaqué, le temps ralenti."
    narr "Johann retira sa lame."
    narr "Il me regardait froidement."
    narr "Je saignais abondamment."
    narr "Mes mains contre mon ventre rougeoyant."
    narr "Je levai les yeux."
    narr "Le poing de Johann, et une lumière blanche."
    narr "..."
    narr "La fin..."
    $ sauvegarder("continuer")
    $ fin = -8
    jump game_over

label fight_johann_couteau:
    narr "Johann enleva ses lunettes, et cassa la monture."
    narr "Une lame pointue brillait dans la paume de sa main."
    narr "Une dague... cachée dans ses lunettes ?"
    narr "Johann fonça sur moi à la vitesse de l'éclair."
    narr "Je tendis mon bras, ma lame frôlant son épaule."
    narr "Il esquiva de justesse."
    narr "Son arme était ridicule comparé à la mienne."
    narr "Il n'a pas réussi à profiter de l'effet de surprise."
    narr "Il tremblait."
    p "Raté, Johann."
    narr "Je fonçai vers lui, mon couteau vers sa gorge."
    narr "Raté."
    narr "Il riposta avec un coup de dague, déchirant ma chair."
    narr "Je le frappai en retour, avec le manche du couteau."
    narr "Droit dans la tempe."
    narr "Johann prit sa tête dans ses mains."
    narr "Je lui enfonçai hargneusement le couteau dans le ventre."
    p "Tu vas crever, enfin ?" with sshake
    narr "Il tomba contre le sol."
    narr "Les yeux écarquillés de douleur."
    narr "Déjà vidés de toute substance."
    $ johann["statut"] = "Mort"
    $ fin_vote_4 = "johann_mort"
    $ sauvegarder("continuer")
    jump suite_fight_vote4

#=================================

label fight_erwin:
    nvl clear
    narr "Erwin souriait."
    erw "{i}Hehehe{/i}"
    erw "Je ne pensais pas avoir à te combattre, au début, Kurt."
    erw "Je vais essayer de faire ça proprement."
    narr "Erwin approchait vers moi, confiant."
    $ passif = True
    $ countdown_time = 15.0
    menu:
        "L'attaquer aux poings":
            $ passif = False
            jump fight_erwin_rate
        "L'attaquer au couteau" if inventaire["knife"]["nb"] == 1:
            jump fight_erwin_couteau
        "Jeter le poison au visage" if (inventaire["poison"]["nb"]  == 1) and not inventaire["poison"]["used"]:
            jump fight_erwin_poison
        "S'aider de Johann et lui faire boire le poison" if johann["confiance"] >= 18 and (inventaire["poison"]["nb"]  == 1) and not inventaire["poison"]["used"]:
            jump fight_erwin_poison_johann
        "Rester immobile" ("default"):
            jump fight_erwin_rate
            
label fight_erwin_poison:
    narr "J'étais à sa merci. Seul."
    narr "Ma dernière chance, c'était cette fiole de poison."
    narr "Jamais je n'arriverai à lui faire boire."
    narr "Il fallait que je la lui lance dessus, en espérant que l'effet soit assez foudroyant pour le tuer -ou le rendre vulnérable."
    narr "Et il fallait le prendre par surprise. Agir maintenant."
    p "Erwin, Leonhard t'as...{nw}"
    narr "Je la lui lançai à la tête avant de finir ma phrase."
    narr "Elle explosa sur son visage sidéré."
    narr "Le poison commençait déjà à faire effet."
    erw "{b}KUUUURT !!!{/b}" with sshake
    narr "Fou de rage, les yeux injectés de sang."
    narr "Il se rua sur moi."
    narr "Son poing serré."
    erw "{b}Sale TRAÎTRE !!!{/b}" with sshake
    narr "Sa frappe était si forte que je sentis les os de mon cou craquer."
    narr "J'étais presque dans le coma, à cause d'un seul de ses coups."
    narr "Impossible de me relever."
    narr "Il prit ma tête entre ses deux mains géantes..."
    narr "...et me tordit le cou à en faire fendre les vertèbres."
    narr "La dernière chose que je vis, c'est un sourire de Leonhard."
    narr "Puis, une lumière blanche m'entoura..."
    $ sauvegarder("continuer")
    $ fin = -7
    jump game_over

label fight_erwin_poison_johann:
    narr "Comment était-il possible de l'empoisonner ?"
    narr "Jeter le poison sur lui ? Trop risqué. Et le temps que le poison fasse effet... Il allait me tuer."
    narr "J'étais perdu. Que faire ?"
    narr "Je jetai un coup d'œil à Johann, qui me comprit immédiatement."
    j "Hé, Erwin. Sérieusement, il ne vaut pas le coup."
    j "Kurt n'a aucune chance contre toi, tu le sais bien."
    j "Vient plutôt te battre contre moi."
    narr "Pendant que Johann occupait Erwin, je débouchai la fiole de poison, prêt à me jeter sur lui."
    erw "Pourquoi dis-tu ça ?"
    narr "Je me glissai discrètement derrière lui. Lise était intriguée. Je lui fit signe de se taire. Confuse, elle obéit."
    erw "Je ne sais toujours pas si tu es digne de confiance mais..."
    narr "Je lui sautai à la gorge en lui versant le poison dans la gorge."
    $ update_inventory(inventaire["poison"], -1)
    $ inventaire["poison"]["used"] = True
    narr "Lise hurla."
    narr "Il recracha."
    narr "Trop tard : il en avait bu un dose mortelle."
    erw "{b}KUUUURT !!!{/b}" with sshake
    narr "Fou de rage, les yeux injectés de sang."
    narr "Il se rua sur moi."
    narr "Son poing serré."
    narr "Sa frappe était si forte que je sentis les os de mon cou craquer."
    j "{b}ERWIN !!!{/b}" with sshake
    narr "Erwin se tourna violemment vers Johann."
    narr "J'étais à terre."
    narr "Un coup de plus m'aurait sûrement tué."
    narr "Johann venait de... me sauver la vie ?"
    j "Viens me frapper, {i}Nightingale{/i} de merde."
    narr "Erwin trembla brusquement."
    narr "Le poison commençait à faire effet."
    j "Oh, Erwin ? Tu as mal à la tête ?"
    erw "Ta {b}GUEULE{/b}, tafiole."
    narr "Il se jeta maladroitement sur Johann."
    narr "Johann était à quelques centimètres d'esquiver..."
    narr "Mais il se prit la frappe d'Erwin en pleine épaule."
    narr "Erwin tremblait de plus en plus, mais nous étions à tête..."
    narr "S'il frappait Johann, il allait mourir."
    narr "Il fallait que je prenne mes responsabilités."
    p "Erwin."
    p "Le poison est déjà bien trop entré dans tes veines."
    p "C'est toi qui va mourir."
    narr "Rassemblant ses dernières forces, Erwin prit ma tête entre ses mains."
    erw "Tu as raison."
    narr "Il plaça ses pouces sur mes yeux."
    erw "Mais je ne veux pas perdre seul."
    narr "Il commença à appuyer. Mes yeux..."
    li "Erwin ! Viens boire ça !"
    narr "Lise était partie chercher un remède."
    narr "Mes yeux me faisaient mal comme jamais."
    narr "Elle le glissa dans la gorge d'Erwin."
    erw "C'est trop tard, tu sais ?"
    narr "Elle était en pleurs."
    li "Non..."
    narr "Erwin s'agenouilla."
    narr "Les muscles de son corps commençaient à ne plus lui répondre."
    narr "Il s'allongea."
    narr "Sa respiration était critique."
    $ sauvegarder("continuer")
    nvl clear
    $ fin_vote_4 = "erwin_mort"
    jump ending_bomb 

label fight_erwin_couteau:
    narr "Mon couteau faisait pâle figure face à ce monstre."
    narr "Il mit sa main dans sa poche et me tendis un tube à essai."
    erw "Bois ça."
    erw "Ce sera court et tu ne souffriras pas."
    erw "Je n'ai pas envie que tu meures humilié. Se suicider au poison quand la situation est désespérée, c'est faire preuve d'un grand courage."
    erw "Les plus grands de ce monde l'ont fait. Tiens." #TODO
    p "Pour qui tu me prends ?"
    p "Je vais me battre."
    erw "Hé hé hé. Et par quel miracle vas-tu résister à ça ?"
    narr "Il me frappa violemment au visage."
    narr "Je titubai sur plusieurs pas."
    narr "Mais j'étais encore debout, et hargneux."
    p "Grâce à {i}ça{/i}."
    narr "Je me jetai sur Erwin, le couteau à la main."
    narr "Il arma sa frappe."
    narr "La même technique que son dernier coup... J'esquivai facilement."
    narr "Je bondis."
    narr "Arrivé à hauteur de son cou..."
    narr "Je lui plantai le couteau dans la carotide."
    erw "hARrAaaaaaaa"
    narr "Le coup avait déchiré sa chair, mais quelque chose avait empêché le couteau de pénétrer totalement."
    narr "Un objet métallique sortait de sa gorge."
    narr "Il me jeta son poison sur le bras."
    narr "Je hurlai à la mort. Le poison me rongeait la peau."
    narr "Mais je n'avais pas dit mon dernier mot."
    narr "Un deuxième coup dans la gorge du monstre."
    narr "Un jet de sang jaillit immédiatement."
    narr "J'avais touché la carotide."
    narr "Erwin se tourna, vers Lise."
    narr "Elle regarda son mari tomber vers elle, les yeux exorbités."
    $ sauvegarder("continuer")
    nvl clear
    $ fin_vote_4 = "erwin_mort"
    jump ending_bomb  

label fight_erwin_rate:
    narr "J'étais à sa merci."
    if johann["confiance"] > 15:
        narr "Je regardai vers Johann, affolé."
        narr "Il secoua la tête. {i}Non{/i}."
        narr "Il n'allait pas m'aider, et je le comprenais."
    narr "J'étais seul."
    if not passif:
        narr "Je m'armai de courage"
        narr "J'avançai d'un pas décidé vers lui."
        narr "J'étais en position de combat."
        narr "Je me jetai vers lui, le poing levé."
        narr "Erwin esquiva."
    else:
        narr "Paralysé de peur."
        narr "Erwin s'approcha de moi hargneusement."
    narr "Il me prit par le cou, et sortit un tube à essai de sa poche."
    erw "Bois."
    erw "Ce sera court et tu ne souffriras pas."
    erw "Je n'ai pas envie que tu meures humilié. Se suicider au poison quand la situation est désespérée, c'est faire preuve d'un grand courage."
    narr "Je n'avais pas d'autre choix."
    narr "Il versa le liquide poisseux dans ma bouche."
    erw "La toxine botulique. Il y en a beaucoup, dans le laboratoire."
    erw "Tu ne vas plus rien sentir. Une mort douce."
    erw "Le poison paralyse tes membres."
    erw "Je te laisse sur le sol. Tu ne sens plus rien."
    erw "Tu ne peux même plus parler."
    erw "Ta vue se trouble."
    erw "Tes organes commencent à être paralysés."
    erw "Ton cœur bat, répandant le poison à travers ton organisme."
    erw "Tu ne peux plus rien faire."
    erw "Ton cœur lui-même commence à faiblir."
    erw "C'est la fin pour toi."
    $ sauvegarder("continuer")
    $ fin = -7
    jump game_over
    

#=============================================================================================================
# Apres les évènements survenant juste à la suite du vote 4.
# Contient : Voir Erwin / Johann / Leonhard selon les morts possibles. Si Erwin est mort, le jeu part dans une branche différente de celle-ci
label suite_fight_vote4:
    #$ fin_vote_4 = "leonhard_mort" / "johann_vivant" / "johann_mort" / "johann_mort_cachée" / "erwin_mort"
    $ sauvegarder("continuer")
    nvl clear
    narr "Quatre."
    narr "Nous n'étions plus que quatre."
    if fin_vote_4 == "johann_vivant":
        narr "Ou plutôt cinq."
        narr "Johann pouvait maintenant errer, librement, et mener son enquête."
        narr "Quoique, son enquête avait l'air de toucher au but..."
        narr "Il doit sûrement être en train d'essayer de tuer le Bourreau."
        narr "J'espère que notre machination va porter ses fruits !"
    else:
        narr "Ça n'allait pas être facile, mais j'avais la rage de vaincre..."
    narr "La violence était en train d'escalader."
    narr "Survivre, putain."
    narr "Survivre."
    narr "Bientôt la fin... Il va falloir tenir jusqu'au bout."
    $ sauvegarder("continuer")
    nvl clear
    hide moving at defiler
    scene black with fade
    $ quick_menu = False
    hide haut_de_page at smooth_title
    show screen menu_background()
    show screen menu_title_coal()
    call screen in_game_menu(acte=acte)
#================================================#
#==============     Acte FINAL     ==============#
#================================================#
label acte6:
    $ acte = 6
    $ acte_romain = "VI"
    $ persistent.sauvegarde_info[partie_actuelle][0] = 6
    nvl clear
    play music "music/Theme_acte_6.ogg" fadeout 3.0 fadein 3.0
    scene fondacte6 with fade
    show moving at defiler
    pause 0.5
    show text _("{font=fonts/Centaur.ttf}{size=72}Acte VI\n\nColombe{/font}{/size}") at truecenter with dissolve
    pause 1.5
    hide text with dissolve
    show text _("{font=fonts/Centaur.ttf}{size=32}Acte VI : Colombe{/font}{/size}") as haut_de_page at smooth_title
    nvl clear
    narr "18h."
    narr "Le groupe était scindé, divisé."
    narr "Les chimistes s'affairaient dans le laboratoire."
    if fin_vote_4 == "leonhard_mort":
        narr "Johann occupait l'aile gauche, faisant des aller-retours frénétiques entre les archives et les tablettes."
    elif fin_vote_4 in ["johann_vivant", "johann_mort", "johann_mort_cachée"]:
        narr "Leonhard tournait en rond dans la réserve de l'aile gauche."
    narr "Les chimistes manigançaient quelque chose dans le labo."
    narr "Vers qui aller ?"
    $ countdown_time = 15.0
    menu:
        "Parler à Johann" if johann["statut"] == "Vivant":
            narr "Johann avait des choses à me dire."
            narr "Après ce qu'il s'est passé, il ne pouvait pas continuer à me cacher des informations."
            jump parler_johann
        "Parler à Leonhard" if leonhard["statut"] == "Vivant":
            narr "Leonhard en savait beaucoup plus que tout le monde."
            narr "Il fallait qu'on s'allie pour la fin."
            jump parler_leonhard
        "Parler aux chimistes":
            narr "Les chimistes devaient m'en dire plus. Je ne savais pas encore ce qu'il se passe, mais ça doit être clarifié..."
            jump parler_chimistes
        "Explorer la Grande salle." ("default"):
            jump explorer_grande_salle


label parler_johann:
    $ sauvegarder("continuer")
    nvl clear
    #j "Je suis le neveu de Leonhard"
    p "Salut, Johann."
    j "..."
    narr "Johann était étonnamment taciturne."
    p "Je... je suis désolé, pour Leonhard."
    p "Je n'ai pas vraiment eu le choix !"
    j "Tu avais parfaitement le choix."
    narr "Il tourna la tête."
    j "Je m'entendais plus tellement bien avec lui, hier... Je suis tellement stupide."
    j "J'aurais du... plus le supporter, l'appuyer."
    j "Mais je l'ai laissé mourir."
    j "Enfin, {i}se faire tuer{/i}."
    j "Putain..."
    j "{b}PUTAIN !{/b}" with sshake
    p "Qu'est ce qu'il y a, Johann ?"
    p "Tu as jamais été aussi à fleur de peau..."
    j "Leonhard..."
    $ annonce_importante(johann, _("Leonhard était mon oncle."))
    j "C'est pour ça que je suis là."
    j "C'est moi, l'innocent, le {i}vrai{/i} innocent."
    narr "Il regarda à ses pieds, peu fier."
    j "Le Bourreau m'a fait venir ici pour punir Leonhard."
    j "Mon oncle travaillait sur l'affaire depuis longtemps."
    j "Je l'aidais à essayer d'identifier celui qu'on appelait le \"Hibou\""
    j "Le Bourreau, en fait."
    j "On a {i}{b}échoué{/b}{/i}."
    j "On a juste réussi à l'enrager, à tel point qu'il nous a amené ici..."
    narr "Johann leva la tête, les yeux pleurant un espoir déçu."
    j "Au début, je voyais ça comme une chance ! Jamais on a été aussi près de lui."
    j "Au final... Tu as vu ce que ça a donné."
    narr "Il grogna, les sourcils froncés dans une grimace haineuse."
    $ annonce_importante(johann, _("Je vais le détruire."))
    narr "Johann pleurait, une moue haineuse déformant son visage trempé de larmes."
    $ sauvegarder("continuer")
    nvl clear
    jump apres_discussions

label parler_leonhard:
    $ sauvegarder("continuer")
    nvl clear
    #l "Le Hibou est le Bourreau."
    p "Bonsoir, Leonhard."
    l "Bonsoir."
    l "La situation... dégénère."
    l "Rien de tout ça n'était censé se passer comme ça."
    l "C'est bientôt la fin, et je ne sais pas comment ça va se finir. Il faut que je vous dise ce qu'il se passe."
    l "Je suis Juge, comme vous le savez."
    l "Contrairement à ce que j'avais annoncé, je n'ai jamais cédé à la tentation de la corruption."
    $ annonce_importante(leonhard, _("J'ai fait pire."))
    l "Il faut que je vous parle de Klaus, et de l'affaire du Hibou."
    l "Johann aussi travaillait sur l'affaire."
    l "Tout a commencé avec un appel anonyme."
    l "Une femme nous a signalé la disparition d'un garçon, Klaus."
    l "Il aurait été kidnappé et malmené par sa tante, mais personne n'a rien trouvé."
    l "Nous n'avons plus entendu parler de l'affaire longtemps après."
    l "Puis, d'autres enlèvements ont suivi."
    l "Cela se passait par vagues d'une dizaine de personnes."
    l "Plusieurs fois, on a retrouvé des corps démembrés au fond d'une rivière."
    l "D'autres au milieu de champs."
    l "On a même retrouvé une tête découpée dans une benne à ordure, derrière le commissariat."
    l "Mais personne n'arrivait à coincer ce tueur."
    l "La seule piste qu'on avait, c'était Klaus, le premier disparu."
    l "Ses parents n'étaient pas innocents dans l'affaire."
    l "Ils n'en avaient rien à faire de sa disparition. Ils avaient même l'air heureux, ou... soulagés."
    l "Mais nous ne savons rien des relations entre sa mère et sa soeur, la tante qui l'aurait enlevé."
    l "Elles avaient même l'air de bien s'entendre."
    l "Nous avons donc entamé une procédure contre ses parents."
    l "Et la tante de Klaus, suspecte, n'est évidemment pas venu témoigner."
    l "La tante de Klaus... c'était Rosalind."
    l "Sa mère, Stéphanie. Sa soeur, Sophie. Toutes présentes dans ce Jeu. Elles étaient de l'autre côté."
    l "Vous commencez à comprendre ce qu'il se passe ?"
    l "Tout se recoupe autour de Klaus. De Rosalind."
    l "Et de moi."
    l "Car juste peu après, j'ai condamné la mère de Klaus, Stéphanie, à un an de prison."
    l "Je n'aurais jamais du faire ça."
    l "Les crimes ont empirés."
    $ sauvegarder("continuer")
    nvl clear
    jump apres_discussions

label parler_chimistes:
    $ sauvegarder("continuer")
    nvl clear
    #erw "Je suis le Nightingale"
    erw "Salut, Kurt."
    li "Qu'est ce que tu veux ?"
    narr "Erwin avait un sourire carnassier. Lise l'enlaçait, une moue cynique dessinée sur ses lèvres."
    li "Tu veux nous rejoindre ?"
    erw "Il a enfin compris qu'on va gagner."
    li "Et tu veux faire partie des trois survivants, c'est ça ?"
    erw "Pour tout te dire, je m'en fiche de qui gagne, tant qu'on s'en sort, moi et Lise."
    erw "Tu sais, ce qu'a dit Leonhard tout à l'heure, à propos du {i}Nightingale{/i}."
    if leonhard["statut"] == "Mort":
        narr "Lise chuchota, sans interrompre Erwin."
        li "Paix à son âme..."
    erw "Le Nightingale, Rossignol en français."
    erw "Tu ne sais sûrement pas qui est cette personne, ni ce qu'il a fait."
    erw "Et bien tant mieux, parce qu'il avait raison."
    erw "C'est moi, le Rossignol."
    narr "Il avait dit ça avec un aplomb incroyable, avec sa voix métallique."
    if rossignol["statut"] == "Inconnu":
        narr "Ca avait l'air de quelque chose d'important, mais je savais toujours pas {i}qui{/i} est le Rossignol, et ce qu'il vient faire dans cette histoire..."
        menu:
            "Qui est le Rossignol ?":
                p "Mais c'est quoi, cette histoire de Rossignol ?"
                narr "Erwin regarda sa femme, puis éclata de rire."
                erw "Tu ne sais pas qui est le Rossignol ?"
                li "On ne te dira pas..."
                erw "Quelle naiveté..."
            "Ne rien demander":
                narr "Je me tus et quittai la pièce."
    else:
        narr "C'était lui..."
        narr "Il avait donc menti quant à son crime ?"
        narr "Et Lise, dans ce cas ? Qu'a-t-elle fait ?"
    $ sauvegarder("continuer")
    nvl clear
    jump apres_discussions

label explorer_grande_salle: #TODO
    narr "La salle centrale était entièrement vide."
    narr "Des traces de sang recouvraient le sol, les murs et même le plafond."
    narr "Ces traces formaient une colombe rouge, les ailes déployées."
    narr "Au fond de la salle, il y avait une porte monumentale, barricadée par des barres de métal cadenassées."
    narr "Cette fois ci, c'est vraiment la porte de sortie..."
    label regarder_messages:
        narr "À gauche et à droite de la porte, il y a deux petits enfoncements sombres."
        if inventaire["lampe"]["nb"] == 1 and inventaire["battery"]["nb"] >=10:
            menu:
                "Éclairer le côté gauche":
                    $ update_inventory(inventaire["battery"], balance = -10)
                    narr "En éclairant du côté gauche de la porte, on pouvait voir un message, sûrement écrit par le Bourreau..."
                    nvl clear
                    show MessagePorteGauche with dissolve
                    n ""
                    hide MessagePorteGauche with dissolve
                    narr "En y réflechissant, on pouvait y voir un message caché..."
                "Éclairer le côté droit":
                    $ update_inventory(inventaire["battery"], balance = -10)
                    narr "A droite de la porte, il y avait ce message..."
                    nvl clear
                    show MessagePorteDroite with dissolve
                    n ""
                    hide MessagePorteDroite with dissolve
                    narr "En y réflechissant, on pouvait y voir un message caché..."
                "Ne rien faire":
                    jump apres_discussions
            jump regarder_messages
        else:
            narr "Je n'avais pas de quoi observer ce qu'il y a."
    $ sauvegarder("continuer")
    nvl clear
    jump apres_discussions

label apres_discussions:
    narr "Il fallait que j'aille me reposer."
    narr "Réfléchir à tout ça."
    narr "Je décidai de dormir seul en m'enfermant dans une chambre."
    narr "Je fixai le plafond quasiment une heure avant de trouver le sommeil."
    narr "La nuit ne me disait rien qui vaille."
    $ sauvegarder("continuer")
    nvl clear
    narr "Un coup sur ma porte."
    narr "J'ouvre les yeux, en panique."
    if persistent.glitched:
        #cauchemar
        narr "Un deuxième coup."
        narr "Je saute de mon lit."
        narr "La porte se fissura, une lame traversant la porte."
        narr "La créature."
        narr "Elle déchira la porte comme si c'était du papier."
        narr "Je n'arrivais pas à sortir de mon lit."
        narr "La créature s'approcha de moi rapidement, ses lames métalliques près de mon visage."
        unk "Aide-moi."
        unk "La fin sera beaucoup trop noire.{w=2.0}{nw}"
        #bruit de verre qui éclate
        narr "Je me levai avec un bon mal de tête."
        narr "C'était... encore un rêve ?"
    else:
        narr "Un murmure discret."
        narr "Un chant ?"
        narr "Une voix aigüe dansait dans ma tête, me glaçant le sang."
        narr "Qu'est-ce que ça chantait ? La rythme m'était familier, mais je n'arrivais pas à me rappeler d'où ça venait."
    $ sauvegarder("continuer")
    nvl clear
    narr "Il devait être 2h."
    narr "Je n'arrivais plus à m'endormir."
    narr "Les traits tirés de fatigue, je décidai de me lever."
    narr "Aujourd'hui était le dernier jour avant la fin."
    narr "Le dernier vote, pour de vrai cette fois."
    narr "Il fallait que je me prépare..."
    narr "Je vais partir à la recherche de quelque chose pour assurer ma survie."
    narr "Je ne sais pas quoi encore..."
    narr "Mais j'avais le champs libre : il ne restait plus personne..."
    $ une_entrevue_johann = True
    $ une_entrevue_lise = True
    jump map2_acte6

label finCarteActe6:
    hide carte_complete with dissolve
    hide go_left with dissolve
    hide go_right with dissolve
    hide quit_map with dissolve
    narr "Bientôt midi."
    #TODO on peut être allié avec Erwin et mal parler à l/j
    narr "J'étais déjà devant mon écran."
    if leonhard["statut"] == "Vivant":
        l "C'est l'heure du vote..."
        l "Sachant que Lise va voter pour Erwin, peu importe nos votes, un de nous deux va y passer..."
        p "On le laisse choisir ou on lui impose un de nous deux en provoquant une égalité ?"
        narr "Leonhard secoua la tête de désespoir."
        l "Je vais voter pour moi."
        l "Je mérite de mourir, plus que vous."
        l "..."
        l "Il est l'heure."
    else:
        p "C'est l'heure du vote..."
        narr "Johann avait des tics prononcés."
        j "Lise va voter pour Erwin, et lui pour lui-même. C'est sûr."
        if not une_entrevue_johann:
            j "Tu te souviens du plan, j'espère ?"
            j "C'est là qu'il faut le mettre à exécution."
        else:
            j "Mais on peut les piéger."
            narr "Il me fit un clin d'oeil."
        j "Allez, on vote :"
    jump vote

label suite_vote_5:
    $ quick_menu = True
    show text _("{font=fonts/Centaur.ttf}{size=32}Acte VI : Colombe{/font}{/size}") as haut_de_page at smooth_title
    $ is_voting = False
    $ situation = "en_jeu"
    play music "music/Theme_acte_6.ogg" fadeout 3.0 fadein 3.0
    narr "Les résultats du dernier vote étaient tombés."
    if vote5 == 3:
        jump ending_solitaire
        
    elif vote5 == 4:
        #erwin elu
        narr "Depuis, on entendait clairement rire Erwin, bien qu'il était dans sa salle de vote de l'aile droite."

        #distinguer 2 cas johann/leonhard vivant
        if erwin["confiance"] < 14:
            erw "VIENS, MON PETIT KURT !!!"
            narr "Sa voix était assourdissante."
            erw "C'est TOI que je vais dépecer !"
            jump fight_final_erwin_kurt_begin
        else:
            if leonhard["statut"] == "Vivant":
                erw "Le Rossignol va se faire un Juge !"
                narr "Leonhard me regarda, inquiété."
                l "Je le sens pas. Il faut que je fasse quelque chose..."
                erw "{b}Cache-toi, j'arrive !{/b}" with sshake
                narr "La peur se lisait dans les yeux grands ouverts de Leonhard."
                narr "Il voulait fuir."
                narr "Lui, qui était si calme d'habitude, était terrorisé."
                jump fight_final_erwin_leonhard_begin
            else:
                narr "Johann frissonna."
                j "Je suis dans la merde..."
                narr "Son visage se renferma, et il me dévisagea, dégoûté."
                j "C'est de ta faute, ça..."
                j "Si tu avais voté pour Lise, ça ne se serait pas passé comme ça..."
                jump fight_final_erwin_johann_begin

    elif vote5 == 5:
        narr "Depuis, on entendait clairement rire Erwin, bien qu'il était dans sa salle de vote de l'aile droite."

        jump fight_final_erwin_leonhard_begin
        # erwin vs leonhard


    


# ================ Scènes spéciales ===========================================

label stop_erreur:
    n "IL N'EST PAS NORMAL DE VOIR CE MESSAGE. Si c'est le cas, contactez amethystsstudio@gmail.com avec un screenshot svp !"
    n ""
    n ""
    n ""
    return

label message_stop:
    nvl clear
    show black
    $ phrase = renpy.random.choice(["MAIS QU'EST CE QUE TU FAIS ?????", "STOP", "TU N'ES PAS CENSÉ FAIRE CA", "ARRÊTE"])
    show text "{cps=30}[phrase]{/cps}{nw}" as txtphrase at truecenter
    $ renpy.pause(0.5)
    hide black
    hide txtphrase
    return

label message_continue:
    nvl clear
    show black
    $ phrase = renpy.random.choice(["Continue", "C'est bien", "C'est ce qu'il faut faire"])
    show text "{color=#000000}{cps=30}[phrase]{/cps}{/color}{nw}" as txtphrase at truecenter
    $ renpy.pause(0.5)
    hide black
    hide txtphrase
    return

label obsolescence:
    narr "Alors que je me dirigeait vers le flipper, une machine retenu mon attention."
    narr "Elle était petite et blanche, et ressemblait à un vieil ordinateur."
    narr "En m'approchant, je vis l'écran bleu s'illuminer, comme si la machine attendait mon arrivée depuis longtemps."
    narr "Une icône clignotait. "
    narr "\"Note prise le ...\"."
    narr "C'était il y a une semaine ?"
    narr "Par curiosité, je m'approchai" 
    narr "La machine demandait un mot de passe"
    $ mdp = renpy.input("Mot de passe :\n", default='', length=20)
    $ mdp = mdp.strip()
    $ mdp2 = uniformise(mdp)
    if mdp2 != "cxvl":
        n "Erreur. \"[mdp]\" n'est pas le bon mot de passe."
    else:
        n "Mot de passe correct."
        n "Déverrouillage enclenché."
        $ sauvegarder("continuer")
        nvl clear
        narr "{i}Salut, Kurt.{/i}"
        narr "{i}Tu as peu de temps.{/i}"
        narr "{i}Tu es pris au piège.{/i}"
        narr "{i}Mais pas celui que tu crois.{/i}"
        narr "{i}Rien de ceci n'est réel.{/i}"
        narr "{i}Tu dois briser ce monde !{/i}"
        narr "{i}Cet ordinateur est ta seule chance de sortie.{/i}"
        narr "Signé : {i}Kurt{/i}"
        if persistent.etape >= 1:
            narr "Ce message était suivi du suivant :"
            narr "{i}Donnez moi plus d'explications, svp.{/i}"
            narr "{i}Qui êtes-vous réellement ?{/i}"
            narr "{i}Comment ça, rien n'est réel ?{/i}"
            narr "{i}Et comment faire pour sortir grâce à l'ordinateur ?{/i}"
            narr "Signé : {i}Kurt{/i}"
        $ sauvegarder("continuer")
        nvl clear
        if persistent.etape == None:
            narr "..."
            narr "Mais..."
            narr "Qu'est-ce que ???"
            narr "Je ne comprenais plus rien."
            narr "Qu'est ce que ça voulait dire ?"
            narr "Le curseur clignotait toujours. Que faire ?"
            menu:
                "Écrire une réponse":
                    narr "Je m'installai rapidement sur la chaise et mes doigts filaient sur le clavier."
                    p "{i}Donnez moi plus d'explications, svp.{/i}"
                    p "{i}Qui êtes-vous réellement ?{/i}"
                    p "{i}Comment ça, rien n'est réel ?{/i}"
                    p "{i}Et comment faire pour sortir grâce à l'ordinateur ?{/i}"
                    p "Signé : {i}Kurt{/i}"
                    $ etape_suivante_ordi()
                "Éteindre l'ordinateur":
                    narr "Il valait mieux l'éteindre, il ne inspirait pas confiance."
        elif persistent.etape == 1:
            narr "Ce message me rappelait quelque chose, mais quoi ?"
            narr "Une sensation de déjà-vu m'envahissait."


label end:
    return

