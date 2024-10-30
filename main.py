nomefile = "prova"

def read_file():
    print("Leggendo il file..")
    try:
        f = open(nomefile, "r")
        for line in f.readlines():
            print(line)
        f.close()
    except Exception:
        print("Could not read to file")


parole= ["XI JINGPING", "FABIO", "FAVIJ", "GRANCHIO", "ROTOLONE"]
print(" Le parole accettate sono: " + str(parole))
scelta = input("Inserisci una parola qualsiasi: ")
scelta = str.upper(scelta)

nomefile = scelta + ".txt"

read_file()

input()