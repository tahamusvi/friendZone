# Generated by Django 4.1 on 2022-08-05 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_avatar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='phoneNumber',
            new_name='index',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='firstName',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='lastName',
        ),
    ]
