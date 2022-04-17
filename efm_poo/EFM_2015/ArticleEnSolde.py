from Article import Article


class ArticleEnSolde(Article):

    # constructeur :
    def __init__(
        self,
        code: int = 0,
        designation: str = "",
        prix: float = 0,
        categorie: str = "",
        remise=0,
    ):
        super().__init__(code, designation, prix, categorie)
        self._remise = remise

    # les accesseurs :
    def setRemise(self, remise) -> None:
        self._remise = remise

    def getRemise(self) -> float:
        return self._remise

    # redifinition de la methode getPrix():
    def getPrix(self) -> float:
        return super().getPrix() - (super().getPrix() * self.getRemise() / 100)
