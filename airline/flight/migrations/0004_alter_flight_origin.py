# Generated by Django 5.0 on 2024-05-15 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0003_flight_destination_flight_origin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='origin',
            field=models.IntegerField(null=True),
        ),
    ]
