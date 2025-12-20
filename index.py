# Exo  1:
class personne:
    def __init__(self,nom,age):
        self.nom = nom
        self.age = age
    
    def se_presenter(self):
        print("Je m'appelle {} et j'ai {} ans.".format(self.nom, self.age))


# Exo  2:
p1 = personne("Safidy", 19)
p2 = personne("Mahefa", 13)
p3 = personne("Kezia", 18)
p1.se_presenter()
p2.se_presenter()
p3.se_presenter()

# Exo 3: Attribut privé
class compteBancaire:
    def __init__(self, titulaire):
        self.titulaire = titulaire
        self.__solde = 0              #__solde est un attr privé == _compteBancaire__solde  / attr privé = attr qui n'est pas accessible en dehors de la classe
    
    def deposer(self,montant):
        self.__solde = montant
        print("Dépot de {} Ar réussi.".format(montant))
    def retirer(self,montant):
        if montant > self.__solde:
            print("Solde insuffisant")
        else:
            self.__solde -= montant
            print("Retrait de {} Ar réussi.".format(montant))
    def afficherSolde(self):
         print("Solde du compte {} : Ar {} .".format(self.titulaire,self.__solde))

c1 = compteBancaire("BOA")
c1.deposer(500)
c1.retirer(100)
c1.afficherSolde()

# Exo 3: Méthodes simples
class rectangle:
    def __init__(self,largeur,hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
    def surface(self):
        surf = self.largeur * self.hauteur
        print("surface : {}".format(surf))

    def perimetre(self):
        per =  (self.largeur + self.hauteur) * 2
        print("perimetre : {}".format(per))
    
r1 = rectangle(4,2)
r1.surface()
r1.perimetre()

# =====NIV INTERMEDIAIRE ========
# Exo 5: Validation de données
class produit:
    def __init__(self,nom):
        self.nom = nom
        self.__prix = 0
    def set_prix(self,montant):
        if montant < 0:
            print("Erreur  :  Montant négatif !")
        else:
            self.__prix = montant
    def afficher(self):
        print("Produit : {} | Prix : {} $".format(self.nom,self.__prix))

prod = produit("Téléphone")
prod.set_prix(550)
prod.afficher()

# Exo 6: Classe avec compteur(attr statique)
class Utilisateur:
    nbUtilisateurs = 0 #L'attribut de la classe
    def __init__(self,nom):
        self.nom = nom
        Utilisateur.nbUtilisateurs += 1
    def afficher():
        print("Le nombre d'utilisateurs est : {}".format(Utilisateur.nbUtilisateurs))
u1 = Utilisateur("Kezia")
u2 = Utilisateur("Safidy")
Utilisateur.afficher()

# Exo 7: Composition (Un objet qui possede un objet d'une autre classe: une voiture a un moteur)
class Moteur:
    def __init__(self,puissance):
        self.puissance = puissance

class Voiture:
    def __init__(self,nom,puissance):
        self.nom = nom
        self.moteur = Moteur(puissance) #moteur est donc un objet d'une autre classe et n'existe qu'avec la voiture créee
    def description(self):
        print("Voiture: {}, Puissance: {} Chevaux".format(self.nom,self.moteur.puissance))

v1 = Voiture("McLaren",1200)
v1.description()

# Exo 8: Liste d'objets
class Etudiant:
    def __init__(self,nom,note):
        self.nom = nom
        self.note = note

class Classe:
    def __init__(self,nom):
        self.nom = nom
        self.etudiants = []
    def ajoutEtudiant(self,etudiant):
        self.etudiants.append(etudiant)
    def moyenne(self):
        moy = 0
        som = 0
        for etudiant in self.etudiants:
            som += etudiant.note
        moy = som/len(self.etudiants)
        print("La moyenne de la classe est : {}".format(moy))
e1 = Etudiant("Safidy",19.5)
e2 = Etudiant("Mahefa",13)
e3 = Etudiant("Kezia",18)
e4 = Etudiant("Steezi",14)
classe1 = Classe("IGGLIA")
classe1.ajoutEtudiant(e1)
classe1.ajoutEtudiant(e2)
classe1.ajoutEtudiant(e3)
classe1.ajoutEtudiant(e4)

classe1.moyenne()


# =====NIV AVANCE ========
# Exo 9 :Héritage simple
class Animal:
    def __init__(self,nom):
        self.nom = nom
    def parler(self):
        print("Bonjour, je suis un animal")

class Chat(Animal):
    def __init__(self, nom,age):
        super().__init__(nom) #appeler le constructeur de la classe mère : obligatoire
        self.age = age
    def parler(self): #La redefinition de la methode parler pour le chat
        print("Meow !")

class Chien(Animal):
    def __init__(self, nom, age):
        super().__init__(nom)
        self.age = age
    def parler(self): #La redefinition de la methode parler pour le Chien
        print("Woaff !")

chien = Chien("Max",5)
chat = Chat("Kitty",3)
chien.parler()
chat.parler()

# Exo 10 : Méthode abstraite : C'est une methode qui est obligatoire pour toute classe fille , c'est le plan à suivre, sinon: Erreur
#une classe qui a une methode abstraite est une classe abstraite. et toute fille de cette classe doiven suivre le plan des methodes abstraites de cette classe mère
from abc import ABC, abstractmethod #obligatoire

class Forme(ABC):
    @abstractmethod
    def aire(): #La methode abstraite que tt les filles doivent contenir sinon erreur et imposible d'instancier
        pass

class Carre(Forme):
    def __init__(self,c):
        super().__init__()
        self.c = c
    def aire(self):
        return self.c*2
class Rectangle(Forme):
    def __init__(self,l,L):
        super().__init__()
        self.l = l
        self.L = L
    def aire(self):
        return self.l * self.L
carr = Carre(4)
rect = Rectangle(4,2)


# Exo 11 : Super & Override
class Employe:
    def __init__(self,nom,salaire):
        self.nom = nom
        self.salaire = salaire
    def calculer_salaire(self):
        print("Salaire : {}".format(self.salaire))
        return self.salaire

class Manager(Employe):
    def __init__(self, nom, salaire):
        super().__init__(nom, salaire)
    def calculer_salaire(self):
        print("{} + Bonus: 500 = {} ".format(super().calculer_salaire(),super().calculer_salaire() + 500))

manager = Manager("Safidy",1000)
manager.calculer_salaire()

# Exo 12 : Polymorphisme reel