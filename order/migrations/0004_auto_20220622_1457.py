# Generated by Django 3.1.14 on 2022-06-22 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0003_promocode"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="promocode",
            name="status",
        ),
        migrations.AddField(
            model_name="promocode",
            name="is_expired",
            field=models.BooleanField(default=False),
        ),
    ]
