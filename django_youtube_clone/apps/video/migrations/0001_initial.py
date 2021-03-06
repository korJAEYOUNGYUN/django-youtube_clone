# Generated by Django 3.0.3 on 2020-02-21 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_file', models.FileField(upload_to='uploads/videos/')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('views', models.PositiveIntegerField(default=0)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Profile')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video.Video')),
            ],
        ),
    ]
