# Generated by Django 4.0.7 on 2023-12-16 02:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0005_alter_ad_id_alter_comment_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ad',
            name='owner',
        ),
    ]
