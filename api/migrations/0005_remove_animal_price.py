# Generated by Django 3.1.1 on 2020-09-29 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200929_1334'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='price',
        ),
    ]
