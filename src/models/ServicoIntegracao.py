from interfaces.DecoderFactory import DecoderFactory

class ServicoIntegracao:
    def registrar_cliente(self, path: str, origem: str):
        decoder = DecoderFactory.fabrica_para_origem(origem)
        msg = decoder.create_registrar_cliente_decoder()
        print(msg.decode(path))
        
    def registrar_conta(self, path: str, origem: str):
        decoder = DecoderFactory.fabrica_para_origem(origem)
        msg = decoder.create_registrar_conta_decoder()
        print(msg.decode(path))
        