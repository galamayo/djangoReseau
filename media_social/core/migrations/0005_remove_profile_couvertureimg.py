# Generated by Django 4.1.4 on 2023-07-12 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_profile_couvertureimg'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='couvertureimg',
        ),
    ]
