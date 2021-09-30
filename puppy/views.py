from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from .models import Person
from .serializers import ContactSerializer
from .pagination import CustomPageNumberPagination

class PersonsView(generics.ListAPIView):
    queryset = Person.objects.all()
    serializer_class = ContactSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ContactSerializer.Meta.fields