from django.urls import path

from .views import all_languages, requested_video

urlpatterns = [
    path("", all_languages, name="languages"),
    path("<str:selected_lang>/", requested_video, name="selected_lang")
]
