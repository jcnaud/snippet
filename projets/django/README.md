#

## Init project

```bash
pip install -r requirements.txt
django-admin startproject mysite
```


Result:

```
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        wsgi.py
```

# Run server

```bash
cd mysite
python manage.py runserver
```

Default open on http://127.0.0.1:8000/

After running **mysite/db.sqlite3** is created


# Create pools
```bash
cd mysite
python manage.py startapp polls
```
