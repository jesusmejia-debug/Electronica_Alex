from datetime import datetime
import struct

# Validaciones

def validar_texto(texto):
    return len(texto.strip()) > 0


def validar_celular(celular):
    return celular.isdigit() and len(celular) == 9 and celular.startswith("9")


def validar_dni(dni):
    return dni.isdigit() and len(dni) == 8


def validar_precio(precio):
    return precio >= 0


def validar_fecha(fecha):
    try:
        datetime.strptime(fecha, "%d/%m/%Y")
        return True
    except ValueError:
        return False


# Funcion de Entrada

def leer_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if validar_texto(texto):
            return texto
        print("Error: el campo no puede estar vacío.")


def leer_celular():
    while True:
        celular = input("Número de celular (9 dígitos, empieza con 9): ").strip()
        if validar_celular(celular):
            return celular
        print("Error: debe tener exactamente 9 dígitos y empezar con 9.")


def leer_dni():
    while True:
        dni = input("DNI del cliente (8 dígitos): ").strip()
        if validar_dni(dni):
            return dni
        print("Error: el DNI debe tener exactamente 8 dígitos numéricos.")


def leer_precio(mensaje):
    while True:
        try:
            precio = float(input(mensaje))
            if validar_precio(precio):
                return precio
            print("Error: el precio no puede ser negativo.")
        except ValueError:
            print("Error: ingrese un precio valido (número).")


def leer_fecha(mensaje):
    while True:
        fecha = input(mensaje).strip()
        if validar_fecha(fecha):
            return fecha
        print("Error: fecha invalida. Use el formato dd/mm/aaaa (ejemplo: 16/09/2026).")


#1. Registrar Ingreso de Televisor

def registrar_ingreso(ingresos):
    print("\n------- REGISTRO DE TELEVISOR -------")

    dni = leer_dni()
    cliente = leer_texto("Nombre del cliente: ")
    celular = leer_celular()
    marca = leer_texto("Marca del televisor: ")
    modelo = leer_texto("Modelo: ")
    serie = leer_texto("Número de serie: ")

    for ingreso in ingresos:
        if ingreso["serie"].lower() == serie.lower() and ingreso["estado"] != "Entregado":
            print("Error: el número de serie ya esta registrado y aun no ha sido entregado.")
            return

    falla = leer_texto("Falla reportada: ")
    presupuesto = leer_precio("Presupuesto estimado de reparación (S/.): ")
    fecha = leer_fecha("Fecha de ingreso (dd/mm/aaaa): ")

    ingreso = {
        "dni": dni,
        "cliente": cliente,
        "celular": celular,
        "marca": marca,
        "modelo": modelo,
        "serie": serie,
        "falla": falla,
        "presupuesto": presupuesto,
        "fecha": fecha,
        "estado": "En reparación"
    }

    ingresos.append(ingreso)
    print("\nTelevisor registrado correctamente.")
    print(f"  Cliente: {cliente} | DNI: {dni}")
    print(f"  Serie: {serie} | Estado: En reparación")


#2. Buscar Registros

def buscar_registro(ingresos):
    if not ingresos:
        print("Todavia no hay televisores registrados.")
        return

    criterio = leer_texto("Ingrese DNI, nombre o celular: ").lower()
    encontrados = []

    for ingreso in ingresos:
        if (ingreso["dni"] == criterio or
            criterio in ingreso["cliente"].lower() or
            ingreso["celular"] == criterio):
            encontrados.append(ingreso)

    if not encontrados:
        print("No se encontraron registros.")
        return

    print(f"\nSe encontraron {len(encontrados)} registro(s):\n")
    for i, ingreso in enumerate(encontrados, 1):
        print(f"---------- REGISTRO {i} ----------")
        print(f"DNI:              {ingreso['dni']}")
        print(f"Cliente:          {ingreso['cliente']}")
        print(f"Celular:          {ingreso['celular']}")
        print(f"Marca:            {ingreso['marca']}")
        print(f"Modelo:           {ingreso['modelo']}")
        print(f"Número de serie:  {ingreso['serie']}")
        print(f"Falla reportada:  {ingreso['falla']}")
        print(f"Presupuesto:      S/. {ingreso['presupuesto']:.2f}")
        print(f"Fecha de ingreso: {ingreso['fecha']}")
        print(f"Estado:           {ingreso['estado']}")
        print()


