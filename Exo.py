#DEBUT
def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def multiply(x,y):
    return x * y

#Définir une fonction qui retourne le résultat de la division de x par y
def divide(x,y):
    #Vérifie si le diviseur est 0
    if y == 0:
        #Afficher un message d'erreur
        print("Wsh tfq tu divises pas par 0 où je te démarre")
        #Retourner vide
        return
    #Sinon, effectuer la division
    else:
        #Retourner le résultat de la division
        return x / y

#Définir une fonction qui retourne le reste de la division euclidienne de x par y
def modulo(x,y):
    #Vérifie si le diviseur est 0
    if y == 0:
        #Afficher un message d'erreur
        print("Wsh tfq tu divises pas (euclidiennement) par 0 où je te démarre")
        #Retourner vide
        return
    #Sinon, effectuer la division euclidienne
    else:
        #Retourner le reste de la division euclidienne
        return x % y

def salaireNet(salaireBrut, coef):
    return salaireBrut * coef                   #sa c fo wsh
    return salaireBrut - (salaireBrut * coef)   #ça c'est bon

def salaireParSeconde(salaireHoraire, heureParJourOuvre, nbJourOuvreParAn):
    return (salaireHoraire * heureParJourOuvre * nbJourOuvreParAn) / 31557600


def INPUT():
    return 'a'
    #POV : la fonction marche déjà (tg c magik)
    #Renvoi un caractere de type string au hasard

#Exercice :
    #Faire un mini-jeu qui affiche un message lorsque INPUT renvoie le bon caractère
    #Le caractère doit être paramétrable

#Définir miniJeuMegaCoolEtBranche qui affiche un message victorieux si INPUT renvoi le caractère choisis au moment de lancer la fonction (c'est un paramètre qui s'appelle charChoisis)
def miniJeuMegaCoolEtBranche(charChoisis):
    #Appeler INPUT et stocker sa résultante dans la variable essaie
    essaie = INPUT()
    #Initialiser un compteur d'essaie
    nbTentatives = 1
    #Tant que essaie est différent de charChoisis
    while essaie != charChoisis:
        #Appeler INPUT et stocker sa résultante dans la variable essaie
        essaie = INPUT()
        #Incrémenter le compteur de tentatives
        nbTentatives = nbTentatives + 1
    #Affichage du message victorieux
    print("You're Winner")
    #Affichage du nombre de tentaives pour obtenir la victoire
    print("#1 Victoire Battle Royal en " + nbTentatives + " essaies B-)")

#Exercice 1 :
    #Faire une fonction qui concatene 2 chaîne de caraftères, les séparants par une virgule

#Définir la fonction concatenate(stringA, stringB) qui répond aux attentes de l'exo 1
def concatenate(stringA, stringB):
    #Initialiser stringifiedA à str(stringA) pour s'assurer d'avoir le bon type
    stringifiedA = str(stringA)
    #Initialiser stringifiedB à str(stringB) pour s'assurer d'avoir le bon type
    stringifiedB = str(stringB)
    #Initialiser la varibale stringFinal à la conctéantion de string1, ", " et string2
    stringFinal = stringifiedA + ", " + stringifiedB
    #Retourner stringFinal
    return stringFinal

#Exercice 2 :
    #Faire une fonction qui itére sur tous les index d'un tableau renvoyant une chaîne de caractères avec l'ensemble des occurences d'un chiffre
    #eg : Pour [0,1,1,1,0,1,1,0,1]
    #La fonction(tableau, 0) doit renvoyer "0, 4, 7" n'hésitez pas à implémenter la première fonction ;)

#Définir la fonction findIndex(tab, elem) qui retourne un string comprenant tout les index où se trouve l'élément recherché
def findIndex(tab, target):
    #Initialiser un pointeur (int)i
    i = 0
    #Initialiser (string)locations vide
    locations = ''
    #Initialiser (boolean)firstTurn à True
    firstTurn = True
    #Tant que i est strictement inférieur à la taille de tab, Alors...
    while i < len(tab):
        #Si tab[i] est égal à target, Alors...
        if tab[i] == target:
            #Si firstTurn est égal à True, Alors...
            if firstTurn == True:
                #Assigner str(i) à locations
                locations = str(i)
                #Assigner firstTurn à False
                firstTurn = False
            #Sinon : firstTurn est différent de True, Alors...
            else:
                #Assigner le retour de concatenate(locations, i) à locations
                locations = concatenate(locations, i)
        #Incrémenter i de 1
        i = i + 1
    #Afficher locations
    print(locations)

#Exercice 3 :
    #Renvoyer / Afficher un message

#Définir la fonction returnString(string) qui retourne un string sous forme de variable
def returnString(string):
    #Afficher string
    print(string)
    #Retourner string
    return string

#Exo bonus yay :
    #Suite de Fibonacci en fonction d'uen valeur de départ et du nombre d'occurence (max 10)

#Définir fibo(startingValue, nbTurn) qui affiche les nbTurn première valeurs depuis startingValue avec la règle de Fibonacci
    #Si nbTurn > 10, Alors...
        #Gronder l'utilisateur (povre CPU smh) et lui dire qu'on en fera que 10
        #

#FIN