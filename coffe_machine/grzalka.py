from abc import ABC, abstractmethod
import time

class Grzalka(ABC):
    def __init__(self, maksymalna_temperatura_grzalki):
        self.temperatura_grzalki = 0
        self.maksymalna_temperatura_grzalki = maksymalna_temperatura_grzalki

    @abstractmethod
    def grzej(self):
        pass

    @abstractmethod
    def wlacz_grzalke(self):
        pass

    @abstractmethod
    def wylacz_grzalke(self):
        pass


class GrzalkaWody(Grzalka):
    def __init__(self):
        super().__init__("grzalka wody")

    def grzej(self):
        print("Grzeje wodę")
        time.sleep(2)

    def wlacz_grzalke(self):
        print("wlaczam grzalke wody")

    def wylacz_grzalke(self):
        print("wylaczam grzalke wody")


class GrzalkaMleka(Grzalka):
    def __init__(self):
        super().__init__("grzalka mleka")

    def grzej(self):
        print("Grzeje mleko")
        time.sleep(3)

    def wlacz_grzalke(self):
        print("wlaczam grzalke mleka")

    def wylacz_grzalke(self):
        print("wylaczam grzalke mleka")