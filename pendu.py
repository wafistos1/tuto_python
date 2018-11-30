""" Tuto de openclassroom LE PENDUE  
"""
from donnes import *
from fonctions import *


motMystere = "wafistos"
motComparer = ""

nb_coups = 5
i=0
while i < 5:#Boucle pricipale 
    lettre_rentrer = (input("Veuillez entrer une lettre: "))

    for lettre in motMystere:
        if lettre in lettre_rentrer:
            print(lettre_rentrer, end='')
            motComparer.(lettre_rentrer)

        else:
            print("*", end='')
    i+=1
    nb_coups -= 1 
    print()      
    print("il vous reste {} coups".format(nb_coups))
#Programme principal
