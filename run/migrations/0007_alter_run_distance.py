# Generated by Django 4.1.7 on 2023-02-24 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('run', '0006_alter_run_distance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='run',
            name='distance',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
