import os
import shutil

# -----------------------------
# Definición de rutas
# -----------------------------
RAW_DIR = "data/raw"
CSV_DIR = "data/processed/csv"
JSON_DIR = "data/processed/json"
TXT_DIR = "data/processed/txt"

# -----------------------------
# Crear estructura de carpetas (si no existen)
# -----------------------------
os.makedirs(RAW_DIR, exist_ok=True)
os.makedirs(CSV_DIR, exist_ok=True)
os.makedirs(JSON_DIR, exist_ok=True)
os.makedirs(TXT_DIR, exist_ok=True)

# -----------------------------
# Crear archivos de ejemplo
# -----------------------------
archivos_ejemplo = [
    "ventas_enero.csv",
    "ventas_febrero.csv",
    "clientes.json",
    "productos.json",
    "notas.txt",
    "readme.txt"
]

for archivo in archivos_ejemplo:
    ruta_archivo = os.path.join(RAW_DIR, archivo)
    if not os.path.exists(ruta_archivo):
        with open(ruta_archivo, "w", encoding="utf-8") as f:
            f.write("")  # archivo vacío

# -----------------------------
# Clasificación de archivos
# -----------------------------
csv_movidos = 0
json_movidos = 0
txt_movidos = 0

for archivo in os.listdir(RAW_DIR):
    ruta_origen = os.path.join(RAW_DIR, archivo)

    if archivo.lower().endswith(".csv"):
        shutil.move(ruta_origen, os.path.join(CSV_DIR, archivo))
        csv_movidos += 1

    if archivo.lower().endswith(".txt"):
        shutil.move(ruta_origen, os.path.join(TXT_DIR, archivo))
        txt_movidos += 1

    elif archivo.lower().endswith(".json"):
        shutil.move(ruta_origen, os.path.join(JSON_DIR, archivo))
        json_movidos += 1

# -----------------------------
# Resultados en consola
# -----------------------------
print("Proceso finalizado correctamente.")
print(f"Archivos CSV movidos: {csv_movidos}")
print(f"Archivos JSON movidos: {json_movidos}")
print(f"Archivos TXT movidos: {txt_movidos}")
