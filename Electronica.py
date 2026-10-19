def validar_texto(texto):
    return len(texto.strip()) > 0

def validar_celular(celular):
    return(
        celular.isdigit()
        and len(celular) == 9
        and celular.startswith("9")
    )

def validar_precio(precio):
    return precio >= 0

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

def leer_precio(mensaje):
    while True:
        try:
            precio = float(input(mensaje))

            if validar_precio(precio):
                return precio

            print("Error: el precio no puede ser negativo.")

        except ValueError:
            print("Error: ingrese un precio valido.")

def registrar_ingreso(ingresos):
    print("\n------- REGISTRO DE TELEVISOR -------")

    cliente = leer_texto("Nombre del cliente: ")
    celular = leer_celular()
    marca = leer_texto("Marca del televisor: ")
    modelo = leer_texto("Modelo: ")
    serie = leer_texto("Numero de serie: ")

    for ingreso in ingresos:
        if (
            ingreso["serie"].lower() == serie.lower()
            and ingreso["estado"] != "Entregado"
        ):
            print("Error: el numero de serie ya esta registrado.")
            return

    falla = leer_texto("Falla reportada: ")

    presupuesto = leer_precio(
        "Presupuesto estimado de reparacion (S/.): "
    )

    fecha = leer_texto("Fecha de ingreso (dd/mm/aaaa): ")

    codigo = "TV-" + str(len(ingresos) + 1)

    ingreso = {
        "codigo": codigo,
        "cliente": cliente,
        "celular": celular,
        "marca": marca,
        "modelo": modelo,
        "serie": serie,
        "falla": falla,
        "presupuesto": presupuesto,
        "fecha": fecha,
        "estado": "En reparacion"
    }

    ingresos.append(ingreso)

    print("\nTelevisor registrado correctamente.")
    print("Codigo asignado: ", codigo)

def buscar_registro(ingresos):
    if len(ingresos) == 0:
        print("Todavia no hay televisores registrados.")
        return

    criterio = leer_texto(
        "Ingrese nombre, celular o codigo: "
    ).lower()

    encontrados = 0

    for ingreso in ingresos:
        if (
            ingreso["codigo"].lower() == criterio
            or ingreso["cliente"].lower() == criterio
            or ingreso["celular"] == criterio
        ):
            print("\n---------- DATOS DEL TELEVISOR ----------")
            print("Codigo: ", ingreso["codigo"])
            print("Clientes: ", ingreso["cliente"])
            print("Celular: ", ingreso["celular"])
            print("Marca: ", ingreso["marca"])
            print("Modelo: ", ingreso["modelo"])
            print("Numero de serie: ", ingreso["serie"])
            print("Falla reportada: ", ingreso["falla"])
            print("Presupuesto: S/.", ingreso["presupuesto"])
            print("Fecha de ingreso: ", ingreso["fecha"])
            print("Estado: ", ingreso["estado"])

            encontrados += 1

    if encontrados == 0:
        print("No se encontraron registros.")

                                        
def actualizar_estado(ingresos):
    if len(ingresos) == 0:
        print("Todavia no hay televisores registrados.")
        return

    codigo = leer_texto("Ingrese el codigo del televisor: ").upper()

    for ingreso in ingresos:
        if ingreso["codigo"].upper() == codigo:
            print("\n---------- DATOS DEL TELEVISOR ----------")
            print("Codigo: ", ingreso["codigo"])
            print("Cliente: ", ingreso["cliente"])
            print("Celular: ", ingreso["celular"])
            print("Marca: ", ingreso["marca"])
            print("Modelo: ", ingreso["modelo"])
            print("Numero de serie: ", ingreso["serie"])
            print("Falla reportada: ", ingreso["falla"])
            print("Presupuesto: S/", ingreso["presupuesto"])
            print("Fecha de ingreso: ", ingreso["fecha"])
            print("Estado actual: ", ingreso["estado"])

            print("1. En reparacion")
            print("2. Reparado")
            print("3. Entregado")

            opcion_estado = input("Seleccione el nuevo estado: ").strip()

            if opcion_estado == "1":
                ingreso["estado"] = "En reparacion"

            elif opcion_estado == "2":
                ingreso["estado"] = "Reparado"

            elif opcion_estado == "3":
                ingreso["estado"] = "Entregado"

            else:
                print("Opcion de estado invalida.")
                return

            print("Estado actualizado correctamente.")
            print("Nuevo estado: ", ingreso["estado"])
            

            if ingreso["estado"] == "Reparado":
                print("Contactar al cliente al: ",ingreso["celular"])
            return


def main():
    ingresos = []
    opcion = ""

    while opcion != "7":
        print("\n========== ELECTRONICA ALEX ==========")
        print("1. Registrar ingreso de televisor")
        print("2. Buscar registro por nombre, celular o codigo")
        print("3. Actualizar estado")
        print("4. Registrar compra de repuesto")
        print("5. Listar ingresos completos")
        print("6. Reporte de compras y ventas")
        print("7. Salir")

        opcion = input("\nElija una opcion (1-7): ").strip()

        if opcion == "1":
            registrar_ingreso(ingresos)

        elif opcion == "2":
            buscar_registro(ingresos)

        elif opcion == "3":
            actualizar_estado(ingresos)

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





    
