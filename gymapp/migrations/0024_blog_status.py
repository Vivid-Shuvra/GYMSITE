# Generated by Django 3.1.2 on 2020-11-24 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymapp', '0023_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
