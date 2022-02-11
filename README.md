# Quiz-I-A
## Problema 1 (7pts):
Se propone que se implemente un algoritmo que, dado un número introducido por el usuario (debe validarse que el input sea un número natural), diga si ese número es primo de Fermat.

***Definición:***
- *Número de Fermat: todo número natural de la forma (2^(2^n)) + 1 para algún n. Si ese número resulta ser primo, se denomina primo de Fermat.*


## Problema 2 (14pts + 2pts):
Una tienda de dispositivos electrónicos te ha contratado para que desarrolles un programa que les ayude a administrar su inventario. La tienda cuenta con los productos de la estructura de datos dada en el archivo e2.py.

El programa en cuestión consta de los siguientes requerimientos:
- **Ver inventario:** debe mostrar todos los productos, con sus respectivos precios y clasificados por marca, según la categoría (Móviles, Laptops o Accesorios) que seleccione el usuario.
- **Registrar compra:** debe solicitarse nombre, apellido y cédula del comprador, y el id del producto que va a comprar. Esta información debe almacenarse en la estructura de datos de su preferencia. Debe mostrarse en pantalla la factura generada, con los datos del comprador, el nombre del producto y el monto a pagar.
- **Menú principal** que permita seleccionar la acción que se quiera realizar.
- Debe volverse al menú principal cada vez que se termine alguna operación (es decir, el código debe seguir ejecutándose hasta que el usuario decida salir).
- Los mensajes por consola deben verse ordenados y ser intuitivos.

Como **requerimiento opcional** (2pts), se plantea una tercera opción en el menú: “Aplicar promoción”. Al seleccionarla, se le agregará el atributo *"promo" : True* a los productos para los que se cumpla que su nombre tenga algún número.
