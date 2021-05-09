from rest_framework import serializers
from .models import Cuy

class CuySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuy
        fields = '__all__'