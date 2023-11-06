class Produkt:
    def __init__(self,ID,namn,pris) -> None:
        self._produktID = ID
        self._namn = namn
        self._pris = pris
    
    def get_ID(self):
        return self._produktID
    
    def get_namn(self):
        return self._namn
    
    def get_pris(self):
        return self._pris
    
    def set_ID(self,ID):
        self._produktID = ID
    
    def set_namn(self,namn):
        self._namn = namn
    
    def set_pris(self,pris:int):
        if pris < 0:
            pris = 0
        self._pris = pris