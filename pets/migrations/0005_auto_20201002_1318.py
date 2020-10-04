# Generated by Django 3.1.1 on 2020-10-02 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0004_auto_20201002_1122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pet',
            name='breed',
        ),
        migrations.AddField(
            model_name='pet',
            name='breed',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pets.breed', verbose_name='Порода'),
        ),
    ]