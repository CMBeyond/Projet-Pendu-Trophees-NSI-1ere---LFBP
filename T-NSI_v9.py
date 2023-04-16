#PENDUE - TROPHÉES NSI

from random import randint

def lettre_hasard():

    global lettre
    nbr=randint(65,90)
    lettre=chr(nbr)

lettre_hasard()

def generateur_de_mots():

    global word_list
    global rg #(random_goal)
    global goal

    word_list=[]

    fichier=open("registre_de_mots_2.txt","r")

    for word in fichier:
        word=word.replace('\n','')
        for elmt in word[0]:
            if elmt==lettre:
                word_list.append(word)

    rg=randint(0,len(word_list)-1)

    goal = word_list[rg]
    """ print(goal,"*objectif*") """ # ENLEVER LES GUILLEMETS (docstring) POUR AFFICHER LE MOT

generateur_de_mots()

def jeu():

    global guess
    global hidden
    global resolu

    resolu=0
    essais= 8

    if len(goal)<8:
        essais= 9-len(goal)

    print("nombre d'éssais:",essais)

    coups= 0

    hidden=[]
    for elmt in goal:
        hidden.append(" _ ")
        hidden[0]=lettre
    print(hidden)

    while resolu!=1:
        print("essais restants:",essais)
        guess=input("Quelle(s) sont la ou les lettres suivantes? ")

        list_g=[]
        congrats=0
        essais-=1
        coups+=1

        for h in range(0,len(guess)):
            list_g.append(guess[h])

        for i in range(0,len(goal)):
            if goal[i] in list_g:
                hidden[i]=goal[i]
                congrats=1

        if congrats==1:
            print("\nBravo tu as trouvé une/des lettre(s)!")
        else: print("\nCe n'est pas la bonne lettre...")

        print(hidden)

        if essais==0 and " _ " in hidden:
            print("\nIl ne te reste plus aucun essais... dommage!")
            print("Le mot était ...",goal)
            resolu=1

        if " _ " not in hidden:
            print("\nBravo, tu as trouvé TOUTES les lettres en",coups,"coups!")
            print(goal)
            resolu=1

jeu()

#IL MANQUE LES ESSAIS ET LES LETTRES A CACHER