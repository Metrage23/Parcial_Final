"""
SISTEMA DE CIFRADO CÉSAR MODIFICADO (+N)

Permite encriptar, desencriptar y guardar mensajes mediante
sustitución de letras con un desplazamiento circular de N posiciones.
"""

ALFABETO = "abcdefghijklmnopqrstuvwxyz"

mensajes_guardados = []


def encriptar(mensaje, n):
    """Desplaza cada letra N posiciones hacia adelante (circular)."""
    resultado = ""
    for caracter in mensaje:
        letra = caracter.lower()
        if caracter.isalpha() and letra in ALFABETO:
            posicion = (ALFABETO.index(letra) + n) % 26
            nueva = ALFABETO[posicion]
            
            resultado += nueva.upper() if caracter.isupper() else nueva
        else:
            
            resultado += caracter
    return resultado


def desencriptar(mensaje, n):
    """Desplaza cada letra N posiciones hacia atrás (circular)."""
    resultado = ""
    for caracter in mensaje:
        letra = caracter.lower()
        if caracter.isalpha() and letra in ALFABETO:
            posicion = (ALFABETO.index(letra) - n) % 26
            nueva = ALFABETO[posicion]
            resultado += nueva.upper() if caracter.isupper() else nueva
        else:
            resultado += caracter
    return resultado


def pedir_mensaje(texto):
    """Pide un mensaje y valida que no esté vacío."""
    while True:
        mensaje = input(texto).strip()
        if mensaje:
            return mensaje
        print("Error: el mensaje no puede estar vacío.")


def pedir_desplazamiento():
    """Pide N y valida que sea un entero mayor o igual a 0."""
    while True:
        try:
            n = int(input("Ingrese el desplazamiento N (entero >= 0): ").strip())
            if n < 0:
                raise ValueError("N no puede ser negativo")
            return n
        except ValueError:
            print("Error: N debe ser un número entero mayor o igual a 0.")


def mostrar_menu():
    print("\nSISTEMA DE CIFRADO CÉSAR MODIFICADO")
    print("=================================")
    print("1. Encriptar mensaje (Opción de Guardar mensaje (S/N))")
    print("2. Desencriptar mensaje")
    print("3. Imprimir mensajes guardados")
    print("4. Salir")
    print("=================================")


def opcion_encriptar():
    mensaje = pedir_mensaje("Ingrese el mensaje a encriptar: ")
    n = pedir_desplazamiento()
    cifrado = encriptar(mensaje, n)

    print(f"\nMensaje original: {mensaje}")
    print(f"Mensaje cifrado:  {cifrado}")

    while True:
        guardar = input("\n¿Desea guardar el mensaje? (S/N): ").strip().upper()
        if guardar == "S":
            mensajes_guardados.append(
                {"original": mensaje, "cifrado": cifrado, "n": n}
            )
            print("Mensaje guardado correctamente.")
            break
        elif guardar == "N":
            print("El mensaje no fue guardado.")
            break
        else:
            print("Error: responda con S o N.")


def opcion_desencriptar():
    mensaje = pedir_mensaje("Ingrese el mensaje cifrado: ")
    n = pedir_desplazamiento()
    original = desencriptar(mensaje, n)
    print(f"\nMensaje cifrado:  {mensaje}")
    print(f"Mensaje original: {original}")


def opcion_imprimir():
    if not mensajes_guardados:
        print("\nNo hay mensajes guardados.")
        return

    print("\nMENSAJES GUARDADOS")
    print("-" * 40)
    for i, registro in enumerate(mensajes_guardados, start=1):
        print(f"{i}. Original: {registro['original']}")
        print(f"   Cifrado:  {registro['cifrado']}")
        print(f"   Desplazamiento (N): {registro['n']}")
        print("-" * 40)


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            opcion_encriptar()
        elif opcion == "2":
            opcion_desencriptar()
        elif opcion == "3":
            opcion_imprimir()
        elif opcion == "4":
            print("\n¡Gracias por usar el sistema! Hasta pronto.")
            break
        else:
            print("\nError: opción inexistente. Elija un número del 1 al 4.")


if __name__ == "__main__":
    main()