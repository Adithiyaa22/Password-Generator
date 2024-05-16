import random

password = int(input("Enter the length of the password "))

c="abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?" 

output = "".join(random.sample(c,password))

print(output)