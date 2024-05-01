from datetime import datetime
import archivos, inicio
def menu_admin():   #"interfaz grafica" del menu de administrador
    print('''    
>ADMINISTRADOR

    [1] Actualizar encomiendas
    [2] Revisar reclamos
    [3] Cerrar sesión''')
    accion=archivos.eleccion(3)
    if accion==1:
        return tabla_encomiendas()
    elif accion==2:
        return revisar_reclamos()
    else:
        return inicio.menu_inicio()
def tabla_encomiendas(): # print de una tabla con todas las encomiendas del archivo "encomiendas.csv"

    lista_encomiendas=archivos.archivo_lista("encomiendas")
    nombre, receptor, peso, destino, estado="NOMBRE", "RECEPTOR", "PESO", "DESTINO", "ESTADO"
    
    print("Encomiendas registradas \n")
    print(f"       |{nombre : ^48s}|{receptor: ^19s}|{peso: ^6s}|{destino: ^14s}|{estado: ^22s}|")
    c=1
    for encom in lista_encomiendas:
        nombre, receptor, peso, destino, estado=encom[0], encom[1], encom[2], encom[3], encom[5]
        if c<10:
            print(f"    [{c}] {nombre : ^48s} {receptor : ^19s} {peso: ^6s} {destino: ^14s} {estado: ^22s}")
        else:
            print(f"   [{c}] {nombre : ^48s} {receptor : ^19s} {peso: ^6s} {destino: ^14s} {estado: ^22s}")
        c+=1
    if c<10:
        print(f"    [{c}] Volver")
    else:
        print(f"   [{c}] Volver")
    print("Seleccione una encomienda a actualizar ")
    accion = archivos.eleccion(c)
    if accion==c:
        return menu_admin()
    else:
        return actualizar_encomiendas(accion)
def actualizar_encomiendas(numero): # actualizacion de la encomienda seleccionada en "tabla_encomiendas()"
    lista_encomiendas=archivos.archivo_lista("encomiendas")
    estado_actual=lista_encomiendas[numero-1][-1]
    if estado_actual=="Emitida":
        lista_encomiendas[numero-1][-1]="Revisada por agencia"
    elif estado_actual=="Revisada por agencia":
        lista_encomiendas[numero-1][-1]="En camino"
    elif estado_actual== "En camino":
        lista_encomiendas[numero-1][-1]="Llegada al destino"
    else:
        print("\n**La encomienda ya se encuentra entregada")     
    if (lista_encomiendas[numero-1][-1])!=estado_actual:
        with open("encomiendas.csv", "w", encoding="utf-8") as archivo:
            print("nombre_articulo, receptor, peso, destino, fecha, estado")
            for encomienda in lista_encomiendas:
                print(",".join(encomienda), file=archivo)
            print("\nEstado de encomienda actualizado exitosamente")
    print("    [1] Actualizar otra encomienda")
    print("    [2] Volver al menu de administrador")
    print("    [3] Cerrar sesion")
    accion=archivos.eleccion(3)
    if accion==1:
        return tabla_encomiendas()
    elif accion==2:
        return menu_admin()
    else:
        return inicio.menu_inicio()

def revisar_reclamos(): # menu de reclamos ubicados en "reclamos.csv"
    lista_reclamos=archivos.archivo_lista("reclamos")
    c=1
    print("\nLista de reclamos: ")
    for reclamo in lista_reclamos:
        print(f"[{c}]", reclamo[1])
        c+=1
    print(f"[{c}] Volver")
    accion=archivos.eleccion(c)
    if c!=accion:
        print(f"\nDescripción reclamo {accion}: ")
        print("   ", lista_reclamos[accion-1][2], "\n")
        print("    [1] Revisar otro reclamo")
        print("    [2] Volver al menú de Administrador")
        accion=archivos.eleccion(2)
        if accion==1:
            return revisar_reclamos()
        else:
            return menu_admin()
    else:
        return menu_admin()