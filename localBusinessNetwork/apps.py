from django.apps import AppConfig


class localBusinessNetworkConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'localBusinessNetwork'
    models = "localBusinessNetwork.models"
