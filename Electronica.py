from modulo_personal import calcular_costo_recursivo
from datetime import datetime
import struct
import json

# Archivos para guardar los registros
ARCHIVO_INGRESOS = "ingresos.json"
ARCHIVO_COMPRAS = "compras.json"

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


# Funciones de Entrada

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


# Guardar y cargar información

def guardar_datos(ingresos, compras):
    try:
        with open(ARCHIVO_INGRESOS, "w", encoding="utf-8") as archivo:
            json.dump(ingresos, archivo, indent=4, ensure_ascii=False)

        with open(ARCHIVO_COMPRAS, "w", encoding="utf-8") as archivo:
            json.dump(compras, archivo, indent=4, ensure_ascii=False)

        return True
    except OSError:
        print("Error al guardar los archivos.")
        return False


def cargar_datos():
    ingresos = []
    compras = []

    try:
        with open(ARCHIVO_INGRESOS, "r", encoding="utf-8") as archivo:
            ingresos = json.load(archivo)
    except FileNotFoundError:
        pass
    except (json.JSONDecodeError, OSError):
        print("No se pudieron cargar los ingresos.")

    try:
        with open(ARCHIVO_COMPRAS, "r", encoding="utf-8") as archivo:
            compras = json.load(archivo)
    except FileNotFoundError:
        pass
    except (json.JSONDecodeError, OSError):
        print("No se pudieron cargar las compras.")

    return ingresos, compras


# 1. Registrar Ingreso de Televisor

def registrar_ingreso(ingresos, compras):
    print("\n------- REGISTRO DE TELEVISOR -------")

    dni = leer_dni()
    cliente = leer_texto("Nombre del cliente: ")
    celular = leer_celular()
    marca = leer_texto("Marca del televisor: ")
    modelo = leer_texto("Modelo: ")
    serie = leer_texto("Número de serie: ")

    for ingreso in ingresos:
        if ingreso["serie"].lower() == serie.lower():
            if ingreso["estado"] != "Entregado":
                print("Error: el numero de serie ya esta registrado y aun no ha sido entregado.")
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
        "cobrado": 0.0,
        "fecha": fecha,
        "estado": "En reparacion"
    }

    ingresos.append(ingreso)
    guardar_datos(ingresos, compras)

    print("\nTelevisor registrado correctamente.")
    print(f"  Cliente: {cliente} | DNI: {dni}")
    print(f"  Serie: {serie} | Estado: En reparacion")


# 2. Buscar Registros

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
        print(f"Cobrado:          S/. {ingreso.get('cobrado', 0.0):.2f}")
        print(f"Fecha de ingreso: {ingreso['fecha']}")
        print(f"Estado:           {ingreso['estado']}")
        print()


# 3. Actualizar Estado

def actualizar_estado(ingresos, compras):
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

    serie = leer_texto("\nIngrese el numero de serie: ")

    for ingreso in encontrados:
        if ingreso["serie"].lower() == serie.lower():
            print(f"\nEstado actual: {ingreso['estado']}")

            if ingreso["estado"] == "En reparacion":
                print("1. En reparacion")
                print("2. Reparado")
            elif ingreso["estado"] == "Reparado":
                print("1. Reparado")
                print("2. Entregado")
            else:
                print("Este televisor ya fue entregado.")
                return

            opcion = input("Seleccione el nuevo estado: ").strip()

            if ingreso["estado"] == "En reparacion":
                if opcion == "1":
                    print("El televisor sigue en reparacion.")
                    return
                elif opcion == "2":
                    ingreso["estado"] = "Reparado"
                else:
                    print("Opción invalida.")
                    return

            elif ingreso["estado"] == "Reparado":
                if opcion == "1":
                    print("El televisor sigue reparado.")
                    return
                elif opcion == "2":
                    ingreso["estado"] = "Entregado"
                    ingreso["cobrado"] = leer_precio("Ingrese el importe cobrado (S/.): ")
                else:
                    print("Opción invalida.")
                    return

            print(f"\nEstado actualizado a: {ingreso['estado']}")

            if ingreso["estado"] == "Reparado":
                print(f"Contactar al cliente al: {ingreso['celular']}")

            guardar_datos(ingresos, compras)
            return

    print("No se encontro un televisor con ese número de serie para este DNI.")


# 4. Registrar Compra de Repuesto

