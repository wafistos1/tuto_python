""" Tuto de openclassroom LE PENDUE  
"""
import random
from donnes import *
from fonctions import *


#Programme principal
motMystere = random.choice(liste_des_mots)
motComparer = "*"*len(motMystere)
score = 0

#Ajouter Joueur
nom_joueur = input("Entrez votre nom: ")
dico = {nom_joueur: score} 

print("**************************************************************")
print("************BIENVENUU AU JEU LE PENDU*************************")
print("**************************************************************")


print(motMystere)
print()
nb_restant = 8
nb_coups = 8
i=0
while (i <= nb_restant) and motComparer != motMystere:#Boucle pricipale 
    lettre_rentrer = (input("\nVeuillez entrer une lettre: "))
    lettre_rentrer = lettre_rentrer.lower()
     
    print()      
    print("il vous reste {} coups".format(nb_coups))
    
        
    motComparer = "".join([motMystere[i] if motMystere[i] == lettre_rentrer else motComparer[i] for i in range(len(motComparer))] )
    print(motComparer, end='')
    nb_coups-=1
    
    
    i+=1
        
if motComparer == motMystere:
        score = nb_coups + 3
        dico[nom_joueur] = score 
        print("\nBravo  vous avez gagnez!!!en {} coups.\n votre score est {} points".format(i, dico[nom_joueur])) 
else:
        print("\nDesole vous avez perdu!! :( \nle mot mystere etais '{}'".format(motMystere.upper()))
    

