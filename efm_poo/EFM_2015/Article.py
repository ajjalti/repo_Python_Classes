class Article:

    # constructeur :
    def __init__(
        self, code: int = 0, designation: str = "", prix: float = 0, categorie: str = ""
    ):
        self._code = code
        self._designation = designation
        self._prix = prix
        self.setCategorie(categorie)

    # accesseur :
    def getCategorie(self) -> str:
        return self._categorie

    def setCategorie(self, categorie: str) -> None:
        catValid = ["Informatique", "Bureautoque", "informatique", "bureautique"]
        if categorie not in catValid:
            raise ValueError("la catégorie n'est pas valid")
        else:
            self._categorie = categorie

    def getPrix(self) -> float:
        return self._prix

    def setPrix(self, prix: float) -> None:
        self._prix = prix

    def getCode(self) -> int:
        return self._code

    def getDesignation(self) -> str:
        return self._designation

    # __str__()
    def __str__(self):
        return f"""{self.getCode()},{self.getDesignation()},{self.getPrix()},{self.getCategorie()}"""

    # Equal method :
    def __eq__(self, other: object) -> bool:
        return (
            self.getCode() == other.getCode()
            and self.getCategorie() == other.getCategorie()
            and self.getPrix() == other.getPrix()
            and self.getDesignation() == other.getDesignation()
        )
