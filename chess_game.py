class Pionek:
    def __init__(self, pozycja:str, zbity:bool, kolor:str):
        self.pozycja = pozycja
        self.zbity = zbity
        self.kolor = kolor

    def ruch(self, nowa_pozycja: str):
        if nowa_pozycja not in plansza:
            print("Niepoprawna pozycja")
            return False

        if plansza[nowa_pozycja] is not None:
            if plansza[nowa_pozycja].kolor == self.kolor:
                print("Na tym polu stoi twój pionek")
                return False
            else:
                print("Zbicie")
                plansza[nowa_pozycja].zbity = True


        plansza[self.pozycja] = None
        plansza[nowa_pozycja] = self
        self.pozycja = nowa_pozycja

        return True

    def czy_wolna_droga(self, nowa_pozycja):
        stara_kolumna = ord(self.pozycja[0]) - ord('a')
        stary_wiersz = int(self.pozycja[1])

        nowa_kolumna = ord(nowa_pozycja[0]) - ord('a')
        nowy_wiersz = int(nowa_pozycja[1])

        krok_kolumny = 0
        krok_wiersza = 0

        #ustalenie kierunku w ktorym sie porusza figura
        if nowa_kolumna > stara_kolumna:
            krok_kolumny += 1
        elif nowa_kolumna < stara_kolumna:
            krok_kolumny -= 1
        else:
            krok_kolumny = 0

        if nowy_wiersz > stary_wiersz:
            krok_wiersza += 1
        elif nowy_wiersz < stary_wiersz:
            krok_wiersza -= 1
        else:
            krok_wiersza = 0

        # ustawienie pole do sprawdzenia jako kolejne pole, na ktorym oryginalnie nie stoi pionek
        aktualna_kolumna = stara_kolumna + krok_kolumny
        aktualny_wiersz = stary_wiersz + krok_wiersza

        pole = chr(aktualna_kolumna + ord('a')) + str(aktualny_wiersz)

        while pole != nowa_pozycja:
            if plansza[pole] is not None:
                return False
            else:
                aktualna_kolumna += krok_kolumny
                aktualny_wiersz += krok_wiersza
                pole = chr(aktualna_kolumna + ord('a')) + str(aktualny_wiersz)
        return True

    def zbicie(self, nowa_pozycja):

        if plansza[nowa_pozycja] is not None and plansza[nowa_pozycja].kolor != self.kolor:
            zbity_pionek = plansza[nowa_pozycja]
            zbity_pionek.zbity = True

            plansza[self.pozycja] = None
            plansza[nowa_pozycja] = self
            self.pozycja = nowa_pozycja


class Pion(Pionek):
    def __init__(self, pozycja:str, zbity:bool, kolor:str):
        super().__init__(pozycja, zbity, kolor)

    def __str__(self) -> str: # zamiast pokazywanie adres obiektu w pamieci, ladnie pojawi sie na planszy p lub P
        if self.kolor == 'bialy':
            return 'p'
        else:
            return "P"

    def ruch(self, nowa_pozycja):
        stara_kolumna = self.pozycja[0]
        stary_wiersz = int(self.pozycja[1])

        nowa_kolumna = nowa_pozycja[0]
        nowy_wiersz = int(nowa_pozycja[1])

        if self.kolor == 'bialy':
            if stary_wiersz == 2 and nowy_wiersz == stary_wiersz + 2 and nowa_kolumna == stara_kolumna: # pionek, który sie nie ruszał może iść o dwa pola do przodu
                return super().ruch(nowa_pozycja)

            elif nowa_kolumna == stara_kolumna and nowy_wiersz == stary_wiersz + 1: # warunek poruszania sie piona
                return super().ruch(nowa_pozycja)

            else:
                print("niedozwolony ruch")
                return False
        else:
            if stary_wiersz == 7 and nowy_wiersz == stary_wiersz - 2 and nowa_kolumna == stara_kolumna:  # pionek, który sie nie ruszał może iść o dwa pola do przodu
                return super().ruch(nowa_pozycja)
            elif nowa_kolumna == stara_kolumna and nowy_wiersz == stary_wiersz - 1: # warunek poruszania sie piona
                return super().ruch(nowa_pozycja)
            else:
                print("niedozwolony ruch")
                return False


