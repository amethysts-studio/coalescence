
define config.default_afm_enable = False
define config.default_afm_time = 15
define config.default_music_volume = 1.0
define config.default_sfx_volume = 0.4


init python:
    config.keymap['game_menu'].remove('K_ESCAPE')
    config.keymap['game_menu'].remove('K_MENU')
    config.keymap['game_menu'].remove('mouseup_3')

    import datetime
    menu = nvl_menu
    # The color of a menu choice when it isn't hovered.
    style.nvl_menu_choice.idle_color = "#ffffff"
    # The color of a menu choice when it is hovered.
    style.nvl_menu_choice.hover_color = "#ffffffff"
    # The color of the background of a menu choice, when it isn't
    # hovered.
    style.nvl_menu_choice_button.idle_background = "#00000000"
    # The color of the background of a menu choice, when it is
    # hovered.
    style.nvl_menu_choice_button.hover_background = "#ff000044"

    # How far from the left menu choices should be indented.
    style.nvl_menu_choice_button.left_margin = 200

    style.nvl_window.background = "nvl_window.png"
    style.nvl_window.xpadding = 55
    style.nvl_window.ypadding = 55

    config.empty_window = nvl_show_core
    config.window_hide_transition = dissolve
    config.window_show_transition = dissolve


label initialisation_debut_partie:
    $ countdown_time = 20
    $ persistent.loadable = True # False en cas de chargement non possible (comme pour une fin de partie par ex)
    hide moving
    $ persistent.partie_actu = "continuer" #une fois le choix fait, on restocke de maniere persistante
    $ situation = "en_jeu" # en_jeu / fin_acte / menu_principal / en_vote / dans_carte / archives / succes
    $ acte = 1
    $ acte_romain = "I"
    $ amour = 10
    $ fin = 0
    $ carte_complete = False
    $ book = ""
    $ clavier_azerty = (_preferences.language == None)
    $ liste_recherches = []
    $ in_archives = False

    $ elus_vote = [[], [], [], [], [], []]
    
    if persistent.jeu_actuel > 1:
        $ persistent.glitched = True

    $ plan_available = False
    $ info_klaus_archives   = False
    $ grosse_balance_sa_mere= False
    $ flingue_owned = False

    $ horreur = True #ofc

    $ archives_dic = {"":"Recherchez des informations...",
        "begin":"Recherchez quelque chose",

        "none":_("Recherche infructueuse...\n\nAucun livre ne parle de ça."),

        "emmy":_("Le dossier d'Emmy est assez succinct. Il mentionne juste son appartenance à une organisation anti-gay allemande, {b}Gesunder Menschenverstand (GM){/b}. Elle y est relativement active.\n\nLe nom d'{b}Isaac{/b} est inscrit dans le dossier, avec une note manuscrite : {i}Proche ?{/i}"),
        "isaac":_("Deux livres mentionnent le prénom Isaac : un livre sur les records de sport, et un livre de science-fiction. D'autres livres contiennent le mot Isaac, mais je ne pense pas que ce soit pertinent.\n\nUn certain Isaac aurait été champion d'apnée il y a trois ans.\nUn autre Isaac était inventeur d'une machine permettant d'échanger les consciences de deux personnes.\n\nLe deuxième livre avait l'air intéressant, mais pas très utile... Enfin je pense ? Il me faut plus d’informations."),

        "kurt": _("Beaucoup de journaux parlent de moi. A vrai dire, avec mon compte {b}Twitter{/b}, je suis un peu une star locale.\n120 000 followers, c'est plus de 10 fois la population de ma ville !\nLe Bourreau a une collection impressionnante de tweets parlant de moi."),

        "alan": _("Le nom d'Alan est surligné dans un journal à la section fait divers :\n\n{i}Alan, jeune adolescent de 17 ans, a été inculpé pour trafic de drogues.{/i}\n\nÉtonnamment, il semble ne pas y avoir plus d'informations."),

        "johann": _("Le nom \"Johann\" a l'air de déclencher quelque chose de spécial. On dirait qu'il faut rentrer un mot de passe directement dans la machine pour accéder à des fichiers..."),

        "sherlock": _("Extrait du journal secret de Johann, Septembre 2013.\n{i}Mon oncle m'a encore proposé de le rejoindre pour cette affaire. Un enlèvement. Signalé anonymement. Moins fun que la dernière, grâce à laquelle j'ai pu me trouver un fournisseur. Mais les enlèvements sont peu nombreux par ici. Cela va m'entraîner pour mon avenir. Dommage que j'ai encore ce statut de stagiaire. J'ai résolu les 5 dernières affaires. Les policiers sont incompétents. En fait, je suis un peu leur Sherlock Holmes, qui résout les affaires de manière désintéressée, par pur plaisir intellectuel. De toute façon, ils ne peuvent pas y arriver sans moi, donc il est évident qu'ils me laissent accès à tout. Et puis, c'est lié aux affaires des {b}Liebert{/b}...{/i}\n\nExtrait du Journal secret de Johann, Janvier 2014\n{i}{b}Rosalind{/b} Liebert séquestre son neveu. Il a envoyé un message à la Police, en envoyant un avion en papier... Quel génie ! Rosalind doit lui mener la vie dur, à ce petit. J'imagine qu'elle surveille tout, même le Jardin. Il a réussi à la dépasser... On a eu le droit de perquisitionner chez elle, mais elle s'était déjà enfuie. Mais où est-elle allée ? Et comment savait-elle qu'on allait chez elle ?{/i}\n\nExtrait du journal secret de Johann, Juillet 2015\n{i}Une première. je me suis fait viré. J'enrage, putain ! {b}Grace{/b} agissait étrangement depuis le début, et voilà que je me trouve écarté de l'enquête ? Ma théorie est bonne, pourtant. Elle satisfait la police, le Juge, et même les journalistes. Oui, car c'est devenu national. L'affaire dépasse tout le monde. Depuis Juin 2014, il y a eu 4 vagues de disparitions dues au {b}\"Hibou\"{/b}. De 8 à 10 personnes à chaque fois. Et ce, moins d'un an après le début de l'affaire {b}Klaus{/b}. Faut pas se moquer de moi. Les affaires du Hibou et de Klaus sont liées, indéniablement. Grace pense que Rosalind est le Hibou qui organise tout ça. Mais non. C'est une vengeance. La famille Liebert est puissante. Quelqu'un veut régler des comptes.{/i}"),

        "leonhard": _("Juge d'instruction chargé de l'affaire du {b}Hibou{/b}. Il aurait condamné une certaine {b}Stéphanie{/b} pour \"négligence menant à la disparition d'un de ses enfants\". Le reste du rapport est effacé.\n\nIl aurait aussi commis quelques bavures. Le Bourreau l'accuse de corruption par la famille d'{b}Alan{/b} pour innocenter ce dernier, mis en examen pour un trafic de drogue présumé."),

        "rosalind": _("Il y a très peu de références à Rosalind dans le livre du Bourreau HowToPunish, malgré l'importance qu'elle semble avoir dans l'affaire...\nPeut-être que le Bourreau lui donne un nom spécial ? Je pourrais chercher à la main et lisant tout le livre, mais je n'ai pas le luxe de m'accorder tout ce temps...\n\nRosalind apparaît par contre dans un rapport de Police. Elle aurait causé la mort de Klaus.\nPar Johann sur l'affaire du Hibou, juin 2015, page 2\n{i}Grace est incompétente, ou bien a d'autres idées en tête. Elle persiste à croire, ou à nous persuader, que Rosalind est le {b}Hibou{/b}, et a organisé ces vagues d'enlèvements. C'est faux. L'affaire {b}Klaus{/b} a en fait déclenché l'affaire du Hibou. Le Hibou est un vengeur de Klaus. Et c'est la personne avec qui il était le plus proche, logiquement. Mais {b}qui{/b} est-ce ?{/i}"),

        "erwin": _("Erwin a été trouvé dans un rapport de soins hospitaliers américains, pour blessures génitales. C'est vrai ? Il n'a pas l'air, vu sa carrure...\nEst-ce que ça a un lien avec sa voix métallique ?\n\nSon nom est mentionné dans un rapport du {b}Aktionsgruppe{/b}..."),

        "lise": _("Le nom de Lise est dans beaucoup de livres. C'est un prénom trop commun..."),

        "stephanie": _("Stéphanie Liebert est mentionnée dans un journal. Belle et heureuse, ayant deux enfants, c'est l'égérie et probablement la future héritière de la riche famille.\n\nToutefois, elle ne semble pas souhaiter prendre part aux activités de sa famille (ou le cache habilement).\n{i}\"Contrairement à ma soeur, j'ai des envies de beau, de propre, de frais. Ma famille est riche mais a mauvaise réputation. Je veux changer tout cela.\"{/i} déclare-t-elle dans une interview à un journal national populaire."),

        "sophie": _("Cataloguée dans le livre du Bourreau {b}HowToPunish{/b}, elle serait la fille de Stéphanie Liebert.\n\nExtrait de notes d'interrogatoire de la Police :\n{i}Par Johann, mai 2015. 3e interrogatoire.\nLa petite (si je peux appeler comme ça une ado qui ose me tenir tête depuis 30 minutes) n'a pas l'air trop attristée de la mort de son frère. Elle en veut à sa mère de ne pas l'avoir protégé. \"Maman est la plus charismatique, mais  la plus faible de la famille. Comme mon frère. Elle est pacifiste. Rosalind a pas hésité à la brusquer quand on a appris ce qu'était mon frère. La révélation a été une bombe. Ce qu'a fait Rosalind à mon frère est impardonnable. Je vais la ****.\" (j'ai un peu changé la forme du contenu, pour la bienséance){/i}"),

        "ukichiro": _("Il est évoqué un certain nombre de fois dans {b}HowToPunish{/b}. Le Bourreau a vraiment l'air de le détester... Il le surnomme \"Le {b}Casoar{/b}\". Qu'est-ce que cela peut bien être ?"),

        "planete": "Czarapata est avant 142857",

        "cxvl": _("Rechreche infurctuesue"),

        "klaus":_("Il y a beaucoup de références à Klaus, et presque uniquement dans {b}HowToPunish{/b}. Presque toutes réclament la vengeance ou parlent de destruction.\n\nKlaus est un sujet obsédant le Bourreau. Pas une phrase parlant de Klaus n'est écrite distinctement. Des traces de larmes sont parfois visible sur les pages.\n\nDes {b}colombes{/b} rouges sont souvent dessinées à côté de ce nom."),

        "hibou":_("Plusieurs livres parlent du \"Hibou\" : le livre du Bourreau ({i}HowToPunish{/i}),  et L'affaire du Hibou est encore floue. Il s'agit d'une série d'enlèvements de grande ampleur, comme jamais il n'y en a eu auparavant"), #TODO

        "rossignol":_("Le Rossignol ({i}Nightingale{/i} en anglais) est un oiseau de la famille des {i}Muscicapidae{/i}.\nIl est notamment réputé pour son chant mélodieux, et peut, par analogie, désigner une personne dont le chant est harmonieux.\n\nFait divers datant d'une dizaine d'années, en Angleterre :\nLe {i}Nightingale{/i} était le surnom d'un membre d'une organisation homophobe allemande, {b}Gesunder Menschenverstand (GM){/b}, qui sévissait dans les quartiers de Londres. Cet individu a réussi à émasculer une trentaine de victimes homosexuelles avant qu'on ne l'arrête. Ses victimes développèrent une voix soprano remarquable, qui rappelle le chant du rossignol."),

        "coalescence":_("Dans 4 milliards d'années, la galaxie d'Andromède va percuter notre galaxie, la Voie Lactée. Cet événement grandiose devrait aboutir à la fusion des deux galaxies en une nouvelle, plus colossale encore. Une géante elliptique, appelée Milkomeda.\n\nLes corps au sein des galaxies ne vont pas réellement se heurter. La plupart des étoiles et planètes vont simplement passer à des milliards de kilomètres les unes des autres. Sans dégâts directs, mais en modifiant potentiellement leurs trajectoires.\n\nCertains autres éléments vont connaître une destinée beaucoup plus gravissime, démesurée, fatale. Ce sont les trous noirs supermassifs au coeur des deux des galaxies. Ils vont s'attirer, lutter, puis fusionner dans un grand fracas cosmique silencieux. Détruisant tout à proximité.\n\nCet évènement a un nom : la Coalescence."),

        "ewen":_("Ici le développeur ! J'espère que le jeu vous plaît, n'hésitez pas à le noter sur Google Play et à me laisser des commentaires, encouragements ou rapports de bugs à amethystsstudio@gmail.com !"),

        "howtopunish":_("Le livre du Bourreau décrit tous les {i}Jeux{/i} qui se sont passés ici. Tous violents, le concept est toujours le même. Des individus se retrouvent coincés dans cette prison et doivent s'entre-tuer, jusqu'à qu'il n'en reste qu'un. Le cinquième Jeu a eu l'air particulièrement violent : personne ne s'en est sorti indemne. Les notes du Bourreau indiquent que tous les participants étaient des commerçants, des éboueurs ou des postiers. Sauf une femme, prénommée Grace. Étrange...\n\nLe livre contient beaucoup d'autres informations étranges. Il contient beaucoup de noms d'oiseaux : Hibou, Casoar, Rossignol, Colombe... Ils correspondent chacun à une personne, mais qui ?\n\nVoici un extrait intéressant:\n{i}Si je fais cela, c'est parce qu'{b}ils{/b} sont impurs. Le Rossignol aurait du être puni depuis longtemps. Le Casoar ne mérite pas une mort directe. Il se la donnera lui-même une fois confronté à l'Horreur.{/i}\n\nPlus loin, il est écrit:\n{i}... jeux n'étaient qu'une excuse pour attirer le Juge et son neveu. Les services secrets aussi. Ils m'appellent le Hibou, il paraît. Quoi qu'il en soit, je les {b}hais{/b} tous.{/i}\n(La suite est illisible)."),

        "grace":_("Une page du livre {i}HowToPunish{/i} est réservée à elle ! Elle serait une agent des services secrets qui {i}en savait trop{/i} sur le Bourreau...\nApparemment, elle serait proche d'un certain Ukichiro. \n\nJe lis : \"C'était un monstre. Klaus ne méritait pas ça. Je l'ai punie pendant mon cinquième Jeu, et tous les suivants. Elle est sage maintenant\". \n\nElle aurait été présente dans tous les jeux à partir du 5e ? Sauf celui là, donc ? Il va falloir que je creuse cette piste..."),

        "creature":_("Le mot Créature n'est écrit nulle part. Peut-être que le Bourreau l'appelle différemment ?"),

        "bourreau":_("Le mot {b}Bourreau{/b} est très peu écrit. Il est seulement présent au début du livre {b}HowToPunish{/b}, avec l'inscription suivante:\n{i}Je suis le Bourreau et voici mon Livre. J'y présente mon Jeu. Le but de ce Jeu est de punir les mauvais humains. Si vous lisez cela, vous êtes peut-être déjà mort. Je vous laisse lire les pages suivantes...{/i}"),

        "casoar":_("Le Casoar est l'oiseau le plus dangereux sur Terre. Ayant une griffe aussi grande que la tête d'un humain, il ressemble plus à un dinosaure qu'à un véritable oiseau.\n\nDe nombreux bouts de papiers déchirés sont regroupés. Certains ont une inscription {i}Confidentiel{/i} ou encore {i}Secret Défense{/i}. D'après ces documents, le Casoar serait également un meurtrier en série, recherché par Interpol et plusieurs services secrets. Discret, il est très peu connu du grand public : la minutie est sa marque de fabrique. Il aurait commis de nombreux vols (les enquêteurs ne sont pas totalement sûrs de l'auteur) et au moins 5 meurtres. Ces derniers sont tous décorrélés et ont eu lieu sur des continents différents. Les forces de l'ordre en ont conclut qu'il s'agissait un tueur à gages. Récemment, des soupçons pèsent sur une riche famille allemande, les {b}Liebert{/b}, avec laquelle le Casoar aurait eu des liens étroits de collaboration."),

        "hibou": _("Le {i}Hibou{/i} apparaît plusieurs fois parmi les livres de la salle : dans le livre du Bourreau (HowToPunish), et dans beaucoup de journaux de faits divers.\n\nL'affaire du Hibou est encore floue. Il s'agit d'une série d'enlèvements de grande ampleur, comme jamais il n'y en a eu auparavant. De temps en temps, des corps sont retrouvés.\n\nExtrait d'un journal local :\n{i}25 mars 2015\nLes enlèvements du Hibou continuent, avec la troisième série ! Quand est-ce que tout cela va finir ? Aujourd'hui, pendant une battue, des policiers ont trouvé le cadavre d'un garçon de 16 ans, qui serait mort depuis un an selon les analyses...{/i}\n\nExtrait d'un journal national:\n{i}2 septembre 2015\nLe Hibou a encore frappé ! La population en a plus qu'assez de ces enlèvements. La Police, scrutée désormais par le pays entier, est vivement critiquée, et son inefficacité pointée du doigt. Un changement de direction est attendu après la disparition inquiétante d'un membre des services secrets dont l'identité et le rôle ne nous a pas été révélé.{/i}"),

        "twitter": _("Le {i}Bourreau{/i} collectionne un nombre incroyable de Tweets. La plupart sont imprimés et glissés dans le dossier Kurt (mais qui {i}imprime{/i} des tweets ?).\n\nUn fil de discussion est particulièrement mis en valeur. Je me souviens encore de celui-là. Il s'agit d'un thread commençant par un meme homophobe que j'avais fait, montrant ma tête. Un utilisateur, @{b}KLosAngeles{/b}, avait cru se reconnaître sur la photo, un peu floue, et croyait que je me moquais de lui. Simple quiproquo au début, et je lui ai précisé que c'était bien moi-même sur la photo.\n\nMais il se trouve que {b}KLosAngeles{/b} était gay, ce qui n'arrangeait pas les choses, parce que ma blague était offensante pour lui de toute façon...  Cela m'a valu une bonne engueulade avec un certain @{b}EsperoGaja393{/b} qui défendait ce dernier. Heureusement, ça c'est bien terminé et personne ne se sentait blessé après quelques explications en MP. Bref, un quiproquo qui a dégénéré en débat sur le droit de rire de tout ou non, même si ça peut offenser certains.\n\nPourquoi le Bourreau a gardé ce fil de discussion en particulier ?"),

        "esperogaja393": _("Un utilisateur de Twitter figurant dans un de mes fils de discussion.\nEspero est proche du mot espoir dans beaucoup de langues\nGaja veut dire fille en portuguais et gay en espéranto. Il n'y a pas d'autres traces de ce mot."),

        "klosangeles": _("Utilisateur de Twitter.\nLa page de KLosAngeles a été imprimée par le Bourreau.\nIl s'appelle Klaus en réalité.\nSa dernière mise à jour date de Juin 2013, et il n'y a pas grand chose d'intéressant sur son profil.\n\nDes notes on été écrites à côté de sa tête.\n{i}Elle l'a confondu avec Kurt. Et il l'a guidée vers moi.{/i}\n\nDes souvenirs resurgissent dans ma mémoire. Une femme, jeune, qui me demande si je connais un Klaus. Je lui montre le tweet, en expliquant la méprise. Elle hoche de la tête, puis me demande mon identifiant Twitter. Et ceux des autres. Je lui dis. Je ne connais même pas son nom. Que s'est-il passé ensuite ? Je n'en ai pas de souvenir. Mais elle avait l'air satisfaite.\n\nC'est à cause de ça que je suis ici ? Juste pour avoir donné un renseignement insignifiant à une femme ?"),

        "shambhala": _("Signifie \"Lieu du bonheur paisible\" en sanskrit, selon un vieux dictionnaire de l'occulte. C'est un royaume fictif venu de la tradition bouddhiste tibétaine.\n\nLe livre HowToPunish comporte aussi beaucoup de références à Shambhala, considéré comme lieu idéal que le Bourreau veut recréer.\n\nExtrait:\n{i}Klaus n'est plus. C'est de la faute de ce monde peuplé de gens mauvais. Je vais recréer Shambala, en emmenant avec moi uniquement les gens bien. Kurt en fait peut-être partie, je vais le tester.{/i}"),

        "colombe": _("Le livre {b}HowToPunish{/b} est rempli de référence à la Colombe.\n\n{i}La Colombe de ma vie est morte. Bien que tombée en plein vol, elle renaîtra de ses cendres, tel un phénix. Elle mérite la paix éternelle qu'elle était censé apporter sur Terre. Pour la faire renaître, laissons-la s'embraser dans un dernier Enfer.\n\nMa Colombe m'apportera la Paix que je mérite.\nNous irons à Shambhala ensemble. Retrouver la tranquilité du début.{/i}"),

        "gesundermenschenverstand":_("Gesunder Menschenverstand est une organisation anti-gay d'origine allemande. Son but est de réprimer les comportements homosexuels, de façon violente (coups, meurtres, viols... et des rumeurs annoncent même pire !), mais aussi de façon plus pernicieuses (slogans, publicité, pressions via des lobbys, \"accompagnement des malades\"...).\n\nSes membres sont publics, exceptés les plus extrêmes. Le {b}Aktionsgruppe{/b}, branche la plus radicale, est dirigée par une femme dont le nom est inconnu. L'organisation vante d'ailleurs le grand nombre de femmes à ses rangs, et se positionne en faveur de l'égalité homme-femme."),

        "aktionsgruppe": _("Le {b}Aktionsgruppe{/b} est la branche la plus radicale de {b}Gesunder Menschenverstand (GM){/b}. Une liste de nom est griffonnée en bas de la photo du London Gazette duquel est extrait l'article. De loin, on aurait dit Emmy, ou Isaac s'il avait les cheveux longs."),

        "biboooup": "Je t'aime ♥",

        "liebert": _("La famille Liebert est une riche famille allemande, très conservatrice. Sa richesse vient d'un héritage conséquent d'un aïeul, mais les membres vivants de la famille n'ont pas de gros revenus déclarés. Des conflits internes auraient éclatés entre 2 sœurs de la famille, {b}Rosalind{/b} et {b}Stéphanie{/b}, en Juillet 2013, selon un paparazzi. Ce dernier a réalisé un reportage intitulé {i}LA FOLLE CHUTE DES LIEBERT{/i}, traçant l'histoire de la famille. Le \"reportage\" en question (si on pouvait qualifier par un tel mot ce type de journalisme de bas niveau) n'a d'ailleurs jamais été publié : seulement des traces et brouillons de celui-ci sont disponibles dans la salle d'archives.\n\nLes services secrets aussi ont enquêté sur cette famille aux activités pas toujours légales, malgré le penchant religieux conservateur de certains membres.\n\nComment le Bourreau a-t-il eu accès à tout ça ?")
        }
    $ archives_liste = archives_dic.keys()



    $ inventaire =     {"usb_key":          {"title": _("Clé USB"),
                                             "text" : _("Une clé USB ordinaire"),
                                             "text_inspect": _("Des lettres sont gravées sur la clé USB :\n\n {i}CXVL{/i}\n\nLorsque la clé avait été insérée dans la tablette, un dossier nommé {i}Hibou{/i} était ressorti du lot, étant beaucoup plus lourd que les autres."),
                                             "icon" : "images/icons/usb_key.png",
                                             "nb"   : 0, 
                                             "max"  : 1,
                                             "connu": False,
                                             "act_word": _("Inspecter")
                                             },
                        "battery":          {"title": _("Batterie"),
                                             "text" : _("À utiliser avec la lampe torche"),
                                             "icon" : "images/icons/flashlight.png",
                                             "nb"   : 0, 
                                             "max"  : 100,
                                             "connu": False,
                                             "act_word": _("Inspecter")
                                             },
                        "lampe":            {"title": _("Lampe torche"),
                                             "text" : _("Pour éclairer les coins sombres. \n\nElle marche à l'aide d'une batterie.\nLa mienne n'est pas très chargée mais elle fait l'affaire.\n\nLe compartiment batterie à l'air amovible."),
                                             "text_inspect": _("Dans le compartiment batterie est caché un papier, plié en deux.\nIl est griffonné : {i}N'oublie pas Ismaël{/i}"),
                                             "icon" : "images/icons/flashlight.png",
                                             "nb"   : 0,
                                             "max"  : 1,
                                             "connu": False,
                                             "act_word": _("Ouvrir")
                                             },
                        "knife":            {"title": _("Couteau"),
                                             "text" : _("Un petit couteau de cuisine \nbien aiguisé"),
                                             "text_inspect": _("La lumière vacillante ne permet pas de le remarquer tout de suite, mais le couteau est finement taillé."),
                                             "icon" : "images/icons/couteau.png",
                                             "nb"   : 0, 
                                             "max"  : 1,
                                             "connu": False,
                                             "act_word": _("Inspecter")
                                             },
                        "poison":           {"title": _("Fiole de Poison"),
                                             "text" : _("De la toxine botulique, un agent paralysant. L'effet est quasi immédiat et dure longtemps."),
                                             "text_inspect": _(""),
                                             "icon" : "",
                                             "nb"   : 0, 
                                             "max"  : 1,
                                             "connu": False,
                                             "used" : False,
                                             "act_word": _("Inspecter")
                                             },
                        "mp3":              {"title": _("Lecteur MP3"),
                                             "text" : _("Un lecteur MP3 vert, avec des écouteurs.\n\nIl a été fréquemment utilisé : de nombreuses traces d'usure témoignent d'un usage intensif. L'écran luit encore d'un halo bleuté.\n\nIl marche peut-être encore."),
                                             "text_inspect": _("Le MP3 indique le titre suivant:\n\n\n   {i}King xf the D34D{/i}"),
                                             "icon" : "images/icons/usb_key.png",
                                             "nb"   : 0, 
                                             "max"  : 1,
                                             "connu": False,
                                             "act_word": _("Écouter")
                                             },
                        }
    $ kurt =        { "nom"      : "Kurt",
                      "char"     : p,
                      "color"    : "#ff0000",
                      "age"      : 19,
                      "image"    : "persos/kurt.png",
                      "statut"   : "Vivant", 
                      "confiance": 10,
                      "arme"     : True,
                      "adjectifs": _("Peu sociable - Nerd"),
                      "situation": _("Étudiant"),
                      "bio" : [[True, _("Je gère un compte Twitter d'humour noir parfois qualifié de raciste, antisémite et sexiste, mais je ne me considère pas comme tel. Je publie surtout des memes pour faire rire mes amis...")],
                              [False, _("Crime : Ne sais pas. Peut-être mon humour politiquement incorrect ?")]
                      ]
                    }
    $ isaac =       { "nom"      : "Isaac",
                      "char"     : isa,
                      "color"    : "#5ba7ff",
                      "age"      : 18  ,
                      "image"    : "persos/isaac.png",
                      "statut"   : "Inconnu", 
                      "confiance": 8,
                      "arme"     : True,
                      "adjectifs": _("Peureux - Vif d'esprit - Fragile"),
                      "situation": _("Étudiant"),
                      "bio" :  [[False, _("Timide et effacé, il est plutôt petit et fébrile. Il a l'air intelligent tout de même")],
                                [False, _("Crime : Se prétend innocent")],
                                [False, _("De nature réservée, il tient à sortir du Jeu coûte que coûte, quitte à se sacrifier pour les autres.")],
                                [False, _("Il a dit vouloir se suicider...")],
                                [False, _("Pendant son tour de garde de la première nuit,il a été assommé par la créature.")],
                                [False, _("Il aime faire la cuisine. Enfin, dans la mesure du possible vu les conditions...")],
                      ]
                    } 
    
    $ leonhard =    { "nom"      : "Leonhard",
                      "char"     : l,
                      "color"    : "#008c3b",
                      "age"      : 53 ,
                      "image"    : "persos/leonhard.png",
                      "statut"   : "Inconnu",
                      "confiance": 8,
                      "arme"     : True,
                      "adjectifs": _("Intelligent - Calme"),
                      "situation": _("Juge"),
                      "bio"      : [[False, _("Il semble en savoir beaucoup sur l'affaire, du moins plus qu'il n'en dit.")],
                              [False, _("Crime : Aurait été corrompu dans une affaire impliquant Alan...")],
                              [False, _("Arme : Utilise la plume en acier de ses lunettes")],
                              [False, _("Il a tué Emmy avec son arme, tordant sa plume. Elle ne semble plus utilisable comme arme.")],

                      ]
                    }
    $ johann =      { "nom"      : "Johann",
                      "char"     : j,
                      "color"    : "#ff7700",
                      "age"      : 24,
                      "image"    : "persos/johann.png",
                      "statut"   : "Inconnu", 
                      "confiance": 8,
                      "arme"     : True,
                      "adjectifs": _("Intelligent - Nerveux - Prétentieux"),
                      "situation": _("Étudiant"),
                      "bio" :  [[False, _("Intellectuel. Il a le tic de remettre ses lunettes de sa main droite, comme si elles étaient trop lourdes pour lui.")],
                                [False, _("Crime : Aurait triché à l'examen d’entrée de son école.")],
                                [False, _("Il s'acharne à chercher la solution pour se sortir du jeu vivant, en jouant avec les Règles du Bourreau.")],
                                [False, _("Arme : Il cachait une lame effilée dans ses lunettes.")],
                                [False, _("Il a tué Emmy avec. Elle a l'air de s'être brisée pendant l'action.")],
                      ]
                    }

    $ alan =        { "nom"      : "Alan",
                      "char"     : ala,
                      "color"    : "#9400ce",
                      "age"      : 19,
                      "image"    : "persos/alan.png",
                      "statut"   : "Inconnu", 
                      "confiance": 8,
                      "arme"     : True,
                      "adjectifs": _("Teigneux - Bagarreur"),
                      "situation": _("Étudiant"),
                      "bio" : [[False, _("Alan est un petit caïd local, irrespectueux et vantard. Puissant physiquement, il peut faire un bon allié.")],
                              [False, _("Crime : Violences en tout genre, trafic de drogues... C'est le plus violent du groupe.")],
                              [False, _("Le Bourreau a confirmé ce qu'il avait annoncé. Il a été honnête.")],
                      ]
                    }
    $ emmy =        { "nom"      : "Emmy",
                      "char"     : e,
                      "color"    : "#ffd",
                      "age"      : 15  ,
                      "image"    : "persos/emmy.png",
                      "statut"   : "Inconnue", 
                      "confiance": 8,
                      "arme"     : True,
                      "adjectifs": _("Timide - Altruiste"),
                      "situation": _("Lycéenne"),
                      "bio"      : [[False, _("Chrétienne. Elle était dans le même collège qu'Isaac mais ne semble pas le connaître plus que ça.")],
                              [False, _("Crime : Se prétend innocente.")],
                              [False, _("Crime (prétendu) : Innocente.")],
                              [False, _("Crime (annoncé par le Bourreau) : A tué ses parents adoptifs")],
                              [False, _("Arme : Cachait une dague dans son soutien-gorge.")],
                      ]
                    }
    $ ukichiro =    { "nom"      : "Ukichiro",
                      "char"     : None,
                      "color"    : "#a0a0a0",
                      "age"      : 32 ,
                      "image"    : "persos/unknown.png",
                      "statut"   : "Inconnu",
                      "confiance": 10,
                      "arme"     : True,
                      "adjectifs": "",
                      "situation": "",
                      "crime"    : "Inconnu",
                      "bio"      : [[False, _("Ukichiro était l'un des participant au Jeu, dans l'aile droite.")],
                                    [False, _("Sa copine a été transformée en cette Créature tueuse et immonde...")]
                      ]
                    }
    $ rosalind =    { "nom"      : "Rosalind",
                      "char"     : r,
                      "color"    : "#ff75de",
                      "age"      : 63 ,
                      "image"    : "persos/rosalind.png",
                      "statut"   : "Inconnue",
                      "confiance": 8,
                      "arme"     : True,
                      "adjectifs": _("Handicapée - Instable"),
                      "situation": _("Retraitée"),
                      "bio"      : [[False, _("Aveugle et manchot, elle dit avoir joué aux trois premiers jeux. Elle ne veut rien dire de plus.")],
                                    [False, _("Malgré le fait qu'elle ait survécu à 3 Jeux, elle ne veut pas partager son expérience. Étrange...")],
                                    [False, _("Elle n'arrête pas de me confondre avec ce 'Klaus'. Ce serait à cause de lui que nous sommes enfermés ici.")],
                      ]
                    }
    
    $ stephanie =   { "nom"      : "Stéphanie",
                      "char"     : None,
                      "color"    : "#a0a0a0",
                      "age"      : 42,
                      "image"    : "persos/unknown.png",
                      "statut"   : "Inconnue",
                      "confiance": 10,
                      "arme"     : True,
                      "adjectifs": _(""),
                      "situation": _(""),
                      "crime"    : "Inconnu",
                      "bio"      : [[False, _("")],
                              [False, _("")]
                      ]
                    }
    $ sophie =      { "nom"      : "Sophie",
                      "char"     : None,
                      "color"    : "#a0a0a0",
                      "age"      : 15 ,
                      "image"    : "persos/unknown.png",
                      "statut"   : "Inconnue",
                      "confiance": 10,
                      "arme"     : True,
                      "adjectifs": "",
                      "situation": "",
                      "crime"    : "Inconnu",
                      "bio"      : [[False, _("")],
                              [False, _("")]
                      ]
                    }
    
    $ erwin =       { "nom"      : "Erwin",
                      "char"     : erw,
                      "color"    : "#efd100",
                      "age"      : 35 ,
                      "image"    : "persos/erwin.png",
                      "statut"   : "Inconnu",
                      "confiance": 8,
                      "arme"     : True,
                      "adjectifs": _("Froid - Dur"),
                      "situation": _("Chimiste"),
                      "bio"      : [[False, _("Extrêmement froid, il a un caractère totalement différent de celui de sa femme, Lise. Physiquement, c'est une armoire à glace : il frappe sûrement plus fort qu'Alan... Un physique singulier pour un chimiste. Sa voix est étrangement grave et métallique.")],
                              [False, _("Crime : Il annonce avoir tué involontairement une dizaine de personnes suite à une expérience qui aurait mal tournée avec sa femme...")],
                              [False, _("Archives : il aurait eu un problème d'ordre génital...")],
                      ]
                    }
    $ lise =        { "nom"      : "Lise",
                      "char"     : li,
                      "color"    : "#4848ea",
                      "age"      : 32 ,
                      "image"    : "persos/lise.png",
                      "statut"   : "Inconnue",
                      "confiance": 8,
                      "arme"     : True,
                      "adjectifs": _("Chaleureuse - Joyeuse"),
                      "situation": _("Chimiste"),
                      "crime"    : _("A intoxiqué et tué tout un village"),
                      "bio"      : [[False, _("Vraiment chaleureuse, elle a un caractère totalement différent de celui de son mari, Erwin. Est-ce seulement une façade ?")],
                              [False, _("Crime : Elle annonce avoir tué involontairement une dizaine de personnes suite à une expérience qui aurait mal tournée avec son mari...")],
                      ]
                    }
    
    $ bourreau =    { "nom"      : "Bourreau",
                      "char"     : b,
                      "color"    : "#a0a0a0",
                      "age"      : 0 ,
                      "image"    : "persos/bourreau.png",
                      "statut"   : "Inconnu",
                      "confiance": 10,
                      "arme"     : True,
                      "adjectifs": "",
                      "situation": "",
                      "crime"    : "Inconnu",
                      "bio"      : [[False, _("Un fou furieux qui nous a enfermés ici pour nous faire nous entretuer.")],
                              [False, _("")]
                      ]
                    }
    $ creature =    { "nom"      : "Creature",
                      "char"     : b,
                      "color"    : "#a0a0a0",
                      "age"      : 0 ,
                      "image"    : "persos/creature.png",
                      "statut"   : "Inconnu",
                      "confiance": 10,
                      "arme"     : True,
                      "adjectifs": "",
                      "situation": "",
                      "crime"    : "Inconnu",
                      "bio"      : [[False, _("")],
                              [False, _("")]
                      ]
                    }

    $ klaus =       { "nom"      : "Klaus",
                      "char"     : None,
                      "color"    : "#a0a0a0",
                      "age"      : 0 ,
                      "image"    : "persos/unknown.png",
                      "statut"   : "Inconnu",
                      "confiance": 10,
                      "arme"     : True,
                      "adjectifs": "",
                      "situation": "",
                      "crime"    : "Inconnu",
                      "bio"      : [[False, _("")],
                              [False, _("")]
                      ]
                    }
    $ grace =       { "nom"      : "Grace",
                      "char"     : None,
                      "color"    : "#a0a0a0",
                      "age"      : 0 ,
                      "image"    : "persos/unknown.png",
                      "statut"   : "Inconnu",
                      "confiance": 10,
                      "arme"     : True,
                      "adjectifs": "",
                      "situation": "",
                      "crime"    : "Inconnu",
                      "bio"      : [[False, _("")],
                              [False, _("")]
                      ]
                    }

    $ rossignol =   { "nom"      : "Rossignol",
                      "char"     : None,
                      "color"    : "#a0a0a0",
                      "age"      : 0 ,
                      "image"    : "persos/unknown.png",
                      "statut"   : "Inconnu",
                      "confiance": 10,
                      "arme"     : True,
                      "adjectifs": "",
                      "situation": "",
                      "crime"    : "Inconnu",
                      "bio"      : [[False, _("")],
                              [False, _("")]
                      ]
                    }
    $ hibou =       { "nom"      : "Hibou",
                      "char"     : None,
                      "color"    : "#a0a0a0",
                      "age"      : 0 ,
                      "image"    : "persos/unknown.png",
                      "statut"   : "Inconnu",
                      "confiance": 10,
                      "arme"     : True,
                      "adjectifs": "",
                      "situation": "",
                      "crime"    : "Inconnu",
                      "bio"      : [[False, _("")],
                              [False, _("")]
                      ]
                    }
    $ casoar =      { "nom"      : "Casoar",
                      "char"     : None,
                      "color"    : "#a0a0a0",
                      "age"      : 0 ,
                      "image"    : "persos/unknown.png",
                      "statut"   : "Inconnu",
                      "confiance": 10,
                      "arme"     : True,
                      "adjectifs": "",
                      "situation": "",
                      "crime"    : "Inconnu",
                      "bio"      : [[False, _("")],
                              [False, _("")]
                      ]
                    }
    $ outsider =    { "nom"      : "Outsider",
                      "char"     : None,
                      "color"    : "#a0a0a0",
                      "age"      : 0 ,
                      "image"    : "persos/unknown.png",
                      "statut"   : "Inconnu",
                      "confiance": 10,
                      "arme"     : True,
                      "adjectifs": "",
                      "situation": "",
                      "crime"    : "Inconnu",
                      "bio"      : [[False, _("")],
                              [False, _("")]
                      ]
                    }

    $ montrer_conf = "implicite" # explicite, implicite, desactivé
    $ liste_persos = [kurt, isaac, leonhard, johann, alan, emmy, ukichiro, rosalind, sophie, stephanie, erwin, lise, bourreau, creature, klaus, grace, hibou, rossignol, casoar, outsider]
    $ persos_joueurs = [kurt, isaac, leonhard, johann, alan, emmy, ukichiro, rosalind, sophie, stephanie, erwin, lise]
    $ persos_non_joueurs = [bourreau, creature, klaus, grace, hibou, rossignol, casoar, outsider]

    $ perso = klaus
    
    $ liste_events = [{"id": -1, "actif": False, "jour":0, "heure" : "00:00", "details" : "CXVL"
    },{
    "id": 101, "actif": False, "jour":1, "heure" : "10:30",
        "details" : _("Je me suis réveillé entouré de 5 inconnus. On est prisonniers d'un malade qui s'appelle le {i}Bourreau{/i}.")
    },{
    "id": 102, "actif": False, "jour":1, "heure" : "10:35",
        "details" : _("Tout le monde ici serait un criminel. Le Bourreau voudrait rendre justice ? Il mentionne pourtant un innocent...")
    },{
    "id": 103, "actif": False, "jour":1, "heure" : "11:24",
        "details" : _("On est retenus dans une sorte de prison. Le Bourreau veut qu'on vote pour s'entre-tuer...")
    },{
    "id": 204, "actif": False, "jour":1, "heure" : "11:42",
        "details" : _("On a débattu avant de voter pour savoir qui éliminer. C'est fou...")
    },{
    "id": 205, "actif": False, "jour":1, "heure" : "12:17",
        "details" : _("Premier vote. Emmy a été élue. Si il y avait eu égalité, il aurait fallu que les élus s'entre-tuent.")
    },{
    "id": 206, "actif": False, "jour":1, "heure" : "12:17",
        "details" : _("Premier vote. Alan a été élu. Si il y avait eu égalité, il aurait fallu que les élus s'entre-tuent.")
    },{
    "id": 207, "actif": False, "jour":1, "heure" : "12:17",
        "details" : _("Premier vote. Il y a eu égalité entre Alan et Emmy. Ils doivent s'entre-tuer.")
    },{
    "id": 208, "actif": False, "jour":1, "heure" : "12:17",
        "details" : _("Premier vote. Il y a eu égalité entre Alan, Isaac et Emmy. Ils doivent s'entre-tuer.")
    },{
    "id": 209, "actif": False, "jour":1, "heure" : "12:48",
        "details" : _("Alan a tué Emmy.")
    },{
    "id": 210, "actif": False, "jour":1, "heure" : "19:00",
        "details" : _("J'ai pu visiter les lieux. Il y a beaucoup de choses à voir...")
    },{
    "id": 211, "actif": False, "jour":1, "heure" : "21:00",
        "details" : _("Nous avons décidé de monter la garde tour à tour, afin de nous protéger et d'éventuellement trouver des indices")
    },{
    "id": 212, "actif": False, "jour":2, "heure" : "07:23",
        "details" : _("Une créature étrange, de métal et de chair, est venue à la fin de la nuit.")
    },{
    "id": 213, "actif": False, "jour":2, "heure" : "07:48",
        "details" : _("Emmy a été tuée.")
    },{
    "id": 214, "actif": False, "jour":2, "heure" : "07:48",
        "details" : _("Alan a été tué.")
    },{
    "id": 215, "actif": False, "jour":2, "heure" : "07:59",
        "details" : _("Isaac a vu la créature. Il affirme qu'elle est faite de chair et de métal... Terrifiant !")
    },{
    "id": 216, "actif": False, "jour":2, "heure" : "09:07",
        "details" : _("Le Bourreau a annoncé être 'parmi nous'... Mais qui est-ce ?")
    },{
    "id": 317, "actif": False, "jour":2, "heure" : "11:12",
        "details" : _("Lors de la visite de la Salle des Archives, Johann a surpris tout le monde en clamant être le Bourreau, ce qui  était faux au final.")
    },{
    "id": 318, "actif": False, "jour":2, "heure" : "12:38",
        "details" : _("2e Vote. Alan a été élu.")
    },{
    "id": 319, "actif": False, "jour":2, "heure" : "12:38",
        "details" : _("2e Vote. Alan et moi avons été élus. Nous allons nous battre.")
    },{
    "id": 320, "actif": False, "jour":2, "heure" : "12:38",
        "details" : _("J'ai réussi à tuer Alan, au prix de quelques cotes...")
    },{
    "id": 321, "actif": False, "jour":2, "heure" : "12:38",
        "details" : _("Isaac a tué Alan à  ma place.")
    },{
    "id": 322, "actif": False, "jour":2, "heure" : "12:38",
        "details" : _("2e Vote. J'ai été élu. Le Bourreau va me tuer.")
    },{
    "id": 323, "actif": False, "jour":2, "heure" : "12:38",
        "details" : _("2e Vote. Emmy a été élue.")
    },{
    "id": 324, "actif": False, "jour":2, "heure" : "12:38",
        "details" : _("2e Vote. Emmy et Johann ont été élus. Ils vont devoir se battre.")
    },{
    "id": 325, "actif": False, "jour":2, "heure" : "12:38",
        "details" : _("Johann a tué Emmy, avec une lame qu'il cachait dans ses lunettes.")
    },{
    "id": 326, "actif": False, "jour":2, "heure" : "12:38",
        "details" : _("2e Vote. Emmy et Leonhard ont été élus. Ils vont devoir se battre.")
    },{
    "id": 327, "actif": False, "jour":2, "heure" : "12:38",
        "details" : _("Leonhard a tué Emmy, avec un stylo-plume en acier.")
    },{
    "id": 328, "actif": False, "jour":2, "heure" : "16:21",
        "details" : _("J'ai visité les archives. L'{b}Index{/b} m'a redirigé vers plusieurs livres et dossiers utiles. J'y ai obtenu quelques renseignements qui me sont encore flous. Il y a quelque chose à creuser par là.")
    },{
    "id": 329, "actif": False, "jour":2, "heure" : "22:09",
        "details" : _("Pour la 2e nuit, nous avons décidé d'adopter la stratégie d'Isaac et de nous enfermer à double tour, et en poussant les lits devant la porte, au cas où le Bourreau aurait accès aux clés.")
    },{
    "id": 330, "actif": False, "jour":3, "heure" : "01:02",
        "details" : _("La nuit est une torture. Je ne peux pas dormir, malgré tous mes efforts.")
    },{
    "id": 331, "actif": False, "jour":3, "heure" : "08:42",
        "details" : _("La Créature est revenue. Isaac était dans le couloir, cette nuit. Il a l'air d'avoir vu quelque chose qui le choquait.")
    },{
    "id": 332, "actif": False, "jour":3, "heure" : "09:06",
        "details" : _("La Créature a tué Alan cette nuit.")
    },{
    "id": 333, "actif": False, "jour":3, "heure" : "09:06",
        "details" : _("La Créature a tué Emmy cette nuit.")
    },{
    "id": 334, "actif": False, "jour":3, "heure" : "09:45",
        "details" : _("Je ne sais pas trop ce qui s'est passé cette nuit. Quoi qu'il en soit, Isaac s'est suicidé, ou a été tué. Les circonstances sont floues... La Créature a laissé un étrange puzzle fait à partir des cadavres des 3 premières victimes. C'est répugnant.")
    },{
    "id": 335, "actif": False, "jour":3, "heure" : "10:00",
        "details" : _("Il reste 3 survivants. Normalement, c'est fini, mais le Bourreau a annoncé que ce n'était que le début... Ne tient-il pas sa parole ?")
    },{
    "id": 436, "actif": False, "jour":3, "heure" : "10:21",
        "details" : _("La porte s'est ouverte, révélant une grande pièce vide, et 3 nouveaux participants... Il va falloir essayer de survivre à nouveau ? Quand cela va-t-il s'arrêter ?")
    },{
    "id": 437, "actif": False, "jour":3, "heure" : "10:35",
        "details" : _("Le Bourreau a fait une annonce importante. Il veut changer les Règles. Il faut maintenant voter pour celui qui va endosser le rôle de Bourreau.")
    },{
    "id": 438, "actif": False, "jour":3, "heure" : "10:48",
        "details" : _("Les personnes de l'aile droite ont déjà participé aux précédents Jeux...")
    },{
    "id": 439, "actif": False, "jour":3, "heure" : "10:52",
        "details" : _("Erwin annonce que la Créature est scellée de leur côté de la prison, dans la Salle de Torture.")
    },{
    "id": 440, "actif": False, "jour":3, "heure" : "10:35",
        "details" : _("3e Vote. Tout le monde a voté contre Rosalind... ? Il y a eu un problème.")
    },{
    "id": 541, "actif": False, "jour":3, "heure" : "10:35",
        "details" : _("Rosalind est morte, emportant de nombreux secrets dans sa tombe...")
    


    }]

    jump acte1

