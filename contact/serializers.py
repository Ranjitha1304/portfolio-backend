from rest_framework import serializers

class ContactSerializer(serializers.Serializer):
    firstName = serializers.CharField(min_length=3, max_length=20)
    lastName = serializers.CharField(required=False, allow_blank=True)
    email = serializers.EmailField()
    message = serializers.CharField(min_length=10)
