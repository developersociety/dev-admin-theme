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
