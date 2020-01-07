from django.db import models


class Service(models.Model):
    CNumber = models.IntegerField()
    CName = models.CharField(max_length=100)
    CFaculty = models.CharField(max_length=100)
    CDuration = models.CharField(max_length=100)
    CFees = models.IntegerField()
    CContent = models.CharField(max_length=100)

class ContactData(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    mobile=models.BigIntegerField()
    location=models.CharField(max_length=100)