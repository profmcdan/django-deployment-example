import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'challengeProject.settings')

import django
django.setup()


# Fake pop scripts
import random
from proTwo.models import User
from faker import Faker


fakegen = Faker()

def add_user():
    pass

def populate(N = 10):

    for entry in range(N):
        fake_firstname = fakegen.name()
        fake_lastname = fakegen.name()
        fake_email = fakegen.email()

        user = User.objects.get_or_create(firstname=fake_firstname, lastname=fake_lastname, email=fake_email)[0]


if __name__ == '__main__':
    print('[INFO] <<< Populating Script ... ')
    populate(100)
    print('[INFO] <<< Populating Complete')
