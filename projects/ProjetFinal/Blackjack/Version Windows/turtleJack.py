import turtle
import blackjack
import time

# Définition du dictionnaire couleur_caractere, qui permet d'obtenir le caractère et la couleur (rouge, noir) d'une couleur de carte (Trèfles, Piques, ...)
couleur_caractere = {
    "Trèfles" : ("♣", "black"),
    "Carreaux" : ("♦", "red"),
    "Cœurs" : ("♥", "red"),
    "Piques" : ("♠", "black")
}

# Définition de la fonction dessine_carte
def dessine_carte(taille : int, carte : tuple, tortue : turtle.Turtle):
    """
    Dessine une carte sur l'écran
    Paramètres:
    taille: Un integer qui détermine la taille de la carte. Correspond à la longueur du côté le plus long de la carte.
    carte: Tuple représentant une carte, de la forme (face, couleur)
    tortue: L'objet Turtle qui va dessiner la carte.
    """
    assert (isinstance(taille, float) or isinstance(taille, int)) and taille > 0, "Le paramètre taille doit être un nombre positif et non-nul."

    assert isinstance(carte, tuple) and len(carte) == 2, "Le paramètre carte doit être un tuple de longueur 2"
    assert carte[0] in blackjack.faces, "La face de la carte peut seulement être 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'V', 'D' ou 'R'"
    assert carte[1] in couleur_caractere, "La couleur de la carte peut seulement être 'Trèfles', 'Carreaux', 'Cœurs' ou 'Piques'"
    assert isinstance(tortue, turtle.Turtle), "Le paramètre tortue doit être un objet Turtle"

    ######## DESSIN DU RECTANGLE DE LA CARTE ########
    tortue.setheading(90) # On s'oriente vers le haut
    position_depart_x, position_depart_y = tortue.pos() # On sauve les coordonnées de départ de la tortue
    tortue.color("black") # Change la couleur de l'encre de la tortue au noir
    tortue.fillcolor(255, 255, 255) # Définit la couleur de l'intérieur du rectangle au blanc
    tortue.begin_fill() # Commence le processus de "fill", pour commencer à définir la partie intérieur du rectangle, qui va être colorier en blanc

    # Dessine le rectangle
    for _ in range(2):
        tortue.forward(taille)
        tortue.right(90)
        tortue.forward(taille*5/7) # On avance de taille*5/7 pour respecter les proportions des cartes réelles
        tortue.right(90)
    tortue.end_fill() # Termine le processus de "fill", pour colorier l'intérieur de rectangle en blanc

    ######## DESSINE COULEUR DE CARTE ########
    tortue.penup()

    # On avance vers le milieu de la carte
    tortue.forward(taille/2.5) # On avance vers le milieu sur l'axe verticale
    tortue.right(90)
    tortue.forward(taille*5/14) # On avance vers le milieu sur l'axe horizontale

    tortue.color(couleur_caractere[carte[1]][1]) # Grâce au dictionnaire couleur_caractere, nous obtenons la bonne couleur (noir, rouge) de la couleur du paramètre carte
    tortue.write(couleur_caractere[carte[1]][0], font=("", int(4/15*taille)), align="center") # Grâce au dictionnaire couleur_caractere, nous obtenons la bon caractère de la couleur du paramètre carte

    ######## ECRIT FACE EN HAUT À GAUCHE ########
    tortue.penup()
    tortue.setposition(position_depart_x, position_depart_y) # Revient à la positition de départ
    tortue.setheading(90) # S'oriente vers le haut
    # Le Turtle monte vers le coin en haut à gauche de la carte
    tortue.forward(47/60*taille)
    tortue.right(90)
    tortue.forward(8/300*taille)

    tortue.write(carte[0], font=("", int(taille/7))) # Le Turtle écrit la face de la carte
    
    ######## ECRIT FACE EN BAS À DROITE ########
    tortue.setposition(position_depart_x, position_depart_y-taille/60) # Revient à la position de départ, mais un peu plus élevé
    # Le Turtle se dirige vers le coin en bas à droite de la carte
    if carte[0] == "10": # Si la face de la carte est "10", il faut plus d'espace pour écrire la face car "10" contient 2 caractères
        tortue.forward(10.25/21 * taille)
    else:
        tortue.forward(12/21 * taille)

    tortue.write(carte[0], font=("", int(taille/7))) # Le Turtle écrit la face de la carte
    tortue.setposition(position_depart_x, position_depart_y) # On revient à la position de départ
    tortue.setheading(0) # On s'oriente vers la gauche

