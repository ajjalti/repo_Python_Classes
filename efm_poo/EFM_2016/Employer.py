from abc import abstractmethod
from IEmployer import IEmployer
from comparable.simple import TextTitle
from datetime import datetime


class Employer(IEmployer):
    # les attributs:
    _dateNaissance = 0
    _mtle = 0
    _nom = ""
    _dateEmbauche = 0
    _salaireBase = 0

    # constructeur :
    def __init__(self,dateNais=0,datDaumbauche=0,mtl=0,salire=0,nom="") -> None:   
        self.setDateNaissance(dateNais)
        self.setDateDaumbauche(datDaumbauche)
        self._mtle=mtl
        self._salaireBase=salire
        self._nom=nom

    # les accesseurs : 
    def getNom(self)->str:
        return self._nom

    def getSalaireBase(self)->int:
        return self._salaireBase

    def getDateDaumbauche(self)->int:
        return self._dateEmbauche

    def getDateNaissance(self)->int:
        return self._dateNaissance

    def getMtle(self)->int:
        return self._mtle

    def setNom(self,nom:str)->None:
        self._nom=nom

    def setSalaireBase(self,salaire:int)->None:
        self._salaireBase=salaire

    def setMtle(self,mtl:int)->None:
        self._mtle=mtl

    # methode date de naissance :
    def setDateNaissance(self, datnaiss) -> None:
        if (self.Calcul(datnaiss) // 365) > 16:
            self._dateNaissance = datnaiss
        else :
            raise ValueError('A very specific bad thing happened.')


    # methode setDateDaumbauche : 
    def setDateDaumbauche(self,dat)->None:
        if(self.Calcul(dat) // 365)>16:
            self._dateEmbauche=dat
        else:
            raise ValueError('A very specific bad thing happened.')

    def Calcul(dat) -> int:
        todayInDays = (
            datetime.today().year * 365
            + datetime.today().month * 12
            + datetime.today().day
        )
        daysBefore = dat.split("-")
        daysBeforeInDays = (
            int(daysBefore[0]) * 365 + int(daysBefore[1]) * 12 + int(daysBefore[2])
        )
        return todayInDays - daysBeforeInDays

    @abstractmethod
    def salaireAPayer():
        pass


    # class __Eq__()
    def __eq__(self, other) -> bool:
        return self._mtle==other.getMtle()
    
        # calcul d'age :
    def Age(self,dateNaissance)->int:
        return self.Calcul(dateNaissance)//365
        
    # calcul d'anné d'encieneté:
    def ancienneté(self,dateDembauche)->int:
        return self.Calcul(dateDembauche)//365

    # calcul de la date de retraite :
    def dateRetraite(self,ageRetraite)->int:
          dateNaissance =   datetime.now().year - self.Age() 
          return dateNaissance+ageRetraite

    def Compare(self,other)->str:
        return TextTitle(self.getNom()) % TextTitle(other.getNom())


    # method __str__()

    def __str__(self) -> str:
        return f'''{self.getNom()}-
{self.getDateNaissance()}-
{self.getDateDaumbauche()}-
{self.getMtle()}-
{self.getSalaireBase()}'''
            