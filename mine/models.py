from django.db import models

# Create your models here.

class Member (models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField()
    date_joined=models.DateTimeField(null=True)

    def __str__(self) -> str:
        return self.firstname 
