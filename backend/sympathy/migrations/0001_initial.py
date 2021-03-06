# Generated by Django 3.0.7 on 2020-10-17 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chat', '0004_chatroom_has_contact'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sympathy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.ChatRoom')),
                ('user1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_one', to='account.UserProfile')),
                ('user2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_two', to='account.UserProfile')),
            ],
        ),
    ]
