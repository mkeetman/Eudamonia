from django.db import models
#from dashboard import models as dashboard_models

# Create your models here.


class Metric(models.Model):
    collection = models.DateTimeField()
    athlete = models.ForeignKey('dashboard.Athlete')

    class Meta:
        abstract = True


class Weight(Metric):
    weight = models.FloatField()
    bmi = models.FloatField()
    fat_percentage = models.FloatField()


class Sleep(Metric):
    duration = models.IntegerField()
    sleep_start = models.TimeField()
    sleep_end = models.TimeField()