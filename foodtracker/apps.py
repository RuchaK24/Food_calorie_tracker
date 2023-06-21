from django.apps import AppConfig


# The FoodtrackerConfig class is a subclass of AppConfig, which is a subclass of Django's built-in
# Python class named object.
class FoodtrackerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'foodtracker'
