#DEBUT

#Définir une fonction withdrawFees qui retire un pourcentage a un total en fonction d'un total et d'un pourcentage
def withdrawFees(total, percent):
    #Définir fees en fonction d'un total et d'un pourcentage
    fees = total * (percent/100)
    #Soustraire fees au total
    result = total - fees
    #Retourner la valeur obtenue
    return result

#Définir une fonction qui retourne le salaire net en fonction du salaire brut(float) et du secteur d'activité(boolean)
def calculBrutEnNet(salaireBrut, isPublic):
    #Si je suis un trvailleur du secteur public
    if isPublic: 
        #Alors je soustrais 15% de mon salaire Brut et je l'assigne à une variable salaireNet
        salaireNet = salaireBrut - (salaireBrut * 15 /100)
    #Sinon : Je suis travailleur du secteur privé
    else:
        #Alors je soustrais 23% de mon salaire Brut et je l'assigne à une variable salaireNet
        salaireNet = salaireBrut - (salaireBrut * 23 /100)
    #Retourner salaireNetx
    return salaireNet

#FIN

    #Sinon : Je suis travailleur du secteur privé
        #Alors je soustrais 23% de douille bien à l'ancienne à l'argent de mon labeur durement gagné