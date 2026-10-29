import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'Creates default Super Admin user from environment variables.'

    def handle(self, *args, **options):
        username = os.getenv('SUPERADMIN_USERNAME', 'admin')
        email = os.getenv('SUPERADMIN_EMAIL', 'admin@its.edu.in')
        password = os.getenv('SUPERADMIN_PASSWORD', 'Admin123!')

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password,
                role=User.Role.SUPERADMIN,
                is_verified=True
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully created Super Admin: {username}'))
        else:
            self.stdout.write(self.style.WARNING(f'Super Admin {username} already exists.'))