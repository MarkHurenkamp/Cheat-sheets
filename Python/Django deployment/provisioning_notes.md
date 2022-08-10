Provisioning a new site
=======================

## Required packages:
* nginx
* Python 3.6+
* venv + pip
* git

Ubuntu install (replace X with the desired python version):
```
$ sudo apt update
$ sudo apt install nginx git python3X python3.X-env
```

## Nginx Virtual Host config:
* See nginx.template.conf
* Replace DOMAIN and USERNAME with appropriate names

## Systemd service:
* See gunicorn.systemd.template.service
* Replace DOMAIN, USERNAME and APPNAME with appropriate names


## Folder structure:

### Project:
```
/home/USERNAME/
└── sites
    ├── DOMAIN1
    |   ├── .env
    |   ├── db.sqlite3
    |   ├── manage.py
    |   ├── static
    |   ├── venv
    |   └── etc.
    └── DOMAIN2
        ├── .env
        ├── db.sqlite3
        └── etc.
```

### Config files:
```
/etc/
├── nginx/sites-available/
|  ├── DOMAIN1
|  └── DOMAIN2
└── systemd/system/
   ├── gunicorn-DOMAIN1.service
   └── gunicorn-DOMAIN2.service
```

## Starting / stopping service:
```
$ sudo systemctl start nginx
$ sudo systemctl daemon-reload
$ sudo systemctl enable gunicorn-DOMAIN1.service
$ sudo systemctl start gunicorn-DOMAIN1.service
```