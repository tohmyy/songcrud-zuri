from django.db import models

class Artiste(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    age = models.IntegerField(null=True)

    def __str__(self):
        return self.first_name

class Song(models.Model):
    title = models.CharField(max_length=120)
    date_released = models.DateField(auto_now=False)
    likes = models.IntegerField(null=True)
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE, blank=False)

    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # artiste = models.One
    def __str__(self):
        return self.title

class Lyric(models.Model):
    content = models.TextField(null=True)
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE, blank=False)


# Create your models here.
