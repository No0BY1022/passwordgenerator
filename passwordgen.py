import random
import string

name = str(input("Name of the password: "))
letters = str(input("Include letters (y/n): "))
symbols = str(input("Include symbols (y/n): "))
numbers = str(input("Include numbers (y/n): "))
length = int(input("Length: "))

def generate_random_letters(x):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(x))

def generate_random_numbers(y):
    return ''.join(str(random.randint(0, 9)) for _ in range(y))

def generate_random_symbols(z):
    symbols = string.punctuation  
    return ''.join(random.choice(symbols) for _ in range(z))

result = ""

total_length = length
num_letters = 0 if letters.lower() != 'y' else total_length // 3
num_symbols = 0 if symbols.lower() != 'y' else total_length // 3
num_numbers = 0 if numbers.lower() != 'y' else total_length - num_letters - num_symbols

if num_letters > 0:
    result += generate_random_letters(num_letters)
if num_symbols > 0:
    result += generate_random_symbols(num_symbols)
if num_numbers > 0:
    result += generate_random_numbers(num_numbers)

result_list = list(result)
random.shuffle(result_list)
result = ''.join(result_list)

print("Generated Password:", result)

try:
    with open("passwords.txt", "a") as file:
        file.write(f"{name}: {result}\n")
        print("Password saved successfully in 'passwords.txt'!")
except Exception as e:
    print(f"An error occurred while saving the password: {e}")
