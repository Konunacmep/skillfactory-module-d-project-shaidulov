# Generated by Django 3.1.1 on 2020-10-02 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0003_auto_20201002_1116'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Pets',
            new_name='Pet',
        ),
    ]
