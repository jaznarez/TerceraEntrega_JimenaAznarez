# Generated by Django 4.2.2 on 2023-08-02 14:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("MercadoApp", "0002_comment"),
    ]

    operations = [
        migrations.RemoveField(model_name="comment", name="post",),
        migrations.AlterField(
            model_name="comment",
            name="created_date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 8, 2, 14, 41, 49, 934249)
            ),
        ),
    ]