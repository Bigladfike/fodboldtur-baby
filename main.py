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

def find_lignende_navn(soegt_navn):
    for navn in fodboldtur.keys():
        if navn.lower() == soegt_navn.lower():
            return navn
    return None

def opret_bruger():
    navn = input("Indtast navn på nyt medlem (for- og efternavn):")
    navn_dele = navn.split()
    if len(navn_dele) < 2:
        print("Fejl: Indtast både for- og efternavn.")
        menu()
        return
    navn = ''.join(word.capitalize() for word in navn_dele)
    if navn in fodboldtur:
        print(f"Fejl: {navn} eksisterer allerede!")
    else:
        fodboldtur[navn] = []
        print(f"{navn} er blevet oprettet")
    menu()


def registrer_betaling():
    navn = input("Indtast navn på medlem: ")
    navne_dele = navn.split()
    navn = ' '.join(word.capitalize() for word in navne_dele)

    if navn not in fodboldtur:
        lignende = find_lignende_navn(navn)
        if lignende:
            print(f"Fejl: Navnet findes ikke. Mente du '{lignende}'?")
        else:
            print("Fejl: Medlemmet findes ikke. Opret medlem først.")
        menu()
        return

    while True:
        try:
            beloeb = int(input("Indtast indbetalt beløb (heltal): "))
            if beloeb <= 0:
                print("Fejl: Beløbet skal være positivt!")
                continue
            if beloeb > 4500:
                print("Fejl: Beløbet kan ikke overstige 4500 kr!")
                continue
            current_total = sum(fodboldtur[navn])
            if current_total + beloeb > 4500:
                print(f"Fejl: Total vil overstige 4500 kr. Maksimal indbetaling nu: {4500 - current_total} kr.")
                continue
            break
        except ValueError:
            print("Fejl: Indtast venligst et heltal!")
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
    print("5: Opret ny bruger")
    valg = input("Indtast dit valg: ")
    if valg == '1':
        printliste()
    elif valg == '2':
        afslut()
    elif valg == '3':
        registrer_betaling()
    elif valg == '4':
        top3_manglende()
    elif valg == '5':
        opret_bruger()
    else:
        print("uglydigt valg nig- i mean !!")
        menu()

try:
    with open(filename, 'rb') as infile:
        fodboldtur = pickle.load(infile)
        for navn in fodboldtur:
            if isinstance(fodboldtur[navn], (int, float)):
                fodboldtur[navn] = [fodboldtur[navn]]
except FileNotFoundError:
    fodboldtur = {}
menu()
