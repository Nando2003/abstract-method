from interfaces.RegistrarDecoder import RegistrarDecoder

class RegistrarClienteTextDecoder(RegistrarDecoder):
    def decode(self, cliente_txt_path: str):
        with open(cliente_txt_path, 'r') as file:
            return file.readline()
 
 