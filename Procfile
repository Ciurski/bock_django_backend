web: python bocksite/manage.py collectstatic --noinput; bin/gunicorn_django --workers=4 --bind=0.0.0.0:$PORT bocksite/bocksite/settings.py
release: python manage.py migrate --noinput
web: gunicorn bocksite.bocksite.wsgi
