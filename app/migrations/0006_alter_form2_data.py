# Generated by Django 5.0.6 on 2024-05-31 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_form2_delete_patientinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form2',
            name='data',
            field=models.JSONField(),
        ),
    ]