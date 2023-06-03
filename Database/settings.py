DB_NAME = 'manzilak'
DB_USER = 'root'
DB_PASSWORD = 'admin123'
DB_HOST = 'localhost'
DB_PORT = '3306'

# Define the database settings dictionary
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': DB_HOST,
        'PORT': DB_PORT,
    }
}
