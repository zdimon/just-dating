# Generated by Django 3.0.7 on 2020-10-17 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermedia', '0003_usermedia_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermedia',
            name='likes',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]