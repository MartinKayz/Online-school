# Generated by Django 3.0.5 on 2020-07-07 11:18

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0004_blogcomments'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='Eligibility',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='Objectives',
            field=models.TextField(default=datetime.datetime(2020, 7, 7, 11, 18, 49, 838184, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
