def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

def modulo(x,y):
    return x % y

def salaireNet(salaireBrut, coef):
    return salaireBrut * coef

def salaireParSeconde(salaireHoraire, heureParJourOuvre, nbJourOuvreParAn):
    return (salaireHoraire * heureParJourOuvre * nbJourOuvreParAn) / 31557600