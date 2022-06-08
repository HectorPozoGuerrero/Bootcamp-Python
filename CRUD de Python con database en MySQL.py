#Debemos de crear un CRUD que modifique la base de datos creada en MySQL.
#En nuestro caso, la base de datos la hemos llamado 'Oficinas'.

#----------------------CONSULTAS---------------------
#Función paramostrar un listado de oficinas:
def consulta_oficina():
    import pymysql
    try:
        conexion = pymysql.connect(host='localhost',
                               user='root',
                               password='47175627m',
                               db='oficinas')
        try:
            with conexion.cursor() as cursor:
                # En este caso no necesitamos limpiar ningún dato
                cursor.execute("SELECT id,nombre,direccion FROM oficinas;")
                # Con fetchall traemos todas las filas
                oficinas = cursor.fetchall()
                # Recorrer e imprimir
                for oficina in oficinas:
                    print(oficina)

        finally:
            conexion.close()

    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al conectar: ", e)

#Funcion para encontrar la oficina por nombre:
def busqueda_oficina_nombre():
    import pymysql
    try:
        conexion = pymysql.connect(host='localhost',
            user='root',
            password='47175627m',
            db='oficinas')
        try:
            nombre_oficina=input('Facilita el nombre de la oficina:\n')
            with conexion.cursor() as cursor:
                consulta = "SELECT id, nombre, direccion FROM oficinas WHERE nombre like %s;"
                cursor.execute(consulta, '%'+nombre_oficina+'%')
                # Con fetchall traemos todas las filas
                oficinas = cursor.fetchall()
                # Recorrer e imprimir
                for oficina in oficinas:
                    print(oficina)
    
        finally:
            conexion.close()
    
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
            print("Ocurrió un error al conectar: ", e)
            
#Función para encontrar oficina por id:
def busqueda_oficina_id():
    import pymysql
    try:
        conexion = pymysql.connect(host='localhost',
            user='root',
            password='47175627m',
            db='oficinas')
        try:
            id_oficina=input('Facilita el id de la oficina:\n')
            with conexion.cursor() as cursor:
                consulta = "SELECT id, nombre, direccion FROM oficinas WHERE id like %s;"
                cursor.execute(consulta, id_oficina)
                # Con fetchall traemos todas las filas
                oficinas = cursor.fetchall()
                # Recorrer e imprimir
                for oficina in oficinas:
                    print(oficina)
    
        finally:
            conexion.close()
    
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
            print("Ocurrió un error al conectar: ", e)
            
#----------------------MODIFICACIONES---------------------     
#Función para modificar el nombre de la oficina:
def modificar_nombre():
    import pymysql
    try:
        conexion = pymysql.connect(host='localhost',
                user='root',
                password='47175627m',
                db='oficinas')
        try:
            with conexion.cursor() as cursor:
                consulta = "UPDATE oficinas SET nombre = %s WHERE id = %s;"
                nuevo_nombre = input('Facilita el nuevo nombre de la oficina:\n')
                id_editar = input('Facilita el id de la oficina a modificar:\n')
                cursor.execute(consulta, (nuevo_nombre, id_editar))
            conexion.commit()
            print('El nombre ha sido modificado\n')
        finally:
                conexion.close()

    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
            print("Ocurrió un error al conectar: ", e)

#Función para modificar la dirección:
def modificar_direccion():
    import pymysql
    try:
        conexion = pymysql.connect(host='localhost',
                user='root',
                password='47175627m',
                db='oficinas')
        try:
            with conexion.cursor() as cursor:
                consulta = "UPDATE oficinas SET nombre = %s WHERE id = %s;"
                nueva_direccion = input('Facilita la nueva dirección de la oficina:\n')
                id_editar = input('Facilita el id de la oficina a modificar:\n')
                cursor.execute(consulta, (nueva_direccion, id_editar))
            conexion.commit()
            print('La dirección ha sido modificado\n')
        finally:
                conexion.close()

    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
            print("Ocurrió un error al conectar: ", e)
            
