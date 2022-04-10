from Employer import Employer
from IR import IR


class Agent(Employer, IR):

    _primeResponsabilite = 0

    def __init__(self, dateNais=0, datDaumbauche=0, mtl=0, salire=0, nom="", prime=0) -> None:
        super().__init__(dateNais, datDaumbauche, mtl, salire, nom)
        self._primeResponsabilite = prime

    # method salaireAPayer():

    def salaireAPayer(self) -> float:
        return (self.getSalaireBase() + self._primeResponsabilite) * (1 - self.getIR())
