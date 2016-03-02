import json
import time
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone


from .models import Survey, Collection, Answer, Choice

# Create your views here.


def index(request):
    pass


@login_required()
def take_survey(request, survey_id=None):

    if survey_id is None:
        survey = get_object_or_404(Survey, pk=request.user.athlete.default_survey.id)
    else:
        survey = get_object_or_404(Survey, pk=survey_id)

    return render(request, 'wellness/survey.html', {'survey': survey})


@login_required()
def submit_survey(request, survey_id):
    collection = Collection(date=timezone.now(), athlete=request.user.athlete, survey=Survey.objects.get(pk=survey_id))
    collection.save()

    questions = Survey.objects.get(pk=survey_id).question_set.all()
    for question in questions:
        collection.answer_set.create(choice=Choice.objects.get(pk=request.POST['question_' + str(question.id)]))
    collection.save()

    score = 0
    for answer in collection.answer_set.all():
        score += answer.choice.choice_value

    return render(request, 'wellness/survey_result.html', {'score': score,
                                                           'collection': collection,})


@login_required()
def graph_wellness(request):
    collections = Collection.objects.filter(athlete=request.user.athlete).order_by('-date')
    wellness_data = []
    choice_data = {}

    for collection in collections:
        score = 0
        for answer in collection.answer_set.all():
            score += answer.choice.choice_value

            if answer.choice.question.question_text in choice_data:
                choice_data[answer.choice.question.question_text].append(
                    [int(time.mktime(collection.date.timetuple())) * 1000, answer.choice.choice_value])
            else:
                choice_data[answer.choice.question.question_text] = [[int(time.mktime(collection.date.timetuple())) * 1000,
                                                           answer.choice.choice_value]]

        wellness_data.append([int(time.mktime(collection.date.timetuple())) * 1000, score])

    context = {'data': json.dumps(wellness_data),
               'choice_data': choice_data}
    return render(request, 'wellness/wellness_graph.html', context)


@login_required()
def collection_detail(request, collection_id):
    collection = get_object_or_404(Collection, pk=collection_id)
    return render(request, 'wellness/collection_detail.html', {'collection': collection})
