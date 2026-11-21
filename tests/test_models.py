from __future__ import annotations

import pytest
from django.apps import apps
from django.core.management import call_command
from django.test import Client

from django_newapp.models import Item


def test_app_is_installed() -> None:
    assert apps.get_app_config("django_newapp").name == "django_newapp"


@pytest.mark.django_db
def test_item_str_is_its_name() -> None:
    item = Item.objects.create(name="Example")
    assert str(item) == "Example"


@pytest.mark.django_db
def test_no_missing_migrations() -> None:
    call_command("makemigrations", "django_newapp", "--check", "--dry-run", verbosity=0)


@pytest.mark.django_db
def test_admin_changelist(admin_client: Client) -> None:
    Item.objects.create(name="Listed")
    response = admin_client.get("/admin/django_newapp/item/")
    assert response.status_code == 200
    assert b"Listed" in response.content
