import json
import time
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required

from wellness.models import Survey, Collection
from .models import Athlete

# Create your views here.

@login_required()
def index(request):

    collections = Collection.objects.filter(athlete=request.user.athlete).order_by('-date')
    wellness_data = []
    choice_data = []

    for collection in collections:
        score = 0

        row = {}
        row['col_time'] = int(time.mktime(collection.date.timetuple())) * 1000

        for answer in collection.answer_set.all():
            score += answer.choice.choice_value
            row[answer.choice.question.question_text] = answer.choice.choice_value

        wellness_data.append({'col_time': int(time.mktime(collection.date.timetuple())) * 1000, 'score': score})
        choice_data.append(row)

    context = {'wellness': json.dumps(wellness_data),
               'choice': json.dumps(choice_data)}

    return render(request, 'dashboard/dashboard-home.html', context)


def user_registration(request):
    return render(request, 'dashboard/user_registration.html', )


def process_registration(request):
    user = User.objects.create_user(username=request.POST['username'],
                                    password=request.POST['password'],
                                    email=request.POST['email'],
                                    first_name=request.POST['firstname'],
                                    last_name=request.POST['lastname'])
    user.groups.add(Group.objects.get(name='Athletes'))
    user.save()

    auth_user = authenticate(username=request.POST['username'], password=request.POST['password'])

    if auth_user is None:
        return "Something went wrong with the login process"
    else:
        if user.is_active:
            login(request, auth_user)
            return render(request, 'dashboard/user_profile_set.html', {'surveys': Survey.objects.all()})
        else:
            return "User isn't active :("


def finish_registration(request):

    athlete = Athlete.objects.create(default_survey=Survey.objects.get(pk=request.POST['survey']), user=request.user)
    athlete.save()

    return redirect('index')

