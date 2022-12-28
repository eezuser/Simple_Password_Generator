# Password Generator
import random

first_name = input(str("First Name:"))
last_name = input(str("Last Name:"))
num = random.randint(1,500000)

def password_generator(first_name, last_name, number):
  t_password = first_name + last_name
  e_password = t_password.encode(encoding="UTF-8",errors="backslashreplace")
  return e_password

final_password = password_generator(first_name, str(num), last_name )
print(" Your password is: " + str(final_password))

