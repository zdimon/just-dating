# Generated by Django 3.0.9 on 2020-08-06 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_auto_20200801_1010'),
    ]

    operations = [
        migrations.CreateModel(
            name='Smile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smile', models.ImageField(upload_to='', verbose_name='Smile Imgage')),
            ],
        ),
        migrations.CreateModel(
            name='Sticker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sticker', models.ImageField(upload_to='', verbose_name='Sticker Imgage')),
            ],
        ),
        migrations.CreateModel(
            name='RoomMessageSticker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.RoomMessage', verbose_name='message')),
                ('sticker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Sticker', verbose_name='sticker')),
            ],
        ),
        migrations.CreateModel(
            name='RoomMessageSmile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.RoomMessage', verbose_name='message')),
                ('smile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Smile', verbose_name='smile')),
            ],
        ),
    ]