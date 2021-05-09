from django.contrib import admin
from .models import Cuy
# Register your models here.
class CuyAdmin(admin.ModelAdmin):
    fields = ['name']

admin.site.register(Cuy, CuyAdmin)