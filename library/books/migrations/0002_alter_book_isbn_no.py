# Generated by Django 4.0 on 2022-10-05 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='ISBN_no',
            field=models.CharField(max_length=20),
        ),
    ]
