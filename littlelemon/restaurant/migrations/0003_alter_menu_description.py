# Generated by Django 4.1.5 on 2023-09-30 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_menu_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='description',
            field=models.TextField(default='', max_length=1000),
        ),
    ]
