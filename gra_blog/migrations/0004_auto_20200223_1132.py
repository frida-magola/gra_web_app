# Generated by Django 3.0.2 on 2020-02-23 11:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gra_blog', '0003_auto_20200223_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 23, 11, 32, 7, 201573, tzinfo=utc)),
        ),
    ]