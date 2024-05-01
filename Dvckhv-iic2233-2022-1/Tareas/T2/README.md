# Tarea 2: DCComando espacial :school_satchel:

## Consideraciones generales :octocat:

<La tarea modela correctamente lo solicitado en las instrucciones, se completa cada nivel correctamente y se prohibe seguir en caso de perder, probé y termine varias partidas con diversos resultados pero quizas exista algun error dentro del codigo al cual no llegue con mis pruebas.>

### Cosas implementadas y no implementadas :white_check_mark: :x:


#### ✅Ventana de Inicio: 4 pts (4%) 
#### ✅Ventana de Ranking: 5 pts (5%)
#### ✅Ventana principal: 7 pts (7%)
#### ✅Ventana de juego: 14 pts (13%)
#### ✅Ventana de post-nivel: 5 pts (5%)
```Se puede navegar correctamente por todas las ventanas creadas segun lo pedido en el enunciado y pauta```
#### Mecánicas de juego: 47 pts (45%)
##### ✅ Arma: 
El arma se mueve y comporta correctamente para la pedido por la pauta, aunque se mueve en una dirección a la vez .
##### 🟠 Aliens y Escenario de Juego 
Los aliens interactuan con el mapa de forma correcta y al aparecer se mueven con una dirección aleatoria y posicion inicial aleatoria.
Dentro de mis pruebas existió un unico error de Qthreads donde si disparaba a 2 aliens simultaneamente saltaba un error, no supe por que ocurria asi que no pude solucionarlo
##### ✅ Fin de Nivel 
Se utiliza la formula dada en el enunciado y termina el nivel en caso de que se  cumpla alguna condicion de termino.
##### ✅ Fin del juego 
Se registra el puntaje independiente de como terminó la partida, el perro solo se rie cuando se gana el nivel y se bloquea el boton de siguiente en caso de que se pierda.
#### Cheatcodes: 8 pts (8%)
##### ✅ Pausa 
Se pausa toda la actividad de la pantalla menos la caida de aliens muertos y en caso de que se reanude todo continua como habia quedado antes de terminar.
##### ✅ O + V+ N + I 
El comando  otorga municiones infinitas como se solicita, para que funcione debe ingresarse 1 caracter por 1, como si de escribir un texto se tratase.

##### ✅  C + I + A 
El comando pasa automaticamente al siguiente nivel, para que funcione debe ingresarse 1 caracter por 1, como si de escribir un texto se tratase.
#### General: 14 pts (13%)
##### ✅ Modularización
Se separa correctamente el codigo entre backend y frontend
##### ✅ Modelación
 Se privilegiando la cohesion y el bajo acoplamiento al utilizar señales y parametros para el trabajo entre archivos.
##### ✅ Archivos 
Se utilizan todos los archivos especificados en el enunciado.
##### ✅ Parametros.py
Se crea el archivo Parametros.py incluyendo lo solicitado en el enunciado y otros parametros que consideré necesarios.
#### Bonus: 10 décimas máximo
##### ✅ Risa Dog 
Una vez termina el nivel y si y solo si se gana, al cambiar el sprite del perro, este se rie como pancho saavedra.
##### ✅ Estrella 
Cada vez que aparece una estrella de la muerte en pantalla y se dispara a esta se pierde una cantidad dada de tiempo que se encuentra en el archivo ```parametros.py```.
##### ✅ Disparos extra 
Aparece una vez por partida el bonus que otorga 3 balas para el nivel en caso de hacer click en el, si no se clickea desaparece tras un tiempo para luego volver a aparecer.
##### ✅ Bomba 
Cuando se dispara a este sprite, los aliens presentes en la pantalla que se encuentren vivos se paralizan durante un tiempo dado por el archivo ```parametros.py```.
## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. para el buen funcionamiento del codigo porfavor mover archivo ```Ventana_Principal.ui``` a la carpeta ```Sprites```, no se encuentra ahi debido a que esta carpeta no se envia.

## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```PyQt5``` (debe instalarse)
1. ```random```: ```random```, ```choice```, ```uniform```


### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```logica_inicio```: Contiene a ```LogicaInicio```, Maneja el menu de inicio, ranking y principal ya que no necesitaban tanta logica como para separlos en 3 

2. ```logica_juego```: Contiene a ```LogicaJuego```, Maneja la Ventana Juego y Postjuego.
3. ```objetos_juego```: Hecha para administrar distintos objetos presentes en el juego, como la Mira,Aliens y Bonus

4. ```ventana_inicio```: Contiene a ```VentanaInicio```, ```VentanaRanking```, ```VentanaPrincipal```, Maneja la parte grafica de estas 3 ventanas de juego

5. ```ventana_juego```: Contiene a ```VentanaJuego```, Maneja la parte grafica de esta ventana.
6. ```ventana_postnivel```: Contiene a ```VentanaPost``` ,Maneja la parte grafica de la ventana.
7. ```parametros```: Hecha para eliminar HardCodeo, contiene todos los parametros utilizados en el codigo(o la gran mayoria). 


## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. las ventanas de Juego y PostJuego se encuentran manejadas por el mismo archivo de Logica que esta ultima ventana utilizaba datos del juego almacenados en LogicaJuego y así no abusaba de señales entre logicas y podia realizar otras cosas a la vez con esos datos
2. Los eventos Bonus fueron tratados de la misma manera y aparecen aleatoreamente como si se tratara de tirar un dado ya que no se mencionaba como estos aparecian 
3. Las Teclas de movimiento son "WASD", el disparo se efectua con la tecla "Espacio", el juego se pausa con la letra "P" y los cheatcodes se realizan de 1 tecla en 1, como si se tratara de escribir un texto normal
4. Los aliens aparecen siempre y cuando hayan 2 o menos en la pantalla, al leer la tarea así lo entendí y funciona perfectamente asi.

Pd: Mi pantalla es de 2560x1600 pixeles, por lo que espero que se vea bien mi tarea en una pantalla de menor resolución.



