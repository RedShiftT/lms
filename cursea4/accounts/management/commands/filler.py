from faker import Faker
from django.core.management.base import BaseCommand
# from accounts.models import Group
from accounts.models import CustomUserManager, CustomGroup
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from accounts.models import CustomUser


class Command(BaseCommand):
    help = 'Creates custom users.'


    def handle(self, *args, **options):
        user_manager = get_user_model().objects
        user_manager.create_superuser(email='a@a.us', password='1', first_name='Клоунович', last_name='Леха', father_name="Клоунович")


        fake = Faker()


        for g in ['101', '102', '201', '202']:
            try:
                group = CustomGroup(name=str(g))
                group.save()
            except:
                pass

            for _ in range(5):
                try:
                    user = user_manager.create_user(
                        email=fake.email(),
                        password=fake.password(),
                        first_name=fake.first_name(),
                        last_name=fake.last_name(),
                        father_name=fake.first_name_male(),
                    )
                    group.user_set.add(user)
                except:
                    pass
