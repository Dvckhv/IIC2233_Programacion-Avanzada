# Tarea 1: DCCasino :school_satchel:

## Consideraciones generales :octocat:

<La tarea modela correctamente lo solicitado en las instrucciones, el codigo es rigido frente al usuario y se completa correctamente la simulacion del casino, probé y termine varias partidas con diversos resultados pero quizas exista algun error dentro del codigo al cual no llegue con mis pruebas.>

### Cosas implementadas y no implementadas :white_check_mark: :x:

#### Programación Orientada a Objetos: 38 pts (28%)
##### ✅  Diagrama <se corrige el diagrama considerando lo mencionado en el avance y modela correctamente el codigo hecho>
##### ✅ Definición de clases, atributos, métodos y properties <se definen las clases especificadas en el enunciado y se utilizan todos los contenidos pedidos para esto>
##### ✅ Relaciones entre clases <Se integra almenos 1 relacion de cada clase y estas tienen sentido en su aplicación>
#### Simulaciones: 10 pts (7%)
##### ✅ Crear partida <Es posible crear partidas en el casino mediante la ejecución del codigo y el flujo de menús >
#### Acciones: 35 pts (26%)
##### ✅ Jugador <todas las acciones del jugador se encuentran bien definidas y se ejecutan eventualmente\>
##### ✅ Juego <se realizan todas las acciones especificadas en el enunciado.>
##### ✅ Bebestible <existen todas las acciones solicitadas y dependiendo del tipo hace lo solicitado>
##### ✅ Casino <estan presentes todas las acciones solicitadas en el enunciado sumada la accion bonus "Show" >
#### Consola: 41 pts (30%)
##### ✅ Menú de Inicio <se presentan las 2 opciones solicitadas en el enunciado>
##### ✅Opciones de jugador <imprime todos los jugadores pertenecientes al archivo y se puede elegir cualquiera de estos\>
##### ✅ Menú principal <perminte unir accion particular del casino y integra todas las opciones solicitadas>
##### ✅ Opciones de juegos <imprime una lista indexada con todos los juegos disponibles en el casino\>
##### ✅ Carta de bebestibles <imprime cada bebestible existente en el archivo utilizando la funcion __str__>
##### ✅ Ver estado del Jugador <imprime correctamente los datos solicitados utilizando la funcion  __str__>
##### ✅ Robustez <en todas las instancias donde un input es solicitado se filtra este y se evita que ingresen valores no deseados \>
#### Manejo de archivos: 13 pts (9%)
##### ✅ Archivos CSV  <se leen los archivos correctamente independiente de la ubicacion de los headers>
##### ✅ parametros.py <se definen los parametros solicitados en el enunciado y no existen "malos parametros" en el archivo>
#### Bonus: 3 décimas máximo
##### ✅ Ver Show <Se creó la funcion Show que realiza lo solicitado en el enunciado, sumando un "show grafico" con arte asci, se encuentra en el Casino.py linea 55>
## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. y no se deben crear archivos o directorios adicionales:


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```random```: ```random```, ```choice```
2. ```abc```: ```ABC```, ```abstractmethod```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```Bebidas```: Contiene a ```Bebestible```, ```Jugo```, ```Gaseosa```, ```BrebajeMagico``` 
2. ```Casino```: Contiene a ```Casino```
3. ```Juego```: Contiene a ```Juego```
4. ```Jugador```: Contiene a ```Jugador```, ```Casual```, ```Ludopata```, ```Tacano```, ```Bebedor```
5. ```Archivos```: Hecha para <Tratar con los archivos .csv utilizados en el codigo >
6.  ```Archivos```: Hecha para <ejecutar graficamente el codigo y filtrar datos entregados por inputs >

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. <la formula para calcular la probabilidad de ganar un juego esta definida en Juego.py linea 13, en una funcion especificada para esto.> 
2. <la formula para calcular probabilidad de ganar del jugador esta definida en Jugador.py linea 131>
3. <dado que en la tarea se mencionaban 2 veces que hacer al momento de no poder pagar un bebestible, mi codigo vuelve al menu de inicio, como especificaba 1 de las 2 menciones.>
4. <al ganar una apuesta se gana el monto apostado y en caso de perder se descuenta este monto, considerando que se entrega el monto duplicado descontando la apuesta, como en un casino real>
5. <las acciones de cada personalidad se encuentran implementadas pero no como una funcion particular de cada clase debido a que actuaban en otras funciones directamente, haciendo mas complejo generar una funcion abstracta para modelarlas o algo similar>
-------