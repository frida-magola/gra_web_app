# Generated by Django 3.0.2 on 2020-02-23 12:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gra_blog', '0006_auto_20200223_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='body',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 23, 12, 26, 20, 325079, tzinfo=utc)),
        ),
    ]