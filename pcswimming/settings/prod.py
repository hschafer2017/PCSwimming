# PRODUCTION SETTINGS
from .base import *
import dj_database_url

SECRET_KEY = os.environ.get('SECRET_KEY')

DATABASES = {
 'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}

