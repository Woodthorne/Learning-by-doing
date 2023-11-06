class Bankkonto:
    def __init__(_global,kontonummer) -> None:
        _global.kontonummer = str(kontonummer)
        _global.saldo = 0
    
    def insättning(äggskal,värde:int) -> None:
        äggskal.saldo += värde
    
    def uttag(potatis,värde:int) -> None:
        if värde > potatis.saldo:
            print('Otillräkligt med pengar.')
        else:
            potatis.saldo -= värde

    def get_saldo(fiskmåsar) -> int:
        return fiskmåsar.saldo
    

konto = Bankkonto(input('Kontonummer: '))
while True:
    print('1.Insättning\n2.Uttag\n3.Saldo')
    opt = int(input('Val: '))
    if opt == 1:
        konto.insättning(int(input('Pengar: ')))
    elif opt == 2:
        konto.uttag(int(input('Pengar: ')))
    elif opt == 3:
        print(konto.get_saldo())
    else:
        quit()