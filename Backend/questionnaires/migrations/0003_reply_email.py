# Generated by Django 4.1.2 on 2022-12-11 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaires', '0002_alter_questionnaire_questionnaire_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='email',
            field=models.CharField(default='none', max_length=254),
            preserve_default=False,
        ),
    ]
