# Simpla application showing how to use django-assets

Project based on Django 1.9

# Test bundle

To see files bundled:

- set `ASSETS_DEBUG` to False
- run `python manage.py collectstatic`
- run `python manage.py assets build`

At this point runserver should be useing build bundles
