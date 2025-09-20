import itertools
import string
import time

def force_brute(contraseña_decifrada):
    caracteres = string.ascii_letters + string.digits
    intentos = 0
    print("Empezando a decifrar...")
    start = time.time()

    for longitud in range(1, 7):
        print("Probando longitud ",longitud)
        for intento in map(''.join, itertools.product(caracteres, repeat=longitud)):
            intentos += 1
            if intento == contraseña_decifrada:
                elapsed = time.time() - start
                print("Contraseña decifrada: " + intento)
                print("Número de intentos:", intentos)
                print(f"Tiempo de ejecución: {elapsed:.4f} s")
                return

    elapsed = time.time() - start
    print("No se encontro la contraseña")
    print(f"Intentos totales: {intentos}")
    print(f"Tiempo transcurrido: {elapsed:.4f} s")

contraseña = input("Ingrese la contrasela a decifrar: ")
force_brute(contraseña)
