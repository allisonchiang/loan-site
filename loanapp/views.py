import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import viewsets
from .serializers import BusinessSerializer, AddressSerializer
from .models import Business, Address

class AddrsssViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all().order_by('Address1')
    serializer_class = AddressSerializer

class BusinessViewSet(viewsets.ModelViewSet):
    queryset = Business.objects.all().order_by('Name')
    serializer_class = BusinessSerializer
