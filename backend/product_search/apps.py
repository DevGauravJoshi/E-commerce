from django.apps import AppConfig


class ProductSearchConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'product_search'

    def ready(self):
        from .views import LoadProducts
        LoadProducts().RedisCreateIndex()
        LoadProducts().RedisDataLoad()