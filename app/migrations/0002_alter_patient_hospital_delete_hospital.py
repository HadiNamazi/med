# Generated by Django 5.0.6 on 2024-05-29 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='hospital',
            field=models.CharField(max_length=50),
        ),
        migrations.DeleteModel(
            name='Hospital',
        ),
    ]