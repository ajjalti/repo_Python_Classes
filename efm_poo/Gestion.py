from Stagiaire import Stagiaire


class Gestion:
    def __init__(self):
        self.__listeStagiaires = []

    # accesseurs
    def setListeStagiares(self, *args) -> None:
        self.__listeStagiaires.extend(args)

    def getListeStagiaires(self) -> list:
        return self.__listeStagiaires

    # classement par moyenne :
    def Classement(self) -> None:
        data = []
        for stagiaire in self.__listeStagiaires:
            data.append(stagiaire.Calcul())
        data.sort()
        data.reverse()
        liste = []
        for i in range(len(data)):
            liste.append(self.SearchByMoyenne(data[i]))
        self.__listeStagiaires.clear()
        self.__listeStagiaires = liste.copy()

    # rechercher un stagiaire par moyenne :
    def SearchByMoyenne(self, moyenne) -> Stagiaire:
        for stg in self.__listeStagiaires:
            if stg.Calcul() == moyenne:
                return stg

    # rechercher un stg par matricule :
    def SearchByMatricule(self, matr) -> Stagiaire:
        for stg in self.getListeStagiaires():
            if stg.getMatricule() == matr:
                return stg

    # afficher tous les stagiaires :
    def Affichage(self) -> None:
        for stg in self.getListeStagiaires():
            print(stg)

    # modifier un stagiare :
    def Modify(self, stg: Stagiaire, *args) -> None:
        if len(args) == 1:
            stg.setNom(args[0])
        if len(args) == 2:
            stg.setNom(args[0])
            stg.setPrenom(args[1])
        if len(args) == 3:
            stg.setNom(args[0])
            stg.setPrenom(args[1])
            stg.setFiliere(args[2])
        if len(args) == 4:
            stg.setNom(args[0])
            stg.setPrenom(args[1])
            stg.setFiliere(args[2])
            stg.setNote1(args[3])
        if len(args) == 5:
            stg.setNom(args[0])
            stg.setPrenom(args[1])
            stg.setFiliere(args[2])
            stg.setNote1(args[3])
            stg.setNote2(args[4])
        if len(args) == 6:
            stg.setNom(args[0])
            stg.setPrenom(args[1])
            stg.setFiliere(args[2])
            stg.setNote1(args[3])
            stg.setNote2(args[4])
            stg.setNote3(args[5])

    # supprimer un stagiaire:
    def Del(self) -> None:
        self.__listeStagiaires.remove(self)

    # afficher la meilleur moyenne :

    def BestGrade(self) -> str:
        self.Classement()
        return f"""meilleur moyenne : {self.getListeStagiaires()[0].Calcul()}
nom du stagiaire : {self.getListeStagiaires()[0].getNom()+' '+self.getListeStagiaires()[0].getPrenom()}"""
