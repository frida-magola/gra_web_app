# Generated by Django 3.0.2 on 2020-02-23 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gra_branches', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.CharField(max_length=30)),
                ('prefix', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Pastor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=5)),
                ('nationality', models.CharField(max_length=30)),
                ('status_matrim', models.CharField(max_length=30)),
                ('wife_name', models.CharField(max_length=30)),
                ('children_num', models.CharField(max_length=30)),
                ('language', models.ManyToManyField(to='gra_branches.Language')),
            ],
        ),
        migrations.AlterField(
            model_name='branche',
            name='pastor',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='gra_branches.Pastor'),
        ),
    ]