class Skoczek(Pionek):
    def __init__(self, pozycja:str, zbity:bool, kolor:str):
        super().__init__(pozycja, zbity, kolor)

    def ruch(self,nowa_pozycja):
        stara_kolumna = ord(self.pozycja[0]) - ord('a') # zamieniam kolumny na liczby, np c - a = 3 - 1 = 2
        stary_wiersz = int(self.pozycja[1])

        nowa_kolumna = ord(nowa_pozycja[0]) - ord('a')
        nowy_wiersz = int(nowa_pozycja[1])

        roznica_kolumn = abs(nowa_kolumna - stara_kolumna)
        roznica_wierszy = abs(nowy_wiersz - stary_wiersz)
        if (roznica_wierszy == 2 and roznica_kolumn == 1) or (roznica_wierszy == 1 or roznica_kolumn == 2):
            return super().ruch(nowa_pozycja)
        else:
            print('niedozwolony ruch')
            return False


    def __str__(self) -> str:
        if self.kolor == 'bialy':
            return 's'
        else:
            return "S"



class Goniec(Pionek):
    def __init__(self, pozycja:str, zbity:bool, kolor:str):
        super().__init__(pozycja, zbity, kolor)

    def ruch(self, nowa_pozycja):
        stara_kolumna = ord(self.pozycja[0]) - ord('a') # np c - a = 3 - 1 = 2
        stary_wiersz = int(self.pozycja[1])

        nowa_kolumna = ord(nowa_pozycja[0]) - ord('a')
        nowy_wiersz = int(nowa_pozycja[1])

        roznica_kolumn = abs(stara_kolumna - nowa_kolumna)
        roznica_wierszy = abs(nowy_wiersz - stary_wiersz)

        if roznica_kolumn == roznica_wierszy:
            if self.czy_wolna_droga(nowa_pozycja):
                return super().ruch(nowa_pozycja)
            else:
                print("niedozwolony ruch")
                return False
        else:
            print('niedozwolony ruch')
            return False

    def __str__(self) -> str:
        if self.kolor == 'bialy':
            return 'g'
        else:
            return "G"



class Wieza(Pionek):
    def __init__(self, pozycja:str, zbity:bool, kolor:str):
        super().__init__(pozycja, zbity, kolor)

    def ruch(self, nowa_pozycja):
        stara_kolumna = ord(self.pozycja[0]) - ord('a')
        stary_wiersz = int(self.pozycja[1])

        nowa_kolumna = ord(nowa_pozycja[0]) - ord('a')
        nowy_wiersz = int(nowa_pozycja[1])

        roznica_kolumn = abs(stara_kolumna - nowa_kolumna)
        roznica_wierszy = abs(nowy_wiersz - stary_wiersz)

        if (roznica_wierszy == 0 and roznica_kolumn > 0) or (roznica_wierszy > 0 and roznica_kolumn == 0):
            if self.czy_wolna_droga(nowa_pozycja):
                return super().ruch(nowa_pozycja)
            else:
                print("niedozwolony ruch")
                return False
        else:
            print('niedozwolony ruch')
            return False

    def __str__(self) -> str:
        if self.kolor == 'bialy':
            return 'w'
        else:
            return "W"

