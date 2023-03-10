# Generated by Django 4.1.6 on 2023-02-12 05:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CustomUser",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        max_length=30,
                        unique=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                code="invalid username",
                                message="User must be alpha-numeric",
                                regex="^[a-zA-Z0-9.+-]*$",
                            )
                        ],
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=75, unique=True, verbose_name="email address"
                    ),
                ),
                ("firstname", models.CharField(blank=True, max_length=75)),
                ("lastname", models.CharField(blank=True, max_length=75)),
                ("fullname", models.CharField(blank=True, max_length=151)),
                ("is_admin", models.BooleanField(default=False)),
                ("is_staff", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=True)),
                ("created_on", models.DateTimeField(auto_now_add=True, null=True)),
                ("modified_on", models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
