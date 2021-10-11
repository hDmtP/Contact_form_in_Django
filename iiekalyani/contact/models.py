from django.db import models

# Create your models here.

class Contact(models.Model):
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    email = models.EmailField(max_length=50)
    mobile = models.IntegerField()
    msg = models.CharField(max_length=300)
    

    def __str__(self) -> str:
        return self.email