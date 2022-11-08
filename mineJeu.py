#Exercice :
    #Faire un mini-jeu qui affiche un message lorsque INPUT renvoie le bon caractère
    #Le caractère doit être paramétrable

#Définir miniJeuMegaCoolEtBranche qui affiche un message victorieux si INPUT renvoi le caractère choisis au moment de lancer la fonction (c'est un paramètre qui s'appelle charChoisis)
def miniJeu(charChoisis):
    #Appeler INPUT et stocker sa résultante dans la variable essaie
    essaie = input("Devine letter now : ")
    #Initialiser un compteur d'essaie
    nbTentatives = 1
    #Tant que essaie est différent de charChoisis
    while essaie != charChoisis:
        #Appeler INPUT et stocker sa résultante dans la variable essaie
        essaie = input("Devine letter now : ")
        #Incrémenter le compteur de tentatives
        nbTentatives = nbTentatives + 1
    #Affichage du message victorieux
    print("You're Winner")
    #Affichage du nombre de tentaives pour obtenir la victoire
    print("#1 Victoire Battle Royal en " + str(nbTentatives) + " essaies B-)")

miniJeu('e')