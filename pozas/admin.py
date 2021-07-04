from django.contrib import admin
from .models import Poza
# Register your models here.

# Register your models here.
class PozaAdmin(admin.ModelAdmin):
    fields = ['numero_poza']

admin.site.register(Poza, PozaAdmin)