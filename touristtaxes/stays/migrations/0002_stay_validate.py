# Generated by Django 2.0 on 2018-03-18 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stays', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stay',
            name='validate',
            field=models.BooleanField(default=False),
        ),
    ]
