# Generated by Django 3.1.7 on 2021-04-01 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0011_auto_20210401_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='slug',
            field=models.SlugField(editable=False, verbose_name='Slug'),
        ),
    ]
