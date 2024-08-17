from django.core.management.base import BaseCommand

from users.models import CustomUser


class Command(BaseCommand):
    help = 'Команда для создания суперпользователя python manage.py create_superuser'

    def handle(self, *args, **options):
        user = CustomUser.objects.create(
            email='admin@localhost',
            first_name='Admin',
            last_name='Admin',
        )

        user.set_password('1234qwer')
        user.is_active = True
        user.is_superuser = True
        user.is_staff = True
        user.save()

        self.stdout.write(self.style.SUCCESS('Суперпользователь создан'))
