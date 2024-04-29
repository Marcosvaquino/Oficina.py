from Model.ordem_servico import OrdemServico, db

class OrdemServicoBLL():

    def getOrdemServicoID(id_veiculo,id_cliente,id_oficina)->int:
        try:
            return db.session.query(OrdemServico).filter_by(id_veiculo=id_veiculo,id_cliente=id_cliente,id_oficina=id_oficina).order_by(OrdemServico.id.desc()).first().id
        except:
            return 0        

    def getOrdensServico():
        return db.session.query(OrdemServico).all()
    
    def getOrdemServico(id):
        return db.session.query(OrdemServico).get(id)
    
    def setItemServico(item):
        db.session.add(item)
        db.session.commit()
    
    def setOrdemServico(ordem:OrdemServico)->int:

        id_veiculo = ordem.id_veiculo
        id_cliente = ordem.id_cliente
        id_oficina = ordem.id_oficina

        db.session.add(ordem)
        db.session.commit()
        
        return OrdemServicoBLL.getOrdemServicoID(id_veiculo,id_cliente,id_oficina)
    
    def updateOrdemServico(ordem:OrdemServico)->int:

        id_veiculo = ordem.id_veiculo
        id_cliente = ordem.id_cliente
        id_oficina = ordem.id_oficina

        db.session.merge(ordem)
        db.session.commit()
        
        return OrdemServicoBLL.getOrdemServicoID(id_veiculo,id_cliente,id_oficina)
    
    
