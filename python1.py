import random

print("bienvenido... ")

caracter = ("+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")

password_length = int(input("escribe la longitud de tu contraseña en numeros..."))

password = ""

for i in range(password_length):
    password += random.choice(caracter)

print(password)