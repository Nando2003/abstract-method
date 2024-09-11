from interfaces.DecoderFactory import DecoderFactory
from models.RegistrarClienteXMLDecoder import RegistrarClienteXMLDecoder
from models.RegistrarContaXMLDecoder import RegistrarContaXMLDecoder

class XMLDecoderFactory(DecoderFactory):
    def create_registrar_cliente_decoder(self):
        return RegistrarClienteXMLDecoder()
    
    def create_registrar_conta_decoder(self):
        return RegistrarContaXMLDecoder() 