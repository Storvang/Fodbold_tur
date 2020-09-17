import pickle, time
filename = 'betalinger.pk'
Savedfilename= 'betalinger2.pk'

fodboldtur ={}

dict = {
    'Hans Hansen': 0,
    'Klaus Klausen': 0,
    'Ole Olsen': 0,
    'Bent Bentsen': 0,
    'Peter Petersen': 0,
    'Anders Andersen': 0,
    'Jens Jensen': 0,
    'Ib Ibsen': 0
    }


def afslut():
    outfile = open(filename, 'wb')
    pickle.dump(dict, outfile)
    outfile.close()
    print("Programmet er afsluttet!")
    quit()



def payMoney():
    name = input('Navn: ')
    amount_string = input('Beløb: ')
    try:
        amount = int(amount_string)
    except ValueError:
        payMoney()
    try:
        dict[name] = int(dict[name])
        dict[name] += amount
    except:
        payMoney()


    dict[name] += amount

    print('Du har nu betalt ' + str(dict[name]) + ' kr.')

    time.sleep(2)
    menu()

def moneyPaid():
    name = input('Navn: ')

    print(name + ' har betalt ' + str(dict[name]) + ' kr.')
    time.sleep(2)
    menu()

def printliste():
    for item in dict.items():
        print(item)
    time.sleep(2)
    menu()

def menu():
    print("MENU")
    print("1: Print liste")
    print("2: Hvor meget har jeg betalt?")
    print("3: Betal")
    print("4: Afslut program")
    valg = input("Indtast dit valg: ")
    if (valg == '1'):
        printliste()
    if (valg == '2'):
        moneyPaid()
    if (valg == '3'):
        payMoney()
    if (valg == '4'):
        afslut()
    else:
        print('Ugyldig indtastning')
        time.sleep(1)
        menu()




infile = open(filename,'rb')
dict = pickle.load(infile)
infile.close()
menu()
