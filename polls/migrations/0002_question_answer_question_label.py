# Generated by Django 5.0 on 2023-12-14 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.CharField(default=0, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='label',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]