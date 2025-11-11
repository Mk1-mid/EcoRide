
# Inventario inicial (cantidad disponible)
inventario_estandar = 100
inventario_premium = 100

# Tarifas por minuto
costo_estandar = 1000.0
costo_premium = 2000.0

# Descuentos y recargos
descuento_tarjeta = 0.10           # 10% si paga con tarjeta y usa más de 60 minutos
recargo_fin_semana = 0.05          # 5% más si es fin de semana
penalizacion_retraso = 0.20        # 20% de penalización por retraso

# ==============================
# 🏁 INICIO DEL PROGRAMA (MENÚ DE BIENVENIDA)
# ==============================

while True:  # Este bucle permite que el programa se reinicie al final
    print("===================================")
    print("🚴‍ Bienvenido a la terminal de alquiler de ECO-RIDE 🚴‍")
    print("===================================")
    bienvenida = int(input("Digita 1 para avanzar o 0 para salir:\n> "))

    if bienvenida == 1:
        bucle = True  # Controla el menú interno de operaciones
        while bucle:
            print("\n======= MENÚ PRINCIPAL =======")
            print("1) Alquilar una bicicleta")
            print("2) Consultar tarifas")
            print("3) Salir al menú inicial")
            opcion = int(input("> "))

            match opcion:
                # ==============================
                # 🚲 OPCIÓN 1: ALQUILAR UNA BICICLETA
                # ==============================
                case 1:
                    print("\nEscoge el tipo de bicicleta:")
                    bicicleta = int(input("1) Estándar\n2) Premium\n> "))

                    # --- Elección Estándar ---
                    if bicicleta == 1:
                        print(f"\n💡 Valor por minuto: ${costo_estandar}")
                        tiempo_uso = float(input("Ingrese el tiempo de uso en minutos:\n> "))

                        if tiempo_uso > 0:
                            metodo_pago = int(input("Método de pago:\n1) Efectivo\n2) Tarjeta\n3) Puntos\n> "))
                            fin_semana = input("¿Es fin de semana? (SI/NO)\n> ").lower()
                            retraso = input("¿Hubo retraso? (SI/NO)\n> ").upper()

                            precio_base = costo_estandar * tiempo_uso
                            total = precio_base

                            # 💳 Descuento si paga con tarjeta y usó más de 60 min
                            if metodo_pago == 2 and tiempo_uso > 60:
                                total *= (1 - descuento_tarjeta)

                            # 🌞 Recargo por fin de semana
                            if fin_semana == "si":
                                total *= (1 + recargo_fin_semana)

                            # ⏰ Penalización por retraso
                            if retraso == "SI":
                                total += (precio_base * penalizacion_retraso)

                            # 📋 Resultado
                            print("\n------- RESUMEN DEL ALQUILER -------")
                            print(f"Tipo: Estándar\nTiempo: {tiempo_uso} min\nPrecio base: ${precio_base}\nTotal a pagar: ${total}\n")

                        else:
                            print("⚠️ Tiempo inválido. Intenta nuevamente.")

                    # --- Elección Premium ---
                    elif bicicleta == 2:
                        print(f"\n💡 Valor por minuto: ${costo_premium}")
                        tiempo_uso = float(input("Ingrese el tiempo de uso en minutos:\n> "))

                        if tiempo_uso > 0:
                            metodo_pago = int(input("Método de pago:\n1) Efectivo\n2) Tarjeta\n3) Puntos\n> "))
                            fin_semana = input("¿Es fin de semana? (SI/NO)\n> ").lower()
                            retraso = input("¿Hubo retraso? (SI/NO)\n> ").upper()

                            precio_base = costo_premium * tiempo_uso
                            total = precio_base

                            # 💳 Descuento si paga con tarjeta y usó más de 60 min
                            if metodo_pago == 2 and tiempo_uso > 60:
                                total *= (1 - descuento_tarjeta)

                            # 🌞 Recargo por fin de semana
                            if fin_semana == "si":
                                total *= (1 + recargo_fin_semana)

                            # ⏰ Penalización por retraso
                            if retraso == "SI":
                                total += (precio_base * penalizacion_retraso)

                            # 📋 Resultado
                            print("\n------- RESUMEN DEL ALQUILER -------")
                            print(f"Tipo: Premium\nTiempo: {tiempo_uso} min\nPrecio base: ${precio_base}\nTotal a pagar: ${total}\n")

                        else:
                            print("⚠️ Tiempo inválido. Intenta nuevamente.")

                    else:
                        print("⚠️ Opción inválida, intenta de nuevo.")

                    # 🔁 Repetir alquiler o salir
                    seguir = input("¿Deseas realizar otro alquiler? (SI/NO)\n> ").lower()
                    if seguir != "si":
                        bucle = False

                # ==============================
                # 💲 OPCIÓN 2: CONSULTAR TARIFAS
                # ==============================
                case 2:
                    print("\n======= TARIFAS DISPONIBLES =======")
                    print(f"🚲 Estándar: ${costo_estandar} por minuto")
                    print(f"🚴 Premium: ${costo_premium} por minuto")
                    print("-----------------------------------")

                # ==============================
                # 🚪 OPCIÓN 3: SALIR DEL MENÚ ACTUAL
                # ==============================
                case 3:
                    print("\nGracias por usar **EcoRide** 🌿")
                    print("Recuerda: ¡pedalear también ayuda al planeta! 💚")
                    bucle = False  # Sale del menú interno

                # ==============================
                # ❌ OPCIÓN INVÁLIDA
                # ==============================
                case _:
                    print("⚠️ Opción no válida, por favor intenta de nuevo.")

    elif bienvenida == 0:
        print("\n👋 ¡Hasta pronto! Gracias por visitar EcoRide 🌎")
        break  # Sale del bucle principal (finaliza el programa)
    else:
        print("⚠️ Opción incorrecta, intenta nuevamente.")