def registrar_compra(compras, ingresos):
    print("\n------- REGISTRO DE COMPRA DE REPUESTO -------")

    if not ingresos:
        print("Primero debe registrar un televisor.")
        return

    dni = leer_dni()
    encontrados = [i for i in ingresos if i["dni"] == dni]

    if not encontrados:
        print("No existe ningun televisor registrado con ese DNI.")
        return

    print("\n---------- TELEVISORES DEL CLIENTE ----------")
    for ingreso in encontrados:
        print(f"Serie: {ingreso['serie']} | {ingreso['marca']} {ingreso['modelo']} | Estado: {ingreso['estado']}")

    serie = leer_texto("\nIngrese el numero de serie del televisor: ")
    existe = False

    for ingreso in encontrados:
        if ingreso["serie"].lower() == serie.lower():
            existe = True
            if ingreso["estado"] == "Entregado":
                print("No se pueden registrar repuestos para un equipo entregado.")
                return
            break

    if not existe:
        print("No se encontro ese numero de serie para el cliente.")
        return

    repuesto = leer_texto("Descripción del repuesto: ")
    costo = leer_precio("Costo del repuesto (S/.): ")
    fecha = leer_fecha("Fecha de compra (dd/mm/aaaa): ")

    compra = {
        "dni": dni,
        "serie": serie,
        "repuesto": repuesto,
        "costo": costo,
        "fecha": fecha
    }

    compras.append(compra)
    guardar_datos(ingresos, compras)
    print("\nCompra de repuesto registrada correctamente.")


# 5. Listar Ingresos 

def listar_ingresos(ingresos):
    if not ingresos:
        print("No hay ingresos registrados.")
        return

    print("\n---------- LISTA DE INGRESOS ----------")
    print("1. Ver todos")
    print("2. Filtrar por estado")
    print("3. Resumen por estado")
    print("4. Filtrar por marca")
    print("5. Filtrar por mes de ingreso")
    opcion = input("Elija una opcion (1-5): ").strip()

    lista = list(ingresos)
    titulo = "TODOS LOS INGRESOS"

    if opcion == "2":
        print("\n1. En reparacion  2. Reparado  3. Entregado")
        e = input("Estado a mostrar (1-3): ").strip()
        estados = {"1": "En reparacion", "2": "Reparado", "3": "Entregado"}
        if e not in estados:
            print("Opcion de estado invalida.")
            return
        lista = [x for x in ingresos if x["estado"].replace("ó", "o").lower() == estados[e].lower()]
        titulo = "ESTADO: " + estados[e].upper()
    elif opcion == "3":
        print("\n---------- RESUMEN POR ESTADO ----------")
        for est in ("En reparacion", "Reparado", "Entregado"):
            grupo = [x for x in ingresos if x["estado"].replace("ó", "o").lower() == est.lower()]
            suma_presupuesto = sum(x["presupuesto"] for x in grupo)
            suma_cobrado = sum(x.get("cobrado", 0.0) for x in grupo)
            print(f"{est}: {len(grupo)} televisor(es) | Presupuesto: S/. {suma_presupuesto:.2f} | Cobrado: S/. {suma_cobrado:.2f}")
        print(f"TOTAL: {len(ingresos)} televisor(es)")
        return
    elif opcion == "4":
        marca = input("Marca a buscar: ").strip().lower()
        if marca == "":
            print("Error: el campo no puede estar vacio.")
            return
        lista = [x for x in ingresos if marca in x["marca"].lower()]
        titulo = "MARCA: " + marca.upper()
    elif opcion == "5":
        texto = input("Mes a consultar (mm/aaaa, ejemplo 11/2026): ").strip()
        try:
            mes = datetime.strptime(texto, "%m/%Y")
        except ValueError:
            print("Error: use el formato mm/aaaa (ejemplo: 11/2026).")
            return
        lista = []
        for x in ingresos:
            f = datetime.strptime(x["fecha"], "%d/%m/%Y")
            if f.month == mes.month and f.year == mes.year:
                lista.append(x)
        titulo = "MES: " + texto
    elif opcion != "1":
        print("Opcion invalida.")
        return

    if not lista:
        print("No hay televisores con ese filtro.")
        return

    print(f"\n--- {titulo} ({len(lista)}) ---")
    for i, ingreso in enumerate(lista, 1):
        print(f"\n[{i}] DNI: {ingreso['dni']} | Cliente: {ingreso['cliente']}")
        print(f"    {ingreso['marca']} {ingreso['modelo']} | Serie: {ingreso['serie']}")
        print(f"    Falla: {ingreso['falla']}")
        print(f"    Presupuesto: S/. {ingreso['presupuesto']:.2f}")
        print(f"    Cobrado: S/. {ingreso.get('cobrado', 0.0):.2f}")
        print(f"    Fecha: {ingreso['fecha']}")
        print(f"    Estado: {ingreso['estado']}")
    print(f"\nTotal presupuestos mostrados: S/. {sum(x['presupuesto'] for x in lista):.2f}")
    print(f"Total cobrado mostrado: S/. {sum(x.get('cobrado', 0.0) for x in lista):.2f}")


