#Suite du cours de openclassroom sur les dictionnaire 

mon_dictionnaire = {}#Creation d'un dico vide 
mon_dictionnaire1= {
    "nom": "Wafi",
    "prenom": "mameri",
    "age": 43
}


print(mon_dictionnaire1)


#Suite de la lecons sur les fichier sur openclassroom 

"""
    Les mode d'ouvertures du fichier
        'r' : ouverture en lecture (Read)
        'w' : ouverture en ecriture(Write). On ecrase si le fichier n'est pas vide
        'a' : ouverture en mode ajout(Append). On ecrit a la fin 
    le mot-cle "with" : ex- with open(le_fichier, mode_ouverture) as variable 
"""
""" Exemples """

""" MODE LECTURE"""
mon_fichier = open("fichier.txt", "r")#ouvrir le fichier en mode lecture 
contenu = mon_fichier.read()#On met tout le contenu du fichier dans un chaine 
print(contenu)# affiche le contenu 
mon_fichier.close()#Fermer le fichier 

"""MODE ECRITURE"""
monFichier = open("fichier.txt", "w")
monFichier.write("Salut je suis une nouvelle phrase dans le fichier texte.")
monFichier.close()
#Ouvrir le fichier pour voir les modifications 
monFichier1 = open("fichier.txt", "r")
contenu = monFichier1.read()
print(contenu)
monFichier1.close()

"""MODE AJOUT"""
monFichier = open("fichier.txt", "a")
monFichier.write("\nCoucou, je suis ajouter apres le dernier texte.")
monFichier.close()
#Ouvrir le fichier pour voir les modifications 
mon_fichier = open("fichier.txt", "r")
contenu = mon_fichier.read()
print(contenu)
mon_fichier.close()
input()

""" MODE WITH"""
with open('fichier.txt', 'r') as mon_fichier:
    texte = mon_fichier.read()
    print(texte)
    