
from Model.carro import Carro

listadeCarros=[]

class CarroBLL():

    #inserindo o carro lista de carros
    def setCarro(carro:Carro):
        listadeCarros.append(carro)        
    
    #localizando o carro na lista de carros
    def getCarro(placa:str)->Carro:
        carro = next((c for c in listadeCarros if c.placa == placa),None)
        return carro
        
    
    #listando todos os carros cadastrados
    def getListCarros()->[]:
        return listadeCarros        