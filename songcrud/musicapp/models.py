from django.db import models

# Create your models here.


class Artiste(models.Model):
    # artiste = models.ManyToManyField()
    stage_name = models.CharField(max_length=264, unique=True)
    first_name = models.CharField(max_length=264)
    last_name = models.CharField(max_length=264)
    age = models.IntegerField()

    def __str__(self):
        return self.stage_name


class Song(models.Model):
    # artiste_id = models.OneToOneField(Artiste, on_delete=models.CASCADE)
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length=265)
    date_released = models.DateField()
    likes = models.IntegerField(null=True)

    def __str__(self):
        return self.title


class Lyric(models.Model):
    song_id = models.OneToOneField(Song, on_delete=models.CASCADE)
    # song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.song_id