class Hetman(Pionek):
    def __init__(self, pozycja:str, zbity:bool, kolor:str):
        super().__init__(pozycja, zbity, kolor)

    def ruch(self, nowa_pozycja):
        stara_kolumna = ord(self.pozycja[0]) - ord('a')
        stary_wiersz = int(self.pozycja[1])

        nowa_kolumna = ord(nowa_pozycja[0]) - ord('a')
        nowy_wiersz = int(nowa_pozycja[1])

        roznica_kolumn = abs(stara_kolumna - nowa_kolumna)
        roznica_wierszy = abs(nowy_wiersz - stary_wiersz)

        if (roznica_wierszy == 0 and roznica_kolumn > 0) or (roznica_wierszy > 0 and roznica_kolumn == 0) or (roznica_wierszy == roznica_kolumn): # polaczenie gonca i wiezy
            if self.czy_wolna_droga(nowa_pozycja):
                return super().ruch(nowa_pozycja)
            else:
                print("niedozwolony ruch")
                return False

        else:
            print('niedozwolony ruch')
            return False

    def __str__(self) -> str:
        if self.kolor == 'bialy':
            return 'h'
        else:
            return "H"

class Krol(Pionek):
    def __init__(self, pozycja:str, zbity:bool, kolor:str):
        super().__init__(pozycja, zbity, kolor)

    def ruch(self, nowa_pozycja):
        stara_kolumna = ord(self.pozycja[0]) - ord('a')
        stary_wiersz = int(self.pozycja[1])

        nowa_kolumna = ord(nowa_pozycja[0]) - ord('a')
        nowy_wiersz = int(nowa_pozycja[1])

        roznica_kolumn = abs(stara_kolumna - nowa_kolumna)
        roznica_wierszy = abs(nowy_wiersz - stary_wiersz)
        if (roznica_wierszy == 1 and roznica_kolumn == 1) or (roznica_wierszy == 1 and roznica_kolumn == 0) or (roznica_wierszy == 0 and  roznica_kolumn == 1):
            return super().ruch(nowa_pozycja)
        else:
            print('niedozwolony ruch')
            return False


    def __str__(self) -> str:
        if self.kolor == 'bialy':
            return 'k'
        else:
            return "K"


########### BIAŁE ##########

#piony
p1: Pion = Pion('a2', False, 'bialy')
p2: Pion = Pion('b2', False, 'bialy')
p3: Pion = Pion('c2', False, 'bialy')
p4: Pion = Pion('d2', False, 'bialy')
p5: Pion = Pion('e2', False, 'bialy')
p6: Pion = Pion('f2', False, 'bialy')
p7: Pion = Pion('g2', False, 'bialy')
p8: Pion = Pion('h2', False, 'bialy')

#skoczek
s1: Skoczek = Skoczek('b1', False, 'bialy')
s2: Skoczek = Skoczek('g1', False, 'bialy')

#goniec
g1: Goniec = Goniec('c1',False, 'bialy')
g2: Goniec = Goniec('f1',False, 'bialy')

#wieza
w1: Wieza = Wieza('a1', False, 'bialy')
w2: Wieza = Wieza('h1', False, 'bialy')

#hetman
h1: Hetman = Hetman('d1', False, 'bialy')

#krol
k1: Krol = Krol('e1',False, 'bialy')


########### CZARNE ##########
P1: Pion = Pion('a7', False,'czarny')
P2: Pion = Pion('b7', False,'czarny')
P3: Pion = Pion('c7', False,'czarny')
P4: Pion = Pion('d7', False,'czarny')
P5: Pion = Pion('e7', False,'czarny')
P6: Pion = Pion('f7', False,'czarny')
P7: Pion = Pion('g7', False,'czarny')
P8: Pion = Pion('h7', False,'czarny')


#skoczek
S1: Skoczek = Skoczek('b8', False,'czarny')
S2: Skoczek = Skoczek('g8', False,'czarny')

#goniec
G1: Goniec = Goniec('c8',False,'czarny')
G2: Goniec = Goniec('f8',False,'czarny')

#wieza
W1: Wieza = Wieza('a8', False,'czarny')
W2: Wieza = Wieza('h8', False,'czarny')

#hetman
H1: Hetman = Hetman('d8', False,'czarny')

