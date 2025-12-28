# Extracción de CUFE desde PDFs – Python

Script desarrollado en Python que procesa facturas en formato PDF, extrae el
CUFE desde la primera página utilizando una expresión regular específica y
almacena la información en una base de datos SQLite.

---

## Descripción del problema

El sistema debe procesar múltiples archivos PDF de facturas y extraer el CUFE,
un identificador alfanumérico que se encuentra en la parte inferior de la primera
página del documento.

La extracción se realiza usando la siguiente expresión regular:

(\b([0-9a-fA-F]\n*){95,100}\b)

La información obtenida se almacena en una base de datos SQLite con los siguientes
campos:

- Nombre del archivo
- Número de páginas
- CUFE
- Peso del archivo

---

## Tecnologías utilizadas

- Python 3
- pdfplumber
- SQLite
- Expresiones regulares (re)

---

## Estructura del proyecto

```text
bills_info_extractor/
├── extract_info.py
├── bills/
│   ├── E54180324100737R001359977300.PDF
│   ├── E54200324101609R001360619800.PDF
├── info_data.db
└── README.md
```

## Instalación y ejecución
1. Ubicarse en la carpeta del proyecto

cd bills_info_extractor

2. Crear y activar entorno virtual

python3 -m venv env

source env/bin/activate

3. Instalar dependencias

pip install pdfplumber

4. Agregar los archivos PDF

Copiar las facturas en formato PDF dentro de la carpeta:
bills/

5. Ejecutar el script

python extract_info.py

## Base de datos SQLite

El script genera automáticamente el archivo:

info_data.db

## Estructura de la tabla

**Tabla:** `info`

| Campo      | Tipo    |
|-----------|---------|
| id        | INTEGER |
| file_name | TEXT    |
| pages     | INTEGER |
| cufe      | TEXT    |
| file_size | INTEGER |

---

## Validaciones y consideraciones técnicas

- Solo se analiza la primera página del PDF
- Se eliminan los saltos de línea del CUFE extraído
- Si el CUFE no se encuentra, se almacena como `NULL`
- SQLite no requiere servidor ni configuración adicional
- No se almacenan archivos PDF, solo metadatos

---

## Ejemplo de salida en consola

```text
Procesado: E54180324100737R001359977300.PDF
Procesado: E54200324101609R001360619800.PDF
```

### Autor
Esteban Cuervo