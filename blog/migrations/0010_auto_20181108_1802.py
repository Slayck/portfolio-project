# Generated by Django 2.0.2 on 2018-11-08 14:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20181107_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pubDate',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 8, 18, 2, 14, 311426)),
        ),
    ]