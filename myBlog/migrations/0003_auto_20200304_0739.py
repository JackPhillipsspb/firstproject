# Generated by Django 3.0.3 on 2020-03-04 04:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myBlog', '0002_zform'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zform',
            name='date',
        ),
        migrations.AddField(
            model_name='zform',
            name='date_pub_forms',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 3, 4, 4, 39, 24, 67275, tzinfo=utc), null=True, verbose_name='Дата сообщения'),
        ),
    ]
