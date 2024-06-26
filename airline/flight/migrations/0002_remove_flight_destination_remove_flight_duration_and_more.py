# Generated by Django 5.0 on 2024-05-15 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flight',
            name='destination',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='origin',
        ),
        migrations.AddField(
            model_name='flight',
            name='FirstName',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='flight',
            name='LastName',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterModelTable(
            name='flight',
            table='Flight',
        ),
    ]
