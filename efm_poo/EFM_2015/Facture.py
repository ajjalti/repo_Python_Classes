import os
import csv
import datetime
from Article import Article


class Facture:
    _numFact = 0
    # constructeur:
    def __init__(self, *achats: Article) -> None:
        self._listeAchat = []
        self._listeAchat.extend(achats)
        Facture._numFact += 1
        self._dateFac = (
            datetime.datetime.now()
        )  # renvoie l'anne le mois le jour l'heure nmb minutes ,secondes, milliseconde

    # les acsseurs :
    def getListAchat(self) -> list:
        return self._listeAchat

    def getDateFacture(self):
        return self._dateFac

    # method ajouter(Article a)

    def ajouter(self, article: Article) -> None:
        if article not in self._listeAchat:
            self._listeAchat.append(article)
        else:
            raise ValueError("article existe d'éjà dans le panier")

    # montant de la facture :
    def montantFacture(self) -> float:
        total = 0
        for article in self.getListAchat():
            total += article.getPrix()
        return total

    # affichage des articles
    def affichage(self) -> str:
        content = f"""Designation\tremise\tprix\t\tquantité\tprixTotal\n"""
        for article in self.getListAchat():
            content += f"""{article.getDesignation()}\t\t{article.getRemise()}\t{article.getPrix()} DH \t 1\t\t{article.getPrix()} DH\n"""
        content += f"""\n\t\t\t\t\t\t\tTotal = {self.montantFacture()} DH"""
        return content

    # enregestrer _ achats :
    def enregestrerAchat(self) -> None:
        data = sorted(self.getListAchat(), key=lambda item: item.getDesignation())
        csvData = []
        for article in data:
            csvData.append(
                [
                    article.getCode(),
                    article.getDesignation(),
                    article.getPrix(),
                    article.getCategorie(),
                ]
            )
        chemin = os.getcwd()
        f = open(chemin + "/achat.csv", "wt")
        content = csv.writer(f, delimiter=";")
        content.writerow(["code", "designation", "prix", "categorie"])
        content.writerows(csvData)

    # __str__()

    def __str__(self) -> str:
        return f"""Numéro facture {Facture._numFact}  date facture {self.getDateFacture()}
Liste des achats 

{self.affichage()}
"""
