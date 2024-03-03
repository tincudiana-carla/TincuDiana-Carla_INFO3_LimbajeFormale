import random

class AutomatFinit:
    def __init__(self):
        self.stare_curenta = 'q0'

    def tranzitie(self, intrare):
        tranzitii = {
            ('q0', 'a'): 'q1',
            ('q0', 'b'): 'q0',
            ('q0', 'c'): 'q0',
            ('q0', 'd'): 'q0',
            ('q1', 'a'): 'q1',
            ('q1', 'b'): 'q2',
            ('q1', 'c'): 'q1',
            ('q1', 'd'): 'q1',
            ('q2', 'a'): 'q2',
            ('q2', 'b'): 'q2',
            ('q2', 'c'): 'q2',
            ('q2', 'd'): 'q2',
            ('q3', 'a'): 'q3',
            ('q3', 'b'): 'q3',
            ('q3', 'c'): 'q3',
            ('q3', 'd'): 'q3'
        }

        if (self.stare_curenta, intrare) in tranzitii:
            self.stare_curenta = tranzitii[(self.stare_curenta, intrare)]
            print(f"Tranzitie: ({self.stare_curenta}, {intrare})")
        else:
            print("Tranzitie invalida pentru starea curenta:", self.stare_curenta)

    def este_stare_finala(self):
        return self.stare_curenta == 'q3'

def generare_limbaj_formal():
    litere = ['a', 'b', 'c', 'd']
    limbaj = set()

    for _ in range(100):
        cuvant = ''.join(random.choices(litere, k=3)) * 2
        lungime_cuvant = len(cuvant)
        if lungime_cuvant <= 6:
            limbaj.add(cuvant)

    return limbaj


def verificare_cuvinte(limbaj, automat):
    cuvinte_verificate = []

    for _ in range(3):
        cuvant = random.choice(list(limbaj))
        cuvinte_verificate.append((cuvant, automat.este_stare_finala()))

    return cuvinte_verificate


automat = AutomatFinit()

limbaj_formal = generare_limbaj_formal()

rezultate_verificare = verificare_cuvinte(limbaj_formal, automat)

for cuvant, este_in_limbaj in rezultate_verificare:
    if este_in_limbaj:
        print(f"Cuvantul '{cuvant}' este in limbaj.")
    else:
        print(f"Cuvantul '{cuvant}' nu este in limbaj.")

