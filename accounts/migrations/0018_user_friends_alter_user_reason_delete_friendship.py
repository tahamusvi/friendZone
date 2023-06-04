# Generated by Django 4.1 on 2022-12-05 16:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_friendship'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Friends',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='reason',
            field=models.CharField(choices=[('u', 'university'), ('h', 'highschool'), ('a', 'Friend'), ('g', 'game'), ('s', 'school'), ('o', 'other'), ('f', 'family'), ('i', 'instagram'), ('t', 'iust')], max_length=1),
        ),
        migrations.DeleteModel(
            name='Friendship',
        ),
    ]
