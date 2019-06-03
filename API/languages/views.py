from django.shortcuts import render
from rest_framework import viewsets
from .models import Language
from .Serializers import LanguageSerializer


class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
