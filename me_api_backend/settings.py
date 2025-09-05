import environ, os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env(DEBUG=(bool, False))


SECRET_KEY = env("SECRET_KEY", default="insecure")
DEBUG = env("DEBUG")
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["*"])


INSTALLED_APPS = [
"django.contrib.admin",
"django.contrib.auth",
"django.contrib.contenttypes",
"django.contrib.sessions",
"django.contrib.messages",
"django.contrib.staticfiles",
"rest_framework",
"corsheaders",
"profiles",
]


MIDDLEWARE = [
"django.middleware.security.SecurityMiddleware",
"django.contrib.sessions.middleware.SessionMiddleware",
"corsheaders.middleware.CorsMiddleware",
"django.middleware.common.CommonMiddleware",
"django.middleware.csrf.CsrfViewMiddleware",
"django.contrib.auth.middleware.AuthenticationMiddleware",
"django.contrib.messages.middleware.MessageMiddleware",
"django.middleware.clickjacking.XFrameOptionsMiddleware",
]


ROOT_URLCONF = "me_api_backend.urls"


DATABASES = {
"default": {
"ENGINE": "django.db.backends.mysql",
"NAME": env("DB_NAME"),
"USER": env("DB_USER"),
"PASSWORD": env("DB_PASSWORD"),
"HOST": env("DB_HOST"),
"PORT": env("DB_PORT"),
}
}


CORS_ALLOWED_ORIGINS = env.list("CORS_ORIGIN_WHITELIST", default=[])
