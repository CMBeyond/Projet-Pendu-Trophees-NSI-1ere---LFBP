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
    print(goal,"*objectif*")

generateur_de_mots()

def correspondance():

    global guess

    global false_guess
    global right_guess

    global liste_g
    global final

    global all_letters

    right_guess = 0
    false_guess = 0
    all_letters = 0

    guess=''

    liste_g = []
    final = []

    for elmt in liste_g:
        for i in range(0,len(liste_g)):
            if i == goal[i]:
                final.insert(i,goal[i].index(i))
                right_guess+=1

            else: false_guess+=1

    if len(liste_g) == len(goal):
        all_letters=1

def jeu():

    global all_letters

    all_letters = 0
    right_guess = 0
    false_guess = 0

    while all_letters==0:
        guess=str(input("Quelle est la lettre suivante"))

        liste_g=[guess]
        print(liste_g)

        correspondance()

        if right_guess>0 and false_guess>0:
            print("Bravo! Tu as trouvé",right_guess,"lettres mais",false_guess,"lettre(s) est/sont faux(sses), essaye encore! (Tu perds un essai...)")

        elif right_guess>0:
            print("Bravo! Tu as trouvé",right_guess,"lettre(s)")

        elif false_guess>0:
            print("Mauvaise(s) lettre(s), essaye encore!")

        right_guess = 0
        false_guess = 0

jeu()

#IL MANQUE LES ESSAIS