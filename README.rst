dev-admin-theme
===============

Description
-----------

**dev-admin-theme** is The Developer Society's customised version of the Django admin.


Installation
------------

Using pip_:

.. _pip: https://pip.pypa.io/

.. code-block:: console

    $ pip dev-admin-theme

Edit your Django project's settings module, and add ``dev_admin_theme`` **before**
``django.contrib.admin``:

.. code-block:: python

    INSTALLED_APPS = [
        # ...
        'dev_admin_theme',
        'django.contrib.admin',
        # ...
    ]


Development Instructions
------------------------

Gulp
~~~~

To run gulp for LESS processing:

.. code-block:: console

    $ npm install
    $ npm start

Keep this terminal window open in the background.

Django
~~~~~~

To run the demo instance (Python 3 only):

.. code-block:: console

    $ cd demo_project
    $ pip install -r requirements.txt
    $ ./manage.py migrate
    $ ./manage.py createsuperuser
    $ ./manage.py runserver
