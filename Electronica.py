def validar_texto(texto):
    return len(texto.strip()) > 0

def validar_celular(celular):
    return(
        celular.isdigit()
        and len(celular) == 9
        and celular.startswith("9")
    )

def leer_texto(mensaje):
    texto = input(mensaje).strip()

    while not validar_texto(texto):
        print("Error: el campo no puede estar vacio.")
        texto = input(mensaje).strip()

    return texto

def leer_celular():
    celular = input("Numero de celular (9 digitos): ").strip()

    while not validar_celular(celular):
        print("Error: ingrese 9 digitos y que empiece con 9.")
        celular = input("Numero de celular (9 digitos):").strip()

    return celular

def registrar_ingreso(ingresos):
    print("\n------- REGISTRO DE TELEVISOR -------")

    cliente = leer_texto("Nombre del cliente: ")
    celular = leer_celular()
    marca = leer_texto("Marca del televisor: ")
    modelo = leer_texto("Modelo: ")
    serie = leer_texto("Numero de serie: ")

    for ingreso in ingresos:
        if ingreso["serie"].lower() == serie.lower():
            print("Error: el numero de serie ya esta registrado.")
            return

    codigo = "TV-" + str(len(ingresos) + 1)

    ingreso = {
        "codigo": codigo,
        "cliente": cliente,
        "celular": celular,
        "marca": marca,
        "modelo": modelo,
        "serie": serie,
    }

    ingresos.append(ingreso)

    print("\nTelevisor registrado correctamente.")
    print("Codigo asignado: ", codigo)

def main():
    ingresos = []
    opcion = ""

    while opcion != "7":
        print("\n========== ELECTRONICA ALEX ==========")
        print("1. Registrar ingreso de televisor")
        print("2. Buscar registro por codigo")
        print("3. Actualizar estado")
        print("4. Registrar compra de repuesto")
        print("5. Listar ingresos completos")
        print("6. Reporte de compras y ventas")
        print("7. Salir")

        opcion = input("\nElija una opcion (1-7): ").strip()

        if opcion == "1":
            registrar_ingreso(ingresos)

        elif opcion == "2":
            print("Pendiente")

        elif opcion == "3":
            print("Pendiente")

        elif opcion == "4":
            print("Pendiente")

        elif opcion == "5":
            print("Pendiente")

        elif opcion == "6":
            print("Pendiente")

        elif opcion == "7":
            print("Hasta pronto.")

        else:
            print("Opcion invalida. Elija del 1 al 7.")

if __name__ == "__main__":
    main()





    
