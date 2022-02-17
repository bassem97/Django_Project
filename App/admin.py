from django.contrib import admin

# Register your models here.
from App.models import Etudiant, Coach, Projet, MemberShipInProject


class MemberShip(admin.StackedInline):
    model = MemberShipInProject
    extra = 0

@admin.register(Projet)
class ProjetAdmin(admin.ModelAdmin):
    inlines  = (MemberShip,)
    list_display = ('nom_projet', 'duree_projet', 'temps_alloue', 'besoins', 'description', 'état', 'createur')
    fieldsets = (
        ('A propos', {'fields': ('nom_projet', 'besoins', 'description')}),
        ('Etat', {'fields': ('état',)}),
        ('Duree', {'fields': ('duree_projet', 'temps_alloue')}),
        (None, {'fields': ('createur', 'superviseur')}),
    )
    list_per_page = 2
    list_filter = ('état','createur')
    search_fields = ['nom_projet']

    def set_to_valid(self, request, queryset):
        # queryset.update(état=True)
        verif_false = False
        verif_true = False
        row_false = queryset.filter(état=False)
        row_true = queryset.filter(état=True)
        if row_false.count() > 0:
            queryset.update(état=True)
            verif = True
        if row_true.count() > 0 and not verif:
            queryset.update(état=False)
            # messages.error(request,'%s invalid'%row.count())

    set_to_valid.short_description = 'validate project'
    actions = ['set_to_valid']


admin.site.register(Etudiant)
admin.site.register(Coach)
