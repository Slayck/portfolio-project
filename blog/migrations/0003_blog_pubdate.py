# Generated by Django 2.0.2 on 2018-11-05 17:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='pubDate',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 5, 21, 3, 1, 876994)),
        ),
    ]
