To map onto a View, simply extend `pg_views.view.View`, assign SQL to the
`sql` argument and define a `db_table`. You must _always_ set `managed = False`
on the `Meta` class.

Views can be created in a number of ways:

1. Define fields to map onto the VIEW output
2. Define a projection that describes the VIEW fields

### Define Fields

Define the fields as you would with any Django Model:

```python
from django_pgviews import view as pg


VIEW_SQL = """
    SELECT name, post_code FROM myapp_customer WHERE is_preferred = TRUE
"""


class PreferredCustomer(pg.View):
    name = models.CharField(max_length=100)
    post_code = models.CharField(max_length=20)

    sql = VIEW_SQL

    class Meta:
      managed = False
      db_table = 'my_sql_view'
```

### Define Projection

`django-pgviews` can take a projection to figure out what fields it needs to
map onto for a view. To use this, set the `projection` attribute:

```python
from django_pgviews import view as pg


class PreferredCustomer(pg.View):
    projection = ['myapp.Customer.*',]
    sql = """SELECT * FROM myapp_customer WHERE is_preferred = TRUE;"""

    class Meta:
      db_table = 'my_sql_view'
      managed = False
```

This will take all fields on `myapp.Customer` and apply them to
`PreferredCustomer`
