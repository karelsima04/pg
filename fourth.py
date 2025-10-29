def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    typ = figurka.get("typ", "").lower()
    r0, c0 = figurka.get("pozice", (None, None))
    r1, c1 = cilova_pozice

    if not (1 <= r1 <= 8 and 1 <= c1 <= 8):
        return False

    if cilova_pozice in obsazene_pozice:
        return False

    dr = r1 - r0
    dc = c1 - c0

    def je_cesta_volna():
        step_r = (dr > 0) - (dr < 0)
        step_c = (dc > 0) - (dc < 0)
        r, c = r0 + step_r, c0 + step_c
        while (r, c) != (r1, c1):
            if (r, c) in obsazene_pozice:
                return False
            r += step_r
            c += step_c
        return True

    if typ == "pěšec" or typ == "pesec":
        if dr == 1 and dc == 0:
            return True
        if r0 == 2 and dr == 2 and dc == 0:
            if (r0 + 1, c0) in obsazene_pozice:
                return False
            return True
        return False

    elif typ == "jezdec":
        return (abs(dr), abs(dc)) in {(1, 2), (2, 1)}

    elif typ == "věž" or typ == "vez":
        if dr == 0 or dc == 0:
            return je_cesta_volna()
        return False

    elif typ == "střelec" or typ == "strelec":
        if abs(dr) == abs(dc):
            return je_cesta_volna()
        return False

    elif typ == "dáma" or typ == "dama":
        if dr == 0 or dc == 0 or abs(dr) == abs(dc):
            return je_cesta_volna()
        return False

    elif typ == "král" or typ == "kral":
        return max(abs(dr), abs(dc)) == 1

    return False


if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))
    print(je_tah_mozny(pesec, (5, 2), obsazene_pozice))
    print(je_tah_mozny(jezdec, (4, 5), obsazene_pozice))
    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))
    print(je_tah_mozny(vez, (8, 1), obsazene_pozice))
    print(je_tah_mozny(vez, (8, 7), obsazene_pozice))
    print(je_tah_mozny(vez, (8, 8), obsazene_pozice))
    print(je_tah_mozny(strelec, (3, 0), obsazene_pozice))
    print(je_tah_mozny(strelec, (3, 6), obsazene_pozice))
    print(je_tah_mozny(dama, (5, 6), obsazene_pozice))
    print(je_tah_mozny(kral, (2, 5), obsazene_pozice))
