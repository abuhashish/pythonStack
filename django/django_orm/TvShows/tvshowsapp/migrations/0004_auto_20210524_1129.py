# Generated by Django 2.2.4 on 2021-05-24 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvshowsapp', '0003_auto_20210524_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='release_date',
            field=models.DateTimeField(),
        ),
    ]
