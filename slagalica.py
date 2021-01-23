import random
import time

class Plocica(object):

    #kljuc je broj, vrijednosti su (naziv, pozicija)
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
    
    @naziv.setter
    def naziv(self, value):
        self.__naziv = value

    @property
    def pozicija(self):
        return Plocica.__plocica_info[self.__broj][1]

    def __repr__(self):
        return self.__class__.__name__ + '(%r, %r)' % (self.__broj, self.__trenutna_pozicija)

    def __str__(self):
        return self.naziv.title() + ' ' + str(self.broj)


class Slagalica(object):

    def __init__(self):
        self.__plocice = []

        brojevi = list(Plocica.brojevi())

        for pozicija in Plocica.trenutne_pozicije():
                self.__plocice.append(Plocica(brojevi[pozicija-1], pozicija))

    @property
    def plocice(self):
        return self.__plocice

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

        return '\n' + '\n'.join(['\t'.join([str(r) for r in red]) for red in s]) + '\n'

    def promjesaj(self):
        self.__plocice = []
        brojevi = list(Plocica.brojevi())
        
        #Fisher-Yates algoritam za miješanje
        
        for i in range(len(brojevi)-1, 0, -1):
            j = random.randint(0, i)
            brojevi[i], brojevi[j] = brojevi[j], brojevi[i]
            
        if self.jeRjesiva(brojevi):
            for pozicija in Plocica.trenutne_pozicije():
                self.__plocice.append(Plocica(brojevi[pozicija-1], pozicija))
        else:
            self.promjesaj()
            
    def jeRjesiva(self, brojevi):
        #provjerava se da li je random slagalica rjesiva
        invCount = 0
        brojevi[brojevi.index('')] = 16
        
        for i in range(4):
            for j in range(i+1, 4):
                if(brojevi[i] > brojevi[j]):
                    invCount += 1
                    
        brojevi[brojevi.index(16)] = ''
        
        if (brojevi.index('')+1) %2 == 0 and invCount % 2 == 0:
            return False
        
        return True

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
    
    def jeSlozena(self):
        s = Slagalica()
        if str(self.__plocice) == str(s.__plocice):
            return True
        return False


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
        self.__plociceZaSlaganje = plocice
        
    def uzmiPlocicu(self, izbor):
        plocica = None
        for p in self.__plociceZaSlaganje:
            if p.broj == izbor.broj:
                plocica = p
        return plocica


class PrikazIgre(object):
    
    def prikaziPocetakIgre(self):
        print("*" * 50)
        print("*" * 17 + " SLIDING PUZZLE " + "*" * 17)
        print("*" * 50)

    def unesiIgraca(self):
        while True:
            ime = input("Unesi ime: ")

            if ime.strip():
                print("*" * 50)
                return ime.strip()
            
    def prikaziPromjesanuPuzzle(self, slagalica):
        print(slagalica)
        return str(slagalica)
    
    def izaberiPlocicuZaSlaganje(self, plociceZaSlaganje):

        text = ">>> Izaberi pločicu:\n" + "\n".join("  " + str(i+1) + ")" + str(plocica) for i, plocica in enumerate(plociceZaSlaganje)) + '\nOdabir: '

        while True:
            izbor = input(text)
            if izbor.isdigit() and int(izbor) >= 1 and int(izbor) <= len(plociceZaSlaganje):
                return int(izbor) - 1
            
    def prikaziRezultat(self, ime, timer, br_poteza):
        rezultat = ime + '\t' + str(timer) + '\t' + str(br_poteza) + '\n'
        print(rezultat)
    

class Igra(object):

    def __init__(self, prikaz = None):
        self.__prikaz = PrikazIgre()
        self.__slagalica = Slagalica()
        self.__igrac = Igrac()
        self.__br_poteza = 0
        self.__timer = time.time()

    @property
    def prikaz(self): return self.__prikaz

    @property
    def slagalica(self): return self.__slagalica

    @property
    def igrac(self): return self.__igrac

    @property
    def br_poteza(self): return self.__br_poteza

    @br_poteza.setter
    def br_poteza(self, value): self.__br_poteza = value

    @property
    def timer(self): return self.__timer

    @timer.setter
    def timer(self, value): self.__timer = value

    def slaganjePuzzle(self):
        
        self.prikaz.prikaziPocetakIgre()    #0
        self.postaviPuzzle()    #1
        
        while self.slagalica.jeSlozena() == False:
            self.pomakniPlocice()   #2  (#2.3)
        
        self.bodovanje()    #3

    def postaviPuzzle(self):

        self.slagalica.promjesaj()  #1.1
        self.prikaz.prikaziPromjesanuPuzzle(self.slagalica) #1.2
        self.timer = time.time() #1.3
        print("Timer je pokrenut.\n")
        self.br_poteza = 0   #1.4

    def pomakniPlocice(self):

        self.igrac.uzmiPlociceZaSlaganje(self.slagalica.dajPlocice())   #2.1
        izbor = self.prikaz.izaberiPlocicuZaSlaganje(self.igrac.plociceZaSlaganje)

        plocica = self.igrac.uzmiPlocicu(self.igrac.plociceZaSlaganje[izbor])

        tp1 = 0
        tp2 = 0

        prazna = None
        for p in self.slagalica.plocice:
            if p.broj == '':
                prazna = p
                tp1 = p.trenutna_pozicija
                
        ind1 = self.slagalica.plocice.index(prazna)
        ind2 = self.slagalica.plocice.index(plocica)
        
        for p in self.slagalica.plocice:
            if p.broj == plocica.broj:
                tp2 = p.trenutna_pozicija
                
        self.slagalica.plocice[ind1] = Plocica(plocica.broj, tp1)
        self.slagalica.plocice[ind1].naziv = plocica.naziv

        self.slagalica.plocice[ind2] = Plocica('', tp2)
        self.slagalica.plocice[ind2].naziv = 'prazno'   #2.2

        self.br_poteza += 1     #2.3
            
        self.prikaz.prikaziPromjesanuPuzzle(self.slagalica) #2.4

    def bodovanje(self):
        self.zaustaviTimer()    #3.1   
        print("\nTimer je zaustavljen.\n")
        ime = self.unosIgraca() #3.2
        self.prikaz.prikaziRezultat(ime, self.timer, self.br_poteza)    #3.3

    def zaustaviTimer(self):
        sekunde = round(time.time()-self.timer, 2)
        if sekunde > 60:
            minute = int(sekunde//60)
            sek = int(sekunde) - (minute*60)
            self.timer = ''.join(str(minute) + '.' + str(sek) + ' min')
        else:
            self.timer = str(sekunde) + ' sek'
        return self.timer
    
    def unosIgraca(self):
        ime = self.prikaz.unesiIgraca()
        return ime


pi = PrikazIgre()
i = Igra()
i.slaganjePuzzle()
