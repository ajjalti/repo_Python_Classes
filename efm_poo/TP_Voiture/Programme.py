from tokenize import Double
from Voiture import Voiture
class Programme:
    def __init__(self):
        self.tableVoitures=[]

# add viecule: 

    def remplir(self,*args)->None:
        if len(self.tableVoitures)<5:
            self.tableVoitures.extend(args)


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
        x=input('entrer le numero du matricul :')
        for voiture in self.tableVoitures:
            if voiture.getMatricul()==int(x):
                print(voiture)
                condition= True
        if not condition:
            print("car doesn't exist")
        
                
        
        