# Définition de la fonction affiche_cartes
def affiche_cartes(taille_carte : int, main : list, cartes_croupier : bool = False, cache : bool = False):
    """
    Affiche les cartes d'une main de cartes.
    Paramètres:
    taille_carte: Un integer qui détermine la taille de la carte. Correspond à la longueur du côté le plus long de la carte.
    main: Une liste composée uniquement de tuples de longueur 2, représentant les cartes
    cartes_croupier: False par défaut. Si c'est True, les cartes sont dessinées en haut de l'écran.
    cache: False par défaut. Si c'est True, une des cartes de la mains est cachée.
    """
    assert (isinstance(taille_carte, float) or isinstance(taille_carte, int)) and taille_carte > 0, "Le paramètre taille_carte doit être un nombre positif et non-nul."

    assert isinstance(main, list), "Le paramètre main n'est pas une liste."
    assert all(len(carte) == 2 for carte in main), "Les tuples dans la liste main ne sont pas composé uniquement de 2 valeurs."

    assert isinstance(cartes_croupier, bool), "Le paramètre cartes_croupier doit être un booléen."

    if cartes_croupier: # Si on veut afficher les cartes du croupier
        tortue = dessin_croupier # La tortue qui va dessiner les cartes est celui qui gère les cartes du croupier, soit dessin_croupier
        tortue.penup()
        tortue.setposition(-taille_carte*len(main)/2 + taille_carte * (1 - 5/7)/2, 150/1440*screen.window_width()) # On se place parfaitement pour que les cartes soient centrées
        if cache: # Si on veut cacher une des cartes
            tortue.pendown()
            dessine_carte(taille_carte, main[0], tortue) # On dessine la première carte, qui est montrée
            tortue.penup()

            # On dessine le rectangle de la deuxième carte
            tortue.forward(taille_carte)
            tortue.pendown()
            tortue.color("black")
            tortue.fillcolor(255, 255, 255)
            tortue.begin_fill()
            tortue.setheading(90)
            for _ in range(2):
                tortue.forward(taille_carte)
                tortue.right(90)
                tortue.forward(taille_carte*5/7)
                tortue.right(90)
            tortue.end_fill()

            tortue.penup()
            # On se dirige vers le milieu de la carte
            tortue.forward(taille_carte/2.5) # On se dirige vers le milieu sur l'axe verticale
            tortue.right(90)
            tortue.forward(taille_carte*5/14) # On se dirige vers le milieu sur l'axe horizontale
            tortue.write("?", font=("", int(4/15*taille_carte)), align="center") # On écrit "?" pour montrer que c'est une carte cachée
            return # Pour ne pas éxécuter le code des prochaines lignes

    else: # Si on veut dessiner les cartes du joueur
        tortue = dessin_joueur # La tortue qui va dessiner les cartes est celui qui gère les cartes du joueur, soit dessin_joueur
        tortue.penup()
        tortue.setposition(-taille_carte*len(main)/2 + taille_carte * (1 - 5/7)/2, -300/1440*screen.window_width()) # On se place parfaitement pour que les cartes soient centrées
    
    tortue.pendown()
    for card in main: # On parcours chaque carte de la liste main
        dessine_carte(taille_carte, card, tortue) # On dessine une carte
        tortue.penup()
        tortue.forward(taille_carte) # On avance pour préparer le dessin de la prochaine carte
        tortue.pendown()
    
    screen.update()

# Définition de la fonction jeu_croupier
def jeu_croupier(main_croupier : list, paquet : list):
    """
    Cette fonction gère le jeu du croupier.
    Paramètres:
    main_croupier: Une liste composée uniquement de tuples de longueur 2, représentant les cartes du croupier
    paquet: Une liste composée uniquement de tuples de longueur 2 représentant les cartes du paquet
    """
    while blackjack.compte_valeur(main_croupier) < 17: # Le croupier est obligé de prendre des cartes tant qu'il n'a pas une valeur totale supérieure à 16
        time.sleep(2) # On fait rien pour 2 secondes, pour donner du temps au joueur pour qu'il puisse analyser la situation
        blackjack.distribue_carte(paquet, main_croupier, 1) # On prend une carte du paquet, puis on le donne au croupier
        # On met à jour les cartes du croupier sur l'écran
        dessin_croupier.clear() # On efface le dessin des cartes du croupier
        affiche_cartes(taille_carte, main_croupier, True) # On redessine les cartes du croupier
        time.sleep(2) # On attend encore 2 secondes, pour donner du temps au joueur pour qu'il puisse analyser la situation

