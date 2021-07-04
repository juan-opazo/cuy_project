from django.forms import ModelForm
from pozas.models import Poza

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
        
