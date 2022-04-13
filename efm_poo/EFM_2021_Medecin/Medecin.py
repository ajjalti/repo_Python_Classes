import re
class Medecin:
    __nom=""
    __prenom=""
    __sexe=""
    __email=""
    __adressCabinet=""
    __telephoneCabinet=""
    compteur=0

    # constructeur : 

    def __init__(self,nom,prenom,sexe,email,adressCabinet,telephoneCabinet)->None:
        self.__nom=nom
        self.__prenom=prenom
        self.__sexe=sexe
        self.setEmail(email)
        self.__adressCabinet=adressCabinet
        self.__telephoneCabinet=telephoneCabinet
        Medecin.compteur+=1

    # les setters et getters : 

    def getNom(self)->str:
        return self.__nom

    def getPrenom(self)->str:
        return self.__prenom
    
    def getSexe(self)->str:
        return self.__sexe

    def getEmail(self)->str:
        return self.__email

    def getAdressCabinet(self)->str:
        return self.__adressCabinet

    def getTelephoneCabinet(self)->str:
        return self.__telephoneCabinet

    def setNom(self,nom)->None:
        self.__nom=nom

    def setPrenom(self,prenom)->None:
        self.__prenom=prenom

    def setEmail(self,email):
        if re.match("^[a-zA-Z]+.[a-zA-Z]+@[a-zA-Z]+.[a-z]{2}$",email)!=None:
            self.__email=email
        else:
            raise Exception("email not valid !")
            

    def setAdressCabinet(self,adress)->None:
        self.__adressCabinet=adress

    def setTelephoneCabinet(self,tel)->None:
        self.__telephoneCabinet=tel

# method afficheinfos()

def afficherinfos(self)->list:
    return [self.getNom(),self.getPrenom(),self.getAdressCabinet(),self.getTelephoneCabinet()]

print(re.match("^[a-zA-Z]+.[a-zA-Z]+@[a-zA-Z]+.[a-z]{3}$","ahmed.ajjalti@gmail.com"))


