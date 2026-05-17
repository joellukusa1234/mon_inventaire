from django.db import models

class Article(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    quantite_en_stock = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nom} ({self.prix} $)"

class Vente(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    date_vente = models.DateTimeField(auto_now_add=True)
    quantite = models.IntegerField(default=1)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Vente de {self.article.nom} le {self.date_vente}"