import variables.variables

usuario = "soluno"
contrasena = "777"

nombre_usuario = input("Ingrese su nombre de usuario: ")

registro_nuevo = False
acceso = False

while nombre_usuario != usuario:

    print("El nombre de usuario no está registrado.")

    registro = input("¿Desea registrarse? (Sí/No): ")

    while registro != "Sí" and registro != "No":

        print("Ingrese Sí o No.")
        registro = input("¿Desea registrarse? (Sí/No): ")

    if registro == "Sí":

        usuario = nombre_usuario
        print("El nombre de usuario ha sido registrado.")

        contrasena = input("Ingrese una contraseña: ")

        registro_nuevo = True
        acceso = True

    else:

        print("Ingrese un nombre de usuario válido.")
        nombre_usuario = input("Ingrese su nombre de usuario: ")

if registro_nuevo == False:

    contrasena_usuario = input("Ingrese la contraseña: ")

    contador = 1

    while contrasena_usuario != contrasena and contador < 3:

        print("La contraseña es incorrecta.")
        contrasena_usuario = input("Ingrese la contraseña: ")

        contador += 1

    if contrasena == contrasena_usuario:

        print("Acceso concedido.")

        acceso = True

    else:
        print("Se agotaron los intentos.")

proyectos = ["Proyecto 1", "Proyecto 2", "Proyecto 3"]

lista_tablas = [
    [[1, 2, 3], [4, 5, 6]],
    [[11, 12, 13], [14, 15, 16]]
]
#Variable para guardar la tabla que el usuario selecciono previamente
tabla_activa = None
nombre_tabla_activa = "uno"

if acceso == True:

    continuar = True

    while continuar:

        print("===== MENU PRINCIPAL =====")

        print("a) Proyectos")

        print ("b) Tablas")

        print("c) Variables")

        print("d) Mostrar")

        print("e) Estadistica")

        print("f) Salir")

        print("==========================")

        opcion = input("Ingrese una opcion: ")

        if opcion == "a":

            print("Proyectos disponibles:")
            for proyecto in proyectos:
                print(proyecto)

            proyecto_seleccionado = input("Ingrese el nombre del proyecto que desea seleccionar: ")

            encontrado = False
            while encontrado == False:
                for proyecto in proyectos:
                    if proyecto == proyecto_seleccionado:
                        encontrado = True

                if encontrado == False:
                    print("El proyecto ingresado no existe.")
                    proyecto_seleccionado = input("Ingrese el nombre del proyecto que desea seleccionar: ")
                    
            print("Proyecto seleccionado:", proyecto_seleccionado)

        elif opcion == "b":

            print("Tablas disponibles:")

            #Recorrido de matrices usando len y range para mostrarlas ordenadas
            for i in range(len(lista_tablas)):
                print(f"Tabla {i + 1}:")
                for fila in lista_tablas[i]:
                    print(fila)

            seleccion = int(input("Ingrese el número de la tabla que desea seleccionar: "))

            #Validacion de rango numerico para la seleccion de la tabla
        
            while seleccion < 1 or seleccion > len(lista_tablas):
                print("Número de tabla inválido.")
                seleccion = int(input(f"Ingrese un número entre 1 y {len(lista_tablas)}: "))
            
            #Guarda latabla sleccionada en la variable global
            tabla_activa = lista_tablas[seleccion - 1]
            nombre_tabla_activa = f"Tabla {seleccion}"
            print(f"¡{nombre_tabla_activa} seleccionada y activada!")

        elif opcion == "c":

            variables.variables.gestionar_variables()

        elif opcion == "d":

            print("Mostar informacion de tabla:")
            
            # Verificamos si el usuario ya seleccionó una tabla previamente en la opción b
            if tabla_activa is None:
                print("No hay ninguna tabla seleccionada. Por favor, vaya a la opción (b) primero.")
            else:
                print(f"Mostrando contenido de la {nombre_tabla_activa}:")
                for fila in tabla_activa:
                    print(fila)

        elif opcion == "e":
            print("Estadística")
            
            # Verificamos si hay una tabla seleccionada
            if tabla_activa is None:
                print("Primero debe seleccionar una tabla en la opción (b).")
            else:
                # Aplanamos la matriz en una sola lista simple usando append
                numeros = []
                for fila in tabla_activa:
                    for valor in fila:
                        numeros.append(valor)
                
                if len(numeros) == 0:
                    print("La tabla está vacía.")
                else:
                    print(f"Valores analizados de la {nombre_tabla_activa}: {numeros}")
                    
                    # 1. Conteo de elementos
                    cantidad = len(numeros)
                    print(f"- Cantidad de elementos: {cantidad}")
                    
                    # 2. Máximo y Mínimo
                    maximo = numeros[0]
                    minimo = numeros[0]
                    for n in numeros:
                        if n > maximo:
                            maximo = n
                        if n < minimo:
                            minimo = n
                    print(f"Valor máximo: {maximo}")
                    print(f"Valor mínimo: {minimo}")
                    
                    # 3. Promedio aritmético
                    suma = 0
                    for n in numeros:
                        suma += n
                    promedio_aritmetico = suma / cantidad
                    print(f"Promedio aritmético: {promedio_aritmetico}")
                    
                    # 4. Promedio geométrico
                    producto = 1
                    for n in numeros:
                        producto = producto * n
                    
                    if producto > 0:
                        promedio_geometrico = producto ** (1 / cantidad)
                        print(f"Promedio geométrico: {promedio_geometrico}")
                    else:
                        print("Promedio geométrico: No aplicable (contiene ceros o negativos)")

        elif opcion == "f":
            print("Programa finalizado.")
            continuar = False

        else:

            print("Opcion incorrecta.")
