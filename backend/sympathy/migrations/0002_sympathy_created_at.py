# Generated by Django 3.0.7 on 2020-10-17 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sympathy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sympathy',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
