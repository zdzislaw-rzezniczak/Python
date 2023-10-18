import modulglowny
from grzalka import GrzalkaWody, GrzalkaMleka
from mlynek import Mlynek
from modulglowny import ModulGlowny
from pojemnikfusy import PojemnikNaFusy
from przepisy import przepisy
from zbiornik import ZbiornikWody, ZbiornikKawy, ZbiornikMleka


class Ekspres:
    def __init__(self, pojemnosc_zbiornika_kawy, pojemnosc_zbiornika_mleka, pojemnosc_zbiornika_wody,
                 pojemnosc_zbiornika_fusow, typ_mlynka):
        self.zbiornik_kawy = ZbiornikKawy(pojemnosc_zbiornika_kawy)
        self.zbiornik_mleka = ZbiornikMleka(pojemnosc_zbiornika_mleka)
        self.zbiornik_wody = ZbiornikWody(pojemnosc_zbiornika_wody)
        self.pojemnik_fusow = PojemnikNaFusy(pojemnosc_zbiornika_fusow)
        self.modul_glowny = ModulGlowny()
        self.mlynek = Mlynek(typ_mlynka)
        self.grzalka_wody = GrzalkaWody()
        self.grzalka_mleka = GrzalkaMleka()

    def get_modul_glowny(self):
        return self.modul_glowny

    def pobierz_przepis(self):
        self.modul_glowny.wyswietl_menu()
        default = przepisy[3]
        wybor = input("Wybierz kawe: ")
        if wybor.isdigit():
            wybor = int(wybor)
        try:
            przepis = przepisy[wybor - 1]
            print(przepis)
            return przepis
        except UnboundLocalError:
            return default
        except IndexError:
            print("Niewłaściwy wybór. Kawa domyślna....")
            return default
        except TypeError:
            print("Niewłaściwy wybór. Kawa domyślna....")
            return default


    def pobierz_skladniki(self, przepis):
        porcji_mleka = przepis["mleko"]
        porcji_wody = przepis["woda"]
        porcji_kawy = przepis["kawa"]
        self.zbiornik_mleka.pobierz_liczbe_porcji(porcji_mleka)
        self.zbiornik_wody.pobierz_liczbe_porcji(porcji_wody)
        self.zbiornik_kawy.pobierz_liczbe_porcji(porcji_kawy)
        self.pojemnik_fusow.dodaj_fusy_po_kawie(porcji_kawy)


    def zrob_kawe(self):
        przepis = self.pobierz_przepis()
        self.pobierz_skladniki(przepis)
        self.mlynek.mielenie_kawy()
        self.grzalka_wody.wlacz_grzalke()
        self.grzalka_mleka.wlacz_grzalke()
        self.grzalka_wody.grzej()
        self.grzalka_mleka.grzej()
        self.grzalka_wody.wylacz_grzalke()
        self.grzalka_mleka.wylacz_grzalke()
        print(f"Kawa: {przepis['nazwa']} gotowa")