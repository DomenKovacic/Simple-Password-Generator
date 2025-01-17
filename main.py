# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = int(input("How many letters?\n"))
nr_symbols = int(input(f"How many symbols?\n"))
nr_numbers = int(input(f"How many numbers?\n"))

random_list = []

for i in range(0, nr_letters):
    random_list.append(random.choice(letters))
for i in range(0, nr_symbols):
    random_list.append(random.choice(symbols))
for i in range(0, nr_numbers):
    random_list.append(random.choice(numbers))

random.shuffle(random_list)
print('Your password is: ' + ''.join(random_list))