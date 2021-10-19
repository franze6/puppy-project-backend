from rest_framework import serializers
from rest_framework.generics import ListAPIView, RetrieveAPIView
from django_filters.rest_framework import DjangoFilterBackend

from .models import Address, Person
from .serializers import PersonsSerializer, PersonDetailSerializer
from .pagination import CustomPageNumberPagination

class PersonsView(ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonsSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = PersonsSerializer.Meta.fields

class PersonDetailView(RetrieveAPIView):
    queryset = Person.objects.all()    
    serializer_class = PersonDetailSerializer
