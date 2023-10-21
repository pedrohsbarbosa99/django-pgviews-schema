**NOTE** You need set `DEFAULT_SCHEMA` in your settings.py if your database use custom schema.

Add `DEFAULT_SCHEMA` in settings.py:

```python
# settings.py
...
DEFAULT_SCHEMA = "your_custom_schema" # default is public if not set
...
```

You can also sen ENV variable `PG_DEFAULT_VIEW_SCHEMA` to set the default schema.
