def validar_texto(texto):
    return len(texto.strip()) > 0


def validar_celular(celular):
    return(
        celular.isdigit()
        and len(celular) == 9
        and celular.startswith("9")
    )


def validar_dni(dni):
    return dni.isdigit() and len(dni) == 8


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


def leer_dni():
    dni = input("DNI del cliente: ").strip()

    while not validar_dni(dni):
        print("Error: el DNI debe tener 8 digitos.")
        dni = input("DNI del cliente: ").strip()

    return dni


def leer_precio(mensaje):
    while True:
        try:
            precio = float(input(mensaje))

            if validar_precio(precio):
                return precio

            print("Error: el precio no puede ser negativo.")

        except ValueError:
            print("Error: ingrese un precio valido.")

#1. Registrar Ingreso de Televisor

def registrar_ingreso(ingresos):
    print("\n------- REGISTRO DE TELEVISOR -------")

    dni = leer_dni()

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

    codigo = dni

    ingreso = {
        "codigo": codigo,
        "dni": dni,
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
    print("DNI del cliente: ", dni)
    print("Codigo asignado: ", codigo)

#2. Buscar Registros

def buscar_registro(ingresos):
    if len(ingresos) == 0:
        print("Todavia no hay televisores registrados.")
        return

    criterio = leer_texto(
        "Ingrese DNI, nombre o celular: "
    ).lower()

    encontrados = 0

    for ingreso in ingresos:
        if (
            ingreso["dni"] == criterio
            or ingreso["cliente"].lower() == criterio
            or ingreso["celular"] == criterio
        ):
            print("\n---------- DATOS DEL TELEVISOR ----------")
            print("DNI: ", ingreso["dni"])
            print("Cliente: ", ingreso["cliente"])
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

#3. Actualizar Estado  

def actualizar_estado(ingresos):
    if len(ingresos) == 0:
        print("Todavia no hay televisores registrados.")
        return

    dni = leer_dni()
    encontrados = []

    for ingreso in ingresos:
        if ingreso["dni"] == dni:
            encontrados.append(ingreso)

    if len(encontrados) == 0:
        print("No se encontraron registros con ese DNI.")
        return

    print("\n---------- DATOS DEL TELEVISOR ----------")

    for ingreso in encontrados:
        print("\nMarca: ", ingreso["marca"])
        print("Modelo: ", ingreso["modelo"])
        print("Numero de serie: ", ingreso["serie"])
        print("Estado: ", ingreso["estado"])
        print("--------------------------------------")

    serie = leer_texto("Ingrese el numero de serie del televisor: ")

    for ingreso in encontrados:
        if ingreso["serie"].lower() == serie.lower():
            print("\nEstado actual: ", ingreso["estado"])
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

    print("No se encontro un televisor con ese numero de serie.")

#4. Registrar Compra de Repuesto

def registrar_compra(compras):
    print("\n------- REGISTRO DE COMPRA DE REPUESTO -------")
    dni = leer_dni()
    repuesto = leer_texto("Descripcion del repuesto: ")
    costo = leer_precio("Costo del repuesto (S/.): ")
    fecha = leer_texto("Fecha de compra (dd/mm/aaaa): ")

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
    if len(ingresos) == 0:
        print("No hay ingresos registrados.")
        return

    print("\n---------- LISTA DE INGRESOS ----------")

    for ingreso in ingresos:
        print("\nDNI: ", ingreso["dni"])
        print("Cliente: ", ingreso["cliente"])
        print("Celular: ", ingreso["celular"])
        print("Marca: ", ingreso["marca"])
        print("Modelo: ", ingreso["modelo"])
        print("Numero de serie: ", ingreso["serie"])
        print("Falla reportada: ", ingreso["falla"])
        print("Presupuesto: S/.", ingreso["presupuesto"])
        print("Fecha de ingreso: ", ingreso["fecha"])
        print("Estado: ", ingreso["estado"])

#6. Reporte de Compras y Presupuestos

def reporte_compras_ventas(ingresos, compras):
    print("\n------- REPORTE DE COMPRAS Y VENTAS -------")
    
    total_compras = 0
    for compra in compras:
        total_compras += compra["costo"]
        
    total_ventas = 0
    for ingreso in ingresos:
        total_ventas += ingreso["presupuesto"]
        
    print(f"Total gastado en compras: S/. {total_compras:.2f}")
    print(f"Total de presupuestos registrado: S/. {total_ventas:.2f}")
    balance = total_ventas - total_compras
    print(f"Balance general: S/. {balance:.2f}")
    
    with open("reporte_compras_ventas.txt", "w", encoding = "utf-8") as archivo:
        archivo.write("=== REPORTE DE COMPRAS Y VENTAS - ELECTRONICA ALEX ===\n")
        archivo.write(f"Total Compras: S/. {total_compras:.2f}\n")
        archivo.write(f"Total Ventas (Ingresos): S/. {total_ventas:.2f}\n")
        archivo.write(f"Balance: S/. {balance:.2f}\n")
        
    print("\nReporte generado y guardado en 'reporte_compras_ventas.txt' exitosamente.")

#Menu Principal

def main():
    ingresos = []
    compras = []
    opcion = ""

    while opcion != "7":
        print("\n========== ELECTRONICA ALEX ==========")
        print("1. Registrar ingreso de televisor")
        print("2. Buscar registro por DNI, nombre o celular")
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
            registrar_compra(compras)

        elif opcion == "5":
            listar_ingresos(ingresos)

        elif opcion == "6":
            reporte_compras_ventas(ingresos, compras)

        elif opcion == "7":
            print("Hasta pronto.")

        else:
            print("Opcion invalida. Elija del 1 al 7.")
            

if __name__ == "__main__":
    main()
