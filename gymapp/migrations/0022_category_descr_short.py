# Generated by Django 3.1.2 on 2020-11-21 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymapp', '0021_blog_short_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='descr_short',
            field=models.CharField(default=False, max_length=350),
        ),
    ]
