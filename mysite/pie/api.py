# seleuchel
from .models import DjangoBoard
from rest_framework import serializers, viewsets


class DjangoBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjangoBoard
        fields = '__all__'

class DjangoBoardViewSet(viewsets.ModelViewSet):
    queryset = DjangoBoard.objects.all()
    serializer_class = DjangoBoardSerializer
