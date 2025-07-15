import string
import secrets

print("Tu generador de contraseñas personal!")

# chars = 'abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ!?¿=&%$#,*+-Ç0123456789'

# Se puede utilizar de esta manera para tener el control de las mayusculas, minusculas, simbolos y numeros.

number = string.digits # 1234...
lower = string.ascii_lowercase # abcd...
upper = string.ascii_uppercase # ABCD...
simbols = '?¿!¡-.,Ç+*$%&/=#)^¨'

all = number + lower + upper + simbols

num = int(input('Cantidad de contraseñas? '))
length = int(input('Longitud de contraseña? '))

print('\nAqui estan tus contraseñas: ')

def validar(password):
    return (
        any(c.isupper() for c in password) and # Any (Si al menos uno es cierto, devuelve True)
        any(c.islower() for c in password) and
        any(c.isdigit() for c in password) and
        any(c in simbols for c in password)
        )
    

for _ in range(num):                        # Cantidad de contraseñas
    while True:                             # Hasta que sea valida
        password = ''
        for _ in range(length):
            password += secrets.choice(all) # Añadir caracteres
        if validar(password):               # Si es valida, la imprime
            print (password)
            break
        # Si NO es valida, vuelve al inicio de while y lo intenta de nuevo


# Utilizar .secrets en vez de .random para el cifrado
            
        