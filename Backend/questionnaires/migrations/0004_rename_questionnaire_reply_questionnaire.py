# Generated by Django 4.1.2 on 2022-12-11 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaires', '0003_reply_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reply',
            old_name='Questionnaire',
            new_name='questionnaire',
        ),
    ]
