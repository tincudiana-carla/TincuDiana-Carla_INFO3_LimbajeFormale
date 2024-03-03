import re

def citeste_fisier():
    cale_fisier = input("Introduceti calea catre fișierul text de verificat: ")

    try:
        with open(cale_fisier, 'r') as file:
            continut = file.read()
            return continut
    except FileNotFoundError:
        print("Fisierul nu a fost gasit.")
        return None

def verifica_format(continut):
    erori = []

    pattern_client = r"Informatii\sdespre\sclient:\s*(.*?),\s*adresa:\s*(.*)"
    match_client = re.search(pattern_client, continut)
    if not match_client:
        erori.append("- Sectiunea de informatii despre client lipseste sau este formatata gresita")

    pattern_produs = r"Produs:\s*(.*?),\s*Pret:\s*(\d+\.\d+),\s*TVA:\s*(\d+%)"
    match_produs = re.findall(pattern_produs, continut)
    if not match_produs:
        erori.append("- Nu exista detalii despre produse sau sunt formatate gresit.")

    return erori

def afiseaza_erori(erori):
    if not erori:
        print("Nu au fost identificate erori în fișierul facturii.")
    else:
        print("Au fost identificate urmaoarele erori în fisierul facturii:")
        for eroare in erori:
            print(eroare)

continut_fisier = citeste_fisier()
if continut_fisier:
    erori_gasite = verifica_format(continut_fisier)
    afiseaza_erori(erori_gasite)
