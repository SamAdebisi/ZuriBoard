# Generated by Django 4.1.2 on 2022-10-26 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0003_alter_lyric_content_alter_song_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lyric',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='song',
            name='title',
            field=models.CharField(max_length=265),
        ),
    ]