init python:
    if not persistent.achievements_dict: #and not config.developer
        persistent.achievements_dict = {
            "premier_choix":    {"type": 0,
                                    "title": _("Décisif !"),
                                    "text": _("Faites votre premier choix"),
                                    "val" : "Facile",
                                    "icon": "images/icons/achievement_bronze.png", # 96x96 image
                                    "obtenu" : False
                                    },
            "decouvre_carte":   {"type": 0, 
                                    "title": _("Explorateur"),
                                    "text": _("Découvrez où vous êtes enfermés"),
                                    "val" : "Facile",
                                    "icon": "images/icons/achievement_bronze.png",
                                    "obtenu" : False
                                    },
            "premier_vote":     {"type": 0, 
                                    "title": _("Juge"),
                                    "text": _("Votez pour la première fois"), 
                                    "val" : "Facile",
                                    "icon": "images/icons/achievement_bronze.png",
                                    "obtenu" : False
                                    },
            "fin_acte6":        {"type": 0, 
                                    "title": _("Survivant"),
                                    "text": _("Sortez vivants du Jeu. Peu importe comment."), 
                                    "val" : "Moyen",
                                    "icon": "images/icons/achievement_argent.png",
                                    "obtenu" : False
                                    },
            "bibliothequaire":  {"type": 0, 
                                    "title": _("Rat de Bibliothèque"),
                                    "text": _("Trouvez quelque chose d'intéressant."), 
                                    "val" : "Moyen",
                                    "icon": "images/icons/achievement_argent.png",
                                    "obtenu" : False
                                    },                     
            "suicidaire":       {"type": 0, 
                                    "title": _("Inconscient"),
                                    "text": _("Votez contre vous-même"), 
                                    "val" : "Facile",
                                    "icon": "images/icons/achievement_bronze.png",
                                    "obtenu" : False
                                    },
            "meurtrier":         {"type": 0, 
                                    "title": _("Meurtrier"),
                                    "text": _("Tuez quelqu'un"), 
                                    "val" : "Moyen",
                                    "icon": "images/icons/achievement_argent.png",
                                    "obtenu" : False
                                    },
            "premiere_mort":    {"type": 0, 
                                    "title": _("Victime"),
                                    "text": _("Mourrez... Une première fois."), 
                                    "val" : "Facile",
                                    "icon": "images/icons/achievement_bronze.png",
                                    "obtenu" : False
                                    },
            "meilleurs_amis":   {"type": 0, 
                                    "title": _("À la vie, à la mort !"),
                                    "text": _("Faites-vous un allié digne de confiance"), 
                                    "val" : "Moyen",
                                    "icon": "images/icons/achievement_argent.png",
                                    "obtenu" : False
                                    },
            "detective":        {"type": 0, 
                                    "title": _("Détective"),
                                    "text": _("Trouvez qui est le Bourreau"), 
                                    "val" : "Difficile",
                                    "icon": "images/icons/achievement_or.png",
                                    "obtenu" : False
                                    },
            "ange":             {"type": 0, 
                                    "title": _("Ange"),
                                    "text": _("Ne soyez impliqués dans aucun meurtre"), 
                                    "val" : "Moyen",
                                    "icon": "images/icons/achievement_or.png",
                                    "obtenu" : False
                                    },
            "demon":            {"type": 0, 
                                    "title": _("Démon"),
                                    "text": _("Soyez impliqués dans chacun des meurtres"), 
                                    "val" : "Difficile",
                                    "icon": "images/icons/achievement_or.png",
                                    "obtenu" : False
                                    },
            "satan":           {"type": 0, 
                                    "title": _("Satan"),
                                    "text": _("Tuez tout le monde"), 
                                    "val" : "Difficile",
                                    "icon": "images/icons/achievement_diamand.png",
                                    "obtenu" : False
                                    },
            "cxvl":             {"type": 0, 
                                    "title": _("CXVL"),
                                    "text": _("Découvrez la Vérité"), 
                                    "val" : "Ultime",
                                    "icon": "images/icons/achievement_diamand.png",
                                    "obtenu" : False
                                    },                     
    #        "piles_rest":       {"type": 1, # Progress achievent
    #                             "title": "Piles",
    #                             "text": "utilisées",
    #                             "icon": "images/icons/achievement1.png",
    #                             "cur_prog": 0, # current progress 
    #                             "max_prog": 4# maximal progress
    #                             }
            }
                                        

        for i, a in persistent.achievements_dict.items():
            if a['type'] == 0:
                achievement.register(i, steam=a['title'])
            if a['type'] == 1:
                achievement.register(i, steam=a['title'], stat_max=a['max_prog'])

