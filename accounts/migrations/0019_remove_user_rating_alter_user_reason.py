# Generated by Django 4.1 on 2022-12-06 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_user_friends_alter_user_reason_delete_friendship'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='Rating',
        ),
        migrations.AlterField(
            model_name='user',
            name='reason',
            field=models.CharField(choices=[('u', 'university'), ('h', 'highschool'), ('a', 'Friend'), ('g', 'game'), ('s', 'school'), ('o', 'other'), ('f', 'family'), ('i', 'instagram')], max_length=1),
        ),
    ]
