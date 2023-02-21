
django-custom-accounts-plus

This module overrides Django's default User model

Important
---------
Add this model at the very start of the project. Before any migration.

Quick start
-----------
1. Add "accounts" to your INSTALLED_APPS setting (in settings.py)like this::
``
INSTALLED_APPS = [
    ...
    'accounts',
]
``
2. Add "AUTH_USER_MODEL" in settings (settings.py) like this::
``
AUTH_USER_MODEL = 'accounts.CustomUser'
``

3. Migrate
``
python manage.py migrate
``

TODO
----

Changelog
---------
1.0.1 - 2023-02-22 Arindam Dutta - First release

Copyright(c) 2023 Arindam Dutta
