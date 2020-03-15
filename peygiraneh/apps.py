from django.apps import AppConfig

import django


class PeygiranehConfig(AppConfig):
    name = 'peygiraneh'

    def ready(self):
        from django.contrib.auth.models import User
        from rest_framework.authtoken.models import Token
        for user in User.objects.all():
            Token.objects.get_or_create(user=user)
