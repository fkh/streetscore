DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'spacialdb0_atogle',                      # Or path to database file if using sqlite3.
        'USER': 'atogle',                      # Not used with sqlite3.
        'PASSWORD': '9087411b5b',                  # Not used with sqlite3.
        'HOST': 'beta.spacialdb.com',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '9999',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'w1-&hl-hx+&+vg4ul0hr=)sjvau^6e#dj-igu@$%e(db=kv9_b'