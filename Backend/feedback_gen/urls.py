"""feedback_gen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from accounts.views import (
    login_view,
    logout_view,
    signup_view
)
from .views import (
    home_view,
    dashboard_view,
    create_questionnaire_view,
    choose_template_for_questionnaire_view,
    my_surveys_view,
    reply_survey_view,
)

urlpatterns = [
    path('', home_view),  # home view
    path('dashboard/', dashboard_view),  # index view

    path('admin/', admin.site.urls),

    path('login/', login_view),
    path('logout/', logout_view),
    path('signup/', signup_view),
    path('choose_template_for_questionnaire/',
         choose_template_for_questionnaire_view),
    path('create_questionnaire/', create_questionnaire_view),
    path('dashboard/my_surveys/', my_surveys_view),
    path('reply_survey/<int:id>/', reply_survey_view),
]
