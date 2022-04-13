from Medecin import Medecin
from MedGeneraliste import MedGeneraliste
from MedSpecialiste import MedSpecialiste


class Menu:

    listeMedecin=[]

    @staticmethod
    def Ajouter():
        choix = input("entrer le type de medecin que vous vouler ajouter : [specialiste => 1  /  generaliste => 2] :")
        match choix:
            case "1":
                Menu.listeMedecin.append(MedSpecialiste(input("entrer nom :"),input("entrer prenom :"),input("entrer sexe :"),input("entrer email :"),input("entrer adress cabinet :"),input("entrer telefone cabinet :"),input("entrer specialite :"),input("entrer tarif horaire :")))
            case "2":
                Menu.listeMedecin.append(MedGeneraliste(input("entrer nom :"),input("entrer prenom :"),input("entrer sexe :"),input("entrer email :"),input("entrer adress cabinet :"),input("entrer telefone cabinet :"),input("entrer nombre de consultation par ans :"),input("entrer le salaire :")))
    @staticmethod
    def Supprimer(nom):
        for med in Menu.listeMedecin:
            if med.getNom()==nom:
                choix = input("voulez vous vraiment supprimer cet medecin ? [oui / non] :")
                match choix:
                    case "oui":
                        Menu.listeMedecin.remove(med)
                        return
                    case "non":
                        pass
                        return
        print("le medecin n'existe pas dans la base de donné")
                
        
    @staticmethod
    def Consulter(nom):
        for med in Menu.listeMedecin:
            if med.getNom()==nom:
                print(med.afficherinfos())
            else:
                print("medecin n'éxiste pas dans la base de donnée")
    @staticmethod
    def Lister():
        for med in Menu.listeMedecin:
            print(med.afficherinfos())
        

    def Quitter():
        pass



