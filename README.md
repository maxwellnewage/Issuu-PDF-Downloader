# Issuu-PDF-Downloader

Este fork arregla los problemas de dependencias y la generación de PDFs.

También se reemplaza el input() por una lista de links de Issuu para automatizar el proceso.

## Cómo funciona
El script [dict_to_json_replay.py](dict_to_json_replay.py) genera el archivo issuu_urls.json en la carpeta [json](json) con el siguiente esquema:

```json
[
    {
        "name": "name of the pdf",
        "url": "issuu url"
    }
]
```

Puedes utilizarlo para bajar las revistas de Replay, o reescribir tu propio json que contenga los links de las revistas que quieras convertir.

Para correrlo, debes ejecutar el script [main.py](main.py). El proceso es el siguiente:
- Carga y convierte el archivo json issuu_urls.json a un diccionario de Python.
- Por cada url, descarga todas las páginas como imágenes. Guarda cada imagen en [images](images).
- Une todas las imágenes en un PDF con la librería FPDF, y luego genera un archivo en la carpeta [pdfs](pdfs).
- Una vez generado el PDF, borra todas las imágenes de la carpeta images.

## Aclaración importante
No funciona con las revistas limitadas en páginas de Issuu. Descarga todo en imágenes, pero luego en el PDF quedan con el mismo efecto blurr.