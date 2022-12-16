from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import render_to_string
from questionnaires.models import Questionnaire, Reply
from questionnaires.shortener import shortener
from django.shortcuts import render


def home_view(request):
    # this is the view users see when on the site but don't have an account

    # django templates
    HTML_STRING = render_to_string('home-view.html', context=None)
    return HttpResponse(HTML_STRING)


@login_required
def dashboard_view(request):
    # this is the view users see when on the site and are logged in

    # django templates
    HTML_STRING = render_to_string('dashboard.html', context=None)
    return HttpResponse(HTML_STRING)


@login_required
def choose_template_for_questionnaire_view(request):

    # django templates
    HTML_STRING = render_to_string(
        'choose-template-for-questionnaire-view.html', context=None)
    return HttpResponse(HTML_STRING)


@login_required
def create_questionnaire_view(request):
    context = {}
    token = ""
    username = request.user.username
    if request.method == "POST":
        url = request.META['HTTP_HOST']
        token = shortener().issue_token()
        title = request.POST.get("title")
        questionnaire = request.POST.get("questionnaire")
        questionnaire_obj = Questionnaire.objects.create(
            author=username, title=title, questionnaire=questionnaire, short_link=token)
        context['url'] = url
        context['token'] = token
        context['object'] = questionnaire_obj
        context["created"] = True
        print(token)

    # django templates
    return render(request, 'create-questionnaire-view.html', context=context)


@login_required
def my_surveys_view(request):

    # from database
    questionnaire_obj = Questionnaire.objects.all()
    reply_obj = Reply.objects.all()
    url = request.META['HTTP_HOST']
    context = {"url": url, "questionnaires": questionnaire_obj,
               'replies': reply_obj}

    # django templates
    HTML_STRING = render_to_string(
        'my-surveys.html', context=context)
    return HttpResponse(HTML_STRING)


def reply_survey_view(request, token):
    questionnaire = Questionnaire.objects.get(short_link=token)
    context = {}
    context['questionnaire_obj'] = questionnaire
    if request.method == "POST":
        reply = request.POST.get("reply")
        email = request.POST.get("email")
        reply_obj = Reply.objects.create(
            questionnaire=questionnaire, email=email, reply=reply)
        context['object'] = reply_obj
        context["replied"] = True

    # django templates
    return render(request, 'reply-view.html', context=context)