#krol
K1: Krol = Krol('e8',False,'czarny')


######### PLANSZA ############
kolumny = "abcdefgh"
wiersze = "12345678"

plansza = {}

for i in kolumny:
    for j in wiersze:
        plansza[i+j] = None


# poczatkowe ustawienie
plansza['a1'] = w1 #przypisanie wartosci a1 na planszy do wiezy
plansza['a2'] = p1
plansza['b1'] = s1
plansza['b2'] = p2
plansza['c1'] = g1
plansza['c2'] = p3
plansza['d1'] = h1
plansza['d2'] = p4
plansza['e1'] = k1
plansza['e2'] = p5
plansza['f1'] = g2
plansza['f2'] = p6
plansza['g1'] = s2
plansza['g2'] = p7
plansza['h1'] = w2
plansza['h2'] = p8

plansza['a8'] = W1
plansza['a7'] = P1
plansza['b8'] = S1
plansza['b7'] = P2
plansza['c8'] = G1
plansza['c7'] = P3
plansza['d8'] = H1
plansza['d7'] = P4
plansza['e8'] = K1
plansza['e7'] = P5
plansza['f8'] = G2
plansza['f7'] = P6
plansza['g8'] = S2
plansza['g7'] = P7
plansza['h8'] = W2
plansza['h7'] = P8

krok = 0

############# FAKTYCZNA GRA #################
while True:
    # wyswietlanie planszy

    #poczatkowa wartosc planszy, ktora sie pozniej bedzie zmieniac
    def wyswietl_plansze():


        for i in range (8,0,-1):
            licznik = 0
            for j in range (1,9):

                kolumna = chr(ord('a') + licznik)

                pole = chr(ord(kolumna)) + str(i)

                if plansza[pole] is None:
                    print(". ", end='')
                else:
                    print(plansza[pole],"",end='')

                licznik += 1

            print("\n")


    wyswietl_plansze() # wyswietlenie planszy

    # musimy ustalić, kto gra? bialy czy czarny
    # parzysty - biale, nieparzyste - czarne


    if krok % 2 == 0:
        print("Teraz gra BIAŁY |||||||||||||||||| JEŚLI CHCESZ ZAKOŃCZYĆ GRĘ, WPISZ 'END'")
        pole_startowe = input("Podaj pole startowe pionka (tego, którego chcesz ruszyć): ")

        if pole_startowe == 'END':
            print("Koniec gry")
            break

        obiekt = plansza[pole_startowe]

        while obiekt is None or obiekt.kolor != 'bialy':
            print("Możesz grać jedynie białymi pionkami!")
            pole_startowe = input("Podaj pole startowe pionka (tego, którego chcesz ruszyć): ")
            obiekt = plansza[pole_startowe]


        pole_docelowe = input("Podaj pole docelowe wybranego pionka: ")


        wynik = obiekt.ruch(pole_docelowe) # nawet przypisanie zmiennej spowoduje wykonanie sie metody

        if wynik:
            krok += 1

    else:
        print("Teraz gra CZARNY |||||||||||||||||| JEŚLI CHCESZ ZAKOŃCZYĆ GRĘ, WPISZ 'END'")
        pole_startowe = input("Podaj pole startowe pionka (tego, którego chcesz ruszyć): ")

        if pole_startowe == 'END':
            print("Koniec gry")
            break


        obiekt = plansza[pole_startowe]

        while obiekt is None or obiekt.kolor != 'czarny':
            print("Możesz grać jedynie czarnymi pionkami!")
            pole_startowe = input("Podaj pole startowe pionka (tego, którego chcesz ruszyć): ")
            obiekt = plansza[pole_startowe]

        pole_docelowe = input("Podaj pole docelowe wybranego pionka: ")


        wynik = obiekt.ruch(pole_docelowe) # nawet przypisanie zmiennej spowoduje wykonanie sie metody

        if wynik:
            krok += 1