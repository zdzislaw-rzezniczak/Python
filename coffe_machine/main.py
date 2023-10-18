from ekspres import Ekspres

ekspres = Ekspres(20, 10, 15, 10, "ceramiczny")

while True:
    ekspres.zrob_kawe()
    print("Pozostało mleka: ", ekspres.zbiornik_mleka.aktualna_pojemnosc)
    print("Pozostało wody: ", ekspres.zbiornik_wody.aktualna_pojemnosc)
    print("Pozostało mleka: ", ekspres.zbiornik_kawy.aktualna_pojemnosc)
    print("Pozostało miejsca na fusy: ", ekspres.pojemnik_fusow.dostepne_miejsce)
