# Generated by Django 4.1.4 on 2023-05-13 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_followerscount_likepost_alter_profile_profileimg'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='biographie',
            new_name='bio',
        ),
    ]