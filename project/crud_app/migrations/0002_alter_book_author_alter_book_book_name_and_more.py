# Generated by Django 5.0.3 on 2024-03-19 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='book',
            name='publication',
            field=models.CharField(max_length=30),
        ),
    ]
