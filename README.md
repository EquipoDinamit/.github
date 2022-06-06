# Examen #3 Examen Práctico (Editando...)
<i>Por medio de hardware realizar acciones en una página web utilizando un servidor con WebSockets.</i>

![Sistema 1](https://github.com/EquipoDinamit/Examen3/blob/main/imagenes/indicaciones.png "Diagrama del sistema")

El sistema se compone de tres módulos o bloques independientes que interactúan entre sí. Dos de los tres módulos son clientes, un <b>cliente emisor</b> (controlado por hardware), un <b>cliente receptor</b> (página web con html) y el <b>servidor</b> que permite la comunicación entre los dos clientes para que sea posible mover objetos o realizar diferentes acciones en la página web con la información que envía el emisor.

# Cliente emisor

### Circuito
Los materiales que se utilizaron son: <br>
<ul>
 <li>Arduino uno.</li>
 <li>8 resistenciias de 1k ohms.</li>
 <li>1 Protoboard.</li>
 <li>7 Push buttos.</li>
</ul>

A continuacion armar el circuito de la imagen.

<img src="https://github.com/EquipoDinamit/Examen3/blob/main/imagenes/Circuito%20emisor.png" alt="Circuito Emisor" style="height: 100%; width:100%;"/>

Los botones tienen asignados los números del 1 al 7 de izquierda a derecha.

### Código

<b>Emisor.ino:</b> 
<ul>
 <li>Abrir el archivo en el IDE de Arduino.</li>
 <li>En la pestaña de Herramientas/Tools seleccionamos la Placa en la que se desea subir el codigo y tambien seleccionamos el Puerto al que este conectado el microocontrolador.</li>
 <li>Darle al boton de "Subir/Upload".</li>
</ul>

Lo que se espera del código "Emisor.ino" es que cada botón nos regrese un valor del 1 al 7 que será leído por el código "ClienteEmisor.py" y enviado al servidor. 

<b>ClienteEmisor.py:</b>
<ul>
 <li>Desde la ubicacion del archivo "Cliente emisor.py" abrir la consola (cmd) y ejecutar el programa.</li>
 <ul>
  <li><b>Ejemplo:</b><br>
    <i>C:\Users\minim\Desktop\Sistema de Computo y Redes\Examen></i><b>python ClienteEmisor.py</b></li>
 </ul>
</ul>

Lo que se espera del código "ClienteEmisor.py" es que pueda conectarse con el servidor cuando el "main.js" se esté ejecutando y que le mande la información leída del arduino para que el servidor la envíe al cliente receptor.

# Servidor
Para tener el servidor desde tu computadora hacer lo siguiente:<br>
En caso de tener un modem de INFINITUM ingresar a http://192.168.1.254/login.html y buscar el apartado "DMZ" (Demilitarized Zone ó Zona desmilitarizada) y activamos la función DMZ.<br>
Buscar el apartado "Mapeo de Puertos/Port Mapping" y una vez ahí en la sección "Reenvió de Puertos" definimos un puerto nuevo y especificamos que se trata de un Protocolo TCP.<br>
<b>Nota:</b> Es importante guardar los datos de la Dirección IP Pública.

<b>main.js:</b><br>
Si es la primera vez que se ejecuta el servidor es necesario hacer lo siguiente:
<ul>
 <li></li>
</ul>

# Cliente receptor 

