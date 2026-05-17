













from django.contrib import admin
from .models import Article, Vente

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prix', 'quantite_en_stock')
    search_fields = ('nom',)

@admin.register(Vente)
class VenteAdmin(admin.ModelAdmin):
    list_display = ('article', 'date_vente', 'total')
    readonly_fields = ('date_vente', 'total')