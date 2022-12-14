# Generated by Django 4.1.2 on 2022-11-01 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0006_alter_song_artiste_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artiste',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='artiste',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='artiste',
            name='stage_name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='date_released',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
