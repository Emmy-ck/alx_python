import random
number = random.randint(-10000, 10000)
x = number % 10 if number >= 0 else -(-number % 10)
output = ""
if x == 0:
    output = "and is 0"
elif x > 5:
    output = "and is greater than 5"
else:
    output = "and is less than 6 and not 0"
print("Last digit of {} is {} {}".format(number, x, output), end="\n")