from django.db.models import fields
from rest_framework import serializers
from .models import Person, Address, Career


class PersonAddressSerializer(serializers.ModelSerializer):
  class Meta:
    model = Address
    fields = [
      'address_plain',
      'is_active',
      'person_id',
    ]

class PersonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'last_name', 'first_name', 'second_name', 'birth_date', 'tax_id', 'insurance_number', 'gender']


class PersonCareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = ['company_id', 'project_id']
        depth = 1


class PersonDetailSerializer(serializers.ModelSerializer):
  address = PersonAddressSerializer(many=True)
  career = PersonCareerSerializer(many=True)
  class Meta:
      model = Person
      fields = [
        'id', 'last_name', 'first_name', 
        'second_name', 'birth_date', 'tax_id', 
        'insurance_number', 'gender', 'description', 
        'address', 'career', 'passport', 'messenger',
        'created_at', 'update_at'
      ]
      depth = 1

