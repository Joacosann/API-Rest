#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

# create superuser
echo "from django.contrib.auth.models import User; \
      User.objects.create_superuser('admin', 'jacosanchezz@gmail.com', 'admin')" \
      | python manage.py shell