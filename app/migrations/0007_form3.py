# Generated by Django 5.0.6 on 2024-06-01 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_form2_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.JSONField()),
            ],
        ),
    ]