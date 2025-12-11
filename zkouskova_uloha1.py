# zadání zní:
# napište funkci filtruj_cisla(typ, cisla), která přijme dva parametry, těmi jsou:
# typ - řetězec, který může nabývat hodnot "kladna", "zaporna", "suda", "licha"
# cisla - seznam cisel
# funkce vrátí nový seznam obsahující pouze ta čísla z parametru cisla, která odpovídají zadanému typu



def filtruj_cisla(typ, cisla):
    vysledek = []
    # moje řešení tady

    


    return vysledek


if __name__ == "__main__":
    print(filtruj_cisla("kladna", [1, -2, 0, 5, -3]))       # [1, 5]
    print(filtruj_cisla("suda", [1, 2, 4, 4, 5]))           # [1, 5]
    print(filtruj_cisla("zaporna", [1, -2, 0, 5, -3]))      # [1, 5]
    print(filtruj_cisla("licha", [1, 2, 3, 4, 5]))          # [1, 5]
    #neexistující typ
    print(filtruj_cisla("xxx", [1, 2, 3]))                  # []