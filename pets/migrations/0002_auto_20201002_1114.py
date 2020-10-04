# Generated by Django 3.1.1 on 2020-10-02 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pets',
            name='gender',
            field=models.BooleanField(null=True, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='breed',
            name='breed_description',
            field=models.TextField(null=True, verbose_name='Характеристика породы'),
        ),
        migrations.AlterField(
            model_name='pets',
            name='photo',
            field=models.ImageField(null=True, upload_to='', verbose_name='Фотография'),
        ),
        migrations.AlterField(
            model_name='pets',
            name='story',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
    ]