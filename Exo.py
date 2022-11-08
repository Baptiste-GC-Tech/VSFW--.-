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

tableau = [0, 10, 15, 5, 1]
print(tableau[2]) #Affiche le 15
len(tableau) #Renvoi 5 (la longueur du tableau)

#Exercice 1 :
    #Faire une fonction qui concatene 2 chaîne de caraftères, les séparants par une virgule

#Exercice 2 :
    #Faire une fonction qui itére sur tous les index d'un tableau renvoyant une chaîne de caractères avec l'ensemble des occurences de'un chiffre
    #eg : Pour [0,1,1,1,0,1,1,0,1]
    #La fonction(tableau, 0) doit renvoyer "0, 4, 7" avec la première fonction

#Exercice 3 :
    #Renvoyer / Afficher un message

#FIN