# Generated by Django 3.1.2 on 2020-11-26 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymapp', '0030_auto_20201126_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='price',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
