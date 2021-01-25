import dj_database_url 
from .base import *

prod_db  =  dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(prod_db)
DEBUG = False
ALLOWED_HOSTS = ['scholarsb.herokuapp.com']
# STATIC_ROOT = os.path.join(BASE_DIR,"staticfiles")

# STATIC_ROOT = os.path.join(BASE_DIR,"staticfiles")
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (
	os.path.join(BASE_DIR,'static'),
)
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
