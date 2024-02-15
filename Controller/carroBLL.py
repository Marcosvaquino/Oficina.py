
from flask import session
from Model.carro import Carro,db
class CarroBLL():

    #inserindo o carro lista de carros
    def setCarro(carro:Carro):
        db.session.add(carro)
        db.session.commit()        
        
    #atualizar o carro na lista de carros
    def updateCarro(carro:Carro):
        db.session.merge(carro)
        db.session.commit()              
    
    #localizando o carro na lista de carros
    def getCarro(placa:str)->Carro:
        return Carro.query.filter_by(placa=placa).first()

    def getCarrosCliente(id:int)->list:
        return Carro.query.filter_by(id_cliente=id).all()         
    
    #listando todos os carros cadastrados
    def getListCarros()->list:
        return Carro.query.filter_by(id_oficina=session['id_oficina']).all()        