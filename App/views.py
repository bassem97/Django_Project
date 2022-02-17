from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from App.models import Projet


def index(request):
    return HttpResponse("salamou3alayakom nesi w a7bebei")


def index2(request, classe):
    return HttpResponse("salamou3alayakom nesi w a7bebei " + classe)


def index_template(request):
    return render(request, 'index.html')


def Affiche_projet(request):
    # return HttpResponse('--'.join(p.nom_projet for p in Projet.objects.all()))
    return render(request, 'index.html', {'projets': Projet.objects.all()})


class Affiche_projets(ListView):
    model = Projet
    template_name = 'index.html'
    context_object_name = 'projets'

# class delete_projet(request)
