# Generated by Django 4.2 on 2023-04-27 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='element',
            name='price',
            field=models.DecimalField(decimal_places=10, max_digits=20),
        ),
    ]
