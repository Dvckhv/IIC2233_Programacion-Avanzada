# Tarea 0: DCCorreos de Chile :school_satchel:

## Consideraciones generales :octocat:

<respecto al programa general, este logra completar con exito todo lo especificado en el enunciado y un poco más que yo consideraba necesario para el tipo de aplicación que se estaba creando, aun se puede mejorar o optimizar el codigo pero este es funcional y a mi parecer claro al momento de leer y navegar, separé el codigo en 5 archivos difentes y creo que así se modulizo bien, pero sé que deben existir mejores maneras de modulizar este. Hablando de errores del programa, dentro de lo testeado por mi logre(que no fue poco) solucionar todos los errores presentados, evitando "bugs" o termino del programa por elecciones maliciosas o que no seguian las instrucciones, espero no existan mas errores y muchas gracias por leer esto :)>

### Cosas implementadas y no implementadas :white_check_mark: :x:
#### Menú de Inicio (18pts) (18%)
##### ✅ Requisitos <Contiene todas las opciones solicitadas>
##### ✅ Iniciar sesión <se verifica correctamente si el usuario existe y si su contraseña coincide, sumado a que se da la opcion de volver a intentarlo o volver al menu inicial>
##### ✅ Ingresar como administrador <al igual que en el inicio de sesión de usuario, si la contraseña es incorrecta se da la opcion de volver al menu inicial o volver a intentarlo>
##### ✅ Registrar usuario <se registra el usuario si se cumplen las condiciones necesarias y al igual que en ambos menus de ingreso se da la opcion de volver a intentarlo o volver al menú de inicio>
##### ✅ Salir <simplemente se cierra el programa y imprime un mensaje de despedida\>
#### Flujo del programa (31pts) (31%) 
##### ✅ Menú de Usuario <contiene las opciones minimas solicitadas y estas se ejecutan de la forma correcta, al igual que con las opciones del menú de inicio, al equivocarse o al terminar una funcion se da la opción de volver a intentarlo,volver al menu o hacer alguna actividad relacionada con la funcion ejecutada\>
##### ✅ Menú de Administrador <Al igual que con el menu de Usuario, contiene las opciones minimas solicitadas,estas se ejecutan de forma correcta y cada opción tiene elecciones extras que facilitan las tareas solicitadas y hace mas "real" o "amigable" el trabajo con el programa\>
#### Entidades 15pts (15%)
##### ✅ Usuarios <Creé una clase para los diferentes usuarios lo que facilita el trabajo con multiples usuarios a la vez, funciona correctamente y se distingue de las otras entidades>
##### ✅ Encomiendas <se logran realizar todas las tareas que involucran Encomiendas (ya sea como administrador o Usuario) sin ningun problema>
##### ✅ Reclamos <Se agregan correctamente los reclamos a el archivo al ingresar como usuario y a la vez se pueden leer facilmente como Administrador(los reclamos son parte de una lista de listas) >
#### Archivos: 15 pts (15%)
##### ✅ Manejo de Archivos <implementé 2 funciones especificas y "genericas", creadas para trabajar con archivos de manera eficaz y modulizada, lo cual me permitió acceder y modificar con exito los 3 archivos utilizados>
#### General: 21 pts (21%)
##### ✅ Menús <graficamente tienen una apariencia agradable y se puede manejar a través de ellos sin ningun problema, evitando diferentes tipos de errores como lo pueden ser el ingreso de una opción fuera del rango solicitado, una contraseña mas larga, etc. >
##### ✅ Parámetros <Se utilizan los parametros entregados como variables de el archivo "**parametros.py**, dado que así se facilita la revision y edicion de estos sin tener que cambiar directamente del codigo\>
##### ✅ Módulos <se utilizan al rededor de 4 modulos creados por mi, los cuales fueron creados el año 2020 y necesitan un recambio
>
##### ✅ PEP8 <intenté cuidadosamente cumplir con todas las normas impuestas al momento de programar, para así facilitar lectura y debugeo, de todas maneras el codigo fue revisado para solucionar algún descuido en las normas.\>

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ``` Main.py```.\
Ademas de los modulos **adjuntos en la carpeta** y los archivos  **.csv** con sus respectivos nombres ya que el codigo no funcionara si los archivos no tienen el nombre original entregado
para el caso de los archivos **.csv** se utilizó:
1. ```encomiendas.csv``` para el archivo con todos los datos de encomiendas.
2. ```reclamos.csv``` para el archivo con los titulos y desarrollos de c/u de los reclamos
3. ```usuarios.csv``` para el archivo con nombre y contraseña de c/u de los usuarios registrados




## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```librería_1```: ```datetime() / datetime```


### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```fUsuario```: Contiene la clase ``` Usuario```, clase que se encarga del manejo de datos y funcionamiento del **Menu de Usuario**
2. ```Admin```: Contiene diferentes funciones para cumplir con todas las tareas que el **Administrador** posee.
3. ```inicio```: Contiene funciones encargadas del modelamiento de la parte inicial del codigo, ingreso de Usuario/Administrador y creacion de usuario nuevo.
3. ```archivos```: Contiene 2  funciones dedicadas a el manejo y trabajo con los archivos **.csv** sumado a una función encargada de procesar las elecciones de la consola

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. **Actualizar Fecha al actualizar estado de encomienda:** debido a que consideré que la fecha se trataba de la ultima modificación que el pedido habia recibido lo que incluye su creación y modificación de su estado.
2. **Llegada a destino v/s En destino:** dado que en ```encomiendas.csv``` no existian encomiendas con el estado *En destino*, consideré que ese estado de "Entregado" era *Llegada a destino*
3. **Botones extras:** al realizar el codigo, fui considerando que deberian haber otras opciones extras al momento de interactuar con el programa y su interfaz, por ejemplo, al no tener encomiendas activas, consideré el añadir una opción de crear una nueva encomienda, o al equivocarse de contraseña o no cumplir con los requisitos, se dio otra oportunidad de realizar la acción o volver al menú u otras.
4. **Encomiendas a si mismo** considere que (al igual que en un correo normal) se pueden hacer encomiendas a si mismo pero al hacerlo, se consultara una 2da vez si esto era lo que se queria hacer.