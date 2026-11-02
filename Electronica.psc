Funcion ok <- validarTexto(t)  
	
	Definir ok Como Logico  
	ok <- (Longitud(t) > 0)  
FinFuncion  


Funcion ok <- validarCelular(c)  
	
	// Celular de 9 dígitos y sin decimales  
	Definir ok Como Logico  
	ok <- (c >= 900000000 Y c <= 999999999 Y c = Trunc(c))  
FinFuncion  

Funcion ok <- validarPrecio(p)  

	Definir ok Como Logico  
	ok <- (p >= 0)  
FinFuncion  

Algoritmo RegistroTelevisoresTaller  
	
	Definir MAX, opcion1, totalIng, totalRep, i, pos, encontrados, nuevo Como Entero  
	Definir codigos, clientes, marcas, modelos, series, fallas, fechas, estados Como Cadena  
	Definir celulares, presupuestos Como Real  
	Definir repProd Como Cadena  
	Definir repCompra, repVenta Como Real  
	Definir cliente, marca, modelo, serie, falla, fecha, producto, criterio, codigo Como Cadena  
	Definir celular, presupuesto, compra, venta, tCompra, tVenta Como Real  
	Definir existe Como Logico  

	MAX <- 500  

	Dimension codigos[501], clientes[501], celulares[501]  
	Dimension marcas[501], modelos[501], series[501], fallas[501]  
	Dimension presupuestos[501], fechas[501], estados[501]  
	Dimension repProd[501], repCompra[501], repVenta[501]  

	totalIng <- 0  
	totalRep <- 0  
	opcion1 <- 0  
	
	Mientras opcion1 <> 7 Hacer  

		Escribir ""  
		Escribir "===== ELECTRÓNICA ALEX ====="  
		Escribir "1. Registrar ingreso de televisor"  
		Escribir "2. Buscar registro"  
		Escribir "3. Actualizar estado (reparado / entregado)"  
		Escribir "4. Registrar compra de repuesto"  
		Escribir "5. Listar ingresos"  
		Escribir "6. Reporte de repuestos"  
		Escribir "7. Salir"  

		Repetir 
			
			Escribir "Elija una opción (1-7): "  
			Leer opcion1  
			Si opcion1 < 1 O opcion1 > 7 Entonces 
				
				Escribir "Error: Opción inválida. Ingrese un número entre 1 y 7." 
				
			FinSi 
			
		Hasta Que opcion1 >= 1 Y opcion1 <= 7 
		
		Segun opcion1 Hacer  
			
			1:  
				// ---------- REGISTRAR INGRESO ----------  		
				Si totalIng >= MAX Entonces  
					Escribir "Capacidad llena."  
				SiNo  
					Repetir  
						
						Escribir "Nombre del cliente: "  
						
						Leer cliente  
						Si No validarTexto(cliente) Entonces  
							
							Escribir "Error: el nombre no puede estar vacío."  
							
						FinSi  
					Hasta Que validarTexto(cliente)  
					
					Repetir  
						Escribir "Celular (9 dígitos): "  
						Leer celular  
						Si No validarCelular(celular) Entonces  
							Escribir "Error: ingrese un celular de 9 dígitos."  
							
						FinSi  
						
					Hasta Que validarCelular(celular)  
					
					Escribir "Marca del televisor: "  
					Leer marca  
					
					Escribir "Modelo: "  
					Leer modelo  
					
					Escribir "Número de serie: "  
					Leer serie  
					
					existe <- Falso  
					
					Si totalIng > 0 Entonces 
						
						Para i <- 1 Hasta totalIng Hacer  
							
							Si i <= 501 Entonces 
								
								Si series[i] = serie Y estados[i] <> "Entregado" Entonces  
									
									existe <- Verdadero  
									
								FinSi  
								
							FinSi 
							
						FinPara  
						
					FinSi 
					
					
					Si existe Entonces  
						Escribir "Aviso: ese televisor ya está registrado en reparación."  	
						
					SiNo  
						
						Escribir "Falla reportada: "  
						Leer falla  
						
						Repetir  
							
							Escribir "Presupuesto (S/): "  
							Leer presupuesto  
							
							Si No validarPrecio(presupuesto) Entonces  
								Escribir "Error: el presupuesto no puede ser negativo."  
								
							FinSi  	
							
						Hasta Que validarPrecio(presupuesto)  
						
						Escribir "Fecha de ingreso (dd/mm/aaaa): "  
						Leer fecha  
						
						totalIng <- totalIng + 1  
						
						codigos[totalIng] <- "TV-" + ConvertirATexto(totalIng)  
						clientes[totalIng] <- cliente  
						celulares[totalIng] <- celular  
						marcas[totalIng] <- marca  
						modelos[totalIng] <- modelo  
						series[totalIng] <- serie  
						fallas[totalIng] <- falla  
						presupuestos[totalIng] <- presupuesto  
						fechas[totalIng] <- fecha  
						estados[totalIng] <- "En reparación"  
						
						Escribir "Ingreso registrado con código: ", codigos[totalIng]  
						
					FinSi  
					
				FinSi  
					
			2:  	
				// ---------- BUSCAR REGISTRO ----------  
				Escribir "Ingrese nombre completo, celular o código: "  
				Leer criterio  
				
				criterio <- Minusculas(criterio)  
				
				encontrados <- 0  
				
				
				
				Para i <- 1 Hasta totalIng Hacer  
					
					Si Minusculas(clientes[i]) = criterio O Minusculas(codigos[i]) = criterio O ConvertirATexto(celulares[i]) = criterio Entonces  
						
						Escribir "-----------------------------------------"  
						Escribir "Código:      ", codigos[i]  
						Escribir "Cliente:     ", clientes[i], "  |  Celular: ", celulares[i]  
						Escribir "Televisor:   ", marcas[i], " ", modelos[i], "  |  Serie: ", series[i]  
						Escribir "Falla:       ", fallas[i]  
						Escribir "Presupuesto: S/ ", presupuestos[i]  
						Escribir "Fecha:       ", fechas[i], "  |  Estado: ", estados[i]  
						
						encontrados <- encontrados + 1  
						
					FinSi  
					
				FinPara  
				
				Si encontrados = 0 Entonces  
					Escribir "Sin resultados."  
					
				FinSi  
				
			3:  
				// ---------- ACTUALIZAR ESTADO ----------  
				Escribir "Código del ingreso (ej. TV-1): "  
				Leer codigo  
				
				pos <- 0  
				
				Para i <- 1 Hasta totalIng Hacer  
					
					Si Minusculas(codigos[i]) = Minusculas(codigo) Entonces  
						pos <- i  
						
					FinSi  
					
				FinPara  
				
				Si pos = 0 Entonces  
					Escribir "Código no encontrado."  
					
				SiNo  
					
					Escribir "-----------------------------------------"  
					Escribir "Código:      ", codigos[pos]  
					Escribir "Cliente:     ", clientes[pos], "  |  Celular: ", celulares[pos]  
					Escribir "Televisor:   ", marcas[pos], " ", modelos[pos], "  |  Serie: ", series[pos]  
					Escribir "Falla:       ", fallas[pos]  
					Escribir "Presupuesto: S/ ", presupuestos[pos]  
					Escribir "Fecha:       ", fechas[pos], "  |  Estado: ", estados[pos]  
					Escribir "1. Marcar como Reparado (avisar al cliente)"  
					Escribir "2. Marcar como Entregado"  
					Leer nuevo  
					Segun nuevo Hacer  
						
						1:  
							estados[pos] <- "Reparado"  
							Escribir "Estado actualizado. Llamar al cliente al: ", celulares[pos]  
							
						2:  
							estados[pos] <- "Entregado"  
							Escribir "Estado actualizado."  
							
						De Otro Modo:  
							Escribir "Opción inválida."  
							
					FinSegun  
					
				FinSi  
				
			4:  
				// ---------- REGISTRAR REPUESTO ----------  
				Si totalRep >= MAX Entonces  
					Escribir "Capacidad llena."  
					
				SiNo  
					
					Repetir  
						
						Escribir "Producto comprado: "  
						Leer producto  
						
						Si No validarTexto(producto) Entonces  
							
							Escribir "Error: el producto no puede estar vacío."  
							
						FinSi  
						
					Hasta Que validarTexto(producto)  
					
					Repetir  
						
						Escribir "Precio de compra (S/): "  
						Leer compra  
						
						Si No validarPrecio(compra) Entonces  
							Escribir "Error: precio inválido."  
							
						FinSi  
						
					Hasta Que validarPrecio(compra)  
					
					Repetir  
						
						Escribir "Precio de venta al cliente (S/): "  
						Leer venta  
						
						
						
						Si No validarPrecio(venta) Entonces  
							Escribir "Error: precio inválido."  
							
						FinSi  	
						
					Hasta Que validarPrecio(venta)  
					
					Si venta < compra Entonces  
						Escribir "Aviso: se venderá con pérdida."  
						
					FinSi  
					
					totalRep <- totalRep + 1  
					repProd[totalRep] <- producto  
					repCompra[totalRep] <- compra  
					repVenta[totalRep] <- venta  
					
					Escribir "Repuesto registrado. Ganancia: S/ ", venta - compra  
					
				FinSi  
				
			5:  
				// ---------- LISTAR INGRESOS ----------  
				
				Si totalIng = 0 Entonces  
					Escribir "No hay ingresos registrados."  
					
				SiNo  
					
					Para i <- 1 Hasta totalIng Hacer  
						
						Escribir "-----------------------------------------"  
						
						Escribir "Código:      ", codigos[i]  
						Escribir "Cliente:     ", clientes[i], "  |  Celular: ", celulares[i]  
						Escribir "Televisor:   ", marcas[i], " ", modelos[i], "  |  Serie: ", series[i]  
						Escribir "Falla:       ", fallas[i]  
						Escribir "Presupuesto: S/ ", presupuestos[i]  
						Escribir "Fecha:       ", fechas[i], "  |  Estado: ", estados[i]  
						
					FinPara  
					
				FinSi  
				
			6:  
				// ---------- REPORTE DE REPUESTOS ----------  
				
				tCompra <- 0  
				tVenta <- 0  
				
				Si totalRep = 0 Entonces  
					Escribir "No hay repuestos registrados."  
				SiNo  
					
					Para i <- 1 Hasta totalRep Hacer  
						
						Escribir i, ". ", repProd[i], " | Compra: S/ ", repCompra[i], " | Venta: S/ ", repVenta[i]  
						tCompra <- tCompra + repCompra[i]  
						tVenta <- tVenta + repVenta[i]  
						
					FinPara  
					
					Escribir "Total compras: S/ ", tCompra  
					Escribir "Total ventas:  S/ ", tVenta  
					Escribir "Ganancia:      S/ ", tVenta - tCompra  
					
				FinSi  	
				
			7:  
				Escribir "Hasta pronto."  
				
			De Otro Modo:  
				
				Escribir "Opción inválida."  
				
		FinSegun  

	FinMientras  

  

FinAlgoritmo 