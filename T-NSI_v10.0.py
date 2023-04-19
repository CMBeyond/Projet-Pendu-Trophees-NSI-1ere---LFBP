#PENDUE - TROPHÉES NSI (Programme 2.10.0)

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

    rg=randint(0,len(word_list))
    rg-=1

    goal = word_list[rg]

    ##print(goal,"*objectif*")## ENLEVER LES GUILLEMETS (docstring) POUR AFFICHER LE MOT

generateur_de_mots()

def rejouer():

    restart=input("\nRejouer?")
    if restart=="oui" or "Oui" or "OUI":
        lettre_hasard()
        generateur_de_mots()
        jeu()

def jeu():

    global guess
    global hidden
    global end

    continuer=""
    end= 0
    essais= len(goal)+3

    print("\nnombre d'éssais:",essais)

    coups= 0

    hidden=[]
    for elmt in goal:
        hidden.append(" _ ")
        hidden[0]=lettre
    print(hidden)

    while end!=1:
        print("essais restants:",essais)
        guess=str(input("Quelle(s) sont la ou les lettres suivantes? "))

        print("Vous avez choisi",guess)

        list_g=[]
        congrats=0
        essais-=1
        coups+=1

        if len(guess) == 1:
            for g in range(0,len(guess)):
                list_g.append(guess.upper()[g])

        if len(list_g) == 1:
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

            end=1

        if " _ " not in hidden:
            print("\nBravo, tu as trouvé TOUTES les lettres en",coups,"coups!")
            print(goal)

            end=1

jeu()

###rejouer()###