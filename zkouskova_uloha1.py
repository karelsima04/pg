# zadání zní:
# napište funkci filtruj_cisla(typ, cisla), která přijme dva parametry, těmi jsou:
# typ - řetězec, který může nabývat hodnot "kladna", "zaporna", "suda", "licha"
# cisla - seznam cisel
# funkce vrátí nový seznam obsahující pouze ta čísla z parametru cisla, která odpovídají zadanému typu


def filtruj_cisla(typ, cisla):
    vysledek = []
    
    if typ == "kladna":
        for c in cisla:
            if c > 0:
                vysledek.append(c)

    if typ == "suda":
        for c in cisla:
            if c %2 == 0:
                vysledek.append(c)

    if typ == "zaporna":
        for c in cisla:
            if c < 0:
                vysledek.append(c)

    if typ == "licha":
        for c in cisla:
            if c %2 != 0:
                vysledek.append(c)


    return vysledek


if __name__ == "__main__":
    print(filtruj_cisla("kladna", [1, -2, 0, 5, -3]))       # [1, 5]
    print(filtruj_cisla("suda", [1, 2, 4, 4, 5]))           # [2, 4]
    print(filtruj_cisla("zaporna", [1, -2, 0, 5, -3]))      # [-2, -3]
    print(filtruj_cisla("licha", [1, 2, 3, 4, 5]))          # [1, 3, 5]
    #neexistující typ
    print(filtruj_cisla("xxx", [1, 2, 3]))                  # []