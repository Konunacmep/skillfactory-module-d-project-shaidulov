# Generated by Django 3.1.1 on 2020-10-03 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0008_auto_20201003_0931'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pet',
            old_name='breed_ref',
            new_name='breed',
        ),
    ]
