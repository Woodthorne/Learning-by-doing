class Kalkylator:
    def __init__(self) -> None:
        self._aktuellaVärdet = 0
    
    def addera(self,tal:int):
        self._aktuellaVärdet += tal
        return self._aktuellaVärdet
    
    def subtrahera(self,tal:int):
        self._aktuellaVärdet -= tal
        return self._aktuellaVärdet
    
    def multiplicera(self,tal:int):
        self._aktuellaVärdet *= tal
        return self._aktuellaVärdet
    
    def dividera(self,tal:int):
        self._aktuellaVärdet /= tal
        return self._aktuellaVärdet
