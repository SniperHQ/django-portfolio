from django.apps import AppConfig
from django.contrib.auth import get_user_model
import os

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        if os.environ.get("RENDER"):
            User = get_user_model()
            if not User.objects.filter(username="admin").exists():
                User.objects.create_superuser(
                    username="admin",
                    email="hendry91234@gmail.com",
                    password="MI95@Sandf"
                )
