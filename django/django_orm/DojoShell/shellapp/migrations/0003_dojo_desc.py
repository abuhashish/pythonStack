# Generated by Django 2.2.4 on 2021-05-23 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shellapp', '0002_auto_20210523_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.TextField(default='hey'),
            preserve_default=False,
        ),
    ]