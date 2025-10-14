def cislo_text(cislo):
    cislo = int(cislo)

    jednotky = ["nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět"]
    nactiny = ["deset", "jedenáct", "dvanáct", "třináct", "čtrnáct", "patnáct", "šestnáct", "sedmnáct", "osmnáct", "devatenáct"]
    desitky = ["", "", "dvacet", "třicet", "čtyřicet", "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"]

    if cislo < 10:
        return jednotky[cislo]
    elif cislo < 20:
        return nactiny[cislo - 10]
    elif cislo < 100:
        d = cislo // 10
        j = cislo % 10
        if j == 0:
            return desitky[d]
        else:
            return desitky[d] + " " + jednotky[j]
    elif cislo == 100:
        return "sto"
    else:
        return "mimo rozsah"


if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)

