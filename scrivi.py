import os


#print ("il percorso assoluto del file è: " , percorso)


controllo_titolo = 1
while controllo_titolo :
    titolo = input("Inserisci il titolo dell'ASCII Art: ")
    
    titolotxt = titolo + ".txt"
    percorso = os.path.abspath(titolotxt) 
    print (percorso)
    if os.path.isfile(percorso):
        print("File già esistente")
    else :
        controllo_titolo = 0

Contenuto = input("Inserisci il testo: ")


relpath = "database/" + titolotxt
f = open(relpath, "x")
f.write(Contenuto)
f.close()

"""#open and read the file after the appending:
f = open(titolo, "r")
print(f.read())"""



