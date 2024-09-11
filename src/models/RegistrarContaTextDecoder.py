from interfaces.RegistrarDecoder import RegistrarDecoder

class RegistrarContaTextDecoder(RegistrarDecoder):
    def decode(self, conta_txt_path: str):
        with open(conta_txt_path, 'r') as file:
            return file.readline()
 