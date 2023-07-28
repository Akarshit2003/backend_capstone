# Generated by Django 4.2.2 on 2023-07-08 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="MenuItems",
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
                ("Title", models.CharField(max_length=255)),
                ("Price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("Inventory", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="SingleMenuItem",
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
                ("name", models.CharField(max_length=255)),
                ("ingredients", models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name="Menu",
        ),
        migrations.AlterField(
            model_name="booking",
            name="No_of_guests",
            field=models.IntegerField(),
        ),
    ]