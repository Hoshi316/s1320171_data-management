import random

print("Rolling dice...")
d1 = random.randint(1, 6)
d2 = random.randint(1, 6)

total = d1 + d2
print(f"Die 1: {d1}")
print(f"Die 2: {d2}")
print(f"Total value: {total}")

if total > 7:
    print("You won!")
else:
    print("You lost!")
