from django.db import models

# Create your models here.
class element(models.Model):
    name=models.CharField(max_length=256)
    price=models.DecimalField(decimal_places=2,max_digits=20)

