# Generated by Django 3.1.1 on 2020-09-29 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_animal_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='money',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]