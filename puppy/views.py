from rest_framework import serializers, status
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Address, Person
from .serializers import PersonsSerializer, PersonDetailSerializer

#from .pagination import CustomPageNumberPagination
from .pagination import get_paginated_response, LimitOffsetPagination

from .services import (person_create, person_update, person_delete,
                        address_create, address_delete, address_update,
                        messenger_create, messenger_delete, messenger_update,                       
                        passport_create, passport_delete)
from .selectors import person_list, get_person

class PersonsView(ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonsSerializer
    #pagination_class = CustomPageNumberPagination
    #filter_backends = [DjangoFilterBackend]
    #filterset_fields = PersonsSerializer.Meta.fields

class PersonListApi(APIView):
    class Pagination(LimitOffsetPagination):
        default_limit = 1

    class FilterSerializer(serializers.Serializer):
        id = serializers.IntegerField(required=False)
        last_name = serializers.CharField(required=False)

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Person
            fields = (
                'id', 'last_name', 'first_name', 'second_name', 
                'birth_date', 'tax_id', 'insurance_number', 'gender'
            )

    def get(self, request):
        filter_serializer = self.FilterSerializer(data=request.query_params)
        filter_serializer.is_valid(raise_exception=True)

        persons = person_list(filters=filter_serializer.validated_data)

        return get_paginated_response(
            pagination_class=self.Pagination,
            serializer_class=self.OutputSerializer,
            queryset=persons,
            request=request,
            view=self
        )



class PersonDetailView(RetrieveAPIView):
    queryset = Person.objects.all()    
    serializer_class = PersonDetailSerializer

class PersonDetailApi(APIView):
    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Person
            fields = ('id', 'last_name', 'first_name', 
                        'second_name', 'birth_date', 'tax_id', 
                        'insurance_number', 'gender', 'description', 
                        'address', 'career', 'passport', 'messenger',
                        'created_at', 'update_at')
            depth = 1

    def get(self, request, person_id):
        person = get_person(id=person_id)
        serializer = self.OutputSerializer(person)
        return Response(serializer.data)

class PersonUpdateApi(APIView):
    class InputSerializer(serializers.Serializer):
        last_name = serializers.CharField(required=False)
        first_name = serializers.CharField(required=False)
        second_name = serializers.CharField(required=False)
        birth_date = serializers.DateField(required=False)
        tax_id = serializers.CharField(required=False)
        insurance_number = serializers.CharField(required=False)
        gender = serializers.CharField(required=False)
        description = serializers.CharField(required=False)

    def post(self, request, person_id):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        person_update(id=person_id, **serializer.validated_data)
        return Response(status=status.HTTP_200_OK)

class PersonDeleteApi(APIView):
    def delete(self, request, person_id):
        person_delete(id=person_id)
        return Response(status=status.HTTP_200_OK)

class PersonCreateApi(APIView):
    class InputSerializer(serializers.Serializer):
        last_name = serializers.CharField()
        first_name = serializers.CharField()
        second_name = serializers.CharField(required=False)
        birth_date = serializers.DateField(required=False)
        tax_id = serializers.CharField(required=False)
        insurance_number = serializers.CharField(required=False)
        gender = serializers.CharField(required=False)
        description = serializers.CharField(required=False)

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        person_create(**serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED)


class AddressCreateApi(APIView):
    class InputSerializer(serializers.Serializer):
        address_plain = serializers.CharField()
        is_active = serializers.BooleanField()
        person_id = serializers.CharField()
        #company_id = serializers.CharField(required=False)

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        address_create(**serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED)

class AddressUpdateApi(APIView):
    class InputSerializer(serializers.Serializer):
        address_plain = serializers.CharField(required=False)
        is_active = serializers.BooleanField(required=False)
        #person_id = serializers.CharField(required=False)

    def post(self, request, id):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        address_update(id=id, **serializer.validated_data)
        return Response(status=status.HTTP_200_OK)

class AddressDeleteApi(APIView):
    def delete(self, request, id):
        address_delete(id=id)
        return Response(status=status.HTTP_200_OK)

class MessengerCreateApi(APIView):
    class InputSerializer(serializers.Serializer):
        name = serializers.CharField()
        is_active = serializers.BooleanField()
        uid = serializers.CharField()
        person_id = serializers.CharField()

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        messenger_create(**serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED)

class MessengerUpdateApi(APIView):
    class InputSerializer(serializers.Serializer):
        name = serializers.CharField(required=False)
        is_active = serializers.BooleanField(required=False)
        uid = serializers.CharField(required=False)
        #person_id = serializers.CharField(required=False)
        #person_id = serializers.CharField(required=False)

    def post(self, request, id):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        messenger_update(id=id, **serializer.validated_data)
        return Response(status=status.HTTP_200_OK)

class MessengerDeleteApi(APIView):
    def delete(self, request, id):
        messenger_delete(id=id)
        return Response(status=status.HTTP_200_OK)

class PassportCreateApi(APIView):
    class InputSerializer(serializers.Serializer):
        series = serializers.CharField()
        number = serializers.CharField()
        issued_date = serializers.DateField()
        issued_by = serializers.CharField()
        issued_by_code = serializers.CharField()
        person_id = serializers.CharField()

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        passport_create(**serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED)

class PassportDeleteApi(APIView):
    def delete(self, request, id):
        passport_delete(id=id)
        return Response(status=status.HTTP_200_OK)