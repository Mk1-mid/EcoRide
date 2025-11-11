estandar = 100
premiun = 100
costo_estandar = 1000.0
costo_premiun = 2000.0
penalizacion = 0.20
print("Bienvenido a la terminal de alquiler")
bienvenida = int(input("Digita 1 para avanzar: \n "))

if bienvenida == 1:
    bucle = True
    while (bucle) == True:
        print("=======Menú de bicicletas======")
        opcion = int(input("Seleciona la opcion \n1)Alquilar una bicicleta \n2)Consultar tarifas \n3)Salir \n"))
        match opcion:
            case 1:
                
                print("Escoge la marca de bicicleta\n")
                bicicleta=int(input("1)Estandar \n2.)Premiun \n"))
                if bicicleta == 1:
                    print(f"El valor estandar es {costo_estandar} \n")
                    tiempo_uso = float(input("Ingrese el tiempo de uso \n"))
                    estandar=estandar-1
                    if tiempo_uso > 0:
                              
                        metodo_pago=int(input("Escoja metodo de pago \n 1)Para cancelar con efectivo \n 2)Para cancelar con tarjeta \n 3)Para cancelar con puntos\n"))
                        fin_semana = input("¿Es fin de semana? SI/NO \n").lower()
                        retraso = input("¿Hubo retraso? SI/NO \n").upper()
                        
                        print("--------------------------")
                        match metodo_pago:
                            case 1:
                                precio_base = costo_estandar * tiempo_uso 
                                print("Tu valor a pagar es:", precio_base)
                            case 2:
                                if tiempo_uso >=  60:
                                    descuento = 0.10
                                    total = costo_estandar* tiempo_uso*(1- descuento)
                                    print("tu valor a pagar es:", total)

                                    if fin_semana == "si":
                                        precio_weekend=total+total*0.05
                                        totalSemana = precio_weekend* tiempo_uso
                                        print("tu valor a pagar mas el fin de semana es de:" , totalSemana)

                                    elif fin_semana == "no":
                                        descuento = 0.10
                                    total = costo_estandar* tiempo_uso*(1- descuento)
                                    print(f"Su precio sigue siendo el mismo de: {total} ")

                                if retraso == "SI":
                                    precio_base=costo_estandar * tiempo_uso 
                                    totalPenalizacion = precio_base+costo_estandar*(1 * 0.20)
                                    print("tu valor a pagar por el retraso es: ",totalPenalizacion)
                                if retraso == "NO":
                                    continue
                                    
                                elif tiempo_uso<60:
                                    total = (costo_estandar * tiempo_uso)
                                    print("tu valor a pagar es:", total)

                                

                            case 3:
                                break

                    elif tiempo_uso == 0:
                        print("Tiempo incorrecto compa")      
                elif bicicleta == 2:
                    print(f"El valor premiun es {costo_premiun}")

