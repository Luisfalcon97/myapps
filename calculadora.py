print("""Bienvenidos a la calculadora
Para salir escribe "Salir"
Las operaciones son suma, multiplicación, división y resta
""")

resultado = ""
while True:
    if not resultado:
        resultado = input("Ingrese un número: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    operacion = input("Ingrese una operación ")
    if operacion.lower() == "salir":
        break
    n2 = input("Ingrese el siguiente número ")
    if n2 == "salir":
        break
    n2 = int(n2)
    if operacion == "suma":
        resultado += n2
    elif operacion == "resta":
        resultado -= n2
    elif operacion == "multiplicación":
        resultado *= n2
    elif operacion == "división":
        resultado /= n2
    else:
        print("Operación no válida")
        break
    print(f"El resultado de la operación es {resultado}")
    