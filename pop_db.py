import os
import django
from faker import Faker
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bikestore_project.settings')
django.setup()

from rent.models import * # import statement must be AFTER the django.setup()


def pop_customer_table(nb):
    """Pre-fill Customer table"""
    p = Faker()
    for _ in range(nb):
        first_name = p.first_name()
        last_name = p.last_name()

        Customer.objects.create(
            f_name = first_name, 
            l_name = last_name,
            email=f'{first_name}.{last_name}@example.com',
            phone = p.phone_number(), 
            address = p.street_address(),
            city = p.city(),
            country = p.country()
        )


def pop_vehicle_size():
    """Pre-fill Size table"""
    labels = ['extra small', 'small', 'medium', 'large', 'extra large']
    for label in labels:
        obj, created = Size.objects.get_or_create(name=label)
        if created:
            print('new object create')
        else:
            print('object retrieved')


def pop_vehicle_type():
    """Pre-fill Type table"""
    labels = ['bike', 'electric bike', 'scooter', 'jetpack']
    for label in labels:
        obj, created = Type.objects.get_or_create(name=label)
        if created:
            print('new object create')
        else:
            print('object retrieved')


def pop_vehicles(nb):
    """Pre-fill Vehicle table"""
    print(nb)
    for _ in range(nb):
        random_type = random.choice(Type.objects.all())
        random_size = random.choice(Size.objects.all())
        Vehicle.objects.create(
            vtype = random_type,
            real_cost = random.randint(23, 100),
            vsize = random_size
        )


# pop_customer_table(20)
# pop_vehicle_size()
# pop_vehicle_type()
# pop_vehicles(2)
