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
#FIN