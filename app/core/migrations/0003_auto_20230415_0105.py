# Generated by Django 3.2.18 on 2023-04-15 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_recipe'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='title',
            field=models.CharField(default='', max_length=255),
        ),
    ]
