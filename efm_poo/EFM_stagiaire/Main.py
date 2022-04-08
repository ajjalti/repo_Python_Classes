from Stagiaire import Stagiaire
from Gestion import Gestion
# initialisation des stagiaires :
stg1 = Stagiaire("Karimi","loubna","TSDM",1,11,16,17)
stg2 = Stagiaire("Jamal","Youssef","TSDM",2,14,15,20)
stg3 = Stagiaire("Ilham","Fayrouz","TSDM",3,12,13,15)

# print(stg1)
# print(stg2)
# print(stg3)

# stg2.setMatricule(1)

# print(stg1.Equals(stg2))

# initialisation de la classe Gestion:
liste = Gestion()

# add objects to the liste:
liste.setListeStagiares(stg1,stg2,stg3)

# print(liste.getListeStagiaires())

# for m in liste.getListeStagiaires():
#     print(m.Calcul())

# classer les objet par moyenne décroissante:
liste.Classement()

# print(liste.getListeStagiaires())

# for m in liste.getListeStagiaires():
#     print(m.Calcul())


# affichage de la liste des stagiaires:
liste.Affichage()

# searh by matricule number:
print(liste.SearchByMatricule(2))

#afficher la meilleur moyenne et son propriétère:
print(liste.BestGrade())

# mofidier un objet avec la classe Gestion:
liste.Modify(stg1,"ahmed")



