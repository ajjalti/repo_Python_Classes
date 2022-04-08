from xmlrpc.client import DateTime


class Employer:
    _dateEmbauche = "jj-month-anne"
    _dateNaissance = "jj-month-anne"
    _mtle = 0
    _nom = ""
    _salaire = 0
    cpt = 0

    def __init__(self, *args):
        if len(args) == 6:
            if Employer.numbreDanne(args[0]) > 5840:
                self._dateEmbauche = args[0]
            if Employer.numbreDanne(args[1]) > 5840:
                self._dateNaissance = args[1]
            self._mtle = args[2]
            self._nom = args[3]
            self._salaire = args[4]
            self.cpt = args[5]

    @classmethod
    def numbreDanne(cls, date):
        day = DateTime().timetuple()[0]
        month = DateTime().timetuple()[1]
        year = DateTime().timetuple()[2]
        datee = date.split("-")
        entree = date[2] * 365 + date[1] * 30 + date[0]
        sortie = year * 365 + month * 30 + day
        return sortie - entree

    