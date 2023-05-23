from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class EMP(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    adresse = models.CharField(max_length=200, null=True, blank=True)
    poste = models.CharField(max_length=200,null=True, blank=True)#poste occupé par l'employé
    department = models.CharField(max_length=255,null=True, blank=True)
    salary= models.DecimalField(max_digits=10, decimal_places=2,null=True)
    nbrAbsences = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name
    
