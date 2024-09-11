from abc import ABC, abstractmethod

class RegistrarDecoder(ABC):
    @abstractmethod
    def decode(self):
        pass
        
