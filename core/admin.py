from django.contrib import admin
from .models import language, video
# Register your models here.

from import_export import resources
from import_export.admin import ImportExportModelAdmin


class LanguageResource(resources.ModelResource):

    class Meta:
        model = language


class VideoResource(resources.ModelResource):

    class Meta:
        model = video


class LanguageAdmin(ImportExportModelAdmin):
    resource_class = LanguageResource


class VideoAdmin(ImportExportModelAdmin):
    resource_class = VideoResource


admin.site.register(language, LanguageAdmin)
admin.site.register(video, VideoAdmin)
