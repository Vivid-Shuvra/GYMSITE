# Generated by Django 3.1.2 on 2020-11-06 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymapp', '0005_pricing_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
    ]
