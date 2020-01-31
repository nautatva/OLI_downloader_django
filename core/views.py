from django.shortcuts import render
from .models import language, video
# Create your views here.


def all_languages(request):
    languages = language.objects.all()
    return render(request, "all_languages.html", {"names": languages})


def requested_video(request, selected_lang=''):
    lang = language.objects.filter(language_name=selected_lang)
    videos = video.objects.filter(language_name__id__in=lang)
    return render(request, "all_videos.html", {"videos": videos})