# 6. Reporte de Compras y Presupuestos

def reporte_compras_ventas(ingresos, compras):
    print("\n------- REPORTE DE COMPRAS Y VENTAS -------")

    total_compras = calcular_costo_recursivo(compras)
    total_presupuestos = sum(i["presupuesto"] for i in ingresos)
    total_ventas = sum(i.get("cobrado", 0.0) for i in ingresos)
    balance = total_ventas - total_compras

    print(f"\nTotal gastado en compras: S/. {total_compras:.2f}")
    print(f"Total de presupuestos registrado: S/. {total_presupuestos:.2f}")
    print(f"Total de ventas registradas (Cobrado): S/. {total_ventas:.2f}")
    print(f"Balance general: S/. {balance:.2f}")

    while True:
        print("\n------- GUARDAR REPORTE -------")
        print("1. Guardar en archivo TXT")
        print("2. Guardar en archivo BINARIO")
        print("3. Ver registros guardados en TXT")
        print("4. Regresar al menu principal")

        opcion = input("\nSeleccione una opcion (1-4): ").strip()

        if opcion == "1":
            with open("reporte_compras_ventas.txt", "w", encoding="utf-8") as archivo:
                archivo.write("=== REPORTE DE COMPRAS Y VENTAS - ELECTRONICA ALEX ===\n")
                archivo.write(f"Total Compras: S/. {total_compras:.2f}\n")
                archivo.write(f"Total Presupuestos: S/. {total_presupuestos:.2f}\n")
                archivo.write(f"Total Cobrado: S/. {total_ventas:.2f}\n")
                archivo.write(f"Balance: S/. {balance:.2f}\n")

            print("\nReporte guardado correctamente en TXT.")
            with open("reporte_compras_ventas.txt", "r", encoding="utf-8") as archivo:
                print("\n--- DATOS LEIDOS DEL ARCHIVO TXT ---")
                print(archivo.read())

        elif opcion == "2":
            compras_centimos = round(total_compras * 100)
            ventas_centimos = round(total_ventas * 100)
            presupuestos_centimos = round(total_presupuestos * 100)
            balance_centimos = round(balance * 100)

            with open("reporte_compras_ventas.bin", "wb") as archivo:
                archivo.write(struct.pack("<iiii",
                    compras_centimos,
                    presupuestos_centimos,
                    ventas_centimos,
                    balance_centimos
                ))

            print("\nReporte guardado correctamente en BINARIO.")

            with open("reporte_compras_ventas.bin", "rb") as archivo:
                bloque = archivo.read(16)
                if len(bloque) != 16:
                    print("Error: registro incompleto.")
                else:
                    compras_leidas, presupuestos_leidos, ventas_leidas, balance_leido = struct.unpack("<iiii", bloque)
                    print("\n--- DATOS LEIDOS DEL ARCHIVO BINARIO ---")
                    print(f"Total Compras: S/. {compras_leidas / 100:.2f}")
                    print(f"Total Presupuestos: S/. {presupuestos_leidos / 100:.2f}")
                    print(f"Total Cobrado: S/. {ventas_leidas / 100:.2f}")
                    print(f"Balance: S/. {balance_leido / 100:.2f}")

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

        elif opcion == "4":
            print("\nRegresando al menu principal...")
            break
        else:
            print("\nOpcion invalida. Elija del 1 al 4.")


# Menú Principal

def main():
    ingresos, compras = cargar_datos()

    print("\nDatos anteriores cargados correctamente.")
    print(f"Televisores registrados: {len(ingresos)}")
    print(f"Compras registradas: {len(compras)}")

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
            registrar_ingreso(ingresos, compras)
        elif opcion == "2":
            buscar_registro(ingresos)
        elif opcion == "3":
            actualizar_estado(ingresos, compras)
        elif opcion == "4":
            registrar_compra(compras, ingresos)
        elif opcion == "5":
            listar_ingresos(ingresos)
        elif opcion == "6":
            reporte_compras_ventas(ingresos, compras)
        elif opcion == "7":
            guardar_datos(ingresos, compras)
            print("\nGuardando datos espere un momento...")
            print("Hasta pronto.")
            break
        else:
            print("Opción invalida. Elija del 1 al 7.")


if __name__ == "__main__":
    main()