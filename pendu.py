""" Tuto de openclassroom LE PENDUE  
"""
from donnes import *
from fonctions import *


motMystere = "wafistos"

motComparer = "********"

print("**************************************************************")
print("************BIENVENUU AU JEU LE PENDU*************************")
print("**************************************************************")
nb_restant = 8
nb_coups = 8
i=0
while (i <= nb_restant) and motComparer != motMystere:#Boucle pricipale 
    lettre_rentrer = (input("Veuillez entrer une lettre: "))
    print()      
    print("il vous reste {} coups".format(nb_coups))
    
        
    motComparer = "".join([motMystere[ind] if motMystere[ind] == lettre_rentrer else motComparer[ind] for ind in range (len(motMystere))] )
    print(motComparer, end='')
    nb_coups-=1
    if motComparer == motMystere:
        print("  wBravo vous avez gagnez!!!en {} coups.".format(i+1))
    i+=1
        
    
    
#Programme principal
