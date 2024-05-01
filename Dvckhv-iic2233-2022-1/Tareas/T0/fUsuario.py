import archivos, parametros, inicio
from datetime import datetime
class Usuario:
    def  __init__(self, nombre) -> None:
        self.nombre=nombre
        self.encomiendas_realizadas=[]      
    def menu_usuario(self):    ##printea el menu de usuario inicial
        print('''
>USUARIO

    [1] Hacer encomienda
    [2] Revisar estado de encomiendas realizadas
    [3] Realizar reclamos
    [4] Ver el estado de los pedidos personales
    [5] Cerrar sesión''')
        accion=archivos.eleccion(5)
        if accion==1:
            return self.hacer_encomiendas()
        elif accion==2:
            return self.revisar_encomiendas()
        elif accion==3:
            return self.realizar_reclamo()
        elif accion==4:
            return self.estado_pedidos()
        else:
            return inicio.menu_inicio()
    def hacer_encomiendas(self): #agrega una encomienda a el archivo .csv de encomiendas
        validez=True
        print("\nIngrese los datos de la encomienda a realizar")
        articulo=input("    -Nombre del articulo: ")
        destinatario= input("    -Nombre del destinatario: ")
        peso= int(input(f"    -Peso[Max {parametros.MAX_PESO} kg]: "))
        articulo=articulo.strip()
        destinatario=destinatario.strip()
        if len(articulo) == 0 or len(destinatario) == 0:
            print("**No puede dejar campos sin completar")
            validez=False
        if articulo.isdigit()==True:
            print("**El articulo no debe ser un numero")
        if   "," in articulo:
            print("**No es valido el uso de comas(,) en el nombre de articulo")
            validez=False
        if peso > parametros.MAX_PESO:
            print("**Peso excede el maximo establecido")
            validez=False
        elif peso<=0:
            print("**El paquete debe cumplir las leyes de la fisica")
            validez=False
        destinatarios_validos=archivos.archivo_lista("usuarios")
        destinatarios_validos=[usuario[0] for usuario in destinatarios_validos]
        if destinatario not in destinatarios_validos:
            validez=False
            print("**No existe el destinatario indicado en la base de datos")
        elif destinatario==self.nombre:
            print("Se enviará el paquete a tu nombre,¿Desea esto?")
            print("[1] Si")
            print("[2] No")
            accion=archivos.eleccion(2)
            if accion==2:
                validez==False
        if validez==True:
            destino=input("    -Destino(Ciudad): ")
            if "," in destino:
                validez=False
                print("**No es valido el uso de comas(,) en el destino")
            for letra in destino:
                if letra.isdigit()==True:
                    validez=False
                    print("**El destino no puede contener numeros")
        if validez==False:
            print("    [1] Intentar nuevamente")
            print("    [2] Cancelar encomienda")
            accion=archivos.eleccion(2)
            if accion==1:
                print("Ingrese los datos de la encomienda nuevamente...")
                return self.hacer_encomiendas()
            elif accion==2:
                print("La encomienda ha sido cancelada")
                return self.menu_usuario()
        else:
            encomienda=[articulo, destinatario, str(peso), destino, str(datetime.now()), "Emitida"]
            self.encomiendas_realizadas.append(encomienda)
            archivos.agregar_texto(encomienda, "encomiendas")
            print("\nEncomienda registrada exitosamente")
            print("    [1] Volver")
            print("    [2] Hacer otra encomienda")
            print("    [3] Cerrar sesión")
            accion= archivos.eleccion(3)
            if accion==1:
                return self.menu_usuario()
            elif accion==2:
                return self.hacer_encomiendas()
            else: 
                return inicio.menu_inicio()
    def revisar_encomiendas(self): # revisa el estado de las encomiendas realizadas mientras el codigo este funcionando
        print("\nListado de encomiendas Realizadas durante la sesión")
        c=1
        if len(self.encomiendas_realizadas)>0:
            c=0
            lista_encomiendas=archivos.archivo_lista("encomiendas")
            estado=""
            for encomienda in self.encomiendas_realizadas:
                c+=1
                for encom in lista_encomiendas:
                    if encomienda[:-1] == encom[:-1]:
                        estado=encom[-1]
                print(f"{c}.- Nombre de articulo:", encomienda[0], "Estado:", estado)
        else:
            print("\nNo ha realizado encomiendas en la sesión actual")
        print("    [1] Volver")
        print("    [2] Realizar encomienda")
        print("    [3] Cerrar sesión")
        accion=archivos.eleccion(3)
        if accion==1:
            return self.menu_usuario()
        elif accion==2:
            return self.hacer_encomiendas()
        else:
            return inicio.menu_inicio()
    def realizar_reclamo(self): #se realizan reclamos a nombre del usuario
        validez=True
        titulo=input("Titulo de su reclamo: ")
        descripcion=input("Desarrolle su reclamo: ")
        if len(titulo) == 0 or len(descripcion) == 0:
            print("**No puede dejar campos sin completar")
            validez=False
        if descripcion.isdigit()==True:
            print("**El cuerpo del reclamo no puede ser un numero")
            validez=False
        if titulo.isdigit()==True:
            print("**El titulo del reclamo no puede ser un numero")
            validez=False
        if   "," in titulo:
            print("**No es valido el uso de comas(,) en el titulo del reclamo")
            validez=False
        reclamo=[self.nombre, titulo, descripcion]
        if validez:
            archivos.agregar_texto(reclamo, "reclamos")
            print("\nReclamo ingresado exitosamente, nos disculpamos por los inconvenientes generados")
            print("    [1] Realizar otro reclamo")
            print("    [2] Volver  ")
            print("    [3] Cerrar sesión")
            accion=archivos.eleccion(3)
            if accion==1:
                return self.realizar_reclamo()
            if accion==2:
                return self.menu_usuario()
            else:
                return inicio.menu_inicio()
        else:
            print("    [1] Intentar nuevamente")
            print("    [2] Cancelar reclamo")
            print("    [3] Cerrar sesión")
            accion=archivos.eleccion(3)
            if accion==1:
                return self.realizar_reclamo()
            elif accion==2:
                return self.menu_usuario()
            else:
                return inicio.menu_inicio()
    def estado_pedidos(self): #ve el estado de los pedidos que tengan el usuario de la sesión como destinatario
        lista_encomiendas=archivos.archivo_lista("encomiendas")
        c=0
        Existencia=False
        for encom in lista_encomiendas:
            if encom[1]==self.nombre:
                Existencia=True
        if Existencia==False:
            print("----------------------------------------------")
            print("No existen encomiendas registradas a su nombre")
            print("----------------------------------------------")
        else:
            nombre, receptor, peso, destino, fecha, estado="NOMBRE", "RECEPTOR", "PESO", "DESTINO", "FECHA", "ESTADO"
            print("Encomiendas registradas a su nombre: \n")
            print(f"       |{nombre : ^48s}|{receptor: ^19s}|{peso: ^6s}|{destino: ^14s}|{fecha:^21s}|{estado: ^22s}|")
            c=0
            for encom in lista_encomiendas:
                if encom[1]==self.nombre:
                    c+=1
                    nombre, receptor, peso, destino, fecha, estado=encom[0], encom[1], encom[2], encom[3], encom[4], encom[5]
                    print(f"    {c}.- {nombre : ^48s} {receptor : ^19s} {peso: ^6s} {destino: ^14s} {str(fecha):^21.19s} {estado: ^22s}")
        print("    [1] Volver")
        print("    [2] Cerrar sesión")
        accion=archivos.eleccion(2)
        if accion==1:
            return self.menu_usuario()
        else:
            return inicio.menu_inicio()
usuarios_sesion=dict() # se guardan los usuarios que alguna vez iniciaron sesion durante la corrida del codigo
#con el uso del dicionario luego se puede volver a utilizar el mismo objeto y mantener las encomiendas para la función revisar_encomiendas