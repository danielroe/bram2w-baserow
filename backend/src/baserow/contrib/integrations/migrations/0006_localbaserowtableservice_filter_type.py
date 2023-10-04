# Generated by Django 3.2.21 on 2023-09-25 14:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "integrations",
            "0005_localbaserowtableservicesort_localbaserowtableservicefilter",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="localbaserowgetrow",
            name="filter_type",
            field=models.CharField(
                choices=[("AND", "And"), ("OR", "Or")],
                default="AND",
                help_text="Indicates whether all the rows should apply to all filters (AND) or to any filter (OR).",
                max_length=3,
            ),
        ),
        migrations.AddField(
            model_name="localbaserowlistrows",
            name="filter_type",
            field=models.CharField(
                choices=[("AND", "And"), ("OR", "Or")],
                default="AND",
                help_text="Indicates whether all the rows should apply to all filters (AND) or to any filter (OR).",
                max_length=3,
            ),
        ),
    ]