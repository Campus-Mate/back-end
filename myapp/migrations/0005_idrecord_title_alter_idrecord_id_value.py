# Generated by Django 5.0.6 on 2024-06-05 11:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0004_alter_idrecord_id_value"),
    ]

    operations = [
        migrations.AddField(
            model_name="idrecord",
            name="title",
            field=models.CharField(default="Untitled", max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="idrecord",
            name="id_value",
            field=models.CharField(max_length=255),
        ),
    ]
