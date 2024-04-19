
from flask import session
from Model.veiculo import Veiculo,db
class VeiculoBLL():

    #inserindo o veiculo lista de veiculos
    def setVeiculo(veiculo:Veiculo):
        db.session.add(veiculo)
        db.session.commit()        
        
    #atualizar o veiculo na lista de veiculos
    def updateVeiculo(veiculo:Veiculo):
        db.session.merge(veiculo)
        db.session.commit()              
    
    #localizando o veiculo na lista de veiculos
    def getVeiculo(placa:str)->Veiculo:
        return Veiculo.query.filter_by(placa=placa).first()

    def getVeiculosCliente(id:int)->list:
        return Veiculo.query.filter_by(id_cliente=id).all()         
    
    #listando todos os veiculos cadastrados
    def getListVeiculos()->list:
        return Veiculo.query.filter_by(id_oficina=session['id_oficina']).all()        