class TV:
    def __init__(self,märke,modell) -> None:
        self._märke = märke
        self._modell = modell
        self.__kanal = 1
        self.__volym = 10
    
    def ändra_kanal(self,kanal:int) -> None:
        self.__kanal = kanal
    
    def justera_volym(self,volym:int) -> None:
        self.__volym = volym
    
    def hämta_märke(self) -> str:
        return self._märke
    
    def hämta_modell(self) -> str:
        return self._modell

    def hämta_kanal(self) -> str:
        return self.__kanal

    def hämta_volym(self) -> int:
        return self.__volym

tv = TV('philip','33T')
tv.__volym = 15
print(tv.__volym)
print(tv.hämta_volym())