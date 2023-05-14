from django.contrib import admin
from django.apps import apps

# Get all models defined in your app
app_models = apps.get_app_config('course').get_models()

# Register each model to the admin page
for model in app_models:
    admin.site.register(model)
