from os import getenv
from pathlib import Path

# User Accounts
AUTH_USER_MODEL = "accounts.CustomUser"  # New custom user
LOGIN_REDIRECT_URL = "registration_home"  # Log In
LOGOUT_REDIRECT_URL = "registration_home"  # Log Out

# Build paths inside the project like this: ROOT_DIR / 'subdir'.
SRC_DIR = Path(__file__).resolve().parent.parent
ROOT_DIR = SRC_DIR.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = getenv("DJANGO_SECRET_KEY", default="INVALID")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = getenv("DJANGO_DEBUG", default=False)

ALLOWED_HOSTS = getenv("DJANGO_ALLOWED_HOSTS", default="").split(",")


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "whitenoise.runserver_nostatic",  # whitenoise
    "django.contrib.staticfiles",
    "django.contrib.sites",
    # 3rd Party
    "crispy_forms",
    "rest_framework",  # rest framework
    "rest_framework.authtoken",  # token authentication
    "dj_rest_auth",  # rest auth
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "dj_rest_auth.registration",
    "drf_spectacular",
    # Local
    "accounts.apps.AccountsConfig",  # accounts apps
    "books.apps.BooksConfig",
    "apis.apps.ApisConfig",
    "todos.apps.TodosConfig",
    "posts.apps.PostsConfig",
]

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        # "rest_framework.permissions.AllowAny",
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        # "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # whitenoise
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [ROOT_DIR / "src/templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.request",
            ],
        },
    },
]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
SITE_ID = 1

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    # "default": {
    #     "ENGINE": "django.db.backends.sqlite3",
    #     "NAME": ROOT_DIR / "db.sqlite3",
    # }
    "default": {
        "ENGINE": getenv("DB_ENGINE"),
        "HOST": getenv("DB_HOST"),
        "NAME": getenv("DB_NAME"),
        "USER": getenv("DB_USER"),
        "PASSWORD": getenv("DB_PASSWORD"),
        "PORT": getenv("DB_PORT"),
    }
}


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "uk"

TIME_ZONE = "Europe/Kiev"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
# http://whitenoise.evans.io/en/stable/

STATIC_URL = "/src/static/"

STATICFILES_DIRS = [ROOT_DIR / "src/static"]

STATIC_ROOT = ROOT_DIR / "src/staticfiles"

STATICFILES_STORAGE = (
    "whitenoise.storage.CompressedManifestStaticFilesStorage"  # whitenoise
)


MEDIA_URL = "/media/"

MEDIA_ROOT = ROOT_DIR / "media"


# email
# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# DEFAULT_FROM_EMAIL = getenv("DEFAULT_FROM_EMAIL")
# EMAIL_HOST = getenv("EMAIL_HOST")
# EMAIL_PORT = getenv("EMAIL_PORT")
# EMAIL_HOST_USER = getenv("EMAIL_USER")
# EMAIL_HOST_PASSWORD = getenv("EMAIL_PASS")
# EMAIL_USE_TLS = getenv("EMAIL_USE_TLS")


# ALPHA_VANTAGE_BASE_URL = getenv(
#     "ALPHA_VANTAGE_BASE_URL", default="https://www.alphavantage.co"
# )
# ALPHA_VANTAGE_API_KEY = getenv("ALPHA_VANTAGE_API_KEY", default="82I46WMYT3C7EX3J")

SPECTACULAR_SETTINGS = {
"TITLE": "Blog API Project",
"DESCRIPTION": "A sample blog to learn about DRF",
"VERSION": "1.0.0",
# OTHER SETTINGS
}
