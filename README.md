django-db-log-requestid
=======================

A small utility to append the `X-Request-Id` header to every SQL query emitted
by Django. This makes it easier to correlate logs from your database server
with your access logs.

Setup
-----
There are two steps needed to set up this module. The first is to configure
Django to use one of our 3 database backends, depending on your choice of
database.

 * `django_db_log_requestid.mysql`
 * `django_db_log_requestid.postgres`
 * `django_db_log_requestid.sqlite3`

Just but the correct database backend into your Django's `DATABASES` setting,
e.g.

    DATABASES = {
        'default': {
            'ENGINE': 'django_db_log_requestid.postgres',
            'NAME': 'mydb',
        }
    }


For the second step, you can either add
`django_db_log_requestid.middleware.DatabaseLogRequestIDMiddleware` to your
`MIDDLEWARES` (Django 1.10+) or `MIDDLEWARE_CLASSES`, or add
`django_db_log_requestid` to your `INSTALLED_APPS`. The latter sets up two
signal listeners to listen for Django's `django.core.signals.request_started`
and `django.core.signals.request_finished`.

Both methods put the `X-Request-Id` header into a threadlocal at the beginning
of every request.

Configuration
-------------

* `REQUEST_ID_HEADER_NAME`: set the name of the header to be used (default:
  `X-Request-Id`)

* `REQUEST_ID_SQL_TEMPLATE`: the template to be used when modifying the SQL
  query (default: `{sql} -- request_id={request_id}`)
* `REQUEST_ID_ENABLE_LOGGING`: if set to `True`, we will log every SQL query
  with the logger name `django_db_log_requestid` and level `INFO`. We recommend
  however to use your Databases logging facilities instead. (default: `False`)


How it works
------------

The database backends provided with `django_db_log_requestid` are (very) thin
wrappers around the stock database backends. They construct cursors which will
modify the SQL query before executing it, by appending the request id as a
comment to the query.


