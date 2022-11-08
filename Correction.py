#DEBUT

def salaireNet(salaireBrut, coeff):
    return salaireBrut - (salaireBrut * coeff)

def salaireParSeconde(salaireHoraire, heureParJourOuvre, jourOuvreParAn):
    #Calculer mon salaire annuel
    salaireAnnuel = salaireHoraire * heureParJourOuvre * jourOuvreParAn
    #Calculer le nombre de seconde dans une année
    nbSecondesParAn = 365 * 24 * 60 * 60
    #Je pose et retourne la division
    return salaireAnnuel / nbSecondesParAn

#FIN