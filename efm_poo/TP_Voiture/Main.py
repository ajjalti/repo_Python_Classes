from Voiture import Voiture
from Programme import Programme

# trois objets de type Voiture:

# un objet par défault:
voiture1 = Voiture()

# deux objets avec initialisation des données:
voiture2 = Voiture("dacia", "noir", 49232323, 5)
voiture3 = Voiture("ferrari", "blue", 1243355, 35)

# deux objets avec initialisation de matricule seulement:
voiture4 = Voiture("", "", 494235535)
voiture5 = Voiture(None, None, 53434335)

# un objet de type Programme:
liste = Programme()

# remplir la liste de notre objet avec des voitures:
liste.remplir(voiture1, voiture2, voiture3, voiture4, voiture5)

# afficher la liste des voitures:
liste.showListe()

# incrémenter les nmbrs de cheveaux par un pour chaque voiture:
liste.upgrade()

# afficher voiture par matricul: 
liste.searchByMatricule()
