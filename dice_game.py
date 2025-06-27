import random

name = input("What is your name? \n> ")
print(f"Hello, {name}!")

print("Rolling dice...")
d1 = random.randint(1, 6)
d2 = random.randint(1, 6)

print(f"Die 1: {d1}")
print(f"Die 2: {d2}")
print(f"Total value: {d1 + d2}")
