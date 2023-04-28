#BLAISE EST PENDUE - TROPHÉES NSI

from random import randint

def jeu():# fonction principale qui permet de jouer

    print("Akwaba sur le Jeu: Blaise est pendu ;)")
    print("Le but du jeu est de découvrir le mot mystère caché")

    lettre_hasard() # permet au programme de choisir une lettre
    generateur_de_mots() # permet au programme de choisir le mot à trouver
    choix_reponse() # permet au joueur d'enter une réponse



def lettre_hasard () : #fonction qui donne une lettre entre A et Z (majuscule)
    global lettre
    nbr = randint (65,90)
    lettre = chr(nbr) # conversion du chiffre choisi au hasard en lettre


def generateur_de_mots () : # fonction qui génère des mots au hasard

    global liste_de_mots
    global h
    global goal
    fichier=open("registre_de_mots_2(1).txt","r") #fichier txt qui constitue le registre de mots du programe
    liste_de_mots=[]

    for ligne in fichier : # on parcours toutes les lignes du fichier
        ligne=ligne.replace('\n','')#on replace les retours à la ligne par une chaine de caractere vide pour ne pas qu'ils soient visibles
        for elmt in ligne[0]: # on parcours toutes les premieres lettres des mots du registre
            if elmt==lettre: # pour tous les mots dont la 1ere lettre commence par la lettre choisi au hasard
                liste_de_mots.append(ligne)#on ajoute les à la liste vide prealablement creee


    for elmt in liste_de_mots : # on parcours les elements de la liste des mots
        h=randint(0,len(liste_de_mots)-1) # choix au hasard d'un indice de la liste"""


    goal=liste_de_mots[h] # mot qui correspoend à l'indice choisi


    print("Votre mot contient",len(liste_de_mots[h]),"lettres")




    global L
    global l
    global Liste
    L=[]
    Liste=[]

    for elmt in goal: # parcours toutes les lettres du mot mystere
        L.append(elmt) # ajoute les lettres à une 1ere liste
        Liste.append(elmt)# ajoute les lettres à une 2nde liste

    """print(Liste)"""
    for i in range(1,len(goal)): # parcours les indices des lettres du mot mystere (sauf la 1ere lettre)
        L[i]=" _" # remplace les lettres par des tirets

    l=''.join(L)
    print(l)


    global essaies
    if len(goal)<=5: # si le nombre de lettres du mot à trouver est inférieur ou égal à 5, le joueur a 8 essaies
        essaies=8
    elif 5<len(goal)<=8: # si le nombre de lettres du mot à trouver est supérieur à 5 et inférieur ou égal à 8 joueur a 12 essaies
        essaies=12
    else:
        essaies=17 # si le nombre de lettres du mot à trouver est supérieur à 8, le joueur a 17 essaies

    print("Vous avez",essaies,"chances")

def choix_reponse(): # le joueur peut choisir à chaque essai son type de réponse, soit une lettre soit un mot
    if essaies==0: # si le nombre d'essai est fini le programme propose de rejouer
        print("C'est perdu!Vous n'avez plus de chances")
        print("Le mot cherché était",goal)
        return rejouer()
    else:
        choix=str(input("Si vous pensez vous a un mot tapez:1 /Si vous pensez a une lettre tapez: 2  "))
        if choix=="1":
            maj1()
        if choix =="2":
            maj2()

def maj1(): # permet au joueur de proposer un mot
    global essaies
    guess1=str(input("Entrer votre mot : "))
    guess1=guess1.upper() #conversion de la reponse en majuscule
    essaies=essaies-1 # compteur du nombre d'essai restant
    if guess1==goal: # compare la reponse du joueur avec le mot mystere
        print("Vous avez proposé",guess1) # si c'est la bonne réponse le joueur gagne
        print ("Félicitations le mot cherché était bien",goal,"!"" C'est Djinzin ;)")
        return rejouer()

    else:
        print("Vous avez proprosé",guess1)
        print("Ce n'est pas la bonne réponse!")
        print(l)
        print("Il vous reste ",essaies,"essaies")
        return choix_reponse()


def maj2(): # permet au joueur de proposer des lettres
    global essaies
    global L
    global l
    global Liste
    guess2=str(input("Donner une proposition de lettre : "))
    guess2=guess2.upper()  #conversion de la reponse en majuscule
    essaies=essaies-1 # compteur du nombre d'essai restant
    L_indices = []
    cpt = False # compteur qui vérifie la présence de la lettre proposée par le joueur dans le mot mystere
    for ltr in goal : # parcours toutes les lettres du mot mystere
        if ltr == guess2: # si une lettre du mot mystere correspond à la proposition du joueur
            cpt = True # le compteur change de valeur

    for i in range (len(goal)) : # parcours les indices du mot mystere

        if cpt == True and guess2 == goal[i] : # si la présence de la lettre proposée est verifiee
            L_indices.append(i) # on ajoute l'indice qui lui correspond dans le mot mystere à une liste

    if guess2 in Liste:
        print("Bonne réponse")
        print("Vous avez proposé la lettre",guess2)
        for i in range(len(L_indices)):
            indice=L_indices[i]
            L[indice]=guess2
        l=''.join(L)
        print(l)
        print("Il vous reste",essaies,"essaies")
        if l==goal:
            print("Félicitation, le mot mystere était",goal)
            return rejouer()
        else:
            return choix_reponse()

    else:
        print("Vous avez choisi la lettre",guess2,)
        print("Ce n'est pas la bonne reponse")
        print(l)
        print("Il vous reste",essaies,"essaies")
        return choix_reponse()

def rejouer():
    global rejouer
    print("Voulez-vous rejouer?")
    rejouer=str(input("Si oui entrez:1/ Si non entrez:2 "))
    if rejouer=="1":
        return jeu()
    else:
        print("A la prochaine pour de nouveaux mots")
        quit()


jeu()



