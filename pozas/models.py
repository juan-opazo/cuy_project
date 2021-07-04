from django.db import models
from django import forms
from django.forms import ModelForm
from django.utils import timezone

POZA_CHOICES = [
    ('REPRODUCTORA', 'Reproductora'),
    ('RECRIA', 'Recria'),
    ('ENGORDE', 'Engorde'),
]
RAZA_CHOICES = [
    ('INTI', 'Inti')
]

# Create your models here.
class Poza(models.Model):

    class EtapaEnPoza(models.TextChoices):
        REPRODUCTORA = 'Reproductora'
        RECRIA = 'Recria'
        ENGORDE = 'Engorde'
    
    class RazaEnPoza(models.TextChoices):
        INTI = 'Inti'

    numero_poza = models.IntegerField()
    etapa = models.CharField(max_length=50,choices=POZA_CHOICES)
    fecha_inicio = models.DateField()
    raza = models.CharField(max_length=50,choices=RAZA_CHOICES)
    machos = models.IntegerField()
    hembras = models.IntegerField()
    peso_promedio = models.FloatField(default=0.0)
    cantidad_gazapos = models.IntegerField(blank=True, default=0)
    cuyes_muertos = models.IntegerField(blank=True, default=0)
    numero_galpon = models.IntegerField()
    actual = models.BooleanField(default=True)
    fecha_termino = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.numero_poza
    def numero_cuyes(self):
        return self.machos + self.hembras
    def tasa_mortalidad(self):
        return self.cuyes_muertos / self.numero_cuyes() * 100
    
class Parto(models.Model):
    poza = models.ForeignKey('Poza',on_delete=models.CASCADE)
    fecha_real = models.DateField(blank=True)
    fecha_probable = models.DateField()

####### FORMS ########
class PozaCreateForm(ModelForm):
    class Meta:
        model = Poza
        fields = [
                    'numero_poza', 
                    'etapa', 
                    'machos', 
                    'hembras', 
                    'raza', 
                    'fecha_inicio', 
                    'numero_galpon'
                ]

class PozaUpdateForm(ModelForm):
    class Meta:
        model = Poza
        fields = [
                    'numero_poza', 
                    'etapa', 
                    'machos', 
                    'hembras', 
                    'raza', 
                    'fecha_inicio', 
                    'numero_galpon',
                    'peso_promedio',
                    'cuyes_muertos',
                    'cantidad_gazapos'
                ]

# class PozaCreateForm(forms.Form):
#     numero_poza = forms.IntegerField()
#     etapa = forms.CharField(widget=forms.Select(choices=POZA_CHOICES))
#     fecha_inicio = forms.DateField()
#     raza = forms.CharField(widget=forms.Select(choices=RAZA_CHOICES))
#     machos = forms.IntegerField()
#     hembras = forms.IntegerField()
#     numero_galpon = forms.IntegerField()