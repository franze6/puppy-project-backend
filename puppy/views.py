from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Contact
from .serializers import ContactSerializer

class ContactsView(APIView):
    def get(self, request):
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response({'persons': serializer.data})

