# Generated by Django 5.0.6 on 2024-06-07 07:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0006_alter_idrecord_id_value"),
    ]

    operations = [
        migrations.AlterField(
            model_name="idrecord",
            name="id_value",
            field=models.CharField(max_length=255),
        ),
    ]