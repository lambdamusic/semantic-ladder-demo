"""
Django settings: the semantics ladder's web pages, local only.

Django here is a way to write pages, not a live backend: no database, no auth, no admin.
Every page reads the experiment's own files when it opens (README.md, PLAN.md, RESULTS.md,
domains/, results/), so a new run shows up on reload. tools/site-dump mirrors the running
site into docs/ as a static site for GitHub Pages.
"""
import sys
from pathlib import Path

WEB_DIR = Path(__file__).resolve().parent
REPO_ROOT = WEB_DIR.parent.parent
sys.path.insert(0, str(REPO_ROOT))          # report.py and the domains, reused as they are
sys.path.insert(0, str(WEB_DIR / "apps"))

SECRET_KEY = "local-only-not-a-secret"
DEBUG = True
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

INSTALLED_APPS = ["django.contrib.staticfiles", "lab"]
MIDDLEWARE = ["django.middleware.common.CommonMiddleware"]
ROOT_URLCONF = "urls"
DATABASES = {}

TEMPLATES = [{
    "BACKEND": "django.template.backends.django.DjangoTemplates",
    "DIRS": [WEB_DIR / "templates-global"],
    "APP_DIRS": True,
    "OPTIONS": {"context_processors": ["lab.views.nav"]},
}]

STATIC_URL = "/static/"
STATICFILES_DIRS = [WEB_DIR / "static"]
STATIC_ROOT = REPO_ROOT / "build" / "collectstatic"

APP_NAME = "Semantics ladder"
