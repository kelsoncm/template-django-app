"""Configuração do Sphinx."""

from __future__ import annotations

import os
import sys
from importlib.metadata import version as package_version
from pathlib import Path

import django

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tests.settings")
django.setup()

project = "django-newapp"
author = "{{AUTHOR}}"
copyright = "{{YEAR}}, {{AUTHOR}}"
release = package_version("django-newapp")

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.githubpages",
    "sphinx.ext.viewcode",
]
autodoc_typehints = "description"
exclude_patterns = ["_build"]

html_theme = "furo"
html_title = f"django-newapp {release}"
