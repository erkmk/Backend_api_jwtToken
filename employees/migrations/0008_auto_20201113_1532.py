# Generated by Django 3.1.1 on 2020-11-13 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0007_auto_20201113_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(default=' ', max_length=254),
        ),
    ]
