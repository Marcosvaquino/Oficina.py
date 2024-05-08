from Model.produto import Produto,db
class ProdutoBLL():      
               
    #inserir produto na lista de produtos
    def setProduto(produto:Produto):
        db.session.add(produto)
        db.session.commit()
        
    #localizando produto na lista de produtos
    def getProdutoId(id:int)->Produto:
        return db.session.query(Produto).filter_by(id=id).first()
    
    def getProdutoCodigo(codigo:str)->Produto:
        return db.session.query(Produto).filter_by(codigo=codigo).first()
    
    def getPridutoDescricao(descricao:str)->Produto:
        return db.session.query(Produto).filter_by(descricao=descricao).first()

    #listando todos os produto na lista de produtos
    def getListadeProdutos()->list:
        return db.session.query(Produto).all()
    

    

 

