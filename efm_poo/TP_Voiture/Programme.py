from Voiture import Voiture
class Programme:
    def __init__(self):
        self.tableVoitures=[]


# methode qui permit d'afficher tous les voitures disponible aux tableaux

    def showListe(self)->None:
        for voiture in self.tableVoitures:
            print(voiture)
# augmenter le nbr de cheveaux de tous les voitures d'un seule coup : 

    def upgrade(self)->None:
        for voiture in self.tableVoitures:
            voiture.updateNbrCheveaux()
        self.showListe()


# search by matricule :

    def searchByMatricule(self)->None:
        condition = False
        for voiture in self.tableVoitures:
            if voiture.getMatricule()==int(input()):
                print(voiture)
                condition= True
        if not condition:
            print("car doesn't exist")
        
                
        
        