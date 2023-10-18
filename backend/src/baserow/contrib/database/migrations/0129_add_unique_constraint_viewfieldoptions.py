# Generated by Django 3.2.21 on 2023-10-02 07:33

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("database", "0128_remove_duplicate_viewfieldoptions"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="gridviewfieldoptions",
            options={"ordering": ("order", "field_id")},
        ),
        migrations.AlterUniqueTogether(
            name="formviewfieldoptions",
            unique_together={("form_view", "field")},
        ),
        migrations.AlterUniqueTogether(
            name="galleryviewfieldoptions",
            unique_together={("gallery_view", "field")},
        ),
        migrations.AlterUniqueTogether(
            name="gridviewfieldoptions",
            unique_together={("grid_view", "field")},
        ),
    ]