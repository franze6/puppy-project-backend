from rest_framework import serializers, status
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Address, Person
from .serializers import PersonsSerializer, PersonDetailSerializer
from .pagination import CustomPageNumberPagination
from .services import person_create, person_update, person_delete
from .selectors import person_list

class PersonsView(ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonsSerializer
    #pagination_class = CustomPageNumberPagination
    #filter_backends = [DjangoFilterBackend]
    #filterset_fields = PersonsSerializer.Meta.fields

class PersonListApi(APIView):
    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Person
            fields = (
                'id', 'last_name', 'first_name', 'second_name', 
                'birth_date', 'tax_id', 'insurance_number', 'gender'
            )
    def get(self, request):
        persons = person_list()
        data = self.OutputSerializer(persons, many=True).data

        return Response(data)

class PersonDetailView(RetrieveAPIView):
    queryset = Person.objects.all()    
    serializer_class = PersonDetailSerializer

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
