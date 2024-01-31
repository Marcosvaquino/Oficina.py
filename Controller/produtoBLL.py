from Model.produto import Produto

ListadeProdutos=[]

class ProdutoBLL():      
               
    #inserir produto na lista de produtos
    def setProduto(produto:Produto):
        ListadeProdutos.append(produto)

    #localizando produto na lista de produtos
    def getProduto(id:str)->Produto:
        produto = next((c for c in ListadeProdutos if c.id == id),None)
        return produto

    #listando todos os produto na lista de produtos
    def getListadeProduos()->[]:
        return ListadeProdutos
    

    

 

