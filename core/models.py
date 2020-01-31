from django.db import models

# Create your models here.


class language(models.Model):

    language_name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Languages'
        verbose_name_plural = 'Languages'

    def __str__(self):
        return self.language_name


class video(models.Model):

    language_name = models.ForeignKey(
        to=language, on_delete=models.CASCADE,)
    video_name = models.CharField(max_length=255, unique=True)
    youtube_url = models.CharField(max_length=255)
    photo_url = models.CharField(max_length=255)
    video_class = models.IntegerField()
    subject = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'video'
        verbose_name_plural = 'videos'

    def __str__(self):
        return self.video_name
