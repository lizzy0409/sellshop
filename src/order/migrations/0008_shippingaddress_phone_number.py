# Generated by Django 4.0.6 on 2022-11-24 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_alter_shippingaddress_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='phone_number',
            field=models.CharField(max_length=200, null=True),
        ),
    ]