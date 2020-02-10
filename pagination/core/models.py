from django.db import models

class full_data(models.Model):
    id_file = models.CharField(max_length=30)
    date_file = models.DateField()
    country_id = models.CharField(max_length=2)
# Create your models here.
