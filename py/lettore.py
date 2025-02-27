import csv

file_path="C:/Users/mdinardo/Desktop/Caricamento_imei/150.txt"
with open (file_path,mode="r",encoding="utf-8") as file:
    contenuto=file.read()
    contenuto_mod=contenuto.replace("\n","")
    l_contenuto=contenuto_mod.split("-")
with open ("C:/Users/mdinardo/Desktop/Caricamento_imei/py_imei.csv", mode="w",newline="", encoding="utf-8") as ex:
    writer = csv.writer(ex)
    for numero in l_contenuto:
        writer.writerow([numero])