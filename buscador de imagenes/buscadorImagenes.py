import os
import shutil
from zipfile import ZipFile

def buscar_imagenes(directorios, nombres_imagenes):
    imagenes_encontradas = []
    for directorio in directorios:
        for root, _, files in os.walk(directorio):
            for nombre in nombres_imagenes:
                if nombre in files:
                    imagenes_encontradas.append(os.path.join(root, nombre))
    return imagenes_encontradas

def copiar_imagenes(imagenes, destino):
    for imagen in imagenes:
        shutil.copy(imagen, destino)

def crear_zip(imagenes, archivo_zip):
    with ZipFile(archivo_zip, 'w') as zipf:
        for imagen in imagenes:
            zipf.write(imagen, os.path.basename(imagen))

def main():
    # Leer el archivo de texto con la lista de nombres de imágenes
    with open('fotos', 'r') as f:
        nombres_imagenes = [line.strip() for line in f.readlines()]

     # Obtener el directorio actual y listar sus elementos
    directorio_actual = os.getcwd()
    elementos_directorio = os.listdir(directorio_actual)

    # Filtrar solo los directorios en el directorio actual
    directorios = [os.path.join(directorio_actual, d) for d in elementos_directorio if os.path.isdir(os.path.join(directorio_actual, d))]

    # Buscar las imágenes en los directorios
    imagenes_encontradas = buscar_imagenes(directorios, nombres_imagenes)

    # Verificar si se encontraron todas las imágenes
    for nombre in nombres_imagenes:
        if not any(nombre in imagen for imagen in imagenes_encontradas):
            print(f"Alerta: No se encontró la imagen {nombre}")

    # Crear un archivo zip con todas las imágenes copiadas
    archivo_zip = 'imagenes.zip'
    crear_zip(imagenes_encontradas, archivo_zip)

if __name__ == '__main__':
    main()
