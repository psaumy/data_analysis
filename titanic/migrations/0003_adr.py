# Generated by Django 2.0.3 on 2018-06-14 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titanic', '0002_auto_20180608_0235'),
    ]

    operations = [
        migrations.CreateModel(
            name='ADR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('load', models.CharField(blank=True, max_length=100)),
                ('cyl1', models.FloatField(blank=True, null=True)),
                ('cyl2', models.FloatField(blank=True, null=True)),
                ('cyl3', models.FloatField(blank=True, null=True)),
                ('mean', models.FloatField(blank=True, null=True)),
                ('cov', models.FloatField(blank=True, null=True)),
                ('rsr', models.FloatField(blank=True, null=True)),
                ('unknwn', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
