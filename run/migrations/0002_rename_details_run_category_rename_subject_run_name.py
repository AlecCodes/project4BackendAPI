# Generated by Django 4.1.7 on 2023-02-23 23:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('run', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='run',
            old_name='details',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='run',
            old_name='subject',
            new_name='name',
        ),
    ]
