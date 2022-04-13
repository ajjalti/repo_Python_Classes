from Medecin import Medecin
class MedGeneraliste(Medecin):
    __nbrConsultasionsParAns=0
    __salaire=0

    # constructeur :
    def __init__(self,nom,prenom,sexe,email,adressCabinet,telephoneCabinet,nbrConsultasionsParAns,salaire)->None:
        super().__init__(nom,prenom,sexe,email,adressCabinet,telephoneCabinet)
        self.__nbrConsultasionsParAns=nbrConsultasionsParAns
        self.__salaire=salaire

    # les setters & getters: 

    def getNbrConParAn(self)->int:
        return self.__nbrConsultasionsParAns

    def getSalaire(self)->float:
        return self.__salaire

    def setNbrConParAn(self,nbr)->None:
        self.__nbrConsultasionsParAns=nbr

    def setSalaire(self,salaire)->None:
        self.__salaire=salaire

    # redifinition de la methode afficherinfos()

    def afficherinfos(self)->str:
        return f'''{self.getNom()}
{self.getPrenom()}
{self.getSexe()}
{self.getEmail()}
{self.getAdressCabinet()}
{self.getTelephoneCabinet()}
{self.getNbrConParAn()}
{self.getSalaire()}'''
