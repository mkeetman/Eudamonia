from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Survey(models.Model):

    def __str__(self):
        return self.survey_name

    survey_name = models.CharField(max_length=25)


class Question(models.Model):

    def __str__(self):
        return self.question_text

    question_text = models.CharField(max_length=100)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)


class Choice(models.Model):

    def __str__(self):
        return self.choice_text

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    choice_value = models.IntegerField()


class Athlete(models.Model):

    def __str__(self):
        return self.user.username

    user = models.OneToOneField(User)
    default_survey = models.ForeignKey(Survey)


class Collection(models.Model):
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE)
    date = models.DateTimeField()
    survey = models.ForeignKey(Survey)


class Answer(models.Model):
    choice = models.ForeignKey(Choice)
    collection = models.ForeignKey(Collection)


