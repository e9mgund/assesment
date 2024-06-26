# Generated by Django 4.2.6 on 2024-05-06 08:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tournament", "0003_teammatch"),
    ]

    operations = [
        migrations.AddField(
            model_name="team",
            name="lost",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="team",
            name="matches",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="team",
            name="won",
            field=models.IntegerField(default=0),
        ),
    ]
