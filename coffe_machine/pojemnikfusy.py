class PojemnikNaFusy:

    def __init__(self, pojemnosc):
        """Pojemnosc to liczba dostepna w porcjach"""
        self.pojemnosc = pojemnosc
        self.dostepne_miejsce = pojemnosc

    def oproznij_pojemnik_na_fusy(self):
        self.dostepne_miejsce = self.pojemnosc

    def dodaj_fusy_po_kawie (self, liczba_porcji):
        self.dostepne_miejsce = self.dostepne_miejsce - liczba_porcji
        if self.dostepne_miejsce <= 0:
            czy_pusty= False
            while not czy_pusty:
                czy_oproznic = input("Brak miejsca w pojemniku na fusy. Czy opróżnić pojemnik? T/N")
                if czy_oproznic.lower() == 't':
                    self.oproznij_pojemnik_na_fusy()
                    czy_pusty = True
                else:
                    print("Niestety brak miejsca uniemożliwia zrobienie kawy")
