# Generated by Django 4.1.7 on 2023-07-17 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='managers',
            name='date_of_start',
            field=models.DateField(max_length=255),
        ),
    ]
