# Generated by Django 5.0 on 2024-05-14 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=12)),
                ('LastName', models.CharField(max_length=12)),
            ],
        ),
    ]