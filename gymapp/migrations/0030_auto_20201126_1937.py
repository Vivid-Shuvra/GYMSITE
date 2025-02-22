# Generated by Django 3.1.2 on 2020-11-26 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymapp', '0029_remove_member_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='member',
            name='customer',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='member',
            name='duration',
            field=models.CharField(max_length=20),
        ),
    ]
