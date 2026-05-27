import sqlite3

conn = sqlite3.connect('biblioteca.db')
cursor = conn.cursor()
cursor.execute(''' CREATE TABLE IF NOT EXISTS libros (
                 codigo_libro INT,
                 nombre TEXT, 
                 autor TEXT, 
                 año_de_publicacion TEXT, 
                 genero TEXT, 
                 sucursal TEXT, 
                 disponible TEXT)''')
cursor.execute(''' CREATE TABLE IF NOT EXISTS usuarios (
                   codigo_cliente INT, 
                   nombre TEXT, 
                   contacto TEXT, 
                   libro_alquilado TEXT, 
                   fecha_de_alquiler TEXT)''')
conn.commit()
registros = [
    (13, "Orgullo y prejuicio", "Jane Austin", "2011", "romantico", "sucursal Rivadavia", "si"),
    (56, "Harry Potter", "J.K Rowling", "2008", "fantasia", "sucursal Devoto", "no"),
    (21, "Alicia en el pais de las maravillas", "Lewis Carroll", "1865", "fantasia", "sucursal vicente lopez", "no"),
    (50, "El Naufrago", "Gabriel Garcia Marquez", "1955", "novela narrativa", "sucursal palermo", "si"),
    (23, "Cien años de soledad", "Gabriel Garcia Marquez", "1967", "realismo magico", "sucursal devoto", "no"),
    (20, "El Hobbit", "J.R.R Tolkien", "1937", "novela", "sucursal palermo", "no")
    ]
#for registro in registros:
    #sql = "INSERT INTO libros VALUES (?,?,?,?,?,?,?)"
    #cursor.execute(sql, registro)
    
registros = [
    (34, "Pamela Gomez", "1120934861", "Harry Potter", "01/11/24"),
    (20, "Camila Gonzales", "1102341940", "Alicia en el pais de las maravillas","03/11/24"),
    (10, "Sofia Gutierrez", "1104359922", "Cien años de soledad", "01/10/24"),
    (71, "Sol Ramirez", "1100742890", "El Hobbit", "25/02/24")
    ]
#for registro in registros:
     #sql = "INSERT INTO usuarios VALUES (?,?,?,?,?)"
     #cursor.execute(sql, registro)


def cargar_libros():
    cursor.execute('SELECT * FROM libros')
    libros = cursor.fetchall()

    return libros

def cargar_usuarios():
    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()
    
    return usuarios


def exportar_a_libroscsv():
    libros = cargar_libros()
    with open("libros.csv", "w", encoding="utf-8") as archivo:
      columnas = ["Codigo_de_libro, ", "Nombre, ", "Autor, " ,"Año_de_publicacion, ", "Genero, ", "Sucursal, ", "Disponible\n"]
      archivo.writelines(columnas)
      for libro in libros:
          archivo.write(f"{libro[0]},{libro[1]},{libro[2]},{libro[3]},{libro[4]},{libro[5]},{libro[6]}\n")
    print("Datos exportados a libros.csv correctamente.")
      

def exportar_a_usuarioscsv():
    usuarios = cargar_usuarios()
    with open("usuarios.csv","w",encoding="utf-8") as f:
        columnas = ["Codigo_cliente, ","Nombre, ","Contacto, ","Libro_alquilado, ","Fecha_de_alquiler\n"]
        f.writelines(columnas)
        for usuario in usuarios:
            f.write(f"{usuario[0]},{usuario[1]},{usuario[2]},{usuario[3]},{usuario[4]}\n")
    print("Datos exportados a usuarios.csv correctamente.")


