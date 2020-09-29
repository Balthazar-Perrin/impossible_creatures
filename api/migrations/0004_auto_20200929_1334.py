# Generated by Django 3.1.1 on 2020-09-29 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200929_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='animal',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='api.animal'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='buyer',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='buyer', to='api.user'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='seller',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='seller', to='api.user'),
        ),
    ]
