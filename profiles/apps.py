from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class profilesConfig(AppConfig):
    name = 'profiles'
    verbose_name = _('profiles')

    def ready(self):
        import profiles.signals  # noqa
