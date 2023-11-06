class Studerande:
    def __init__(self,ID:str) -> None:
        self._studentID = ID
        self._kurser = []
        self._betyg = {}
    
    def ny_kurs(self,kurs:str) ->  None:
        if kurs not in self._kurser:
            self._kurser.append(kurs)
            self._betyg[kurs] = 'Betyg saknas'
        else:
            print('Kursen existerar redan.')
    
    def ändra_betyg(self,kurs:str,betyg:str) -> None:
        if kurs in self._kurser:
            self._betyg[kurs] = betyg
        else:
            print('Kursen existerar inte.')
    
    def hämta_betyg(self,kurs:str) -> str:
        if kurs in self._kurser:
            return self._betyg[kurs]
        else:
            print('Kursen existerar inte.')