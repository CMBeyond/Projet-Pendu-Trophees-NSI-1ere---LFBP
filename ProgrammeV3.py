#PENDUE - TROPHÉES NSI

from random import randint

def rejouer():
    global rejouer
    print("Voulez-vous rejouer?")
    rejouer=str(input("Si oui entrez:1/ Si non entrez:2 "))
    if rejouer=="1":
        return jeu()
    else:
        print("A la prochaine pour de nouveaux mots")
        quit()



def jeu():
    print("Akwaba sur le Jeu: Blaise est pendu ;)")
    print("Le but du jeu est de découvrir le mot mystère caché")

    lettre_hasard()
    generateur_de_mots()
    choix_reponse()



def lettre_hasard () : #fonction qui donne une lettre entre A et Z (majuscule)
    global lettre
    nbr = randint (65,90)
    lettre = chr(nbr) # conversion du chiffre choisi au hasard en lettre
    """print(lettre)"""

def generateur_de_mots () : # fonction qui genere des mots au hasrd

    global liste_de_mots
    global h
    global goal
    fichier=open("registre_de_mots_2(1).txt","r") #fichier txt qui contient une multitude de mots

    liste_de_mots=[]

    for ligne in fichier : # on parcours toutes les lignes du fichier
        ligne=ligne.replace('\n','')#on replace les retours à la ligne par une chaine de caractere vide pour ne pas qu'ils ne se voyent pas
        for elmt in ligne[0]:
            if elmt==lettre:
                liste_de_mots.append(ligne)#on ajoute les mots à la liste vide prealablement creee


    for elmt in liste_de_mots : # on parcours les elements de la liste des mots
        h=randint(0,len(liste_de_mots)) # choix au hasard d'un indice de la liste"""


    goal=liste_de_mots[h]


    #print(liste_de_mots[h]) # renvoie le mot qui correspoend à l'indice #chaine
    print("Votre mot contient",len(liste_de_mots[h]),"lettres")


    global L
    global l
    global Liste
    L=[]
    Liste=[]

    for elmt in goal:
        L.append(elmt)
        Liste.append(elmt)
    """print(Liste)"""
    for i in range(1,len(goal)):
        L[i]=" _"

    l=''.join(L)
    print(l)



    global essaies
    if len(goal)<=5:
        essaies=8
    elif 5<len(goal)<=8:
        essaies=12
    else:
        essaies=17

    print("Vous avez",essaies,"chances")

def choix_reponse():
    if essaies==0:
        print("C'est perdu!Vvous n'avez plus de chances")
        print("Le mot cherché était",goal)
        return rejouer()
    else:
        choix=str(input("Si vous Pensez vous a un mot tapez:1 /Si vous pensez a une lettre tapez: 2"))
        if choix=="1":
            maj1()
        else:
            maj2()

def maj1():
    global essaies
    guess1=str(input("Entrer votre mot"))
    guess1=guess1.upper()
    essaies=essaies-1
    if guess1==goal:
        print("Vous avez proposé",guess1)
        print ("Félicitations le mot cherché était bien",goal,"!"" C'est Djinzin ;)")
        return rejouer()

    else:
        print("Vous avez proprosé",guess1)
        print("Ce n'est pas la bonne réponse!")
        print(l)
        print("Il vous reste ",essaies,"essaies")
        return choix_reponse()


def maj2():
    global essaies
    global L
    global l
    global Liste
    guess2=str(input("Donner une proposition de lettre"))
    guess2=guess2.upper()
    essaies=essaies-1
    L_indices = []
    cpt = False
    for ltr in goal :
        if ltr == guess2:
            cpt = True


    for i in range (len(goal)) :

        if cpt == True and guess2 == goal[i] :
            L_indices.append(i)

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
            print("Félicitation, le mot cherché était",goal)
            return rejouer()
        else:
            return choix_reponse()

    else:
        print("Vous avez choisi la lettre",guess2,)
        print("Ce n'est pas la bonne reponse")
        print(l)
        print("Il vous reste",essaies,"essaies")
        return choix_reponse()

jeu()



