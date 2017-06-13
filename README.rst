dev-admin-theme
===============

Description
-----------

**dev-admin-theme** brings fresh air to the default Django Admin
interface which hasn't changed 10 years from the very first version of
Django framework. This theme just makes UI modern and clean.

This app just overrides default admin's CSS. All changes are about
colors, margins, sizes. Nothing major.

**No any markup changes**.

Installation
------------

Install via pip:
``pip install dev-admin-theme``

1. Put ``dev_admin_theme`` app in your *INSTALLED\_APPS* **before**
   ``django.contrib.admin``:

   ::

       INSTALLED_APPS = (
           ...
           'dev_admin_theme',
           'django.contrib.admin',
           ...
       )

2. That's it.

Compatibility
~~~~~~~~~~~~~

Works correct in Django 1.6+. Older Django versions use a slightly
different way to show icons, so it requires changing markup or adding
python logic to make this theme compatible.

Testing
~~~~~~~

Tested in: - IE7+ (IE7 and IE8 are OK in terms of graceful degradation)
- FF30+ (Windows, Ubuntu, OSX) - Chrome 35+ (Windows, Ubuntu, OSX) -
Safari 8 (OSX)

