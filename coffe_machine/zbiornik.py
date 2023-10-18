class Zbiornik:

    def __init__(self, pojemnosc):
        self.pojemnosc = pojemnosc
        self.aktualna_pojemnosc = pojemnosc

    komunikat_uzupelnij_zbiornik = "Uzupelnij zbiornik"
    komunikat_braku_zawartosci = "Zbiornik pusty"
    komunikat_czy_uzupelnic_zbiornik = "Czy uzupełnić zbiornik"

    def get_aktualna_pojemnosc(self):
        return self.aktualna_pojemnosc

    def get_pojemnosc(self):
        return self.pojemnosc

    def uzupelnij_zbiornik(self, value):
        self.aktualna_pojemnosc = value

    def pobierz_liczbe_porcji (self, liczba_porcji):
        zawartosc_po_zuzyciu = self.aktualna_pojemnosc - liczba_porcji
        if zawartosc_po_zuzyciu > 0:
            self.aktualna_pojemnosc = zawartosc_po_zuzyciu
        else:
            print(self.komunikat_braku_zawartosci)
            print(self.komunikat_uzupelnij_zbiornik)
            self.uzupelnij_zbiornik(value= self.get_pojemnosc())


class ZbiornikMleka(Zbiornik):
    komunikat_uzupelnij_zbiornik = "Uzupelnij zbiornik mleka"
    komunikat_braku_zawartosci = "Zbiornik mleka pusty "
    komunikat_czy_uzupelnic_zbiornik = "Czy uzupełnić zbiornik mleka"


class ZbiornikWody(Zbiornik):
    komunikat_uzupelnij_zbiornik = "Uzupelnij zbiornik wody"
    komunikat_braku_zawartosci = "Zbiornik wody pusty "
    komunikat_czy_uzupelnic_zbiornik = "Czy uzupełnić zbiornik wody"


class ZbiornikKawy(Zbiornik):
    komunikat_uzupelnij_zbiornik = "Uzupelnij zbiornik kawy"
    komunikat_braku_zawartosci = "Zbiornik kawy pusty "
    komunikat_czy_uzupelnic_zbiornik = "Czy uzupełnić zbiornik kawy"
