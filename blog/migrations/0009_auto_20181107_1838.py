# Generated by Django 2.0.2 on 2018-11-07 14:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20181107_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pubDate',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 7, 18, 38, 1, 842192)),
        ),
    ]
