# Generated by Django 3.0.7 on 2021-04-12 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usermedia', '0005_auto_20201017_2334'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermedia',
            name='likes',
        ),
    ]
