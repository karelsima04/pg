def je_prvocislo(cislo):
    if cislo <= 1:
        return False
    if cislo == 2:
        return True
    if cislo % 2 == 0:
        return False
    i = 3
    while i * i <= cislo:
        if cislo % i == 0:
            return False
        i += 2
    return True

def vrat_prvocisla(maximum):
    maximum = int(maximum)
    vysledek = []
    for n in range(2, maximum + 1):
        if je_prvocislo(n):
            vysledek.append(n)
    return vysledek

if __name__ == "__main__":
    cislo = input("Zadej maximum: ")
    prvocisla = vrat_prvocisla(cislo)
    print(prvocisla)
