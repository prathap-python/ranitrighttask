web: gunicorn rankitrighttask.wsgi:task --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate