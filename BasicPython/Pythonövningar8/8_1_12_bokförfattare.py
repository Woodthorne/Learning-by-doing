class Författare:
    def __init__(self,namn:str,födelseår:int) -> None:
        self._namn = namn
        self._födelseår = födelseår
    
    def get_name(self):
        return self._namn

class Bok:
    def __init__(self,titel:str,utgivningsår:int,författare:str,födelseår:int) -> None:
        self._författare = Författare(författare,födelseår)
        self._titel = titel
        self._utgivningsår = utgivningsår
    
    def get_author(self) -> str:
        return self._författare.get_name()

bok = Bok('Elementary Linear Algebra 10th Ed.',2011,'Howard Anton',1939)
print(bok.get_author())