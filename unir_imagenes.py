from PIL import Image
import os
import math

# Configuración
CARPETA_IMAGENES = "./imagenes"  # Cambia esto si tus imágenes están en otra carpeta
SALIDA_CARPETA = "./salida"  # Carpeta donde se guardarán las imágenes unidas
IMAGENES_POR_UNION = 12  # Número máximo de imágenes por imagen unida

# Crear la carpeta de salida si no existe
os.makedirs(SALIDA_CARPETA, exist_ok=True)

# Obtener la lista de imágenes en la carpeta (ordenadas numéricamente)
imagenes = sorted([img for img in os.listdir(CARPETA_IMAGENES) if img.endswith(('.jpg', '.png', '.jpeg'))])

# Dividir las imágenes en grupos de IMAGENES_POR_UNION
num_grupos = math.ceil(len(imagenes) / IMAGENES_POR_UNION)

for i in range(num_grupos):
    grupo = imagenes[i * IMAGENES_POR_UNION:(i + 1) * IMAGENES_POR_UNION]
    imagenes_abiertas = [Image.open(os.path.join(CARPETA_IMAGENES, img)) for img in grupo]

    # Obtener ancho y alto máximo
    ancho_max = max(img.width for img in imagenes_abiertas)
    altura_total = sum(img.height for img in imagenes_abiertas)

    # Crear nueva imagen
    imagen_unida = Image.new("RGB", (ancho_max, altura_total))

    # Pegar las imágenes una debajo de otra
    y_offset = 0
    for img in imagenes_abiertas:
        imagen_unida.paste(img, (0, y_offset))
        y_offset += img.height

    # Guardar la imagen unida
    salida_nombre = os.path.join(SALIDA_CARPETA, f"unida_{i+1}.jpg")
    imagen_unida.save(salida_nombre)

    print(f"Imagen guardada: {salida_nombre}")

print("Proceso completado. 🎉")
