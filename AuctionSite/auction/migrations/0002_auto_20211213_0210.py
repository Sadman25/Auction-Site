# Generated by Django 3.1.7 on 2021-12-12 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='cover_photo',
            field=models.ImageField(upload_to=''),
        ),
    ]
