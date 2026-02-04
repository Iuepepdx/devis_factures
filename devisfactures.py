# Welcome to hell :D
estimates_counter = int(input("combien de devis voulez vous ?"))
id = str(input("Rentrez votre nom et prénom  ").split(" "))
print(id)
estimates = {}

# Fonction ajout de devis
def estimates_add(): 
    for i in range(estimates_counter): 
        estimates["Devis "+str(i)] = []
        estimates["Devis "+str(i)].append(input("Donnez une description\n"))
        estimates["Devis "+str(i)].append(input("Donnez la quantité\n"))
        estimates["Devis "+str(i)].append(input("Donnez le prix\n"))  
        print(estimates["Devis "+str(i)])
    return modele()

def modele():        # Fonction qui montre la facture
    if len(estimates[:[2]])>10:
        print("ok")

    else:
        for devis in range(estimates):
            print(f"votre {estimates["Devis "]+str(devis)}")

estimates_add()
'''
    print(f" ______________________________________________________________________\n|                                                                      |\n|                                                                      |\n|       Facture                             {comp_name}             |\n|                                                                      |\n|  {comp_adress}                                      |\n|  {client_name}                                                           |\n|  {client_adress}                                    |\n|                                                                      |\n|                                                                      |\n|  Facture N°: {fact_num}                                                  |\n|  Date : {fact_date}                                 |\n|  Echéance : {echeance}                              |\n |                                                                      |\n|                                                                      |\n|  Description:                         Quantité    Prix(€)    Montant ||                                                                      |\n")

    for i in range(len(prodlist)):
        montanttotal += prodlist[i][1]*prodlist[i][2]
        print("|  ",prodlist[i][0],"      ",prodlist[i][1]," ",prodlist[i][2]," ", prodlist[i][1]*prodlist[i][2],"|\n")

    print("|                                                                      |\n|  Montant total: ", montanttotal," " )
'''