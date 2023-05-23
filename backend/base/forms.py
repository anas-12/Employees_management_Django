from django import forms
from .models import EMP

class EmpForm(forms.ModelForm):
    poste = forms.ChoiceField(choices=[
        ('Manager', 'Manager'),
        ('Assistant manager', 'Assistant manager'),
        ('Employé de bureau', 'Employé de bureau'),
        ('Technicien', 'Technicien'),
        ('Assistant marketing','Assistant marketing'),
        ('Responsable des ventes','Responsable des ventes')
    ])

    class Meta:
        model = EMP
        fields = '__all__'
        widgets = {
            'poste': forms.Select(attrs={'class': 'form-control'})
        }
        

class FeedbackForm(forms.Form):
    email = forms.EmailField(label="Entrez votre email", max_length=100)
    name = forms.CharField(label="Entrez votre nom", max_length=100)
    feedback = forms.CharField(label="Votre Feedback", widget=forms.Textarea)
    
    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
