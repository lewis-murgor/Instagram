# Generated by Django 4.0.3 on 2022-04-01 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gram', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]