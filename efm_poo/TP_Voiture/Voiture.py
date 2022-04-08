class Voiture:
    def __init__(
        self,
        marque: str = "",
        color: str = "",
        matricul: int = 0,
        nbrcheveaux: int = 0,
    ) -> None:
        self.__marque = marque
        self.__color = color
        self.__matricul = matricul
        self.__nbrcheveaux = nbrcheveaux

    # les accesseurs :

    def getMarque(self) -> str:
        return self.__marque

    def getColor(self) -> str:
        return self.__color

    def getNbrCheveaux(self) -> int:
        return self.__nbrcheveaux

    def getMatricul(self) -> int:
        return self.__matricul

    # les modificateurs :

    def setMarque(self, marque: str) -> None:
        self.__marque = marque

    def setColor(self, color: str) -> None:
        self.__color = color

    def setNbrCheveaux(self, nbr: int) -> None:
        self.__nbrcheveaux = nbr

    def updateNbrCheveaux(self)->None:
        self.__nbrcheveaux+=1

    # methode presentation():

    def Presentation(self) -> str:
        return self.__str__()

    # __str__()

    def __str__(self) -> str:
        return f"""la marque : {self.getMarque()}
la couleur : {self.getColor()}
la matricule : {self.getMatricul()}
le nombre de cheveaux : {self.getNbrCheveaux()}
        """
