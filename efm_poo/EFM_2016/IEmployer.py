from abc import ABC, abstractmethod
from datetime import date, datetime


class IEmployer(ABC):

    @abstractmethod
    # calcul d'age :
    def Age(dateNaissance) -> int:
        pass

    @abstractmethod
    # calcul d'anné d'encieneté:
    def ancienneté(dateDembauche) -> int:
        pass

    @abstractmethod
    # calcul de la date de retraite :
    def dateRetraite(ageRetraite) -> int:
        pass