# On initialise plein de variables importantes
dessineur = turtle.Turtle(visible=False) # Turtle qui va dessiner tout qui n'est pas mis à jour
dessin_joueur = turtle.Turtle(visible=False) # Turtle qui va dessiner les cartes du joueur
dessin_croupier = turtle.Turtle(visible=False) # Turtle qui va dessiner les cartes du croupier
annonceur_gagnant = turtle.Turtle(visible=False) # Turtle qui va annoncer le résultat de la partie
annonceur_gagnant.setposition(0, 0) # On place le Turtle annonceur_gagnant au milieu de l'écran
annonce_balance = turtle.Turtle(visible=False) # Turtle qui va mettre à jour la balance du joueur
screen = turtle.Screen() # On stocke l'object Screen dans la variable screen
balance = 100 # On initialise la variable qui stocke la balance du joueur
max_balance = balance # On initialise la variable qui va stocker la valeur maximale atteint par la balance du joueur

screen.colormode(255) # On définit le mode de définition des couleur (RGB dans ce cas)
screen.setup(1.0, 1.0) # Pour que l'écran prend le plus d'espace possible
screen.bgcolor(53, 101, 77) # On change la couleur de l'arrière plan à un vert d'une table de casino
screen.tracer(0) # Pour qu'on ne voit pas l'animation lente des dessins des Turtle
dessin_joueur.width(3) # Augmente la largeur du stylo de la tortue dessin_joueur
dessin_croupier.width(3) # Augmente la largeur du stylo de la tortue dessin_croupier
dessineur.width(3) # Augmente la largeur du stylo de la tortue dessineur
taille_carte = 160 # On définit la taille des cartes utilisées dans le jeu

dessineur.penup()

#### DESSIN DU PANNEAU EN HAUT À GAUCHE QUI INFORME L'UTILISATEUR À PROPOS DES CONTRÔLES ####
dessineur.setposition(-0.5 * screen.window_width(), 0.5 * screen.window_height()) # On place la tortue dessineur en haut à gauche
dessineur.setheading(0) # On s'oriente vers la gauche
dessineur.pendown()
dessineur.fillcolor(255, 255, 255) # On met la couleur de l'intérieur de panneau au blanc
dessineur.begin_fill() # Commence le processus de "fill", pour commencer à définir la partie intérieur du panneau, qui va être colorier en blanc
# On dessine le contour du rectangle
dessineur.forward(120)
dessineur.setheading(270)
dessineur.forward(80)
dessineur.setheading(180)
dessineur.forward(120)

dessineur.end_fill() # Termine le processus de "fill", pour colorier l'intérieur de rectangle en blanc

dessineur.penup()

####### On écrit le texte qui parle des contrôles du jeu #######
dessineur.setposition(-0.5 * screen.window_width() + 60, 0.5*screen.window_height()-25) 
dessineur.write("Contrôles: ", font=("Helvetica Neue", 14, 'bold'), align="center")

dessineur.setposition(-0.5 * screen.window_width() + 60, 0.5*screen.window_height()-50)
dessineur.write("ESPACE - Hit", font=("Helvetica Neue", 11), align="center")

dessineur.setposition(-0.5 * screen.window_width() + 60, 0.5*screen.window_height()-70)
dessineur.write("S - Rester", font=("Helvetica Neue", 11), align="center")
#################################################################

#### DESSIN DU PANNEAU EN BAS À GAUCHE QUI INFORME L'UTILISATEUR À PROPOS DE SA BALANCE ####
dessineur.setposition(-0.5 * screen.window_width(), -0.5 * screen.window_height()+170) # On se place vers le coin en bas à gauche de l'écran
# De même que pour le panneau pour les contrôles, on dessine un rectangle blanc avec le processus de "fill"
dessineur.pendown()
dessineur.begin_fill()
dessineur.setheading(0)
dessineur.forward(170)
dessineur.setheading(270)
dessineur.forward(170)
dessineur.setheading(180)
dessineur.forward(170)
dessineur.end_fill()
dessineur.penup()

# On écrit le texte "Balance" dans ce panneau
dessineur.setposition(-0.5 * screen.window_width()+85, -0.5*screen.window_height()+120)
dessineur.pencolor("red")
dessineur.write("Balance:", font=("Helvetica Neue", 29), align="center")

