class AutomatCafea:
    def __init__(self):
        self.stare_curenta = 'q0'
#C = cafea, T = ceai, A = cappucino, H = ciocolata calda, OK = buton de confirmare
#q0 = stare initiala; q1,q2,q3,q4 = starile initiale, de exemplu q1 este pt cafea, g2 este pentru ceai s.a.m.d

    def tranzitie(self, intrare):
        tranzitii = {
            ('q0', 'C'): 'q1',
            ('q0', 'T'): 'q2',
            ('q0', 'A'): 'q3',
            ('q0', 'H'): 'q4',
            ('q1', 'OK'): 'q4',
            ('q2', 'OK'): 'q4',
            ('q3', 'OK'): 'q4',
            ('q4', 'OK'): 'q0'
        }

        if (self.stare_curenta, intrare) in tranzitii:
            self.stare_curenta = tranzitii[(self.stare_curenta, intrare)]
        else:
            print("Tranzitie invalida pentru starea curenta:", self.stare_curenta)

    def afisare_stare_curenta(self):
        print("Stare curenta: " + self.stare_curenta)


automat = AutomatCafea()
automat.afisare_stare_curenta()

automat.tranzitie('C')
automat.afisare_stare_curenta()

automat.tranzitie('T')
automat.afisare_stare_curenta()

automat.tranzitie('A')
automat.afisare_stare_curenta()

automat.tranzitie('H')
automat.afisare_stare_curenta()

automat.tranzitie('OK')
automat.afisare_stare_curenta()

