from django.db import models

# Create your models here.
# covid_data.csv
class world(models.Model):
    country_name = models.CharField(max_length=255, blank=False, null=True)
    date = models.DateField(blank=False, null=True)
    total_cases = models.IntegerField(blank=True, null = True)
    total_deaths = models.IntegerField(blank=True, null = True)
    total_recovered = models.IntegerField(blank=True, null = True)
    active_cases = models.IntegerField(blank=True, null = True)

class india_statewise(models.Model):
    state_name = models.CharField(unique=True, max_length=30, blank=False, null=True)
    total_cases = models.IntegerField(blank=True, null = True)
    total_deaths = models.IntegerField(blank=True, null = True)
    total_recovered = models.IntegerField(blank=True, null = True)
    active_cases = models.IntegerField(blank=True, null = True)

    class Meta:
        db_table = "statewise_data"
