# Generated by Django 3.1.3 on 2020-12-21 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orphanage', '0002_auto_20201218_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='deleted',
            field=models.IntegerField(default=0),
        ),
    ]
