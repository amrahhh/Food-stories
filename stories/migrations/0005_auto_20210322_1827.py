# Generated by Django 3.1.7 on 2021-03-22 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0004_auto_20210320_0718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='slug',
            field=models.SlugField(editable=False, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='story',
            name='slug',
            field=models.SlugField(editable=False, verbose_name='Slug'),
        ),
    ]
