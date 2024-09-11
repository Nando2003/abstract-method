from interfaces.DecoderFactory import DecoderFactory
from models.RegistrarClienteTextDecoder import RegistrarClienteTextDecoder
from models.RegistrarContaTextDecoder import RegistrarContaTextDecoder

class TextDecoderFactory(DecoderFactory):
    def create_registrar_cliente_decoder(self):
        return RegistrarClienteTextDecoder()
    
    def create_registrar_conta_decoder(self):
        return RegistrarContaTextDecoder() 