# Generated by Django 4.1.2 on 2022-10-27 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0005_song_likes_alter_lyric_song_id_alter_song_artiste_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='artiste_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicapp.artiste'),
        ),
    ]
