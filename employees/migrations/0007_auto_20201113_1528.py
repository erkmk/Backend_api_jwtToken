# Generated by Django 3.1.1 on 2020-11-13 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0006_auto_20201113_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]
