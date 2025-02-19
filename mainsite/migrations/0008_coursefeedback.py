# Generated by Django 3.0.5 on 2020-07-08 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0007_auto_20200708_1309'),
    ]

    operations = [
        migrations.CreateModel(
            name='coursefeedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=350)),
                ('profilepic', models.ImageField(upload_to='')),
                ('comment', models.TextField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.Course')),
            ],
        ),
    ]
