import os
import requests
import zipfile
from urllib.parse import unquote
from tqdm import tqdm

# UNPACKER MODPACK

def clean_directory(directorio):
    # Verificar si el directorio existe
    if os.path.exists(directorio):
        # Iterar sobre los archivos en el directorio
        for archivo in os.listdir(directorio):
            # Construir la ruta completa al archivo
            ruta_archivo = os.path.join(directorio, archivo)
            # Verificar si es un archivo
            if os.path.isfile(ruta_archivo):
                # Eliminar el archivo
                os.remove(ruta_archivo)
                print(f"Archivo eliminado: {ruta_archivo}")
            # Si es un directorio, llamar a la función recursivamente
            elif os.path.isdir(ruta_archivo):
                clean_directory(ruta_archivo)
        print(f"Directorio limpiado: {directorio}")
    else:
        print(f"El directorio {directorio} no existe.")

def download_file(link, minecraft_directory):
    # Create the folder if it doesn't exist
    os.makedirs(minecraft_directory, exist_ok=True)

    # Extract the file name from the URL
    path_name = os.path.join(minecraft_directory, link.split('/')[-1])
    file_name = os.path.basename(link)
    file_name = unquote(file_name)

    # Fetch file size
    response = requests.head(link)
    file_size = int(response.headers.get('content-length', 0))

    # Download the file with progress bar
    with requests.get(link, stream=True) as r:
        with open(path_name, 'wb') as f:
            with tqdm(total=file_size, unit='B', unit_scale=True, desc=file_name, ascii=True) as pbar:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                        pbar.update(len(chunk))

    print(f"- Archivo {file_name} descargado en: {path_name}")

    # Extract the downloaded file
    extract_zip(path_name, minecraft_directory)

def extract_zip(zip_file, extract_path):
    # Extract the downloaded file
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_path)

    print(f"- Archivo extraido en: {extract_path}")

# Example usage
    
# Esta parte solo se ejecutará si main.py se ejecuta como script principal

if __name__ == "__main__":
    user_windows = os.environ['USERNAME']
    minecraft_directory = f"C://Users//{user_windows}//AppData//Roaming//.minecraft//mod"
    link = "https://github.com/Halosesparta13/Lucky-World-Launcher/raw/main/Part%201.zip"
    download_file(link, minecraft_directory)


# FORGE INSTALLER

# MENU
