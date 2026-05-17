from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Vente

def liste_articles(request):
    articles = Article.objects.all()
    return render(request, 'gestion/liste.html', {'articles': articles})

def vendre_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if article.quantite_en_stock > 0:
        vente = Vente.objects.create(article=article, total=article.prix)
        article.quantite_en_stock -= 1
        article.save()
        return redirect('recu_vente', vente_id=vente.id)
    return redirect('liste_articles')

def recu_vente(request, vente_id):
    vente = get_object_or_404(Vente, id=vente_id)
    return render(request, 'gestion/recu.html', {'vente': vente})