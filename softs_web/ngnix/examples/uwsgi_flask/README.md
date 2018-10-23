# Nginx + uxsgi + flask



## Installation

```bash
pip install -r requirements.txt
```

## Démarer le wsgi

/var/www/project/venv/bin/uwsgi --ini /var/www/project/uwsgi.ini

uwsgi --master-fifo fifo --ini uwsgi.ini
