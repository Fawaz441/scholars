import dj_database_url 
from .base import *

prod_db  =  dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(prod_db)
DEBUG = False
ALLOWED_HOSTS = ['scholarsb.herokuapp.com']
# STATIC_ROOT = os.path.join(BASE_DIR,"staticfiles")
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
