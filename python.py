#coding:utf-8

class Humain:
    """Classe qui definit un humain"""
    lieu_habitation = "Terre"

    def __init__(self, name, age):
        self.name = name
        self.age  = age
        print("Un humain qui s'appelle {} et qui a {} ans a ete cree. ".format(self.name, self.age))
    
    def parler(self, message):
        print("{} a dit : {}".format(self.name, message))
        print("ton lieu d'habitations est : ", self.lieu_habitation)

    
    def changer_planete(cls, nouvelle_planete):#methode de class
        Humain.lieu_habitation = nouvelle_planete
    
    changer_planete = classmethod(changer_planete)

    def definiton():
        print("Bonjour vous etes dans la fonction statique")
    
    definiton = staticmethod(definiton)
        

#Programme pricipal


h1 = Humain("wafi", 42)
h1.parler("Salut!!")


print("Planete actuelle : {}". format(Humain.lieu_habitation))
Humain.changer_planete("Mars")

print("Planete apres changement : {}".format(Humain.lieu_habitation))

h1.changer_planete("Pluto")
h1.parler("Salutot")

Humain.definiton()