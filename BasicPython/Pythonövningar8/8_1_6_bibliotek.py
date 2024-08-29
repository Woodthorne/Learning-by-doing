class Bibliotek:
    def __init__(self, namn:str) -> None:
        self._namn = namn
        self.__böcker = []
    
    def lägg_till_bok(self,bok:str) -> None:
        self.__böcker.append(bok)
    
    def lista_böcker(self) -> list:
        return self.__böcker