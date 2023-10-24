# SQL Views for Postgres

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Adds first-class support for [PostgreSQL Views][pg-views] in the Django ORM and custom schema support.
Fork of the [django-pgviews-redux][django-pgviews-redux] by [xelixdev][xelixdev] with support for Django 3.2+ and schema postgres.

[pg-views]: http://www.postgresql.org/docs/9.1/static/sql-createview.html
[django-pgviews-redux]: https://github.com/xelixdev/django-pgviews-redux
[xelixdev]: https://github.com/xelixdev
[documentation]: https://pedrohsbarbosa99.github.io/django-pgviews-schema/

For full documentation, see [here][documentation].

## Examples

```python
from django.db import models

from django_pgviews import view as pg


class Customer(models.Model):
    name = models.CharField(max_length=100)
    post_code = models.CharField(max_length=20)
    is_preferred = models.BooleanField(default=False)

    class Meta:
        app_label = 'myapp'

class PreferredCustomer(pg.View):
    projection = ['myapp.Customer.*',]
    dependencies = ['myapp.OtherView',]
    sql = """SELECT * FROM myapp_customer WHERE is_preferred = TRUE;"""

    class Meta:
      app_label = 'myapp'
      db_table = 'myapp_preferredcustomer'
      managed = False
```

**NOTE** It is important that we include the `managed = False` in the `Meta` so
Django 1.7 migrations don't attempt to create DB tables for this view.

The SQL produced by this might look like:

```postgresql
CREATE VIEW myapp_preferredcustomer AS
SELECT * FROM myapp_customer WHERE is_preferred = TRUE;
```

To create all your views, run `python manage.py sync_pgviews`

You can also specify field names, which will map onto fields in your View:

```python
from django_pgviews import view as pg


VIEW_SQL = """
    SELECT name, post_code FROM myapp_customer WHERE is_preferred = TRUE
"""


class PreferredCustomer(pg.View):
    name = models.CharField(max_length=100)
    post_code = models.CharField(max_length=20)

    sql = VIEW_SQL
```
