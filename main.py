import secrets
import string

def generar_contrasena_segura():
    while True:
        try:
            longitud = int(input("Ingrese la longitud deseada para la contraseña (mínimo 6 caracteres): "))
            if longitud < 6:
                print("La longitud debe ser al menos de 6 caracteres. Inténtalo de nuevo.")
            else:
                break
        except ValueError:
            print("Por favor, ingrese un número válido.")

    
    letras_mayus = string.ascii_uppercase
    letras_minus = string.ascii_lowercase
    digitos = string.digits
    simbolos = '!@#$%^&*()-_+=<>?'

    
    caracteres = letras_mayus + letras_minus + digitos + simbolos

    
    contrasena = [
        secrets.choice(letras_mayus),
        secrets.choice(letras_minus),
        secrets.choice(digitos),
        secrets.choice(simbolos)
    ]

    if longitud > 4:
        contrasena += [secrets.choice(caracteres) for _ in range(longitud - 4)]

   
    secrets.SystemRandom().shuffle(contrasena)
    return ''.join(contrasena)

contrasena_segura = generar_contrasena_segura()
print("Contraseña segura generada:", contrasena_segura)
