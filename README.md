Bienvenidos a Ender3V3-SE Klipper Edition!

Este fork de Klipper fue diseñado con la finalidad de dotar a la impresora Creality Ender3-V3SE de la capacidad de operar bajo Klipper manteniendo la función de Display y la nivelación automática

Es importante destacar que para que funcione debe instalar esta versión de Klipper en una Raspberry Pi o similar

El código fuente fue adaptado desde el original de Klipper y desde el fork de JP Curti (https://github.com/jpcurti/E3V3SE_display_klipper).

En la versión inicial se corrigio un problema sobre el fichero prtouch el cual generaba que el nozzle quede algo más alejado de la cama calefactora.

Para compilar su propio firmware debe configurar con el comando make menuconfig ejecutado desde la consola en la carpeta de Klipper

Verifique que las opciones se vean como en la siguiente imagen:

![image](https://github.com/user-attachments/assets/3d4ad8d0-8f08-411f-b565-5a1ced36bc91)

Luego presione Esc y confirme con Y.

Escriba en la consola make y espere , al finalizar se generara un fichero llamado Klipper.bin el cual deberá grabar en su impresora 3d en reemplazo del firmware.

Importante: recuerde que la configuración anterior habilita la conexión vía USB-C de su impresora , no necesita utilizar el cable UART para conectarse a ella.

Gracias por su tiempo :-)