# Avec le Turtle annonce_balance, on écrit la balance du début de la partie, de l'utilisateur
annonce_balance.penup()
annonce_balance.setposition(-0.5 * screen.window_width()+85, -0.5*screen.window_height()+50) # On se place correctement
annonce_balance.pencolor("red") # Change la couleur du Turtle au rouge
annonce_balance.write(balance, font=("Helvetica Neue", 29), align="center") # Écrit la balance de l'utilisateur

#### DESSIN DU PANNEAU À DROITE QUI INFORME L'UTILISATEUR À PROPOS DU RECORD ACTUEL ####
dessineur.setposition(0.5 * screen.window_width(), 60) # On se place à droite avec la tortue dessineur
dessineur.pendown()
dessineur.color("black") # Définit la couleur du contour du panneau au noir
dessineur.fillcolor("white") # On définit la couleur de l'intérieur de panneau au blanc

# De même que pour les panneaux à propos des contrôles et de la balance, on dessine un rectangle blanc avec le processus "fill"
dessineur.begin_fill()
dessineur.setheading(180)
dessineur.forward(170)
dessineur.setheading(270)
dessineur.forward(120)
dessineur.setheading(0)
dessineur.forward(170)
dessineur.end_fill()
dessineur.penup()

dessineur.setposition(0.5 * screen.window_width() - 85, 30) # On se place correctement dans le panneau à droite
dessineur.write("Record Actuel: ", font=("Helvetica Neue", 14, "bold"), align="center") # On écrit "Record Actuel" dans le panneau

dessineur.setposition(0.5 * screen.window_width() - 85, -17) # On descend un peu
with open("record.txt", "r") as record: # On ouvre le fichier record.txt, qui stocke le record actuel
    dessineur.write(record.read(), font=("Helvetica Neue",18), align="center") # On affiche le record actuel

# Écrit le texte "Vos cartes" en bas au centre de l'écran
dessineur.setposition(0, -360/1440*screen.window_width())
dessineur.write("Vos cartes", font=("Helvetica Neue", 50), align="center")

# Écrit le texte "Cartes du croupier" en haut au centre de l'écran
dessineur.setposition(0, 315/1440*screen.window_width())
dessineur.write("Cartes du croupier", font=("Helvetica Neue", 50), align="center")

screen.update() # On met à jour l'écran

paquet = [] # Initialise la variable paquet, qui va stocker le paquet de cartes
main_joueur = [] # Initialise la variable main_joueur, qui va stocker les cartes du joueur
main_croupier = [] # Initialise la variable main_croupier, qui va stocker les cartes du croupier
termine = False # Initialise la variable termine, qui va être mis à True lorsqu'une partie est terminée
pari = 0 # Initialise la variable qui va stocker le pari de l'utilisateur

def demander_pari() -> int:
    """
    Cette fonction demande au joueur son pari, puis le renvoi sous forme de integer.
    """
    global balance
    message = "Entrez votre pari:" # Initialise le message qui va apparaître dans la fenêtre 
    ok = False # Ce booléen sera seulement True lorsque l'utilisateur entre un pari valide
    pari = 0 # Initialise la variable pari
    while not ok: # Tant que l'utilisateur n'a pas entrer un pari valide
        try:
            pari = int(screen.textinput("Pari", message)) # On met l'entrée de l'utilisateur dans la variable pari.
            if pari < 0: # Si le pari est un nombre négatif
                message = "Le pari doit être un nombre supérieur à 0. Entrez votre pari:" # On met à jour le message qui apparait dans la fenêtre pour informer l'utilisateur à propos de son erreur
            elif balance < pari: # Si le joueur n'a pas assez d'argent pour son pari
                message = "Vous n'avez pas assez d'argent pour ce pari. Entrez votre pari:" # On met à jour le message qui apparait dans la fenêtre pour informer l'utilisateur à propos de son erreur
            else: # Si le pari est valide
                ok = True # On met le booléen ok à True pour arrêter de demander à l'utilisateur son pari
                balance -= pari # On enleve l'argent à l'utilisateur
                # On met à jour la balance de l'utilisateur
                annonce_balance.clear() # On efface le nombre de la balance sur l'écran
                annonce_balance.write(balance, font=("Helvetica Neue", 40), align="center") # On remet la balance mise à jour
        except: # Ce code est seulement éxécuté si le joueur n'a pas entrer un nombre
            message = "Cela n'est pas un nombre. Entrez votre pari:" # On met à jour le message qui apparait dans la fenêtre pour informer l'utilisateur à propos de son erreur
    return pari # On renvoi le pari de l'utilisateur
        
# Définition de la fonction initialise_partie
def initialise_partie():
    """
    Cette fonction initialise les variables nécéssaire au fonctionnement du jeu pour le début de chaque partie.
    """
    global paquet, main_croupier, main_joueur, pari, termine

    paquet = blackjack.creer_paquet() # Stocke le paquet de cartes dans la variable paquet

    dessin_croupier.clear() # Efface le dessin des cartes du croupier
    dessin_joueur.clear() # Efface le dessin des cartes du joueur
    annonceur_gagnant.clear() # Efface le dessin du message du résultat de la partie
    pari = demander_pari() # On demande à l'utilisateur son pari
    screen.listen()
    main_joueur = [] # On réinitialise la main du joueur
    main_croupier = [] # On réinitialise la main du croupier
    blackjack.distribue_carte(paquet, main_joueur, 2) # On donne 2 cartes au joueur
    blackjack.distribue_carte(paquet, main_croupier, 2) # On donne 2 cartes au croupier
    affiche_cartes(taille_carte, main_joueur) # On affiche les cartes du joueur
    affiche_cartes(taille_carte, main_croupier, True, True) # On affiche les cartes du croupier, avec une carte cachée
    termine = False # On recommence une partie, donc la partie n'est plus terminée, donc on met le booléen termine à False


initialise_partie()

# Définition de la fonction hit
def hit():
    """
    Cette fonction est appelée lorsque l'utilisateur appuie sur la touche Espace. Elle transmet l'action "Hit" du joueur à la fonction Jouer.
    """
    global termine
    if not termine: # Si la partie n'est pas encore terminée
        jouer("hit") # On envoi l'action "hit" au jeu

# Définition de la fonction rester
def rester():
    """
    Cette fonction est appelée lorsque l'utilisateur appuie sur la touche S. Elle transmet l'action "Rester" du joueur à la fonction Jouer.
    """
    global termine
    if not termine: # Si la partie n'est pas encore terminée
        jouer("rester") # On envoi l'action "Rester" au jeu

