from django.db import models


class Email(models.Model):
    from_email = models.EmailField()
    full_name = models.CharField(max_length=255)
    phone_number = models.TextField()
    subject = models.CharField(max_length=100)
    body = models.TextField()
