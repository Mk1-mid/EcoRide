estandar = 100
premiun = 100
costo_estandar = 1000.0
costo_premiun = 2000.0
penalizacion = 0.20

print("Bienvenido a la terminal de alquiler")
try:
    bienvenida = int(input("Digita 1 para avanzar: \n "))
except ValueError:
    bienvenida = 0

if bienvenida == 1:
    bucle = True
    while bucle:
        print("=======Menú de bicicletas======")
        try:
            opcion = int(input("Selecciona la opción \n1) Alquilar una bicicleta \n2) Consultar tarifas \n3) Salir \n"))
        except ValueError:
            print("Ingrese una opción válida numérica.")
            continue
        
        match opcion:
            case 1:
                print("Escoge la marca de bicicleta\n")
                try:
                    bicicleta = int(input("1) Estandar \n2) Premiun \n"))
                except ValueError:
                    print("Opción inválida, inténtalo de nuevo.")
                    continue

                match bicicleta:
                    case 1:
                        print(f"El valor estandar es {costo_estandar} por minuto\n")
                        try:
                            tiempo_uso = float(input("Ingrese el tiempo de uso en minutos:\n"))
                        except ValueError:
                            print("Por favor, ingresa un número válido para el tiempo de uso.")
                            continue
                        
                        if tiempo_uso > 0:
                            try:
                                metodo_pago = int(input("Escoja método de pago \n1) Efectivo \n2) Tarjeta \n3) Puntos\n"))
                            except ValueError:
                                print("Método de pago inválido.")
                                continue
                            fin_semana = input("¿Es fin de semana? SI/NO \n").lower()
                            retraso = input("¿Hubo retraso? SI/NO \n").upper()
                            precio_base = costo_estandar * tiempo_uso
                            total = precio_base
                            if metodo_pago == 2 and tiempo_uso > 60:
                                total *= 0.9
                            elif metodo_pago == 3 and tiempo_uso < 10:
                                total = total
                            if fin_semana == "si":
                                total *= 1.05
                            if retraso == "SI":
                                total += precio_base * penalizacion
                            print("--------------------------")
                            print(f"Tipo de bicicleta: Estandar\nTiempo de uso: {tiempo_uso} min\nPrecio base: {precio_base}\nTotal a pagar: {total}")
                        else:
                            print("Tiempo incorrecto, inténtalo de nuevo")
                    
                    case 2:
                        print(f"El valor premiun es {costo_premiun} por minuto\n")
                        try:
                            tiempo_uso = float(input("Ingrese el tiempo de uso en minutos:\n"))
                        except ValueError:
                            print("Por favor, ingresa un número válido para el tiempo de uso.")
                            continue
                        
                        if tiempo_uso > 0:
                            try:
                                metodo_pago = int(input("Escoja método de pago \n1) Efectivo \n2) Tarjeta \n3) Puntos\n"))
                            except ValueError:
                                print("Método de pago inválido.")
                                continue
                            fin_semana = input("¿Es fin de semana? SI/NO \n").lower()
                            retraso = input("¿Hubo retraso? SI/NO \n").upper()
                            precio_base = costo_premiun * tiempo_uso
                            total = precio_base
                            if metodo_pago == 2 and tiempo_uso > 60:
                                total *= 0.9
                            elif metodo_pago == 3 and tiempo_uso < 10:
                                total = total
                            if fin_semana == "si":
                                total *= 1.05
                            if retraso == "SI":
                                total += precio_base * penalizacion
                            print("--------------------------")
                            print(f"Tipo de bicicleta: Premiun\nTiempo de uso: {tiempo_uso} min\nPrecio base: {precio_base}\nTotal a pagar: {total}")
                        else:
                            print("Tiempo incorrecto, inténtalo de nuevo")
                    
                    case _:
                        print("Opción inválida, selecciona 1 o 2.")
                        continue

                seguir = input("¿Deseas realizar otro alquiler? SI/NO \n").lower()
                if seguir != "si":
                    print("Gracias por usar EcoRide.")
                    
                    bucle = False

            case 2:
                print(f"Tarifas:\nEstandar: ${costo_estandar} por minuto\nPremiun: ${costo_premiun} por minuto")

            case 3:
                print("Gracias por usar EcoRide.")
                bucle = False

            case _:
                print("Ingrese una opción válida.")
else:
    print("Por favor digite 1 para avanzar. Vuelva a iniciar el programa.")
