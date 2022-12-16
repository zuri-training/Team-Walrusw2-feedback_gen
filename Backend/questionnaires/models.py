from django.db import models

# Create your models here.


class Questionnaire(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=40)
    questionnaire = models.CharField(max_length=10000)
    short_link = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Reply(models.Model):
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)
    email = models.CharField(max_length=254)
    reply = models.CharField(max_length=10000)
