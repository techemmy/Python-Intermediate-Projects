import random

symbols = [chr(i) for i in range(33, 48)]
uppercase_letters = [chr(i) for i in range(65, 65+26)]
lowercase_letters = [chr(i) for i in range(97, 97+26)]
numbers = [chr(i) for i in range(48, 48+10)]
simlr_chr = ['1', 'l', 'o', '0', 'i']

characters = [symbols, uppercase_letters, lowercase_letters, numbers, simlr_chr]
password_length = int(input("Enter your password length > "))
password_characters = []

per_chr, remainder = divmod(password_length, len(characters))

password_characters = [random.choice(j) for i in range(per_chr)
                                        for j in characters]

for i in range(remainder):
    password_characters += random.sample(random.choice(characters), 1)

password = ''.join(password_characters)
print(password)