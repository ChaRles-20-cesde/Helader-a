helados = []  # Lista para almacenar los helados
contador_id = 1  # Contador para asignar IDs únicos

print("\nGestión de Helados")
while True:
    print("\n1. Agregar un helado")
    print("2. Ver lista de helados")
    print("3. Modificar un helado")
    print("4. Eliminar un helado")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":  # Agregar un helado
        print("Bienvenido a la página de helados")
        nombre = input("Ingrese el nombre del helado: ")
        descripcion = input("Ingrese la descripción del helado: ")

        while True: 
            precio = input("Digite el precio del producto: ").replace('.', '')  
            if precio.replace(',', '.', 1).isdigit():  
                precio = float(precio.replace(',', '.'))   # Error: variable mal escrita
                break
            else:
                print("Error: El precio debe ser un número válido.")

        helado = {"id": contador_id, "nombre": nombre, "descripcion": descripcion, "precio": precio}  # Error en claves del diccionario
        helados.append(helado) # Error: variable mal escrita
        contador_id += 1
        print("Helado agregado correctamente.")

    elif opcion == "2":  # Ver lista de helados
        if not helados:  # Error: variable incorrecta
            print("No hay helados registrados.")
        else:
            print("\nLista de Helados:")
            for helado in helados:
                print(f"ID: {helado['id']}, Nombre: {helado['nombre']}, Descripción: {helado['descripcion']}, Precio: ${helado['precio']:.0f}")

    elif opcion == "3":  # Modificar un helado
        id_modificar = input("Ingrese el ID del helado a modificar: ")

        if id_modificar.isdigit():
            id_modificar = int(id_modificar)
            encontrado = False

            for helado in helados:
                if helado["id"] == id_modificar:
                    nuevo_nombre = input("Nuevo nombre (deje en blanco para no cambiar): ")  # Error: doble signo igual
                    nueva_descripcion = input("Nueva descripción (deje en blanco para no cambiar): ")
                    nuevo_precio = input("Nuevo precio (deje en blanco para no cambiar): ")

                    if nuevo_nombre:
                        helado["nombre"] = nuevo_nombre
                    if nueva_descripcion:
                        helado["descripcion"] = nueva_descripcion
                    if nuevo_precio:
                        nuevo_precio = nuevo_precio.replace('.', '')  
                        if nuevo_precio.replace(',', '.', 1).isdigit():
                            helado["precio"] = float(nuevo_precio.replace(',', '.'))
                        else:
                            print("Error: El precio debe ser un número válido.")

                    print("Helado modificado correctamente.")
                    encontrado = True
                    break

            if not encontrado:
                print("Error: No se encontró un helado con ese ID.")
        else:
            print("Error: El ID debe ser un número.")

    elif opcion == "4":  # Eliminar un helado
        id_eliminar = input("Ingrese el ID del helado a eliminar: ")

        if id_eliminar.isdigit():
            id_eliminar = int(id_eliminar)
            encontrado = False

            for helado in helados:
                if helado["id"] == id_eliminar:
                    helados.remove(helado)  # Error: variable incorrecta
                    print("Helado eliminado correctamente.")
                    encontrado = True
                    break

            if not encontrado:
                print("Error: No se encontró un helado con ese ID.")
        else:
            print("Error: El ID debe ser un número.")

    elif opcion == "5":  # Salir
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida, intente nuevamente.")
