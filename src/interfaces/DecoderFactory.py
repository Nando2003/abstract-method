from abc import ABC, abstractmethod

class DecoderFactory(ABC):
    @abstractmethod
    def create_registrar_cliente_decoder(self):
        pass
    
    @abstractmethod
    def create_registrar_conta_decoder(self):
        pass
    
    @staticmethod
    def fabrica_para_origem(origem: str):
        from models.TextDecoderFactory import TextDecoderFactory
        from models.XLMDecoderFactory import XMLDecoderFactory
        
        if origem == 'X':
            return TextDecoderFactory()
        elif origem == 'Y':
            return XMLDecoderFactory()
        else:
            raise ValueError(f"Origem desconhecida: {origem}")