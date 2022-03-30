python -V
pylint --load-plugins pylint_django --disable=missing-docstring --django-settings-module=mysite.settings ./mysite/mysite
pylint --load-plugins pylint_django --disable=missing-docstring --django-settings-module=mysite.settings ./mysite/myapp