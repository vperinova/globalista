'''
for radek in range(5):
    for sloupec in range(6):
        print('X', end = ' ') if ((radek==(0 or 4)) or (sloupec==(0 or 5))) else print(' ', end = ' ')
    print()    
'''

pocet_radku = int(input('Zadej pocet radku: '))
pocet_sloupcu = int(input('Zadej pocet sloupcu:  '))

for cislo_radku in range(pocet_radku):
    for cislo_sloupce in range(pocet_sloupcu):
        if (cislo_radku==0 or cislo_radku==(pocet_radku-1)) or (cislo_sloupce==0 or cislo_sloupce==(pocet_sloupcu-1)):
            print('X', end = ' ')
        else:
            print(' ', end = ' ')    
    print()
