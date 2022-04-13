from Medecin import Medecin


class MedSpecialiste(Medecin):

    __specialite=""
    __tarifHoraire=""

    # constructeur : 
    def __init__(self,nom,prenom,sexe,email,adressCabinet,telephoneCabinet,specialite,tarifHoraire)->None:
        super().__init__(nom,prenom,sexe,email,adressCabinet,telephoneCabinet)
        self.__specialite=specialite
        self.__tarifHoraire=tarifHoraire


    # les setters : 
    def getSpecialite(self)->str:
        return self.__specialite

    def getTarifHoraire(self)->str:
        return self.__tarifHoraire

    def setSpecialite(self,specialite)->None:
        self.__specialite=specialite

    def setTarifHoraire(self,tarif)->None:
        self.__tarifHoraire=tarif

    # redifinition de la methode afficherinfos()

    def afficherinfos(self)->str:
        return f'''{self.getNom()}
{self.getPrenom()}
{self.getSexe()}
{self.getEmail()}
{self.getAdressCabinet()}
{self.getTelephoneCabinet()}
{self.getSpecialite()}
{self.getTarifHoraire()}'''