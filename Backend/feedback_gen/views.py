from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import render_to_string


def home_view(request):
    # this is the view users see when on the site but don't have an account

    # django templates
    HTML_STRING = render_to_string('home-view.html', context=None)
    return HttpResponse(HTML_STRING)


@login_required
def index_view(request):
    # this is the view users see when on the siteand are logged in

    # django templates
    HTML_STRING = render_to_string('index.html', context=None)
    return HttpResponse(HTML_STRING)
