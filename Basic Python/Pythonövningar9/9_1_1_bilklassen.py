class Bil:
    def __init__(self, färg:str, märke:str) -> None:
        self._färg = färg.lower()
        self._märke = märke.lower().capitalize()
        self._hastighet = 0
    
    @property
    def färg(self):
        return self._färg
    
    @property
    def märke(self):
        return self._märke

    @property
    def hastighet(self):
        return self._hastighet
    
    @hastighet.setter
    def hastighet(self,value:int):
        self._hastighet = value

    def accelerera(self) -> None:
        self.hastighet += 1
        print('Bilen kör ', self.hastighet)
    
    def bromsa(self) -> None:
        if self.hastighet > 0:
            self.hastighet -= 1
            print('Bilen kör ',self.hastighet)
        else:
            print('Bilen står redan stilla.')
    
    def info(self) -> None:
        print(f'Det här är en {self.färg} {self.märke}.')
    

class Elbil(Bil):
    def __init__(self, färg:str, märke:str) -> None:
        super().__init__(färg, märke)
        self._batterikapacitet = 100

    @property
    def batterikapaciet(self):
        return self._batterikapacitet
    
    def accelerera(self) -> None:
        if self._batterikapacitet > 0:
            self._batterikapacitet -= 5
            return super().accelerera()
        else:
            print('Slut på batteri.')
    
    def info(self) -> None:
        print(f'Det här är en {self.färg} {self.märke} med {self.batterikapacitet}% batterikapacitet kvar.')

class Motor:
    def __init__(self,typ:str) -> None:
        self._typ = typ
        self._effekt = '150hk'
    
    @property
    def typ(self):
        return self._typ
    
    @property
    def effekt(self):
        return self._effekt

motor = 'El'
bilen = Elbil('blå','volvo')
bil2 = Bil('GRÖN','TEsla')
bilen.info()
bil2.info()

# while True:
#     opt = input('Gasa, bromsa, info, eller sluta: ').lower()
#     if opt == 'gasa':
#         bilen.accelerera()
#     elif opt == 'bromsa':
#         bilen.bromsa()
#     elif opt == 'info':
#         bilen.info()
#     elif opt == 'sluta':
#         quit()