#-------------------CREACIÓN-----------------------
#Función para añadir informaciónala db.
def crear_oficina():
    import pymysql
    try:
        conexion = pymysql.connect(host='localhost',
                user='root',
                password='47175627m',
                db='oficinas')
        try:
            with conexion.cursor() as cursor:
                consulta = ("INSERT INTO oficinas(nombre, direccion) VALUES (%s, %s);")
                nombre_nuevo=input('Facilita el nombre de la nueva oficina:\n')
                direccion_nueva= input('Facilita la dirección de la nueva oficina:\n')
                #Podemos llamar muchas veces a .execute con datos distintos
                cursor.execute(consulta, (nombre_nuevo, direccion_nueva))
            conexion.commit()
            print('Oficina '+nombre_nuevo+' creada.\n')
        finally:
                conexion.close()
    
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al conectar: ", e)

#-----------------BORRAR----------------------------
def eliminar_oficina():
    import pymysql
    try:
        conexion= pymysql.connect(host='Localhost', 
                                  user='root',
                                  password='47175627m',
                                  db='oficinas')
        try:
            with conexion.cursor() as cursor:
                consulta = "DELETE FROM oficinas WHERE nombre = %s;"
                borrar_oficina = input('Indica el nombre de la oficina a eliminar:\n')
                cursor.execute(consulta, (borrar_oficina))
                conexion.commit()
        finally:
            conexion.close()

    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
            print("Ocurrió un error al conectar: ", e)
            
#Una vez hemos creado todas las funciones que necesitamos, crearmos el menú.

#Esquema del menú
'''
1.Crear una oficina nueva
2.Consultas
    -Listado de oficinas
    -Consulta por nombre
    -Consulta por id
3.Modificaciones
    -Modificar el nombre
    -Modificar la dirección
4.Eliminar oficina
5.Salir
'''

#Empezamos a configurar el menú principal.
'''Tras deliberar como organizarlo he decidido gestionarlo de la siguiente manera,
puesto que considero que no se complica tanto el codigo y no debo de realizar
tantos bucles anidados que pueden ser confusos.

También comentar que, de esta manera no he de utilizar el TRY para indicar algún tipo
de error que puede surgir. Todo lo que no sean las strings informadas lo marcará como
error y volverá a solicitar que introduzcas un numero.'''

def menu_print():
    print('''__MENU__\n
    1.Crear una oficina nueva
    2.Consultas
        -Listado de oficinas
        -Consulta por nombre
        -Consulta por id
        -Volver
    3.Modificaciones
        -Modificar el nombre
        -Modificar la dirección
        -Volver
    4.Eliminar oficina
    5.Salir\n
    ''')
    opcion=input('Elije una opción con el número de la indicada:\n')
    validar_opcion_menu(opcion)


def validar_opcion_menu(opcion):
    if opcion == '1':
        crear_oficina()
    elif opcion == '2':
        menu_consultas()
    elif opcion == '3':
        menu_modificaciones()
    elif opcion == '4':
        eliminar_oficina()
    elif opcion == '5':
        print('¡Adiós! :)')
    else:
       print('Opción incorrecta')
       menu_print()
       
'''En este apartado diseñare el menu dentro de '2.Consultas',de esta manera 
cuando elijas dicha opción deberán de seleccionar las variantes que tienen.'''
    
def menu_consultas():
    print('''
          1.Listado de oficinas
          2.Consulta por nombre
          3.Consulta por id
          4.Volver''')
    opcion_consultas = input('Selecciona una de las opciones:\n')
    validar_opcion_consultas(opcion_consultas)
     
def validar_opcion_consultas(opcion_consultas):
    if opcion_consultas == '1':
        consulta_oficina()
    elif opcion_consultas == '2':
        busqueda_oficina_nombre()
    elif opcion_consultas == '3':
        busqueda_oficina_id()
    elif opcion_consultas == '4':
        menu_print()

'''Realizaremos ahora el submenu de modificaciones.'''

def menu_modificaciones():
    print('''
          1.Modificar el nombre
          2.Modificar la dirección
          3.Volver''')
    opcion_modificaciones = input('Selecciona una opción:\n')
    validar_opcion_modificaciones(opcion_modificaciones)

def validar_opcion_modificaciones(opcion_modificaciones):
    if opcion_modificaciones == '1':
        modificar_nombre()
    elif opcion_modificaciones == '2':
        modificar_direccion()
    elif opcion_modificaciones == '3':
        menu_print()

    
while True:
    menu_print()