from rest_framework import serializers
from .models import Email

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = [ 'from_email', 'full_name', 'phone_number', 'subject', 'body']

