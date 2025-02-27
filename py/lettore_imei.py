import os
import easyocr
import re

def estrai_numeri_da_immagine(immagine_path):
    reader = easyocr.Reader(['en'], gpu=True)
    results = reader.readtext(immagine_path)
    numeri = []
    
    for (bbox, text, prob) in results:
        testo_pulito = text.strip()  # Rimuove spazi bianchi all'inizio e alla fine
        
        # Cerca numeri di 15 cifre ignorando prefissi e caratteri non numerici
        numeri_trovati = re.findall(r'(?<!\d)(\d{15})(?!\d)', testo_pulito)
        if not numeri_trovati:
            # Se non trova numeri, prova a cercare anche in una versione pulita
            testo_pulito = re.sub(r'[^0-9]', '', testo_pulito)  # Rimuove tutto tranne cifre
            numeri_trovati = re.findall(r'(?<!\d)(\d{15})(?!\d)', testo_pulito)
        
        if numeri_trovati:
            numeri.extend(numeri_trovati)

    return list(set(numeri))  # Rimuovi duplicati se necessario

def salva_numeri_in_file(numeri, file_output):
    with open(file_output, 'w') as f:
        for numero in numeri:
            f.write(f"{numero}\n")

if __name__ == "__main__":
    cartella_immagini = r"path"
    file_output = "numeri_estratti.txt"

    numeri_totali = []
    for filename in os.listdir(cartella_immagini):
        if filename.endswith((".jpg", ".jpeg", ".png", ".bmp")):
            immagine_path = os.path.join(cartella_immagini, filename)
            print(f"Elaborando {immagine_path}...")  # Messaggio di debug
            
            if os.path.isfile(immagine_path):
                try:
                    numeri = estrai_numeri_da_immagine(immagine_path)
                    numeri_totali.extend(numeri)
                except Exception as e:
                    print(f"Errore durante l'elaborazione di {filename}: {e}")
            else:
                print(f"File non trovato: {immagine_path}")

    salva_numeri_in_file(numeri_totali, file_output)
    print(f"Numeri estratti e salvati in {file_output}")
