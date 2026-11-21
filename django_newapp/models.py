from django.db import models
from django.utils.translation import gettext_lazy as _


class Item(models.Model):
    """Modelo de exemplo: troque pelos modelos da aplicação e gere a migração com ``makemigrations``."""

    name = models.CharField(_("name"), max_length=255, unique=True)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)

    class Meta:
        verbose_name = _("item")
        verbose_name_plural = _("items")
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name
