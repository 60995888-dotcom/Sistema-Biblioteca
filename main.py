libros = []
print("Bienvenid@ a la biblioteca universitaria!!!!!")

def registrar_libro():
    print("\n--- REGISTRAR LIBRO ---")
    titulo = input("Ingrese el titulo: ")
    autor = input("Ingrese el autor: ")
    codigo = input("Ingrese el codigo: ")
    
    libro = {
        "titulo": titulo,
        "autor": autor,
        "codigo": codigo,
        "estado": "Disponible"
    }

    libros.append(libro)
    print("Libro registrado correctamente.")

def mostrar_libros():
    print("\n--- LISTA DE LIBROS ---")


    if len(libros) == 0:
        print("No hay libros registrados.")
    else:
        for libro in libros:
            print("--------------------")
            print("Titulo:", libro["titulo"])
            print("Autor:", libro["autor"])
            print("Codigo:", libro["codigo"])
            print("Estado:", libro["estado"])

def prestar_libro():
    codigo = input("Ingrese el codigo del libro: ")

    for libro in libros:
        if libro["codigo"] == codigo:
            if libro["estado"] == "Disponible":
                libro["estado"] = "Prestado"
                print("Libro prestado correctamente.")
            else:
                print("El libro ya esta prestado.")
            return

    print("Libro no encontrado.")

def devolver_libro():
    codigo = input("Ingrese el codigo del libro: ")

    for libro in libros:
        if libro["codigo"] == codigo:
            if libro["estado"] == "Prestado":
                libro["estado"] = "Disponible"
                print("Libro devuelto correctamente.")
            else:
                print("El libro ya esta disponible.")
            return

    print("Libro no encontrado.")

def menu():
    while True:
        print("\n===== BIBLIOTECA =====")
        print("1. Registrar libro")
        print("2. Mostrar libros")
        print("3. Prestar libro")
        print("4. Devolver libro")
        print("5. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            registrar_libro()
        elif opcion == "2":
            mostrar_libros()
        elif opcion == "3":
            prestar_libro()
        elif opcion == "4":
            devolver_libro()
        elif opcion == "5":
            print("Gracias por utilizar el sistema.")
            break
        else:
            print("Opcion incorrecta.")

menu()

