# Generated by Django 4.0.6 on 2022-11-01 07:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_remove_productreview_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreview',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 1, 11, 28, 59, 511305)),
        ),
    ]
