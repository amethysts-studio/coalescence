init python:
    noisedissolve = ImageDissolve(im.Tile("Transitions/noisetile.png"), 0.5, 1)
    inkdissolve = ImageDissolve(im.Tile("Transitions/inktile.jpg"), 2.0, 1)
    speedinkdissolve = ImageDissolve(im.Tile("Transitions/inktile.jpg"), 1.0, 8)
    updissolve = ImageDissolve(im.Tile("Transitions/uptile.png"), 2.0, 64)
    griffesdissolve = ImageDissolve(im.Tile("Transitions/griffes.png"), 1.0, 32)
    tpdissolve = ImageDissolve(im.Tile("Transitions/teleport.png"), 2.0, 64)

#init 2 python:
#    def save_playtime(d):
#        renpy.store.playtime += renpy.get_game_runtime()
#        renpy.clear_game_runtime()
#        d["playtime"] = renpy.store.playtime
#    config.save_json_callbacks = [save_playtime]

    if config.developer:
        preferences.skip_unseen = True

    def encode(): #Send useful info to the dev
        message = "-"
        for i in range(1, 9): #Morts
            if persistent.fins[str(i)][1]:
                message += "1"
            else:
                message += "0"
        message += "\n+"
        for i in range(9): #Fins
            if persistent.fins[str(i)][1]:
                message += "1"
            else:
                message += "0"
        

    def annonce_importante(qui, quoi, unknown=False):
        #unknown is when discovering the character for the first time. It displays the illustration
        name = "???" if unknown else qui["nom"]
        if unknown:
            nvl_clear()
            renpy.show(qui["nom"].lower()+"_portrait", at_list=[smooth(time=1.0, alpha_max=0.5)])
        if not renpy.is_skipping():
            renpy.show_screen(_screen_name= 'message_important', name = name, color = qui["color"], important_sentence = quoi, unknown = unknown)
        if unknown:
            renpy.pause(2.0, hard=True)
            renpy.pause(4.0)
            renpy.hide(qui["nom"].lower()+"_portrait")
        else:
            renpy.say(qui["char"], quoi)

    def ajoute_instabilite(balance):
        if persistent.instabilite == None:
            persistent.instabilite = balance
        else:
            persistent.instabilite += balance
        if balance < 0:
            renpy.call(label = "message_continue")
        elif balance >= 1:
            renpy.call(label = "message_stop")

    def etape_suivante_ordi():
        if persistent.etape == None:
            persistent.etape = 1
        else:
            persistent.etape += 1

    def nouvelle_simulation():
        if persistent.jeu_actuel == None:
            persistent.jeu_actuel = 1
        else:
            persistent.jeu_actuel += 1

    def romain(n):
        if n ==0:
            return ""
        elif n < 4:
            return "I"+romain(n-1)
        elif n == 4:
            return "IV"
        elif n < 9:
            return "V"+romain(n-5)
        elif n == 9:
            return "IX"
        elif n < 40:
            return "X"+romain(n-10)
        elif n < 50:
            return "XL"+romain(n-40)
        elif n < 90:
            return "L"+romain(n-50)
        else:
            return "XXXXX"

    def majuscule_au_debut(s): #il faut un string s uniformisé
        if len(s) > 0:
            return chr(ord(s[0])-32)+s[1:]
        else:
            return "_"

    def uniformise(string):
        new_string = ""
        for lettre in string:
            code = ord(lettre)
            if 65 <= code <= 90:
                new_string += chr(code+32)
            elif 97 <= code <= 122:
                new_string += lettre
            elif lettre == "é" or lettre == "è" or lettre == "É" or lettre == "È" or lettre == "ê" or lettre == "Ê":
                new_string += "e"
        return new_string

    def distance_edition(mot1, mot2):
        dist = { (-1,-1): 0 }
        for i,c in enumerate(mot1) :
            dist[i,-1] = dist[i-1,-1] + 1
            dist[-1,i] = dist[-1,i-1] + 1
            for j,d in enumerate(mot2) :
                opt = [ ]
                if (i-1,j) in dist : 
                    x = dist[i-1,j] + 1
                    opt.append(x)
                if (i,j-1) in dist : 
                    x = dist[i,j-1] + 1
                    opt.append(x)
                if (i-1,j-1) in dist :
                    x = dist[i-1,j-1] + (1 if c != d else 0)
                    opt.append(x)
                dist[i,j] = min(opt)
        return dist[len(mot1)-1,len(mot2)-1]

    def recherche_flex(mot, liste):
        if len(mot) == 2:
            if mot == "gm":
                return "gm"
            else:
                return "none"
        else:
            #retrourne le mot de la liste le plus proche si sa distance < 3
            bon_mot = "none"
            for i in range(3): # 0, 1, 2
                for mot_test in liste:
                    if distance_edition(mot, mot_test) < 3-i:
                        bon_mot = mot_test
            return bon_mot #si aucun trouvé, renvoie le message d'erreur par défaut du dico

    def str_to_perso(liste_persos, chaine):
        for test in liste_persos:
            if test["nom"].lower() == chaine:
                return test

    def resultat_vote(dico):
        max_votes = 0
        for i in dico:
            if dico[i] > max_votes:
                max_votes = dico[i]
        liste_elus = []
        for i in dico:
            if dico[i] == max_votes:
                liste_elus.append(i)
        liste_elus.sort()
        return liste_elus

    #liste_events = [] # Will be defined at the beginning of every game, but must be there bc of the python syntax shit
    def modif_resume(evt, notify = True, set_value=True):
        n = len(liste_events) # Scope of liste_events not defined (access possible only in game, after init)
        for i in range(1, n):
            if liste_events[i]["id"] == evt:
                liste_events[i]["actif"] = set_value
                if notify:
                    renpy.notify(_("Journal mis à jour"))
                break
                    
    def modif_bio(perso, bio_id, notify=True, set_value=True):
        perso["bio"][bio_id][0] = set_value
        if notify:
            renpy.notify(_("Dossier {i}")+perso["nom"]+_("{/i} mis à jour"))

    def modif_confiance(liste_persos, liste_balance, display=True):
        for perso, balance in zip(liste_persos, liste_balance):
            if perso["statut"][:6] == "Vivant":
                perso["confiance"] += balance
                nom = perso["nom"]
                persistent.confiance[nom][0] = max(0, min(perso["confiance"], persistent.confiance[nom][0]))
                persistent.confiance[nom][1] = min(20, max(perso["confiance"], persistent.confiance[nom][1]))
                if not achievement.has("meilleurs_amis"):
                    if perso["confiance"] > 17:
                        get_achievement("meilleurs_amis")
            
        if display and not renpy.is_skipping():
            renpy.show_screen(_screen_name='scr_conf_update', liste_persos = liste_persos, liste_modif = liste_balance)

    def get_qualificatif(i, string):
        if i < 0:
            return _("Inconnu")
        if string == "explicite":
            return str(i)
        elif string == "implicite":
            if i <= 1:
                return _("Ennemi")
            elif i <=7:
                return _("Méfiant")
            elif i <=12:
                return _("Neutre")
            elif i <=18:
                return _("Confiant")
            else:
                return _("Allié")
        else:
            return "???"

    def is_daylight():
        hour = int(str(datetime.datetime.now().time())[:2])
        return (8 <= hour and hour <= 19)

    def distance_edition(mot1, mot2):
        dist = { (-1,-1): 0 }
        for i,c in enumerate(mot1) :
            dist[i,-1] = dist[i-1,-1] + 1
            dist[-1,i] = dist[-1,i-1] + 1
            for j,d in enumerate(mot2) :
                opt = [ ]
                if (i-1,j) in dist : 
                    x = dist[i-1,j] + 1
                    opt.append(x)
                if (i,j-1) in dist : 
                    x = dist[i,j-1] + 1
                    opt.append(x)
                if (i-1,j-1) in dist :
                    x = dist[i-1,j-1] + (1 if c != d else 0)
                    opt.append(x)
                dist[i,j] = min(opt)
        return dist[len(mot1)-1,len(mot2)-1]

    def sauvegarder(partie_a_sauvegarder, montrer = True):
        for cle in persistent.sauvegarde_info:
            persistent.sauvegarde_info[cle][2]=False
        persistent.sauvegarde_info[partie_a_sauvegarder][2]=True
        renpy.save(partie_a_sauvegarder)

        #year, month, day, hour, minute, second, dow, doy, dst = time.localtime()
        a = str(datetime.datetime.now())
        month, day, hour, minute = a[5:7], a[8:10], a[11:13], a[14:16]
        last_played = str(day)+"/"+str(month)+", "+str(hour)+"h"+str(minute)
        persistent.sauvegarde_info[partie_a_sauvegarder][1] = last_played

        #persistent.sauvegarde_info[partie_a_sauvegarder][3] = str(hours)+"h"+str(minutes) #Obsolete
        
        if montrer:
            renpy.notify(_("Partie sauvegardée"))
            renpy.pause(2.0)
            #renpy.say(n, "\n•")

    def chercher_derniere_sauvegarde(dico_info):
        for cle in dico_info:
            if dico_info[cle][2]:
                return int(cle[-1]), dico_info[cle][0]
        else:
            return (0, 0)

    def rot13(chaine):
        new_chain = chaine.lower()
        empty_chain = ""
        for char in new_chain:
            n = ord(char)
            if 96 < n < 123:
                if renpy.random.random() <0.5:
                    empty_chain += chr(((n-97+13)%26)+65)
                else:
                    empty_chain += chr(((n-97+13)%26)+97)
            else:
                empty_chain += char
        return empty_chain

    def vigenere(texte, cle):
        return "Fonction manquante"

    def get_info_achievement(ach_id, cache = False):
        name = persistent.achievements_dict[ach_id]["title"]
        texte = persistent.achievements_dict[ach_id]["text"]
        obtenu = achievement.has(ach_id)
        val = persistent.achievements_dict[ach_id]["val"]
        if cache and not obtenu: 
            name = rot13(name)
            texte = "<encrypted> "+rot13(texte)+" </encrypted>"      
        return (name,texte,obtenu,val)

    def compte_achievements(l):
        nb = 0
        for i in l:
            if achievement.has(i):
                nb += 1
        total = len(l)
        return nb,total


    def get_achievement(ach_id):
        persistent.achievements_dict[ach_id]["obtenu"] = True
        if not achievement.has(ach_id):
            ach = persistent.achievements_dict[ach_id]
            achievement.grant(ach_id)
            if not renpy.is_skipping():
                renpy.show_screen(_screen_name='scr_achievement_get', title=ach['title'], a_text=ach['text'], icon=ach['icon'])

    def update_inventory(objet, balance, montrer = True):
        #Adding items
        objet["nb"] += balance

        #Overload
        if objet["nb"] > objet["max"]:
            objet["nb"] = objet["max"]

        #Acknowledge known item (now accessible from the menu)
        objet['connu'] = True

        #Notifying the player
        if montrer:
            nb = objet['nb']
            nb_max = objet['max']
            if objet["title"] != "Batterie": #General case
                renpy.notify("{i}   "+objet['title']+" :  "+str(nb)+" / "+str(nb_max))
            else:
                if balance >= 0:
                    renpy.notify("{i}   Batterie :  +"+str(balance)+"% → "+str(nb)+" %")
                else:
                    renpy.notify("{i}   Batterie :  "+str(balance)+"% → "+str(nb)+" %")
            