def modificar_libros():
        campo = input("¿Que campo de la tabla desea modificar? (codigo_libro,nombre,autor,año_de_publicacion,genero,sucursal,disponible): ")
        cod_libro = int(input("Ingrese el codigo del libro que quiere modificar: "))
        if campo == "codigo_libro" or campo == "codigo libro":
            nuevo_cod = int(input("Ingrese el nuevo codigo para el libro: "))
            cursor.execute("UPDATE libros SET codigo_libro=? WHERE codigo_libro=?",(nuevo_cod,cod_libro))
            conn.commit()
        elif campo == "nombre":
            nuevo_nom = input("Ingrese el nuevo nombre para el libro: ")
            cursor.execute("UPDATE libros SET nombre=? WHERE codigo_libro=?",(nuevo_nom,cod_libro))
            conn.commit()
        elif campo == "autor":
            nuevo_autor = input("Ingrese el nombre del nuevo autor para el libro: ")
            cursor.execute("UPDATE libros SET autor=? WHERE codigo_libro=?",(nuevo_autor,cod_libro))
            conn.commit()
        elif campo == "año de publicacion" or campo == "año_de_publicacion":
            new_year = input("Ingrese el nuevo año de publicacion para el libro: ")
            cursor.execute("UPDATE libros SET año_de_publicacion=? WHERE codigo_libro=?",(new_year,cod_libro))
            conn.commit()
        elif campo == "genero" or campo == "género":
            nuevo_genero = input("Ingrese el nuevo genero para el libro: ")
            cursor.execute("UPDATE libros SET genero=? WHERE codigo_libro=?",(nuevo_genero,cod_libro))
            conn.commit()
        elif campo == "sucursal":
            nueva_sucursal = input("Ingrese la nueva sucursal para el libro: ")
            cursor.execute("UPDATE libros SET sucursal=? WHERE codigo_libro=?",(nueva_sucursal,cod_libro))
            conn.commit()
        elif campo == "disponible":
            disponibilidad = input("Ingrese el nuevo estado de disponibilidad para el libro (si/no): ")
            cursor.execute("UPDATE libros SET disponible=? WHERE codigo_libro=?",(disponibilidad,cod_libro))
            conn.commit()

def modificar_usuarios():
        campo = input("¿Que campo de la tabla desea modificar? (codigo_cliente,nombre,contacto,libro_alquilado,fecha_de_alquiler): ")
        cod_cliente = int(input("Ingrese el codigo del usuario que quiere modificar: "))
        if campo == "codigo_cliente" or campo == "codigo cliente":
            nuevo_cod = int(input("Ingrese el nuevo codigo para el usuario: "))
            cursor.execute("UPDATE usuarios SET codigo_cliente=? WHERE codigo_cliente=?",(nuevo_cod,cod_cliente))
            conn.commit()
        elif campo == "nombre":
            nuevo_nom = input("Ingrese el nuevo nombre para el usuario: ")
            cursor.execute("UPDATE usuarios SET nombre=? WHERE codigo_cliente=?",(nuevo_nom,cod_cliente))
            conn.commit()
        elif campo == "contacto":
            nuevo_contacto = input("Ingrese el nuevo numero de contacto para el usuario: ")
            cursor.execute("UPDATE usuarios SET contacto=? WHERE codigo_cliente=?",(nuevo_contacto,cod_cliente))
            conn.commit()
        elif campo == "libro alquilado" or campo == "libro_alquilado":
            nuevo_libro = input("Ingrese el nuevo libro alquilado para el usuario: ")
            cursor.execute("UPDATE usuarios SET libro_alquilado=? WHERE codigo_cliente=?",(nuevo_libro,cod_cliente))
            conn.commit()
        elif campo == "fecha de alquiler" or campo == "fecha_de_alquiler":
            nueva_fecha = input("Ingrese la nueva fecha de alquiler para el usuario: ")
            cursor.execute("UPDATE usuarios SET fecha_de_alquiler=? WHERE codigo_cliente=?",(nueva_fecha,cod_cliente))
            conn.commit()

def agregar_usuario():
        cod_cliente = int(input("Ingrese codigo de cliente: "))
        nombre = input("Ingrese el nombre del cliente: ")
        contacto = input("Ingrese el numero de telefono del cliente: ")
        libro_alquilado = input("Ingrese el nombre del libro que alquiló el cliente: ")
        fecha_alquiler = input("Ingrese la fecha en la que el cliente alquiló el libro: ")
        cursor.execute("INSERT INTO usuarios VALUES(?,?,?,?,?)",(cod_cliente,nombre,contacto,libro_alquilado,fecha_alquiler))
        conn.commit()
        exportar_a_usuarioscsv()

