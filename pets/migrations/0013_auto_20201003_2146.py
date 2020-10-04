# Generated by Django 3.1.1 on 2020-10-03 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0012_auto_20201003_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='age',
            field=models.CharField(blank=True, help_text='Примеры заполнения: 1 год; 5 месяцев; 7 лет; 2 дня', max_length=20, null=True, verbose_name='Примерный возраст'),
        ),
    ]