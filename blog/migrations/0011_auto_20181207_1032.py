# Generated by Django 2.0.2 on 2018-12-07 06:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20181108_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pubDate',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 7, 10, 32, 5, 596181)),
        ),
    ]