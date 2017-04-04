pocet_radku = int(input('Zadej pocet radku: '))
for cislo_radku in range(pocet_radku):
    '''
    if cislo_radku == 0:
        print('první řádek')
    else:
        print('není první')
    '''
    print('prvni radek') if cislo_radku==0 else print('neni prvni')