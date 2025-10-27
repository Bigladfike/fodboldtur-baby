import pickle

filename = 'betalinger.pk'
fodboldtur = {}

def afslut():
    with open(filename, 'wb') as outfile:
        pickle.dump(fodboldtur, outfile)
    print("Programmet er afsluttet!")

def printliste():
    print("\n=== OVERSIGT OVER INDBETALINGER ===")
    for navn, beloeb in fodboldtur.items():
        rest = 4500 - sum(beloeb)
        print(f"{navn}: {sum(beloeb)} kr. indbetalt – ", end="")
        if rest > 0:
            print(f"mangler {rest} kr.")
        else:
            print("har betalt det fulde beløb!")
    print("====================================\n")
    menu()



def registrer_betaling():
    navn = input("Indtast navn på medlem: ")
    beloeb = float(input("Indtast indbetalt beløb: "))
    if navn not in fodboldtur:
        fodboldtur[navn] = []
    fodboldtur[navn].append(beloeb)
    print(f"{beloeb} kr. registreret for {navn}.")
    menu()

def top3_manglende():
    print("\n=== TOP 3 DER MANGLER AT BETALE MEST ===")
    rest_dict = {}
    for navn, beloeb in fodboldtur.items():
        rest = 4500 - sum(beloeb)
        if rest > 0:
            rest_dict[navn] = rest
    sorteret = sorted(rest_dict.items(), key=lambda x: x[1], reverse=True)
    for navn, rest in sorteret[:3]:
        print(f"{navn} mangler {rest} kr.")
    print("=========================================\n")
    menu()



def menu():
    print("MENU")
    print("1: Print liste")
    print("2: Afslut program")
    print("3: Registrer betaling")
    print("4: Top 3 der mangler mest")
    valg = input("Indtast dit valg: ")
    if valg == '1':
        printliste()
    elif valg == '2':
        afslut()
    elif valg == '3':
        registrer_betaling()
    elif valg == '4':
        top3_manglende()

try:
    with open(filename, 'rb') as infile:
        fodboldtur = pickle.load(infile)
        for navn in fodboldtur:
            if isinstance(fodboldtur[navn], (int, float)):
                fodboldtur[navn] = [fodboldtur[navn]]
except FileNotFoundError:
    fodboldtur = {}
menu()