#3. Actualizar Estado

def actualizar_estado(ingresos):
    if not ingresos:
        print("Todavia no hay televisores registrados.")
        return

    dni = leer_dni()
    encontrados = [i for i in ingresos if i["dni"] == dni]

    if not encontrados:
        print("No se encontraron registros con ese DNI.")
        return

    print("\n---------- TELEVISORES DEL CLIENTE ----------")
    for ingreso in encontrados:
        print(f"{ingreso['marca']} {ingreso['modelo']} | Serie: {ingreso['serie']} | Estado: {ingreso['estado']}")

    serie = leer_texto("\nIngrese el numero de serie del televisor a actualizar: ")

    for ingreso in encontrados:
        if ingreso["serie"].lower() == serie.lower():
            print(f"\nEstado actual: {ingreso['estado']}")
            print("1. En reparacion")
            print("2. Reparado")
            print("3. Entregado")

            opcion = input("Seleccione el nuevo estado (1-3): ").strip()

            estados = {
                "1": "En reparacion",
                "2": "Reparado",
                "3": "Entregado"
            }

            if opcion in estados:
                ingreso["estado"] = estados[opcion]
                print(f"\nEstado actualizado a: {ingreso['estado']}")

                if ingreso["estado"] == "Reparado":
                    print(f"Contactar al cliente al: {ingreso['celular']}")
            else:
                print("Opción de estado invalida.")
            return

    print("No se encontro un televisor con ese número de serie para este DNI.")


#4. Registrar Compra de Repuesto

def registrar_compra(compras, ingresos):
    print("\n------- REGISTRO DE COMPRA DE REPUESTO -------")

    dni = leer_dni()

    existe = any(i["dni"] == dni for i in ingresos)
    if not existe:
        print("Error: no existe ningún televisor registrado con ese DNI.")
        print("Primero debe registrar el ingreso del televisor.")
        return

    repuesto = leer_texto("Descripción del repuesto: ")
    costo = leer_precio("Costo del repuesto (S/.): ")
    fecha = leer_fecha("Fecha de compra (dd/mm/aaaa): ")

    compra = {
        "dni": dni,
        "repuesto": repuesto,
        "costo": costo,
        "fecha": fecha
    }

    compras.append(compra)
    print("\nCompra de repuesto registrada correctamente.")


#5. Listar Ingresos

def listar_ingresos(ingresos):
    if not ingresos:
        print("No hay ingresos registrados.")
        return

    print("\n---------- LISTA DE INGRESOS ----------")
    for i, ingreso in enumerate(ingresos, 1):
        print(f"\n[{i}] DNI: {ingreso['dni']} | Cliente: {ingreso['cliente']}")
        print(f"    {ingreso['marca']} {ingreso['modelo']} | Serie: {ingreso['serie']}")
        print(f"    Falla: {ingreso['falla']}")
        print(f"    Presupuesto: S/. {ingreso['presupuesto']:.2f} | Fecha: {ingreso['fecha']}")
        print(f"    Estado: {ingreso['estado']}")


#6. Reporte de Compras y Presupuestos

