# Generated by Django 3.0.7 on 2020-10-13 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_contactrequest_is_rejected'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactrequest',
            old_name='is_rejected',
            new_name='is_refused',
        ),
    ]
