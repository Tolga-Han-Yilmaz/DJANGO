# Generated by Django 4.1 on 2022-08-22 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=32)),
                ("last_name", models.CharField(max_length=32)),
                ("number", models.IntegerField()),
                ("description", models.TextField(blank=True, null=True)),
                ("register_date", models.DateField(auto_now_add=True)),
                ("last_update_date", models.DateTimeField(auto_now=True)),
                ("is_Active", models.BooleanField(default=True)),
            ],
        ),
    ]