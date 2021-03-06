from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


def is_esprit_mail(email):
    if not str(email).endswith('@esprit.tn'):
        raise ValidationError("Votre email est invalide ", params={'value': email})

    # Create your models here.


class User(models.Model):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    email = models.EmailField('Email', validators=[is_esprit_mail])
    def __str__(self):
    #     # return  'prenom : '+ self.prenom + ', nom : '+self.nom+', email : '+self.email
        return f'prenom={self.prenom}, nom={self.nom},email={self.email} '

class Etudiant(User):
    groupe = models.CharField(max_length=30)


class Coach(User):
    pass


class Projet(models.Model):
    nom_projet = models.CharField('Titre Projet', max_length=30)
    duree_projet = models.IntegerField('Duree Estime', default=0)
    temps_alloue = models.IntegerField('Temps alloué ', validators=[MinValueValidator(1), MaxValueValidator(10)])
    besoins = models.TextField(max_length=100)
    description = models.TextField(max_length=100)
    état = models.BooleanField(default=False)

    # One to One
    createur = models.OneToOneField(
        Etudiant,
        related_name="project_owner",
        on_delete=models.CASCADE
    )

    # One to many
    superviseur = models.ForeignKey(
        Coach,
        on_delete=models.SET_NULL,
        null = True,
        related_name='project_coach'
    )

    # Many to Many
    members = models.ManyToManyField(
        Etudiant,
         # table association
        through='MemberShipInProject',
        related_name='les_membres'
    )


class MemberShipInProject(models.Model):
    projet = models.ForeignKey(Projet,on_delete=models.CASCADE)
    etudiant = models.ForeignKey(Etudiant,on_delete=models.CASCADE)
    time_allocated_by_member = models.IntegerField('Temps alloué par etudiant')
