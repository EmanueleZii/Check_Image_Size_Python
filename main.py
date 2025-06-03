import os
from PIL import Image

# Cambia il percorso alla cartella delle immagini e al file di output
folder_path = "C:/La_cartella_piena_di_immagini"
input(f"cartella da scansionare:\n {folder_path}");
output_file = "C:/Users/utente/La_Cartella_in_cui_vuoi_il_file_txt"
input(f"cartella per il file log delle scansioni: \n {output_file}")

def check_image_size(folder_path, output_file):
    with open(output_file, 'a') as f:
        f.write("Scansione della cartella: " + folder_path + "\n")
        for filename in os.listdir(folder_path):
            if filename.endswith(('.png', '.jpg', '.jpeg')):
                file_path = os.path.join(folder_path, filename)
                try:
                    with Image.open(file_path) as img:
                        file_size_kb = os.path.getsize(file_path) / 1024  # Converti byte in kilobyte
                        f.write(f"Nome: {filename}, Dimensione: {file_size_kb:.2f} KB\n")
                        if file_size_kb > 1024:  # 1 megabyte = 1024 KB
                            f.write("  * Questa immagine supera 1 megabyte.\n")
                except Exception as e:
                    f.write(f"Errore durante il controllo dell'immagine {filename}: {e}\n")
        f.write("\n")


check_image_size(folder_path, output_file)
