from django.db import models

# Create your models here.

class Trainee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    national_num = models.IntegerField(default=000000000)
    address = models.CharField(null=True, max_length=120)
