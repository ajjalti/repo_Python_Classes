# partie pour
# passer des tests

from ArticleEnSolde import ArticleEnSolde
from Facture import Facture

# création des objets:

article1 = ArticleEnSolde(1, "a", 23, "informatique", 1.3)
article2 = ArticleEnSolde(2, "c", 30, "informatique", 3)
article3 = ArticleEnSolde(3, "w", 40, "informatique", 2)
article4 = ArticleEnSolde(4, "d", 87, "bureautique", 1)

achat = Facture(article1, article2, article3, article4)

# enregestrer les achats dans un fichier csv:
achat.enregestrerAchat()

# afficher le buletin d'achat avec le total de la commande
print(achat.affichage())
