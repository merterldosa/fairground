# Generated by Django 4.2.6 on 2023-10-23 00:34

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Saju",
            fields=[
                ("idx", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=30)),
                ("birth", models.CharField(max_length=8)),
                (
                    "solar",
                    models.CharField(
                        choices=[("solar", "양력"), ("lunar", "음력")],
                        max_length=6,
                        verbose_name="양력",
                    ),
                ),
                (
                    "sigan",
                    models.CharField(
                        choices=[
                            ("1", "자"),
                            ("2", "축"),
                            ("3", "인"),
                            ("4", "묘"),
                            ("5", "진"),
                            ("6", "사"),
                            ("7", "오"),
                            ("8", "미"),
                            ("9", "신"),
                            ("10", "유"),
                            ("11", "술"),
                            ("12", "해"),
                            ("13", "모름"),
                        ],
                        max_length=6,
                        verbose_name="자",
                    ),
                ),
                ("date_joined", models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
