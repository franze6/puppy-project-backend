from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'last_name', 'first_name', 'second_name', 'birth_date', 'tax_id', 'insurance_number', 'gender']