from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.core.management import call_command


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
