from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework_mongoengine import viewsets
from apiMongo.serializers import GameSerializer
from .models import Game
from rest_framework import generics, status
from django_filters.rest_framework import FilterSet, filters
from django.http import Http404
import mongoengine
from django_filters import rest_framework

# controlres = espera a acao pra agir
# Create your views here.

@api_view(['GET'])
def index(request, format=None):
    return Response({
        'api': 'API Mongo ENGENHARIA',
        'version': '1.0',
    })

class GameViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = GameSerializer

    # Filtering by id,name,price and link
    def get_queryset(self):
        queryset = Game.objects.all()
        idGame = self.request.query_params.get('id',None)
        nameGame = self.request.query_params.get('name',None)
        priceGame = self.request.query_params.get('price',None)
        linkGame = self.request.query_params.get('link',None)
        
        if idGame is not None:
            queryset = queryset.filter(id = idGame)
        if nameGame is not None:
            queryset = queryset.filter(name__icontains = nameGame)
        if priceGame is not None:
            queryset = queryset.filter(price__lte = priceGame)
        if linkGame is not None:
            queryset = queryset.filter(link = linkGame)
        return queryset

    # Implements the DELETE
    def delete(self,request):
        self.get_queryset().delete()    
        return Response()



