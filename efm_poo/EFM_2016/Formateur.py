from Employer import Employer
from IR import IR
class Formateur(Employer,IR):
    
    _heureSup=0
    _remunirationHSup=70

    # constructeur : 
    def __init__(self,dateNais=0,datDaumbauche=0,mtl=0,salire=0,nom="",heurSup=0):
        super().__init__(dateNais,datDaumbauche,mtl,salire,nom)
        self._heureSup=heurSup
    
    def getRemunirationHSup(self)->int:
        return self._remunirationHSup


    # method salaireAPayer()

    def salaireAPayer(self)->float:
        return (self.getSalaireBase() + min(self._heureSup,30) * self.getRemunirationHSup())*(1-IR.getIR())

    # method __str__()

    def __str__(self) -> str:
        return f'''{super().__str__()}-
{self._heureSup}-
{self.getRemunirationHSup()}'''
    



    