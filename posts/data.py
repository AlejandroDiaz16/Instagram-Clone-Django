from datetime import date

users = [
    {
        'email': 'cvander@platzi.com',
        'first_name': 'Christian',
        'last_name': 'Van der Henst',
        'password': '1234567',
        'is_admin': True
    },
    {
        'email': 'freddier@platzi.com',
        'first_name': 'Freddy',
        'last_name': 'Vega',
        'password': '987654321'
    },
    {
        'email': 'yesica@platzi.com',
        'first_name': 'Yésica',
        'last_name': 'Cortés',
        'password': 'qwerty',
        'birthdate': date(1990, 12,19)
    },
    {
        'email': 'arturo@platzi.com',
        'first_name': 'Arturo',
        'last_name': 'Martínez',
        'password': 'msicomputer',
        'is_admin': True,
        'birthdate': date(1981, 11, 6),
        'bio': "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
    }
]

from posts.models import User

for user in users:
    obj = User(**user)
    obj.save()
    print(obj.pk, ':', obj.email)