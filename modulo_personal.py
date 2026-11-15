def calcular_costo_recursivo(compras, i=0):
    if i >= len(compras):  # Caso base / Condición de parada
        return 0.0
    return compras[i]["costo"] + calcular_costo_recursivo(compras, i + 1)
