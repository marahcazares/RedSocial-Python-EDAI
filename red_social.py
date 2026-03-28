# Definimos un diccionario vacío para almacenar los usuarios, contraseñas, amigos y publicaciones
usuarios = {}

def agregar_usuario():
    nombre = input("Ingresa el nombre de usuario: ")
    contrasena = input("Ingrese la contraseña: ")
    if nombre in usuarios:
        print("El usuario ya existe.")
    else:
        usuarios[nombre] = {"contrasena": contrasena, "amigos": [], "publicaciones": []}
        print("Usuario agregado correctamente.")

def ingresar_al_sistema():
    nombre = input("Ingrese el nombre de usuario: ")
    contrasena = input("Ingrese la contraseña: ")
    if nombre in usuarios and usuarios[nombre]["contrasena"] == contrasena:
        print(f"¡Bienvenido, usuario {nombre}!")
        menu_usuario(nombre)
    else:
        print("No se encontró usuario o la contraseña es incorrecta.")

def menu_usuario(nombre_usuario):
    while True:
        print("\n1. Hacer publicación")
        print("2. Ver publicaciones")
        print("3. Eliminar publicación")
        print("4. Agregar amigo")
        print("5. Ver amigos")
        print("6. Eliminar amigo")
        print("7. Ver publicaciones de amigos")
        print("8. Ver amigos de amigos")
        print("9. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            hacer_publicacion(nombre_usuario)
        elif opcion == "2":
            ver_publicaciones(nombre_usuario)
        elif opcion == "3":
            eliminar_publicacion(nombre_usuario)
        elif opcion == "4":
            agregar_amigo(nombre_usuario)
        elif opcion == "5":
            ver_amigos(nombre_usuario)
        elif opcion == "6":
            eliminar_amigo(nombre_usuario)
        elif opcion == "7":
            ver_publicaciones_amigos(nombre_usuario)
        elif opcion == "8":
            ver_amigos_amigos(nombre_usuario)
        elif opcion == "9":
            break
        else:
            print("Opción no válida. Por favor, seleccione otra opción.")

def hacer_publicacion(nombre_usuario):
    publicacion = input("Escribe tu publicación: ")
    usuarios[nombre_usuario]["publicaciones"].append(publicacion)
    print("Publicación creada exitosamente.")

def ver_publicaciones(nombre_usuario):
    if usuarios[nombre_usuario]["publicaciones"]:
        print(f"Publicaciones de {nombre_usuario}:")
        for i, publicacion in enumerate(usuarios[nombre_usuario]["publicaciones"], 1):
            print(f"{i}. {publicacion}")
    else:
        print("No hay publicaciones.")

def eliminar_publicacion(nombre_usuario):
    if usuarios[nombre_usuario]["publicaciones"]:
        ver_publicaciones(nombre_usuario)
        num_publicacion = input("Ingrese el número de la publicación que desea eliminar: ")
        try:
            num_publicacion = int(num_publicacion)
            if 1 <= num_publicacion <= len(usuarios[nombre_usuario]["publicaciones"]):
                del usuarios[nombre_usuario]["publicaciones"][num_publicacion - 1]
                print("Publicación borrada exitosamente.")
            else:
                print("El número de publicación especificado no se encontró en la lista.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
    else:
        print("No hay publicaciones para eliminar.")

def agregar_amigo(nombre_usuario):
    nombre_amigo = input("Ingrese el nombre del amigo que desea agregar: ")
    if nombre_amigo == nombre_usuario:
        print("No puedes agregarte a ti mismo como amigo.")
    elif nombre_amigo not in usuarios:
        print("Error: El amigo especificado no se encontró en la lista.")
    elif nombre_amigo in usuarios[nombre_usuario]["amigos"]:
        print("Este usuario ya está en su lista de amigos.")
    else:
        usuarios[nombre_usuario]["amigos"].append(nombre_amigo)
        usuarios[nombre_amigo]["amigos"].append(nombre_usuario)
        print(f"{nombre_amigo} agregado correctamente a su lista de amigos.")

def ver_amigos(nombre_usuario):
    if usuarios[nombre_usuario]["amigos"]:
        print(f"Amigos de {nombre_usuario}:")
        for amigo in usuarios[nombre_usuario]["amigos"]:
            print(amigo)
    else:
        print("No tienes amigos.")

def eliminar_amigo(nombre_usuario):
    nombre_amigo = input("Ingrese el nombre del amigo que desea eliminar: ")
    if nombre_amigo in usuarios[nombre_usuario]["amigos"]:
        usuarios[nombre_usuario]["amigos"].remove(nombre_amigo)
        print(f"{nombre_amigo} eliminado de su lista de amigos.")
    else:
        print("El amigo especificado no se encontró en la lista de amigos o no tienes amigos.")

def ver_publicaciones_amigos(nombre_usuario):
    amigos = usuarios[nombre_usuario]["amigos"]
    if amigos:
        print("Publicaciones de amigos:")
        for amigo in amigos:
            if usuarios[amigo]["publicaciones"]:
                print(f"Publicaciones de {amigo}:")
                for publicacion in usuarios[amigo]["publicaciones"]:
                    print(f"- {publicacion}")
            else:
                print(f"{amigo} no tiene publicaciones.")
    else:
        print("No tienes amigos para ver sus publicaciones.")

def ver_amigos_amigos(nombre_usuario):
    '''Se itera sobre los amigos del usuario, después para cada amigo del usuario obtiene la lista de amigos de ese amigo
    la clave es el nombre del amigo de un amigo y el valor es la lista de amigos de ese amigo de un amigo
    '''
    amigos_de_amigos = {amigo_de_amigo: usuarios[amigo_de_amigo]["amigos"] for amigo in usuarios[nombre_usuario]["amigos"]
                        for amigo_de_amigo in usuarios[amigo]["amigos"] if amigo_de_amigo != nombre_usuario}
    if amigos_de_amigos:
        print(f"Amigos de amigos:")
        for amigo_de_amigo, amigos in amigos_de_amigos.items():
            print(f"Amigos de {amigo_de_amigo}:")
            for amigo in amigos:
                print(f"- {amigo}")
    else:
        print("No hay amigos de amigos para mostrar.")

def borrar_usuario():
    nombre = input("Ingrese el nombre del usuario a borrar: ")
    contrasena = input("Ingrese la contraseña: ")
    if nombre in usuarios and usuarios[nombre]["contrasena"] == contrasena:
        del usuarios[nombre]
        print("Usuario borrado exitosamente.")
    else:
        print("Usuario no encontrado o contraseña incorrecta.")

def mostrar_usuarios():
    print("Usuarios registrados:")
    for usuario in usuarios:
        print(usuario)
    if not usuarios:
        print("No hay usuarios registrados.")

def guardar_usuarios():
    with open("usuarios.txt", "w") as f:
        for usuario, info in usuarios.items():
            contrasena = info["contrasena"]
            amigos = ",".join(info["amigos"])
            publicaciones = ",".join(info["publicaciones"])
            f.write(f"{usuario}:{contrasena}:{amigos}:{publicaciones}\n")

def cargar_usuarios():
    try:
        with open("usuarios.txt", "r") as f:
            for linea in f:
                usuario, contrasena, amigos, publicaciones = linea.strip().split(":")
                # Verificamos si la línea tiene amigos
                if amigos:
                    usuarios[usuario] = {"contrasena": contrasena, "amigos": amigos.split(","), "publicaciones": publicaciones.split(",")}
                else:
                    usuarios[usuario] = {"contrasena": contrasena, "amigos": [], "publicaciones": []}
    except FileNotFoundError:
        pass

def main():
    cargar_usuarios()
    while True:
        print("\nMenú:")
        print("1. Dar de alta al usuario")
        print("2. Ingresar al sistema")
        print("3. Borrar usuario")
        print("4. Mostrar usuarios existentes")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_usuario()
        elif opcion == "2":
            ingresar_al_sistema()
        elif opcion == "3":
            borrar_usuario()
        elif opcion == "4":
            mostrar_usuarios()
        elif opcion == "5":
            guardar_usuarios()
            print("Saliendo del sistema")
            break
        else:
            print("Opción no válida. Por favor, seleccione otra opción.")

if __name__ == "__main__":
    main()

