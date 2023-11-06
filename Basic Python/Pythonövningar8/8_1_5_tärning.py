import random

class Tärning:
    def __init__(self,sidor:int = 6) -> None:
        self._antalSidor = sidor
    
    def get_antalSidor(self) -> int:
        return self._antalSidor
    
    def slå_tärning(self) -> int:
        return random.randint(1,self._antalSidor)