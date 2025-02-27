import csv

file_path="path"
with open (file_path,mode="r",encoding="utf-8") as file:
    contenuto=file.read()
    contenuto_mod=contenuto.replace("\n","")
    l_contenuto=contenuto_mod.split("-")
with open ("path", mode="w",newline="", encoding="utf-8") as ex:
    writer = csv.writer(ex)
    for numero in l_contenuto:
        writer.writerow([numero])
