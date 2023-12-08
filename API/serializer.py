from rest_framework import serializers
from .models import Datos


class DatosSerializer(serializers.Serializer):
    class Meta:
        model = Datos
        fields = "__all__"
