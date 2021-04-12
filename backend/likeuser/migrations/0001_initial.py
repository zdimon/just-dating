# Generated by Django 3.0.7 on 2020-10-17 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liked_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liked_user', to='account.UserProfile')),
                ('liking_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liking_user', to='account.UserProfile')),
            ],
        ),
    ]