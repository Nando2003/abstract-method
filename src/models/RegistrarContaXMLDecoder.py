from interfaces.RegistrarDecoder import RegistrarDecoder
import xml.etree.ElementTree as ET

class RegistrarContaXMLDecoder(RegistrarDecoder):
    def decode(self, conta_xml_path: str):
        tree = ET.parse(conta_xml_path)
        root = tree.getroot()
        message = root.find("message")
        
        if message is not None:
            return message.text
    
        raise Exception()
 