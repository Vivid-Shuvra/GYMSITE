# Generated by Django 3.1.2 on 2020-11-06 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymapp', '0006_features'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descriptionOne', models.TextField()),
                ('descriptionTwo', models.TextField()),
            ],
        ),
    ]
