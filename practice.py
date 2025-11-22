
size = input("Jakou velikost pizzy si přejete S - small, M - medium, L - large?\n")
bill = 100

if size == "S":
    feferonky = input("Přejete si na pizzu feferonky? ANO nebo NE?\n")
    if feferonky == "ANO":
        bill = bill + 20
    elif feferonky == "NE":
        bill = bill
    else:
        print("Neplatná volba.")

elif size == "M":
    feferonky = input("Přejete si na pizzu feferonky? ANO nebo NE?\n")
    if feferonky == "ANO":
        bill = bill + 70
    elif feferonky == "NE":
        bill = bill + 50
    else:
        print("Neplatná volba.")
    sýr = input("Přejete si na pizzu více sýru? ANO nebo NE?\n")
    if sýr == "ANO":
        bill = bill + 70
    elif sýr == "NE":
        bill = bill + 50
    else:









