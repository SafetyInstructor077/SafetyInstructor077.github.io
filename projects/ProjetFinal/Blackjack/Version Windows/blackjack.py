import random

couleurs = ("Trèfles", "Carreaux", "Cœurs", "Piques") # Initialise la liste des couleurs des cartes
faces = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "V", "D", "R") # Initialise la liste des faces des cartes

# Initialise le dictionnaire faces_valeur, qui va nous permettre d'obtenir la valeur d'une carte avec sa face
faces_valeur = {
    "A" : 11,
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "10" : 10,
    "V" : 10,
    "D" : 10,
    "R" : 10
}

# Définition de la fonction creer_paquet
def creer_paquet() -> list:
    """
    Crée le paquet de 52 cartes
    Renvoie une liste, composé de 52 tuples représentant les cartes
    """
    paquet = [] # Initialise une liste
    for couleur in couleurs: # Parcours les tuples des couleurs et des faces pour crée chaque carte
        for face in faces:
            paquet.append((face, couleur)) # On ajoute la carte au paquet
    return paquet # Renvoie le paquet de cartes

# Définition de la fonction distribute_carte
def distribue_carte(paquet : list, main : list, nombre_de_cartes : int):
    """
    Prend un certain nombre de cartes de la liste paquet, selon la variable nombre_de_cartes, et les distibue à la liste main
    Paramètres:
    paquet: Une liste composée uniquement de tuples de longueur 2 représentant les cartes du paquet
    main: La liste qui recoit les cartes
    nombre_de_cartes: Nombre de cartes distribuées à la main
    """
    assert isinstance(paquet, list), "Le paramètre paquet n'est pas une liste."
    assert all(isinstance(carte, tuple) for carte in paquet), "La liste paquet n'est pas composée uniquement de tuples."
    assert all(len(carte) == 2 for carte in paquet), "Les tuples dans la liste paquet ne sont pas composé uniquement de 2 valeurs."

    assert isinstance(main, list), "Le paramètre main n'est pas une liste."
    assert all(len(carte) == 2 for carte in main), "Les tuples dans la liste main ne sont pas composé uniquement de 2 valeurs."

    assert isinstance(nombre_de_cartes, int), "Le paramètre nombre_de_cartes n'est pas un nombre entier."
    assert nombre_de_cartes >= 1, "Le paramètre nombre_de_cartes ne peut pas être inférieure ou égale à 0."
    assert nombre_de_cartes <= len(paquet), "Il n'y a pas assez de cartes dans la liste paquet pour le nombre de cartes distribuées."

    for i in range(nombre_de_cartes): # On effectue le prochain code dans la fonction nombre_de_cartes fois
        main.append(paquet.pop(random.randint(0, len(paquet)-1))) # On prend une carte aléatoire de la liste paquet, on l'a supprime, et on l'ajoute à la main 

# Définition de la fonction evalue_partie
def evalue_partie(main_joueur : list, main_croupier : list):
    """
    Prend en paramètre les cartes du joueur et du croupier, pour proclamer le gagnant
    Paramètres:
    main_joueur: Une liste composée uniquement de tuples de longueur 2, représentant les cartes du joueur
    main_croupier: Une liste composée uniquement de tuples de longueur 2, représentant les cartes du croupier
    """
    assert isinstance(main_joueur, list), "Le paramètre main_joueur n'est pas une liste."
    assert all(len(carte) == 2 for carte in main_joueur), "Les tuples dans la liste main_joueur ne sont pas composé uniquement de 2 valeurs."
    assert isinstance(main_croupier, list), "Le paramètre main_croupier n'est pas une liste."
    assert all(len(carte) == 2 for carte in main_croupier), "Les tuples dans la liste main_croupier ne sont pas composé uniquement de 2 valeurs."

    joueur_gagne = True # On assume au tout début que le joueur a gagné, pour ensuite voir si on peut réfuter cette supposition
    valeur_croupier = compte_valeur(main_croupier) # On stocke la valeur de la main du croupier dans la variable valeur_croupier
    valeur_joueur = compte_valeur(main_joueur) # On stocke la valeur de la main du joueur dans la variable valeur_joueur
    if valeur_croupier < 22 and valeur_joueur < valeur_croupier: # Si le croupier n'a pas une valeur supérieur à 21, et si sa main a plus de valeur que celle du joueur
        joueur_gagne = False # Le joueur a perdu
    
    elif valeur_croupier == valeur_joueur: # Si les mains du joueur et de croupier sont égaux
        joueur_gagne = "egal" # On met la variable joueur_gagne à "egal" pour monter qu'il y a égalité

    return joueur_gagne # On renvoie le résultat de la partie

# Définition de la fonction compte_valeur
def compte_valeur(main : list) -> int:
    """
    Prend en paramètre une liste main, et calcule sa valeur dans le jeu Blackjack
    Paramètres:
    main: Une liste composée uniquement de tuples de longueur 2, représentant les cartes
    Renvoie un integer, représentant la valeur de la liste main 
    """
    assert isinstance(main, list), "Le paramètre main n'est pas une liste."
    assert all(len(carte) == 2 for carte in main), "Les tuples dans la liste main ne sont pas composé uniquement de 2 valeurs."

    valeur = 0 # Initialise la variable qui va stocker la valeur de la main
    ace_count = 0  # Initialise la variable qui va stocker le nombre d'Ace dans la main
    for carte in main: # On parcourt tous les cartes dans la main
        valeur += faces_valeur[carte[0]] # On ajoute la valeur de la carte à la variable valeur, grâce au dictionnaire faces_valeur
        if carte[0] == "A": # Si la carte est un Ace, on ajoute 1 à la variable ace_count
            ace_count += 1 
    
    # Pour chaque Ace, on enlève 10 de la valeur de la main tant que la valeur est supérieur à 21
    i = 0
    while valeur > 21 and i != ace_count:
        valeur -= 10
        i += 1
    
    return valeur # On renvoie la valeur de la carte