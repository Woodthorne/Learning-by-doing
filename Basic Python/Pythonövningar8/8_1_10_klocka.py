class Klocka:
    def __init__(self) -> None:
        self._timmar = 0
        self._minuter = 0
        self._sekunder = 0
    
    def set_timmar(self,num:int) -> None:
        if -1 < num < 24:
            self._timmar = num
            print('Timmar har ändrats')
        else:
            print('Timmar får endast vara mellan 0-23')
    
    def set_minuter(self,num:int) -> None:
        if -1 < num < 60:
            self._minuter = num
            print('Minuter har ändrats')
        else:
            print('Minuter får endast vara mellan 0-59')
    
    def set_sekunder(self,num:int) -> None:
        if -1 < num < 60:
            self._sekunder = num
            print('Sekunder har ändrats')
        else:
            print('Minuter får endast vara mellan 0-59')
    
    def get_timmar(self) -> int:
        return self._timmar
    
    def get_minuter(self) -> int:
        return self._minuter
    
    def get_sekunder(self) -> int:
        return self._sekunder
    
    def tick(self):
        self._sekunder += 1
        if self._sekunder > 59:
            self._sekunder -= 60
            self._minuter += 1
            if self._minuter > 59:
                self._minuter -= 60
                self._timmar += 1
                if self._timmar > 23:
                    self._timmar -= 24