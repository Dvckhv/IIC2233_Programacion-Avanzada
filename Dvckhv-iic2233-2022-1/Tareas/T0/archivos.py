def archivo_lista(archivo): #se transforma un archivo ".csv" a una lista de listas dada la recurrencia en el uso de ellas
    with open(archivo+".csv", encoding="utf-8") as file:
        lista_archivo=[]
        for linea in file:
            lista_archivo.append(linea.strip())
        if archivo=="reclamos":
            lista_archivo=[ i.split(",", maxsplit=2) for i in lista_archivo]
        else:
            lista_archivo=[ i.split(",") for i in lista_archivo]
    lista_archivo=lista_archivo[1:]
    return lista_archivo
def agregar_texto(lista_texto, archivo): #se agrega la lista de texto al final de un archivo especificado separado por comas
    with open(archivo+".csv", "r", encoding="utf-8") as file:
        nueva_linea=False
        if file.readlines()[-1][-1] == "\n":
            nueva_linea=True
    with open(archivo+".csv", "a", encoding="utf-8")as file:
        if nueva_linea==False:
            print("", file=file)
        print(",".join(lista_texto), file=file)
def eleccion(maximo): # funcion encargada de retornar un numero dentro de un rango, se evita fallos del codigo.
    elec=input("Indique su opción: ")
    if elec.isdigit()==False:
        print("debe ingresar un numero")
        return eleccion(maximo)
    int_elec=int(elec)
    float_elec=float(elec)
    if float_elec-int_elec>0:
        print(f"debe ser un numero entero entre 1 y {maximo}")
        return eleccion(maximo)
    if int_elec>maximo or int_elec<=0:
        print("opcion fuera de rango, intente nuevamente...")
        return eleccion(maximo)
    else:
        return int_elec