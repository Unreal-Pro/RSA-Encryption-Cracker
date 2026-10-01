import random
# Import random to use for generating the very legitimate key

length = int(input("How long is the target private key? "))
# Takes the length of the needed key from the user

print(random.randint(10 ** (length - 1), (10 ** length) - 1))
# Prints the very legitimate private key
