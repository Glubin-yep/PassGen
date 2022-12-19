import random as ran

print("Entry a length for password ")
length = int(input(""))

symbol = "qwertyuiop[]asdfghjkl;'zxcvbnm,./1234567890-=QWERTYUIOP{}ASDFGHJKL:ZXCVBNM<>? !@#$%^&*()_+"
password = ""

for x in range(length):
    password += symbol[ran.randint(0,len(symbol))]

print(password)
