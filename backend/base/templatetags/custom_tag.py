from django import template
register=template.Library()
from ..models import EMP

def get_value(dictionnaire,key):
    return dictionnaire.get(key)



def addClasse(champs,arg):
    return champs.as_widget(attrs={'class':arg})


register.filter('getValue',get_value)
register.filter('addClasse',addClasse)