def reporte_compras_ventas(ingresos, compras):

    print("\n------- REPORTE DE COMPRAS Y VENTAS -------")

    # Calcular los totales
    total_compras = sum(c["costo"] for c in compras)
    total_ventas = sum(i["presupuesto"] for i in ingresos)
    balance = total_ventas - total_compras

    # Mostrar resultados
    print(f"\nTotal gastado en compras: S/. {total_compras:.2f}")
    print(f"Total de presupuestos registrado: S/. {total_ventas:.2f}")
    print(f"Balance general: S/. {balance:.2f}")

    # Submenú para elegir el tipo de archivo
    while True:
        print("\n------- GUARDAR REPORTE -------")
        print("1. Guardar en archivo TXT")
        print("2. Guardar en archivo BINARIO")
        print("3. Ver registros guardados en TXT")
        print("4. Regresar al menu principal")

        opcion = input("\nSeleccione una opcion (1-4): ").strip()

        # OPCION 1: Guardar en TXT
        if opcion == "1":

            with open("reporte_compras_ventas.txt", "w", encoding="utf-8") as archivo:
                archivo.write("=== REPORTE DE COMPRAS Y VENTAS - ELECTRONICA ALEX ===\n")
                archivo.write(f"Total Compras: S/. {total_compras:.2f}\n")
                archivo.write(f"Total Ventas (Ingresos): S/. {total_ventas:.2f}\n")
                archivo.write(f"Balance: S/. {balance:.2f}\n")

            print("\nReporte guardado correctamente en TXT.")
            print("\n--- DATOS GUARDADOS EN TXT ---")
            with open("reporte_compras_ventas.txt", "r", encoding="utf-8") as archivo:
                print(archivo.read())

        # OPCION 2: Guardar en BINARIO
        elif opcion == "2":

            # Convertir los montos a centimos para guardar enteros
            compras_centimos = round(total_compras * 100)
            ventas_centimos = round(total_ventas * 100)
            balance_centimos = round(balance * 100)

            # Guardar los tres valores en formato binario
            with open("reporte_compras_ventas.bin", "wb") as archivo:
                archivo.write(struct.pack("<iii",
                    compras_centimos,
                    ventas_centimos,
                    balance_centimos
                ))

            print("\nReporte guardado correctamente en BINARIO.")

            # Leer el archivo binario para comprobar los datos
            with open("reporte_compras_ventas.bin", "rb") as archivo:
                bloque = archivo.read(12)

                if len(bloque) != 12:
                    print("Error: registro incompleto.")
                else:
                    compras_leidas, ventas_leidas, balance_leido = struct.unpack("<iii", bloque)

                    print("\n--- DATOS LEIDOS DEL ARCHIVO BINARIO ---")
                    print(f"Total Compras: S/. {compras_leidas / 100:.2f}")
                    print(f"Total Ventas: S/. {ventas_leidas / 100:.2f}")
                    print(f"Balance: S/. {balance_leido / 100:.2f}")
            # OPCION 3: Ver registros guardados en TXT
        elif opcion == "3":
            print("\n--- REGISTROS GUARDADOS EN TXT ---")
            try:
                with open("reporte_compras_ventas.txt", "r", encoding="utf-8") as archivo:
                    datos = archivo.read()

                if datos:
                    print(datos)
                else:
                    print("El archivo TXT esta vacio.")

            except FileNotFoundError:
                print("Todavia no existe un archivo TXT. Primero debe guardar un reporte.")

        # OPCION 4: Regresar
        elif opcion == "4":
            print("\nRegresando al menu principal...")
            break
        else:
            print("\nOpcion invalida. Elija del 1 al 4.")

#Menu Principal

def main():
    ingresos = []
    compras = []

    while True:
        print("\n========== ELECTRONICA ALEX ==========")
        print("1. Registrar ingreso de televisor")
        print("2. Buscar registro por DNI, nombre o celular")
        print("3. Actualizar estado")
        print("4. Registrar compra de repuesto")
        print("5. Listar ingresos completos")
        print("6. Reporte de compras y ventas")
        print("7. Salir")

        opcion = input("\nElija una opción (1-7): ").strip()

        if opcion == "1":
            registrar_ingreso(ingresos)

        elif opcion == "2":
            buscar_registro(ingresos)

        elif opcion == "3":
            actualizar_estado(ingresos)

        elif opcion == "4":
            registrar_compra(compras, ingresos)

        elif opcion == "5":
            listar_ingresos(ingresos)

        elif opcion == "6":
            reporte_compras_ventas(ingresos, compras)

        elif opcion == "7":
            print("Hasta pronto.")
            break

        else:
            print("Opción invalida. Elija del 1 al 7.")


if __name__ == "__main__":
    main()