from Model.oficina import Oficina,db
class OficinaBLL():

    def consultaCNPJ(cnpj: int) -> Oficina:
        return db.session.query(Oficina).filter_by(cnpj=cnpj).first()
    
    def consultaEmail(email: str) -> Oficina:
        return db.session.query(Oficina).filter_by(email=email).first()
    
    def setOficina(oficina: Oficina)->bool:
        try:
            db.session.add(oficina)
            db.session.commit()
            return True
        except:
            return False
        
    def getOficina(id: int) -> Oficina:
        return db.session.query(Oficina).filter_by(id=id).first() 