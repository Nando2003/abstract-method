from models.ServicoIntegracao import ServicoIntegracao

if __name__ == "__main__":
    service = ServicoIntegracao()
    service.registrar_cliente('data/conta.xml', 'Y')
    