def agregar_libro():
        cod_libro = int(input("Ingrese el código del libro: "))
        nomb = input("Ingrese nombre del libro: ")
        autor = input("Ingrese nombre del autor del libro: ")
        publicacion = input("Ingrese el año de publicacion del libro: ")
        gen = input("Ingrese el género del libro: ")
        sucursal = input("Ingrese la sucursal en donde se encuentra el libro: ")
        disponible = input("Ingrese si el libro esta disponible (si/no): ")
        cursor.execute("INSERT INTO libros VALUES(?,?,?,?,?,?,?)",(cod_libro,nomb,autor,publicacion,gen,sucursal,disponible))
        conn.commit()
        exportar_a_libroscsv()

while True:
    print("\nMenú de opciones:")
    print("1. Ver libros")
    print("2. Ver libros disponibles")
    print("3. Consultar libros por género")
    print("4. Ver usuarios registrados")
    print("5. Agregar un registro")
    print("6. Modificar un registro")
    print("7. Eliminar un registro")
    print("8. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("\nTodos los libros:")
        libros = cargar_libros()
        for libro in libros:
            print(libro)

    elif opcion == "2":
        print("Todos los libros disponibles:")
        libros = cargar_libros()
        valor = "si"
        cursor.execute("SELECT * FROM libros WHERE disponible=?",(valor,))
        libros_disponibles = cursor.fetchall()
        for libro in libros_disponibles:
            print(libro)

    elif opcion == "3":
        genero = input("Ingrese el género del libro que quiere consultar: ")
        libros = cargar_libros()
        cursor.execute("SELECT * FROM libros WHERE genero=?",(genero,))
        libros_genero = cursor.fetchall()
        for libro in libros_genero:
            print(libro)

    elif opcion == "4":
        diccionario_usuarios = {}
        usuarios = cargar_usuarios()
        for usuario in usuarios:
            diccionario_usuarios[usuario[0]] = {
                "nombre": usuario[1],
                "contacto": usuario[2],
                "libro_alquilado": usuario[3],
                "fecha_de_alquiler": usuario[4]
            }
        for usuario,datos in diccionario_usuarios.items():
            print("\n")
            print("Codigo cliente:",usuario)
            print("Nombre:",datos["nombre"])
            print("Contacto:",datos["contacto"])
            print("Libro alquilado:",datos["libro_alquilado"])
            print("Fecha de alquiler:",datos["fecha_de_alquiler"])
        
    elif opcion == "5":
        respuesta = input("¿Desea agregar un registro en la tabla 'libros' o en la tabla 'usuarios'?: ")
        if respuesta == "usuarios":
            agregar_usuario()

        elif respuesta == "libros":
            agregar_libro()


    elif opcion == "6":
        resp = input("¿Desea modificar un registro de la tabla 'usuarios' o en la tabla 'libros'?: ")
        if resp == "libros":
            modificar_libros()
            exportar_a_libroscsv()
        elif resp == "usuarios":
            modificar_usuarios()
            exportar_a_usuarioscsv()

    elif opcion == "7":
        eliminar = input("¿Desea eliminar un registro de la tabla 'libros' o de la tabla 'usuarios'?: ")
        if eliminar == "libros":
            codigo_libro = int(input("Ingrese el codigo del libro que desea eliminar: "))
            cursor.execute("DELETE FROM libros WHERE codigo_libro=?", (codigo_libro,))
            conn.commit()
            exportar_a_libroscsv()
        elif eliminar == "usuarios":
            codigo_cliente = int(input("Ingrese el codigo del cliente que desea eliminar: "))
            cursor.execute("DELETE FROM usuarios WHERE codigo_cliente=?",(codigo_cliente,))
            conn.commit()
            exportar_a_usuarioscsv()


    elif opcion == "8":
        print("Saliendo...hasta luego!")
        break

    else:
        print("Opcion incorrecta,intentelo nuevamente\n")


conn.close()