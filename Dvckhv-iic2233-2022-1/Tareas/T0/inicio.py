import archivos, fUsuario, Admin, parametros
def menu_inicio(): #printea el menu de inicio 
    print('''
---- Bienvenid@ a DCCorreos de Chile ----

>INICIO

    [1] Iniciar sesion como usuario
    [2] Iniciar sesion como administrador
    [3] Registrarse como usuario
    [4] Salir del Programa''')
    accion=archivos.eleccion(4)
    if accion==1:
        print(">INGRESO USUARIOS")
        return ingreso_usuario()
    elif accion==2:
        print(">INGRESO ADMINISTRADOR")
        return ingreso_admin()
    elif accion==3:
        print(">REGISTRO DE USUARIO")
        return nuevo_usuario()
    elif accion==4:
        print("-------------------------------------------------------------")
        print("Hasta la proxima, gracias por preferir DCCorreos de Chile :)")
        print("-------------------------------------------------------------")
        
def ingreso_usuario(usuario=""): #  sistema de ingreso del usuario
    if usuario=="":
        usuario=input("Usuario: ")
    clave=input("Contraseña: ")
    lista_usuarios=archivos.archivo_lista("usuarios")
    usuario_existe=False
    for i in range(len(lista_usuarios)):
        if usuario==lista_usuarios[i][0]:
            usuario_existe=True
            posicion=i
    if usuario_existe==True:
        if clave==lista_usuarios[posicion][1]:
            print("\nCredenciales correctas")
            if (usuario in fUsuario.usuarios_sesion) == False: #se revisa si anteriormente se ha ingresado con el usuario en un diccionario para asi "Restaurar sesion"
                u=fUsuario.Usuario(usuario)
                fUsuario.usuarios_sesion[usuario]=u
            return fUsuario.usuarios_sesion[usuario].menu_usuario()  # instancia de clase Usuario utilizando un diccionario creado en el archivo "fUsuario.py"
        else:
            print("\n**contraseña incorrecta...")
            print("    [1] Volver a intentar")
            print("    [2] Volver al menu de inicio")
            accion=archivos.eleccion(2)
            if accion==1:
                return ingreso_usuario(usuario)
            else:
                return menu_inicio()
    else:
        print("**El usuario ingresado no se encuentra en la base de datos")
        print("    [1] Volver a intentar")
        print("    [2] Volver al menu de inicio")
        accion=archivos.eleccion(2)
        if accion==1:
            return ingreso_usuario()
        else:
            return menu_inicio()

def ingreso_admin(): #sistema de ingreso del administrador
        clave=input("Contraseña: ")
        if clave==parametros.CONTRASENA_ADMIN:
            print("Contraseña correcta")
            return Admin.menu_admin()
        else:
            print("**contraseña incorrecta, intente nuevamente")
            return ingreso_admin()
def nuevo_usuario(): # sistema de registro de nuevo usuario
    usuario=input(f"Ingrese nombre de usuario[minimo {parametros.MIN_CARACTERES} caracteres alfabéticos]:")
    alfanumerico="abcdefghijklmnñopqrstuvwxyz0123456789"
    alfabetico="abcdefghijklmnñopqrstuvwxyz"
    if len(usuario)<parametros.MIN_CARACTERES:
        print("**El nombre de usuario debe ser mas largo")
        print("    [1] Intentar nuevamente")
        print("    [2] Volver")
        accion=archivos.eleccion(2)
        if accion==1:
            return nuevo_usuario()
        if accion==2:
            return menu_inicio()
    for letra in usuario.lower(): 
        if letra not in alfabetico:
            print("**El usuario debe contener solo caracteres alfabéticos")
            print("    [1] Intentar nuevamente")
            print("    [2] Volver")
            accion=archivos.eleccion(2)
            if accion==1:
                return nuevo_usuario()
            if accion==2:
                return menu_inicio()
    lista_usuarios=archivos.archivo_lista("usuarios")
    for usuarios in lista_usuarios:
        if usuarios[0]==usuario:
            print("**El usuario elegido ya existe")
            print("    [1] Intentar nuevamente")
            print("    [2] Iniciar sesion como usuario")
            print("    [3] Volver")
            accion=archivos.eleccion(3)
            if accion==1:
                return nuevo_usuario()
            elif accion==2:
                return ingreso_usuario()
            else:
                return menu_inicio()
    
  
    clave=input(f"Ingrese contraseña[minimo {parametros.LARGO_CONTRASENA} caracteres alfanumericos]: ")
    for caracter in clave.lower():
        if caracter not in alfanumerico:
            print("**Clave no valida")
            print("    [1] Intentar nuevamente")
            print("    [2] Volver")
            accion=archivos.eleccion(2)
            if accion==1:
                return nuevo_usuario()
            else:
                return menu_inicio()
    archivos.agregar_texto([usuario, clave], "usuarios")
    print("Usuario registrado exitosamente!!")
    u=fUsuario.Usuario(usuario)
    fUsuario.usuarios_sesion[usuario]=u
    return u.menu_usuario()  # instancia de clase Usuario utilizando un diccionario creado en el archivo "fUsuario.py"