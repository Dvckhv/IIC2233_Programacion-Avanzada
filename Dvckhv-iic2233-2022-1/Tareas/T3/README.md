# Tarea 3: DCCasillas :school_satchel:


## Consideraciones generales :octocat:
La tarea comunica correctamente servidor y clientes, se puede jugar una partida de DCCasillas satisfactoriamente pero la comunicacion realizada en esta partida no se encuentra encriptada, sumado a que no se desarrolló correctamente el eliminar un usuario mientras se está en partida o en sala de espera.

### Cosas implementadas y no implementadas :white_check_mark: :x:

Explicación: mantén el emoji correspondiente, de manera honesta, para cada item. Si quieres, también puedes agregarlos a los títulos:
- ❌ si **NO** completaste lo pedido
- ✅ si completaste **correctamente** lo pedido
- 🟠 si el item está **incompleto** o tiene algunos errores

**⚠️⚠️NO BASTA CON SOLO PONER EL COLOR DE LO IMPLEMENTADO**,
SINO QUE SE DEBERÁ EXPLICAR QUÉ SE REALIZO DETALLADAMENTE EN CADA ITEM.
⚠️⚠️

#### Networking: 23 pts (18%)
##### ❌✅🟠 Protocolo 
se aplica correctamente el protocolo pedido y este es funcional
##### ✅ Correcto uso de sockets 
se realiza lo pedido respecto a sockets, manteniendo así una comunicación constante entre cliente y servidor mediante el uso de threads
##### ✅ Conexión
se pueden comunicar todos los mensajes que necesité comunicar
##### ✅ Manejo de clientes 
Al utilizar threads para comunicar el servidor con los diversos clientes, este no se bloquea de ninguna forma.
#### Arquitectura Cliente - Servidor: 31 pts (25%)
##### ✅ Roles
Mantuve (o intenté) manejar todo lo posible en el servidor, para así evitar posibles alteraciones al codigo por parte del usuario que pudieran beneficiarlo. el usuario y servidor cumplen con lo solicitado en el enunciado.
##### ✅ Consistencia
cada vez que se realiza un cambio en el juego, este se notifica a todos los clientes para que lo modifiquen en su interfaz, y por otra parte, en mi planteamiento de la tarea no fueron necesarios los locks, por lo que los "utilicé" cuando fuera necesario. 
##### ✅ Logs 
dado que el servidor no posee interfaz grafica, este comunica los cambios a base de los logs minimos solicitados por el enunciado
#### Manejo de Bytes: 26 pts (21%)
##### ✅ Codificación 
se codifican los mensajes utilizando el metodo mencionado en el enunciado, 
#####  🟠 Decodificación 
se realiza el proceso inverso de la misma manera aunque falto utilizar el identificador de cada bloque, pero esto se implementa facilmente guardando la los mensajes en una lista de tuplas y luego ordenandolas con un sort de los indices de bloque para finalmente unirlo todo ya ordenado.
##### ❌ Encriptación 
por falta de tiempo no alcancé a implementar la encriptación, asi que no existe en mi codigo
##### ❌ Desencriptación 
al igual que la encriptación, esto no se encuentra implementado
##### ✅ Integración
a pesar de no implementar encriptacion y desencriptacion, las funciones que hacen eso estan añadidas(sin alterar nada) en el enunciado realizando correctamente el protocolo de estar implementadas.
#### Interfaz: 23 pts (18%)
##### ✅ Ventana inicio
Funcional, cumple con lo solicitado en el enunciado
##### 🟠 Sala de Espera 
Es una Ventana funcional pero no cumple con eliminar a los usuarios que se desconecten de esta sala, por lo que en ese caso particular falla.

##### 🟠 Sala de juego 
al igual que la sala de espera, esto solo falla en el caso particular de desconectarse en medio de la partida.
##### 🟠 Ventana final 
No tuve tiempo suficiente para visualizar esta casilla pero deberia estar correctamente implementada
#### Reglas de DCCasillas: 18 pts (14%)
##### ✅ Inicio del juego 
los turnos se asignan en orden de llegada y los colores aleatoriamente.
##### ✅ Ronda 
se desarrolla correctamente el turno del jugador cumpliendo con todo lo solicitado en el enunciado
##### ✅ Termino del juego 
El juego termina correctamente cuando un jugador llega con ambas piezas a la casilla final
#### General: 4 pts (3%)
##### ✅ Parámetros (JSON) 
todos los parametros utilizados se encuentran en alguno de los archivos
#### Bonus: 5 décimas máximo
##### ❌ Cheatcode
no se implementa este bonus
##### ❌ Turnos con tiempo 
no se implementa este bonus
##### 🟠 Rebote
creo que este bonus esta implementado, lamentablemente no lo alcanze a probar

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es el respectivo   ```main.py``` para servidor y cliente.

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. Porfavor añadir la carpeta Sprites a cliente/frontend osinó el codigo no mostrara ninguna grafica.
