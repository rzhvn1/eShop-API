# Generated by Django 3.1.14 on 2022-06-23 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0005_remove_promocode_is_expired"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cart",
            name="cart_price",
            field=models.FloatField(default=0),
        ),
    ]
