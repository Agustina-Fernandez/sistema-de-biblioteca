# 📚 Sistema de Gestión de Biblioteca 

Este proyecto consiste en una aplicación interactiva basada en consola desarrollada en Python para la administración y control de inventarios de libros y préstamos de usuarios en una biblioteca. El sistema almacena la información de manera persistente en una base de datos relacional y automatiza la generación de reportes en archivos planos.


## 🛠️ Tecnologías Utilizadas

* **Python 3.13.2**
* **SQLite3:** Motor de base de datos integrado para la gestión de datos relacionales.
* **CSV (Comma-Separated Values):** Formato para la exportación automatizada de reportes.


## 📋 Funcionalidades del Sistema

La aplicación ofrece un menú interactivo con 8 opciones que permiten realizar las siguientes tareas:

1. **Visualización Total de Inventario:** Muestra la lista completa de todos los libros almacenados en el sistema.
2. **Filtro de Disponibilidad:** Permite consultar rápidamente cuáles libros se encuentran listos para préstamo (disponibles).
3. **Búsqueda por Género:** Filtra y despliega los libros que coincidan exactamente con un género literario ingresado por el usuario.
4. **Registro de Usuarios:** Muestra un listado detallado de los clientes, sus datos de contacto, el libro que tienen alquilado y la fecha de la transacción.
5. **Altas de Registros (Create):** Permite ingresar nuevos libros al inventario o registrar nuevos usuarios con sus respectivas asignaciones de préstamos.
6. **Modificaciones (Update):** Permite actualizar de forma individual campos de las tablas (como el estado de disponibilidad, datos del autor, sucursal, datos de contacto del usuario, entre otros).
7. **Bajas de Registros (Delete):** Elimina registros de la base de datos basándose en el código único del libro o del cliente.
8. **Salir del Sistema:** Finaliza la ejecución de la aplicación de manera segura.


## 📂 Estructura del Proyecto

El repositorio está organizado con los siguientes archivos fundamentales para su ejecución:

* **`libreria.py`**: Archivo de código fuente principal en Python que contiene la lógica del menú, los métodos de consulta SQL y la manipulación de flujos por consola.
* **`biblioteca.db`**: Archivo de base de datos local SQLite que contiene de forma persistente las tablas de `libros` y `usuarios`.
* **`libros.csv`**: Reporte plano generado automáticamente por el sistema con la información estructurada del inventario de libros.
* **`usuarios.csv`**: Reporte plano generado automáticamente por el sistema con la lista de clientes y estados de alquileres.
