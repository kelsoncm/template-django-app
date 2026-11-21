<!-- template:start -->
# template-django-app

Template de aplicação Django reutilizável (pacote instalável), com Ruff, pytest-django e cobertura mínima de 100%,
teste de migrações pendentes, pre-commit, documentação Sphinx (Furo) no GitHub Pages e release por tag com
publicação no PyPI via Trusted Publishing (sem token). Matriz de CI: Django 5.2 LTS, 6.0 e 6.1.

## Como usar

1. **Use this template > Create a new repository** (ex.: `django-auth-meuprovedor`).
2. Clone e rode o inicializador (só biblioteca padrão do Python 3.10+):

   ```bash
   python template_init.py --name auth_meuprovedor --title "Auth Meu Provedor" --description "..."
   ```

   `--name` vira o pacote `django_<name>` (rótulo da app) e o nome no PyPI `django-<name>`. O exemplo
   `django_newapp` e os marcadores são trocados e o script se apaga. Use `--dry-run` para conferir antes.
3. Desenvolva:

   ```bash
   python -m venv .venv && . .venv/bin/activate   # no Windows: .venv\Scripts\activate
   pip install -e ".[dev,docs]"
   pre-commit install --install-hooks -t pre-commit -t pre-push
   ```

4. Troque o modelo de exemplo `Item` pelos seus e recrie a migração inicial
   (`django-admin makemigrations django_<name> --settings=tests.settings --pythonpath=.`).
5. Ative o GitHub Pages (*Settings > Pages > Source: GitHub Actions*) e configure o Trusted Publisher no PyPI.

---
<!-- template:end -->
# django-newapp

{{DESCRIPTION}}

[![Tests](https://github.com/{{OWNER}}/django-newapp/actions/workflows/tests.yml/badge.svg)](https://github.com/{{OWNER}}/django-newapp/actions/workflows/tests.yml)

Documentação: <https://{{OWNER}}.github.io/django-newapp/>

## Instalação

```bash
pip install django-newapp
```

```python
INSTALLED_APPS = [
    # ...
    "django_newapp",
]
```

```bash
python manage.py migrate
```

## Desenvolvimento

```bash
pip install -e ".[dev,docs]"
pre-commit install --install-hooks -t pre-commit -t pre-push
ruff check . && ruff format --check . && pytest
django-admin makemigrations django_newapp --settings=tests.settings --pythonpath=.
sphinx-build -W -b html docs docs/_build/html
```

## Release

1. Atualize `version` no `pyproject.toml` e a seção no `CHANGELOG.md`.
2. `git tag vX.Y.Z && git push origin vX.Y.Z`: o workflow `release.yml` confere a versão, cria a release e publica
   no PyPI.

## Licença

[MIT](LICENSE.md).
