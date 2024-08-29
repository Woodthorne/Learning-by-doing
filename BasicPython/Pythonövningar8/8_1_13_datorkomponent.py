# Program not done.

import time

class CentralProcessingUnit:
    def __init__(self) -> None:
        self._speed = 1.8
    
    def _delay(self):
        time.sleep(3 / self._speed)
    
    def fetch_to_ram(self,var:str):
        self._delay()
        computer._ram.memory[var] = computer._ssd.memory[var]

class RandomAccessMemory:
    def __init__(self) -> None:
        self._capacity = 16000
        self._used = 0
        self._memory = {}
    
    @property
    def memory(self):
        return self._memory
    
    @memory.setter
    def memory(self,key,val):
        self._memory[key] = val
        for item in self._memory:
            print(item)
    
class SolidStateDrive:
    def __init__(self,name:str) -> None:
        self._name = name
        self._capacity = 500000
        self._memory = {'green':'stuff'}
    
    @property
    def memory(self):
        return self._memory
    
    @memory.setter
    def memory(self,key,val):
        self._memory[key] = val
        

class Computer:
    def __init__(self) -> None:
        self._cpu = CentralProcessingUnit()
        self._ram = RandomAccessMemory()
        self._ssd = SolidStateDrive('C')

computer = Computer()
computer._cpu.fetch_to_ram('green')
print(computer._ram.memory['green'])