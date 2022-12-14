# Generated by Django 4.1.1 on 2022-09-11 17:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scheduler',
            name='added_date',
        ),
        migrations.RemoveField(
            model_name='scheduler',
            name='content',
        ),
        migrations.RemoveField(
            model_name='scheduler',
            name='updated_date',
        ),
        migrations.AddField(
            model_name='scheduler',
            name='Request',
            field=models.CharField(choices=[('POST', 'POST'), ('GET', 'GET')], default='GET', help_text='Request Type', max_length=5),
        ),
        migrations.AddField(
            model_name='scheduler',
            name='date_to_execute',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 11, 17, 34, 37, 727275)),
        ),
        migrations.AddField(
            model_name='scheduler',
            name='request_body',
            field=models.TextField(default='{}', help_text='Please fill this field only if you are sending a post request', verbose_name='Request Body'),
        ),
        migrations.AddField(
            model_name='scheduler',
            name='status',
            field=models.CharField(choices=[('scheduled', 'scheduled'), ('sent', 'sent')], default='scheduled', max_length=20),
        ),
    ]
