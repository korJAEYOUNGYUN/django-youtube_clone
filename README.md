## YouTube clone with django

A simple youtube clone app using django and mysql.

See [here](https://github.com/korJAEYOUNGYUN/youtube_clone) for screenshots.

## Features

- User model with additional fields for profile(avatar)
- Uploading, deleting and updating videos
- simple comments for videos

## Requirements

- Django
- MySQL
- MySQL connector for python
- env for DB access information

## Installation

```
git clone https://github.com/korJAEYOUNGYUN/django-youtube_clone.git
pip install -r requirements.txt
```

## Run
Dev:

```
python manage.py migrate --settings=django_youtube_clone.settings.development
python manage.py runserver --settings=django_youtube_clone.settings.development
```

Deploy:

```
python manage.py migrate
python manage.py collecstatic
python manage.py runserver
```

## Test

```
python manage.py test --settings=django_youtube_clone.settings.development
```