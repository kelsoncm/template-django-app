from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class Config(AppConfig):
    """Configuração da aplicação."""

    name = "django_newapp"
    label = "django_newapp"
    verbose_name = _("{{TITLE}}")
    default_auto_field = "django.db.models.BigAutoField"
