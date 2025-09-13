from random import choices
import string
from time import sleep

print('---------- RANDOM PASSWORD GENERATOR ----------')
generated_password = []
characters = string.ascii_letters + string.digits + string.punctuation

size = int(input('How many characters you need in this password?\n'))

password = choices(characters, k = size)
for x in password:
	generated_password.append(x)

final_password = ''.join(generated_password)
print('Generating password.', end ='\r')
sleep(1)
print('Generating password..', end ='\r')
sleep(1)
print('Generating password...')
sleep(1)
print(f'Your password: {final_password}')