from faker import Faker
from django.core.management.base import BaseCommand
from accounts.models import CustomGroup
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Creates custom users.'


    def handle(self, *args, **options):
        user_manager = get_user_model().objects
        user_manager.create_superuser(email='admin@lms.edu', password='Gjcnfdnt5', first_name='Админстратор', last_name='Хостингов', father_name="Сетевикович")


        fake = Faker()


        for g in ['101', '102', '201', '202']:
            student = user_manager.create_user(email=f'stundent{g}@lms.edu', password=f'cneltyn{g}', first_name='Алексей',
                                     last_name='Алексеев', father_name="Алексеевич")
            try:
                group = CustomGroup(name=str(g))
                group.save()
            except:
                continue
            student.group.add(group)
            for _ in range(5):
                try:
                    user = user_manager.create_user(
                        email=fake.email(),
                        password=fake.password(),
                        first_name=fake.first_name(),
                        last_name=fake.last_name(),
                        father_name=fake.first_name_male(),
                    )
                    user.group.add(group)
                except:
                    print('oops')

        lecGr = CustomGroup(name='lector')
        lecGr.save()
        lector = user_manager.create_user(email=f'lector@lms.edu', password=f'ktrwbz', first_name='Евгений', last_name='Евгеньев', father_name="Евгениевич")
        lector.group.add(lecGr)
