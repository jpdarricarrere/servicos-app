from rest_framework import serializers
from services.models import ServiceModel


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceModel
        fields = ('id',
                  'nome',
                  'categoria',
                  'telefone',
                  'email',
                  'link_imagem',
                  'contratado')
