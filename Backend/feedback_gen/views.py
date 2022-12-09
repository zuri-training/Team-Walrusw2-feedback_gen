from django.http import HttpResponse

html_string = """
<h1>This is the view users see when on the site but don't have an account</h1>
"""


def home_view(request):
    # this is the view users see when on the site but don't have an account
    return HttpResponse(html_string)
