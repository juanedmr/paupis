# Generated by Django 5.0 on 2023-12-14 03:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_question_answer_question_label'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='pub_date',
        ),
    ]
