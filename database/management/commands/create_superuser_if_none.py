import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = "Create default superuser if none exists"

    def handle(self, *args, **kwargs):
        if not User.objects.filter(is_superuser=True).exists():
            email = os.environ.get("DJANGO_SUPERUSER_EMAIL")
            username = os.environ.get("DJANGO_SUPERUSER_USERNAME")
            password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")

            if not all([email, username, password]):
                self.stderr.write("❌ Superuser env variables not set.")
                return

            self.stdout.write(f"Creating superuser {email}...")
            User.objects.create_superuser(email=email, username=username, password=password)
            self.stdout.write(self.style.SUCCESS("✅ Superuser created."))
        else:
            self.stdout.write("ℹ️ Superuser already exists.")