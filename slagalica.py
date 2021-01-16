import random

class Plocica(object):
    
    #kljuc je broj, vrijednosti su (naziv?, pozicija)
    __plocica_info = {1: ("jedan", 1),
                      2: ("dva", 2),
                      3: ("tri", 3),
                      4: ("cetiri", 4),
                      5: ("pet", 5),
                      6: ("sest", 6),
                      7: ("sedam", 7),
                      8: ("osam", 8),
                      9: ("devet", 9),
                      10: ("deset", 10),
                      11: ("jedanaest", 11),
                      12: ("dvanaest", 12),
                      13: ("trinaest", 13),
                      14: ("cetrnaest", 14),
                      15: ("petnaest", 15),
                      '': ("prazno", 16)}
    
    __trenutne_pozicije = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

    @staticmethod
    def brojevi():
        return Plocica.__plocica_info.keys()
    
    @staticmethod
    def trenutne_pozicije():
        return list(Plocica.__trenutne_pozicije)
    
    def __init__(self, broj, trenutna_pozicija):
        self.__broj = broj
        self.__trenutna_pozicija = trenutna_pozicija

    @property
    def broj(self):
        return self.__broj
    
    @property
    def trenutna_pozicija(self):
        return self.__trenutna_pozicija
    
    @property
    def naziv(self):
        return Plocica.__plocica_info[self.__broj][0]

    @property
    def pozicija(self):
        return Plocica.__plocica_info[self.__broj][1]

    def __repr__(self):
        return self.__class__.__name__ + '(%r, %r)' % (self.__broj, self.__trenutna_pozicija)
    
    def __str__(self):
        return self.naziv.title() + ' ' + str(self.trenutna_pozicija)


class Slagalica(object):
    
    def __init__(self):
        self.__plocice = []

        brojevi = list(Plocica.brojevi())
        
        for pozicija in Plocica.trenutne_pozicije():
                self.__plocice.append(Plocica(brojevi[pozicija-1], pozicija))
        
    def __str__(self):
        d = {}
        key = 1
        for r in range(4):
            for c in range(4):
                d[key]=[r,c]
                key += 1

        s = [[0 for r in range(4)] for c in range(4)]
        

        for plocica in self.__plocice:

            for key in d.keys():
                if key == plocica.trenutna_pozicija:
                    r = d[key][0]
                    c = d[key][1]
                    s[r][c] = plocica.broj
                    
        return '\n'.join(['\t'.join([str(r) for r in red]) for red in s])
    
    def promjesaj(self):
        self.__plocice = []
        brojevi = list(Plocica.brojevi())
        for pozicija in Plocica.trenutne_pozicije():
            broj = random.sample(brojevi, 1)[0]
            brojevi.remove(broj)
            self.__plocice.append(Plocica(broj, pozicija))

    def dajPlocice(self, broj_plocica = 1):
        danePlocice = []

        prazna = None

        for plocica in self.__plocice:
            if plocica.naziv == 'prazno':
                prazna = plocica

        prvaSlijeva = prazna.trenutna_pozicija - 1
        prvaSdesna = prazna.trenutna_pozicija + 1
        cetvrtaSlijeva = prazna.trenutna_pozicija - 4
        cetvrtaSdesna = prazna.trenutna_pozicija + 4
        
        for plocica in self.__plocice:
            
            if prazna.trenutna_pozicija in [5,9,13]:
                if plocica.trenutna_pozicija == prvaSdesna:
                    danePlocice.append(plocica)
                elif plocica.trenutna_pozicija == cetvrtaSlijeva:
                    danePlocice.append(plocica)
                elif plocica.trenutna_pozicija == cetvrtaSdesna:
                    danePlocice.append(plocica)
                    
            elif prazna.trenutna_pozicija in [4,8,12]:
                if plocica.trenutna_pozicija == prvaSlijeva:
                    danePlocice.append(plocica)
                elif plocica.trenutna_pozicija == cetvrtaSlijeva:
                    danePlocice.append(plocica)
                elif plocica.trenutna_pozicija == cetvrtaSdesna:
                    danePlocice.append(plocica)
                    
            else:  
                if plocica.trenutna_pozicija == prvaSlijeva:
                    danePlocice.append(plocica)
                elif plocica.trenutna_pozicija == prvaSdesna:
                    danePlocice.append(plocica)
                elif plocica.trenutna_pozicija == cetvrtaSlijeva:
                    danePlocice.append(plocica)
                elif plocica.trenutna_pozicija == cetvrtaSdesna:
                    danePlocice.append(plocica)
                    
        return danePlocice


class Igrac(object):

    def __init__(self):
        self.__plociceZaSlaganje = []

    @property
    def plociceZaSlaganje(self):
        return self.__plociceZaSlaganje

    @plociceZaSlaganje.setter
    def plociceZaSlaganje(self, value):
        self.__plociceZaSlaganje = value

    def uzmiPlociceZaSlaganje(self, plocice):
        self.__plociceZaSlaganje += plocice

    def sloziPlocicu(self, izbor):
        plocica = None
        for p in self.__plociceZaSlaganje:
            if p.broj == izbor:
                plocica = p
        plocica = self.__plociceZaSlaganje.remove(plocica)
        return plocica
