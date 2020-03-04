# Generated by Django 3.0.3 on 2020-03-04 04:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myBlog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='zForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128, null=True, verbose_name='Имя')),
                ('email', models.CharField(blank=True, max_length=256, null=True, verbose_name='email')),
                ('subject', models.CharField(blank=True, max_length=128, null=True, verbose_name='Тема')),
                ('message', models.TextField(blank=True, max_length=2056, null=True, verbose_name='Сообщение')),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime(2020, 3, 4, 4, 38, 36, 326631, tzinfo=utc), null=True, verbose_name='Дата сообщения')),
            ],
            options={
                'verbose_name': 'Форма связи',
                'db_table': 'Форма связи',
            },
        ),
    ]
