# test

from random_password_creator import Password

Password = Password('iuds', 82)
Password.set_the_charset()
Password.generate_password()
print(Password.get_password())