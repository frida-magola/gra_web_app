# Generated by Django 3.0.2 on 2020-02-21 17:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gra_news', '0005_auto_20200221_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2020, 2, 21, 17, 10, 36, 389807, tzinfo=utc)),
        ),
    ]
