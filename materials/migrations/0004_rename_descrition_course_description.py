# Generated by Django 5.0.2 on 2024-02-27 21:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0003_quantity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='descrition',
            new_name='description',
        ),
    ]
