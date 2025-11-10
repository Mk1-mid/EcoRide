estandar = 100
premuin = 100
costo_estandar = 1000.0
costo_premuin = 2000.0

print("Bienvenido a la terminal de alquiler")
Bienvenida = int(input("Digita 1 para avanzar: \n "))

if Bienvenida == 1:
    bucle = True
    while (bucle) == True:
        print("=======Menú de bicicletas======")
        opcion = int(input("Seleciona la opcion \n Digita 1 para alquilar una bicicleta \n Digita 2 para consultar tarifas \n y digita para salir"))
        match opcion:
            case 1:
                
                print("que bicicleta quieres")
                bicicleta=int(input("1)Estandar. \n 2.)Premiun"))
                if bicicleta == 1:
                    print(f"El valor estandar es {costo_estandar}")
                    tiempo_uso = int(input("Ingrese el tiempo de uso "))
                    estandar=estandar-1
                    if tiempo_uso > 0:
                        precio_base = costo_estandar * tiempo_uso       
                        metodo_pago=int(input("escoja metodo de pago \n digita 1 para efectivo \n  digita 2 para tarjeta \n digita 3 para puntos\n :"))
                        match metodo_pago
                            case 1:
                                print("tu valor a pagar es:", costo_estandar * tiempo_uso)
                            case 2:
                                print("tu valor a pagar es:", costo_estandar * tiempo_uso)
                                

                else bicicleta == 2:
                    print(f"El valor premiun es {costo_premuin}")
                
