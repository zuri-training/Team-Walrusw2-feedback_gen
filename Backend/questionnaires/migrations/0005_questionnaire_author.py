# Generated by Django 4.1.2 on 2022-12-11 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaires', '0004_rename_questionnaire_reply_questionnaire'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionnaire',
            name='author',
            field=models.CharField(default='none', max_length=100),
            preserve_default=False,
        ),
    ]