# Définition de la fonction joueur
def jouer(action : str):
    """
    Cette fonction est le cœur du jeu, qui gère son bon fonctionnement.
    Paramètres:
    action: Représente l'action du joueur. C'est soit "Hit" ou "Rester"
    """
    global termine, pari, balance, max_balance
    if action == "hit": # Si le joueur a décidé de Hit
        blackjack.distribue_carte(paquet, main_joueur, 1) # On donne une carte au joueur

        # On met à jour les cartes sur l'écran
        dessin_joueur.clear()
        affiche_cartes(taille_carte, main_joueur)

        if blackjack.compte_valeur(main_joueur) > 21: # Si la valeur de la main du joueur a dépassée 21
            termine = True # Le jeu est terminé donc on met la variable termine à False
            annonceur_gagnant.color("red") # On change la couleur de l'encre du Turtle annonceur_gagnant au rouge
            annonceur_gagnant.write("Perdu!", font=("Helvetica Neue", 80, 'bold'), align="center") # On écrit "Perdu!" sur l'écran
            screen.update()

            if balance == 0: # Si le joueur n'a plus d'argent
                time.sleep(2) # On attend 2 secondes

                # On efface tous les dessins
                dessin_croupier.clear()
                dessin_joueur.clear()
                dessineur.clear()
                annonce_balance.clear()
                annonceur_gagnant.clear()

                with open("record.txt", "r") as record: # On ouvre le fichier record.txt
                    if max_balance > int(record.read()): # On regarde si le joueur a atteint un nouveau record
                        # Si un nouveau record a été atteint, on change le record dans le fichier record.txt
                        with open("record.txt", "w") as record:
                            record.write(str(max_balance))

                        annonceur_gagnant.color(57, 255, 20) # Change la couleur de l'encre du Turtle annonceur_gagnant au vert
                        annonceur_gagnant.write("Félicitations! Vous avez battu le record avec votre balance maximale de " + str(max_balance) + ".", font=("Helvetica Neue", 35, 'bold'), align="center") # On écrit un message de félicitation, et on affiche la balance maximale
                    else:
                        annonceur_gagnant.color("red") # Change la couleur de l'encre du Turtle annonceur_gagnant au vert
                        annonceur_gagnant.write("Vous avez perdu le jeu. Votre balance maximale était de " + str(max_balance) + ".", font=("Helvetica Neue", 35, 'bold'), align="center") # On dit au joueur qu'il a perdu, et on lui dit sa balance maximale atteinte
                screen.update() # On met l'écran à jour
                time.sleep(10) # On attend 10 secondes
                exit() # On quitte le programme

    else: # Si le joueur a décidé de "Rester"
        termine = True # le jeu est terminé, donc on met le booléen termine à True
        affiche_cartes(taille_carte, main_croupier, True) # On affiche la carte cachée du croupier
        jeu_croupier(main_croupier, paquet) # On appelle la fonction jeu_croupier pour qu'il fait son tour
        resultat = blackjack.evalue_partie(main_joueur, main_croupier) # Avec la fonction evalue_partie, on détermine le gagnant
        if resultat == True: # Si le joueur a gagné
            annonceur_gagnant.color(57, 255, 20) # Change la couleur de l'encre du Turtle annonceur_gagnant au vert
            annonceur_gagnant.write("Gagné!", font=("Helvetica Neue", 80, 'bold'), align="center") # On écrit "Gagné!"
            screen.update()
            balance += 2 * pari # le joueur reçoit 2 fois son pari
            if balance > max_balance: # Si une nouvelle balance maximale est atteinte
                max_balance = balance # on change la variable max_balance au nouveau maximum

            # On met à jour la balance de l'utilisateur
            annonce_balance.clear()
            annonce_balance.write(balance, font=("Helvetica Neue", 40), align="center")

        elif resultat == False: # Si le joueur a perdu
            annonceur_gagnant.color("red") # Change la couleur de l'encre du Turtle annonceur_gagnant au rouge
            annonceur_gagnant.write("Perdu!", font=("Helvetica Neue", 80, 'bold'), align="center") # On écrit perdu
            screen.update()
            if balance == 0: # Si le joueur n'a plus d'argent
                time.sleep(2) # On attend 2 secondes

                # On efface tous les dessins
                dessin_croupier.clear() 
                dessin_joueur.clear()
                dessineur.clear()
                annonce_balance.clear()
                annonceur_gagnant.clear()
                
                with open("record.txt", "r") as record: # On ouvre le fichier record.txt
                    if max_balance > int(record.read()): # On regarde si le joueur a atteint un nouveau record
                        # Si un nouveau record a été atteint, on change le record dans le fichier record.txt
                        with open("record.txt", "w") as record:
                            record.write(str(max_balance))

                        annonceur_gagnant.color(57, 255, 20) # Change la couleur de l'encre du Turtle annonceur_gagnant au vert
                        annonceur_gagnant.write("Félicitations! Vous avez battu le record avec votre balance maximale de " + str(max_balance) + ".", font=("Helvetica Neue", 35, 'bold'), align="center") # On écrit un message de félicitation, et on affiche la balance maximale
                    else:
                        annonceur_gagnant.color("red") # Change la couleur de l'encre du Turtle annonceur_gagnant au vert
                        annonceur_gagnant.write("Vous avez perdu le jeu. Votre balance maximale était de " + str(max_balance) + ".", font=("Helvetica Neue", 35, 'bold'), align="center") # On dit au joueur qu'il a perdu, et on lui dit sa balance maximale atteinte
                screen.update() # On met l'écran à jour
                time.sleep(10) # On attend 10 secondes
                exit() # On quitte le programme

        else: # Si c'est une égalité
            annonceur_gagnant.color(20, 20, 20) # On change la couleur du Turtle annonceur_gagnant au gris
            annonceur_gagnant.write("Égalité.", font=("Helvetica Neue", 80, 'bold'), align="center") # On écrit "Égalité"
            balance += pari # On redonne l'argent à l'utilisateur
            # On met à jour la balance de l'utilisateur
            annonce_balance.clear()
            annonce_balance.write(balance, font=("Helvetica Neue", 40), align="center")
            screen.update()
        
    if termine: # Si le jeu est terminé
        time.sleep(3) # on attend 3 secondes
        initialise_partie() # on commence une nouvelle partie

screen.onkeypress(hit, "space") # on detecte l'appuie de la touche Espace

# on detecte l'appuie de la touche S
screen.onkeypress(rester, "s")
screen.onkeypress(rester, "S")

screen.listen() # on dit à l'écran d'écouter pour les appuies de touches
screen.mainloop() 
