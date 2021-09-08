from rest_framework import serializers

class ContactSerializer(serializers.Serializer):
    last_name = serializers.CharField()
    first_name = serializers.CharField()
    second_name = serializers.CharField()