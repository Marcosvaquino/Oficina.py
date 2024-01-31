
from Model.carro import Carro
from Data.bd import executar,selectAll,selectOne

class CarroBLL():

    #inserindo o carro lista de carros
    def setCarro(carro:Carro):

        sql = f"INSERT INTO carro (id_oficina,id_cliente,placa,modelo,marca,cor,ano_fabricacao,ano_modelo,status,observacao) VALUES (1,{carro.id_cliente},'{carro.placa}','{carro.modelo}','{carro.marca}','{carro.cor}','{carro.ano_fabricacao}','{carro.ano_modelo}',{carro.status},'{carro.observacao}')"
        print(sql)
        if executar(sql):
            return True
        else:
            return False
              
    
    #localizando o carro na lista de carros
    def getCarro(placa:str)->Carro:

        sql = f"SELECT * FROM carro WHERE placa = '{placa}'"
        result = selectOne(sql)
        if result==None:
            return None
        else:
            return Carro(result[0],result[1],result[2],result[3],result[4],result[5],result[6])            
    
    #listando todos os carros cadastrados
    def getListCarros()->[]:
        sql = f"SELECT * FROM carro"
        result = selectAll(sql)

        print(result)

        if result==None:
            return None
        if len(result)==0:
            return None
        else:
            listadeCarros = []
            for r in result:
                listadeCarros.append(Carro.from_dict(r))

        return listadeCarros        