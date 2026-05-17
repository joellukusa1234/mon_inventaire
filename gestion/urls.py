from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_articles, name='liste_articles'),
    path('vendre/<int:article_id>/', views.vendre_article, name='vendre_article'),
    path('recu/<int:vente_id>/', views.recu_vente, name='recu_vente'),
]