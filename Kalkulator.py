import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')
calc_open = True

def dodawanie(*args):
    return sum(args)

def odejmowanie(a, b):
    return a - b

def mnozenie(*args):
    wynik = 1
    for arg in args:
        wynik *= arg
    return wynik

def dzielenie(a, b):
    return a / b


def pobierz_liczby(ilosc=2):
    liczby = []
    for i in range(ilosc):
        while True:
            try:
                liczba = float(input(f"Podaj składnik {i+1}: "))
                liczby.append(liczba)
                break
            except ValueError:
                print("Podana wartość nie jest liczbą. Spróbuj ponownie.")
    return liczby

def Kalkulator():
    print(f"Podaj typ działania matematycznego posługując się cyfrą według schematu: \n 1 - dodawanie, \n 2 - odejmowanie, \n 3 - mnożenie, \n 4 - dzielenie")
    dzialanie = input()
        
    if dzialanie == '1':
        liczby = pobierz_liczby(int(input("Ile liczb chcesz dodać? ")))
        logging.info(f"Dodaję {liczby}")
        wynik = dodawanie(*liczby)
    elif dzialanie == '2':
        liczby = pobierz_liczby(2)
        logging.info(f"Odejmuję {liczby[0]} i {liczby[1]}")
        wynik = odejmowanie(liczby[0], liczby[1])
    elif dzialanie == '3':
        liczby = pobierz_liczby(int(input("Ile liczb chcesz pomnożyć? ")))
        logging.info(f"Mnożę {liczby}")
        wynik = mnozenie(*liczby)
    elif dzialanie == '4':
        liczby = pobierz_liczby(2)
        if liczby[1] ==0:
            print("Nie można dzielić przez zero!")
            return
        logging.info(f"Dzielę {liczby[0]} przez {liczby[1]}")
        wynik = dzielenie(liczby[0], liczby[1])
    else:
        print("Nieprawidłowy wybór.")
        return
    
    print(f"Wynik to {wynik}")
while calc_open:
    Kalkulator()
    decyzja = input("Jeśli chcesz kontynuować, wciśnij \"t\" ")
    if decyzja == "t":
        calc_open = True
    else:
        calc_open = False
        print("Zamykam kalkulator")

