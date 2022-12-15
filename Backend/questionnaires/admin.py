from django.contrib import admin
from .models import Questionnaire, Reply


class QuestionnaireAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'title']
    search_fields = ['id', 'title', 'questionnaire']


# Register your models here.
admin.site.register(Questionnaire, QuestionnaireAdmin)


class ReplyAdmin(admin.ModelAdmin):
    list_display = ['id', 'email']
    search_fields = ['id', 'email', 'questionnaire']


# Register your models here.
admin.site.register(Reply, ReplyAdmin)
