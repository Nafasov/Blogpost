from rest_framework import serializers

from main.models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'image', 'email', 'message', 'created_date']
