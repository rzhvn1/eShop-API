# Generated by Django 3.1.14 on 2022-06-21 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cart",
            name="cart_price",
            field=models.FloatField(blank=True, null=True),
        ),
    ]
