# Generated by Django 4.0.6 on 2022-11-22 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0019_alter_product_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.size'),
        ),
    ]
