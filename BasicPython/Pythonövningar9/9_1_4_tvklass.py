# Pogram is functional, but limited.

class TV:
    def __init__(self) -> None:
        self._märke = 'Philips'
        self._modell = 'TK23'
        self._infraröd_frekvens = 320
        self._påslagen = False
        self._kanal = 1
        self._ljud_av = False
        self._volym = 1
    
    @property
    def påslagen(self) -> bool:
        return self._påslagen
    
    @property
    def kanal(self) -> int:
        return self._kanal
    
    @kanal.setter
    def kanal(self,value:int) -> None:
        self._kanal = value
    
    def öka_volymen(self, signal):
        if signal == self._infraröd_frekvens and self._påslagen:
            if self._volym < 10:
                self._volym += 1
                print('Volym',self._volym)
            else:
                print('Volymen är redan 10')
    
    def minska_volymen(self, signal):
        if signal == self._infraröd_frekvens and self._påslagen:
            if self._volym > 0:
                self._volym -= 1
                print('Volym', self._volym)
            else:
                print('Volymen är redan 0.')
    
    def stäng_av_ljud(self, signal):
        if signal == self._infraröd_frekvens and self._påslagen:
            if self._ljud_av:
                self._ljud_av = False
            else:
                self._ljud_av = True
    
    def slå_på(self, signal):
        if signal == self._infraröd_frekvens and not self._påslagen:
            self._påslagen = True
    
    def slå_av(self, signal):
        if signal == self._infraröd_frekvens and self._påslagen:
            self._påslagen = False

class Fjärrkontroll:
    def __init__(self) -> None:
        self._tv = TV()
        self._frekvens = 320
    
    def on_off(self) -> None:
        if self._tv.påslagen:
            self._tv.slå_av()
        else:
            self._tv.slå_på()
    
    def ändra_kanal(self, value) -> None:
        self._tv.kanal = value