def pago():
    print("Se iniciará el proceso de pago")
    numero_tarjeta = int(input("Por favor digite el número de la tarjeta: "))
    numero_identificacion = int(input("Ingrese el número de identificación: "))
    print("Su pago fue aceptado. Por favor, retire su ticket.")

    while True:
        print("Bienvenido a la compra de boletos de tren. Por favor, ingrese el número correspondiente al destino al cual desea ir:")
        print("Destinos:\n1-- Paris\n2-- Tokio\n3-- España\n4-- Londres\n5-- Japón\n\n0-- Salir")
        numero_menu = int(input())

        if numero_menu == 1:
            destino = "Paris"
            print(f"Su destino elegido es {destino}")
        elif numero_menu == 2:
            destino = "Tokio"
            print(f"Su destino elegido es {destino}")
        elif numero_menu == 3:
            destino = "España"
            print(f"Su destino elegido es {destino}")
        elif numero_menu == 4:
            destino = "Londres"
            print(f"Su destino elegido es {destino}")
        elif numero_menu == 5:
            destino = "Japón"
            print(f"Su destino elegido es {destino}")
        elif numero_menu == 0:
            print("Muchas gracias por visitarnos. Nos vemos, vuelva pronto.")
            break

if __name__ == "__main__":
    pago()


