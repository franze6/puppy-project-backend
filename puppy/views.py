from rest_framework import generics

from .models import Person
from .serializers import ContactSerializer
from .pagination import CustomPageNumberPagination

class PersonsView(generics.ListAPIView):
    queryset = Person.objects.all()
    serializer_class = ContactSerializer
    pagination_class = CustomPageNumberPagination