#============ VIBRATIONS ============#

    import math

    class Shaker(object):
    
        anchors = {
            'top' : 0.0,
            'center' : 0.5,
            'bottom' : 1.0,
            'left' : 0.0,
            'right' : 1.0,
            }
    
        def __init__(self, start, child, dist):
            if start is None:
                start = child.get_placement()
            #
            self.start = [ self.anchors.get(i, i) for i in start ]  # central position
            self.dist = dist    # maximum distance, in pixels, from the starting point
            self.child = child
            
        def __call__(self, t, sizes):
            # Float to integer... turns floating point numbers to
            # integers.                
            def fti(x, r):
                if x is None:
                    x = 0
                if isinstance(x, float):
                    return int(x * r)
                else:
                    return x

            xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

            xpos = xpos - xanchor
            ypos = ypos - yanchor
            
            nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
            ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

            return (int(nx), int(ny), 0, 0)
    
    def _Shake(start, time, child=None, dist=100.0, **properties):

        move = Shaker(start, child, dist=dist)
    
        return renpy.display.layout.Motion(move,
                      time,
                      child,
                      add_sizes=True,
                      **properties)

    Shake = renpy.curry(_Shake)

    sshake = Shake((0, 0, 0, 0), 1.0, dist=15)
    bigshaq = Shake((0, 0, 0, 0), 2.0, dist=30)
    megashake = Shake((0, 0, 0, 0), 4.8, dist=20)

    
    def glitch(child, randomobj=renpy.random.Random(), chroma=config.gl2): # this is a transform
        # largeur et hauteur du child
        cwidth, cheight = renpy.render(child, 0, 0, 0, 0).get_size()
        if not cwidth or not cheight:
            return child
        lizt = []
        offt = 0
        theights = [randomobj.randint(0, cheight) for k in range(min(cheight, randomobj.randint(20, 40)//2))]
        theights.sort()
        # la somme de la taille de tous les morceaux
        fheight = 0
        while fheight<cheight:
            # theight c'est la hauteur du morceau
            theight = theights.pop(0)-fheight if theights else cheight-theight
            band = Transform(child,
                             crop=(-offt, fheight, cwidth, theight),
                             )
            if chroma:
                band = chromatic_offset(Flatten(band), chzoom=1.0+.5*offt/cwidth)
            lizt.append(band)
            fheight += theight
            if offt:
                offt = 0
            else:
                offt = randomobj.randint(-30, 30)
        return Fixed(Transform(child, alpha=.0),
                     VBox(*lizt),
                     fit_first=True,
                     # crop_relative=True,
                     # crop=(0, 0, 1.0, 1.0),
                     )

label quit:
    $ persistent.test = "isok"
