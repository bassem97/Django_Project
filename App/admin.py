from django.contrib import admin

# Register your models here.
from App.models import Etudiant, Coach, Projet


@admin.register(Projet)
class ProjetAdmin(admin.ModelAdmin):
    list_display = ('nom_projet', 'duree_projet', 'temps_alloue', 'besoins', 'description', 'état', 'createur')
    fieldsets = (
        ('A propos', {'fields': ('nom_projet', 'besoins', 'description')}),
        ('Etat', {'fields': ('état',)}),
        ('Duree', {'fields': ('duree_projet', 'temps_alloue')}),
        (None, {'fields': ('createur', 'superviseur')}),
    )
    list_per_page = 2

    def set_to_valid(self, request, queryset):
        queryset.update(état=True)

    set_to_valid.short_description = 'validate project'
    actions = ['set_to_valid']


admin.site.register(Etudiant)
admin.site.register(Coach)
