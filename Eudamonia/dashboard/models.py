from django.db import models
from django.contrib.auth.models import User
#from wellness import models as wellness_models


# Create your models here.

class Coach(models.Model):

    def __str__(self):
        return self.user.username

    user = models.OneToOneField(User)


class Athlete(models.Model):

    def __str__(self):
        return self.user.username

    user = models.OneToOneField(User)
    default_survey = models.ForeignKey('wellness.Survey')
    coaches = models.ManyToManyField(Coach)
