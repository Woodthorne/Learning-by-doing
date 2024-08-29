class Djur:
    def __init__(self,art:str,föda:str,livsmiljö:str) -> None:
        self._art = art
        self._föda = föda
        self._livsmiljö = livsmiljö
    
    def hämta_art(self) -> str:
        return self._art
    
    def hämta_föda(self) -> str:
        return self._föda
    
    def hämta_livsmiljö(self) -> str:
        return self._livsmiljö
    
    def ändra_art(self,art:str) -> None:
        self._art = art
    
    def ändra_föda(self,föda:str) -> None:
        self._föda = föda
    
    def ändra_livsmiljö(self,livsmiljö:str) -> None:
        self._livsmiljö = livsmiljö

katt = Djur('katt','kattmat','hus')
häst = Djur('häst','gräs','stall')
tiger = Djur('tiger','kött','jungeln')

print(tiger.hämta_art())
tiger.ändra_art('fisk')
print(tiger.hämta_art())