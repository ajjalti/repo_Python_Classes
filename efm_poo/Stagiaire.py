class Stagiaire:
    __Matricule: int = 0
    __Nom: str = ""
    __Prenom: str = ""
    __Filiere: str = ""
    __Note1: float = 0.0
    __Note2: float = 0.0
    __Note3: float = 0.0
    compteur = 0
    # les accesseurs :

    def getMatricule(self) -> int:
        return self.__Matricule

    def getNom(self) -> str:
        return self.__Nom

    def getPrenom(self) -> str:
        return self.__Prenom

    def getFiliere(self) -> str:
        return self.__Filiere

    def getNote1(self) -> float:
        return self.__Note1

    def getNote2(self) -> float:
        return self.__Note2

    def getNote3(self) -> float:
        return self.__Note3

    # les modificateurs

    def setMatricule(self, matricule) -> None:
        self.__Matricule = matricule

    def setNom(self, nom) -> None:
        self.__Nom = nom

    def setPrenom(self, prenom) -> None:
        self.__Prenom = prenom

    def setFiliere(self, filiere) -> None:
        self.__Filiere = filiere

    def setNote1(self, note) -> None:
        self.__Note1 = note

    def setNote2(self, note) -> None:
        self.__Note2 = note

    def setNote3(self, note) -> None:
        self.__Note3 = note

    # constructeur

    def __init__(self, *args):
        Stagiaire.compteur += 1
        self.__Matricule = Stagiaire.compteur
        if args:
            if len(args) == 1:
                self.__Nom = args[0]
            if len(args) == 2:
                self.__Nom = args[0]
                self.__Prenom = args[1]
            if len(args) == 3:
                self.__Nom = args[0]
                self.__Prenom = args[1]
                self.__Filiere = args[2]
            if len(args) == 7:
                self.__Nom = args[0]
                self.__Prenom = args[1]
                self.__Filiere = args[2]
                self.__Matricule = args[3]
                self.__Note1 = args[4]
                self.__Note2 = args[5]
                self.__Note3 = args[6]

    # methode RAZ:

    def RAZ(self) -> None:
        Stagiaire.compteur = 0

    # method Equals :

    def Equals(self, stg2) -> bool:
        if self.getMatricule() == stg2.getMatricule():
            return True
        return False

    # method Calcul :
    def Calcul(self) -> float:
        return (self.getNote1() + self.getNote2() + self.getNote3()) / 3

    # __str__()

    def __str__(self) -> str:
        return f"""Matricule : {self.getMatricule()}
Nom : {self.getNom()}
Prenom : {self.getPrenom()}
Filiere : {self.getFiliere()}
Note1 : {self.getNote1()}
Note2 : {self.getNote2()}
Note3 : {self.getNote3()}"""
