from django.db.models import fields
from rest_framework import serializers
from .models import Person

class PersonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'last_name', 'first_name', 'second_name', 'birth_date', 'tax_id', 'insurance_number', 'gender']


class PersonDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'last_name', 'first_name', 'second_name', 'birth_date', 'tax_id', 'insurance_number', 'gender', 'description', 'created_at', 'update_at']