# Generated by Django 3.0.2 on 2020-01-31 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Languages',
                'verbose_name_plural': 'Languages',
            },
        ),
        migrations.CreateModel(
            name='video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_name', models.CharField(max_length=255, unique=True)),
                ('youtube_url', models.CharField(max_length=255)),
                ('photo_url', models.CharField(max_length=255)),
                ('video_class', models.IntegerField()),
                ('subject', models.CharField(max_length=255)),
                ('language_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.language')),
            ],
            options={
                'verbose_name': 'video',
                'verbose_name_plural': 'videos',
            },
        ),
    ]
