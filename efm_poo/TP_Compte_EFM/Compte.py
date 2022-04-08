from random import random
from datetime import datetime
class Compte:
    __numero:int=0
    __dateDouverture=""
    __solde:float=0.0

    def __init__(self,solde=0):
        self.__numero=random.randint(10000,99999)
        self.__dateDouverture=datetime.today().date()
        self.__solde=solde  

# les accesseurs : 
    def getNumero(self)->int:
        return self.__numero
    def getDateDouverture(self)->str:
        return self.__dateDouverture
    def getSolde(self)->float:
        return self.__solde

    def setNumero(self,numero)->None:
        if len(str(numero))==5:
            self.__numero=numero
    def setDateDouverture(self,datedouverture:datetime)->None:
        self.__dateDouverture=datedouverture
    def setSolde(self,solde)->None:
        self.__solde=solde
    
# methode créditer :
    
    def Crediter(self,montant:float)->None:
        self.__solde+=montant

# methode débiter : 

    def Débiter(self,montant:float)->None:
        if self.__solde>montant:
            self.__solde-=montant
    

            

