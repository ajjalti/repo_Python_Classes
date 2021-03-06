from abc import ABC, abstractmethod, abstractproperty

# class impot sur revenu :
class IR(ABC):
    
    _tranches = [
        [0, 28000],
        [28001, 40000],
        [40001, 50000],
        [50001, 60000],
        [60001, 150000],
        [150001],
    ]
    _tauxIR = [0, 12, 24, 34, 38, 40]

    # fonction statique qui retourne le taux qui correspond au salaire passé en paramètre :
    @staticmethod
    def getIR(salaire):
        salaireAnnuel = salaire * 12
        table = IR._tranches
        if min(table[0]) <= salaireAnnuel <= max(table[0]):
            return IR._tauxIR[0]/100
        if min(table[1]) <= salaireAnnuel <= max(table[1]):
            return IR._tauxIR[1]/100
        if min(table[2]) <= salaireAnnuel <= max(table[2]):
            return IR._tauxIR[2]/100
        if min(table[3]) <= salaireAnnuel <= max(table[3]):
            return IR._tauxIR[3]/100
        if min(table[4]) <= salaireAnnuel <= max(table[4]):
            return IR._tauxIR[4]/100
        if table[5] <= salaireAnnuel:
            return IR._tauxIR[5]/100

print(IR.getIR(3000))