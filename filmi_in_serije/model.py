class Filmi:
    def __init__(self, naslovi=None):
        self.naslovi = [] if naslovi is None else naslovi

    def dodaj_naslov(self, naslov):
        self.naslov.append(naslov)

class Naslov:
    def __init__(self, naslov, serija, zanr, leto_izdaje, pogledano):
        self.naslov = naslov
        self.serija = serija
        self.zanr = zanr
        self.leto_izdaje = leto_izdaje
        self.pogledano = False

    def gledano(self):
        self.pogledano = True