# Generated by Django 5.1.4 on 2024-12-20 11:48

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Job",
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
                ("title", models.CharField(max_length=255)),
                ("company_name", models.CharField(max_length=255)),
                ("location", models.CharField(max_length=255)),
                ("salary", models.CharField(blank=True, max_length=100, null=True)),
                ("posted_date", models.DateField()),
                ("details_url", models.URLField()),
            ],
        ),
    ]
