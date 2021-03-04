import os

#ruta del directorio en variable
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sqlite = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(base_dir,'db/sqlite/db.sqlite3'),
    }

}

postgresql = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db',
        'USER' : 'postgres',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT':'5432'
    }

}