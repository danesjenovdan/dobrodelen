from .base import *

DEBUG = os.getenv("DJANGO_DEBUG", False)

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "changeme")

STATIC_ROOT = os.getenv("DJANGO_STATIC_ROOT", os.path.join(BASE_DIR, "static"))
STATIC_URL = os.getenv("DJANGO_STATIC_URL", "/static/")
MEDIA_ROOT = os.getenv("DJANGO_MEDIA_ROOT", os.path.join(BASE_DIR, "media"))
MEDIA_URL = os.getenv("DJANGO_MEDIA_URL", "/media/")

ALLOWED_HOSTS = ["wagtail", "localhost", "api.dobrodelen.si"]
CSRF_TRUSTED_ORIGINS = ["https://api.dobrodelen.si", "https://dobrodelen.si"]

# DJANGO STORAGE SETTINGS
if os.getenv("DJANGO_ENABLE_S3", False):
    STORAGES["default"] = {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
    }
    AWS_ACCESS_KEY_ID = os.getenv("DJANGO_AWS_ACCESS_KEY_ID", "")
    AWS_SECRET_ACCESS_KEY = os.getenv("DJANGO_AWS_SECRET_ACCESS_KEY", "")
    AWS_STORAGE_BUCKET_NAME = os.getenv("DJANGO_AWS_STORAGE_BUCKET_NAME", "djnd")
    AWS_DEFAULT_ACL = "public-read"
    AWS_QUERYSTRING_AUTH = False
    AWS_LOCATION = os.getenv("DJANGO_AWS_LOCATION", "dobrodelen")
    AWS_S3_REGION_NAME = os.getenv("DJANGO_AWS_REGION_NAME", "fr-par")
    AWS_S3_ENDPOINT_URL = os.getenv(
        "DJANGO_AWS_S3_ENDPOINT_URL", "https://s3.fr-par.scw.cloud"
    )
    AWS_S3_SIGNATURE_VERSION = os.getenv("DJANGO_AWS_S3_SIGNATURE_VERSION", "s3v4")
    AWS_S3_FILE_OVERWRITE = False
