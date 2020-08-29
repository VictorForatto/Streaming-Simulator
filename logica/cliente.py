clientes = []

def incluir_cliente(id_cliente,senha_cliente,nome_cliente,data_nascimento,endereço_cliente,telefone_cliente,email_cliente,cpf_cliente,rg_cliente):    
    cliente = [id_cliente,senha_cliente,nome_cliente,data_nascimento,endereço_cliente,telefone_cliente,email_cliente,cpf_cliente,rg_cliente]
    clientes.append(cliente)
    
def listar_cliente():
    return clientes
        
def remover_cliente(id_cliente):
    for c in clientes:
        if (c[0] == id_cliente):
            clientes.remove(c)
            return True
    return False

def iniciar_cliente():
    incluir_cliente("123","123","Roberto","03/12/1998","Rua das Palmeiras","39983546","roberto_98@hotmail.com","99873456","1234567")
    incluir_cliente("12345","12345","José","08/05/1970","Rua da Bica","45474893","josé_70@hotmail.com","9945781","11451367")
