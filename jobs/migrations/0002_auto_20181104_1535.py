# Generated by Django 2.0.2 on 2018-11-04 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='summary',
            new_name='title',
        ),
    ]
