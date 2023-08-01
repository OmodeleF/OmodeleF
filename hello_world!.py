from datetime import datetime

name = input("What is your name? ")

print(f"Hello {name}")

year_of_birth = input("What is your year of birth? ")

year_now = datetime.now().year

age = year_now - int(year_of_birth)

print(f"Your age is {age} years old")

print("Goodbye!")

