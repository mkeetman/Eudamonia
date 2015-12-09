from django.contrib import admin

# Register your models here.

from .models import Survey, Question, Choice, Athlete

admin.site.register(Survey)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Athlete)