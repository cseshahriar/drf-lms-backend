import logging
from django.core.management.base import BaseCommand, CommandError
from accounts.models import User
from django.conf import settings
logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("email", nargs="+", type=str)

    def handle(self, *args, **options):
        if settings.DEBUG:
            email = options["email"][0]
            logger.info(f"{'-' * 5} email {email} {type(email)}")
            if User.objects.filter(email=email).exists():
                logger.info(f"{'-' * 5} user exists {email}")
                user = User.objects.filter(email=email).first()
                user.set_password("admin@123#")
                user.is_active = True
                user.is_staff = True
                user.is_superuser = True
                user.save()
            else:
                user = User.objects.create(email=email)
                user.set_password("admin@123#")
                user.is_active = True
                user.is_staff = True
                user.is_superuser = True
                user.save()
                logger.info(f"user created user: {user} pass: admin@123#")
        else:
            raise CommandError("This command only run in DEBUG mode")

        self.stdout.write(
            self.style.SUCCESS('Successfully close'))
