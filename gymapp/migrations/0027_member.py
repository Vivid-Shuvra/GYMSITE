# Generated by Django 3.1.2 on 2020-11-25 07:09

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gymapp', '0026_pricing_offerprice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, default='', max_length=250)),
                ('phone', models.CharField(blank=True, default='', max_length=20)),
                ('date', models.DateTimeField(default=datetime.datetime.today)),
                ('status', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gymapp.customer')),
                ('price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gymapp.pricing')),
            ],
        ),
    ]
