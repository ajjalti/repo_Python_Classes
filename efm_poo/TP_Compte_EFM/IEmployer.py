from abc import ABC
from datetime import date
class IEmployer(ABC):


    def Calcul(dat)->int:
        today = str(date.today()) # 'anne-month-day'
        today = today.split('-')
        todayInDays = today[0]*365 + today[1]*12 + today[2]
        daysBefore = dat.split('-')
        daysBeforeInDays = daysBefore[0]*365 + daysBefore[1]*12 + daysBefore[2]
        return todayInDays//daysBeforeInDays

    # calcul d'age :
    def Age(dateNaissance)->int:
        IEmployer.Calcul(dateNaissance)
        
    # calcul d'anné d'encieneté:
    def ancienneté(dateDembauche)->int:
        IEmployer.Calcul(dateDembauche)

    # calcul de la date de retraite :
    # def dateRetraite(dateNaissance,ageRetraite)->str:
    #     dateNaissance = dateNaissance.split('-')
    #     dateNaissanceInDays = dateNaissance[0]*365 + dateNaissance[1]*12 + dateNaissance[2]
    #     ageRetraiteInDays = ageRetraite*365
    #     return 
