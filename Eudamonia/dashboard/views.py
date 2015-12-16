from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.models import User

from wellness.models import Athlete, Survey

# Create your views here.


def user_registration(request):
    return render(request, 'dashboard/user_registration.html', )


def process_registration(request):
    user = User.objects.create_user(request.POST['username'],
                                    request.POST['password'],
                                    request.POST['email'],
                                    first_name=request.POST['firstname'],
                                    last_name=request.POST['lastname'])

    login(request, user)

    return render(request, 'dashboard/user_profile_set.html', {'surveys': Survey.object.all()})


def finish_registration(request):

    athlete = Athlete.objects.create()

    return "Thanks for registering " + request.user.first_name