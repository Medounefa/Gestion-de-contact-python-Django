# Generated by Django 4.0.3 on 2022-03-18 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='archive',
            field=models.BooleanField(default=False),
        ),
    ]
