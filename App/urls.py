from django.urls import path, include

from App.views import Affiche_projets, Affiche_projet, index_template, index2, index

urlpatterns = [
    path('a/', index),
    path('a/<classe>', index2),
    path('home', index_template),
    path('projet', Affiche_projet),
    path('projet2', Affiche_projets.as_view()),
    # path('delete_proj', Affiche_projets.as_view()),
]
