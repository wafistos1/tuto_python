"""Fichier qui contient les fonctions """
dico={}

#Creer une fonction qui verifie si le nom du joueur existe ou non 
def verifier(nom_joueur):
    with open("fichier.txt", "r") as mon_fichier:
        contenu1 = {} 
        contenu = mon_fichier.read()
        contenu = contenu.splitlines()
    for ele in contenu:
         
        contenu1 =  ele.split(":")


    print(contenu1)
    for element in contenu:
        if element == nom_joueur:
            print("bonjour {} ".format(nom_joueur))
            return True
        else:
            print("Bienvenue vous etes un nouvelle joueur")
            return False

verifier("wafistos")


#print(contenu)

    