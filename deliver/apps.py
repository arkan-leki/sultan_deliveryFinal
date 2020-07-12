from django.apps import AppConfig


class DeliverConfig(AppConfig):
    name = 'deliver'
    verbose_name = 'سولتان گه‌یاندن'


from suit.apps import DjangoSuitConfig


class SuitConfig(DjangoSuitConfig):
    layoutt = 'vertical'
