from logica import cliente

def incluir_cliente():
    id_cliente = str(input("Insira o Id : "))
    senha_cliente = str(input("Insira a senha da conta : "))
    nome_cliente = str(input("Insira o nome: "))
    data_nascimento = str(input("Insira a data de nascimento : "))
    endereço_cliente = str(input("Insira o seu endereço : "))
    telefone_cliente = str(input("Insira o telefone : "))
    email_cliente = str(input("Insira o email : "))
    cpf_cliente = str(input("Insira o CPF : "))
    rg_cliente = str(input("Insira o RG : "))
    
    cliente.incluir_cliente(id_cliente, senha_cliente, nome_cliente, data_nascimento, endereço_cliente, telefone_cliente, email_cliente, cpf_cliente, rg_cliente)


#---------------------------------------------------------

def imprimir_cliente(cliente):
    print ("-----------------------")
    print ("Id : ", cliente[0])
    print ("Nome : ", cliente[2])
    print ("Data de nascimento : ", cliente[3])
    print ("Email : ", cliente[6])
    print ("CPF : ", cliente[7])
    print ("RG : ", cliente[8])
    print ("-----------------------")

def imprimir_dados(cliente):
    print ("----------------------")
    print ("Email : ", cliente[6])
    print ("Senha : ", cliente[1])

def imprimir_login(cliente):
    print ("----------------------")
    print ("Id : ", cliente[0])
    print ("Senha : ", cliente[1])
    print ("Nome : ", cliente[2])
    print ("Data de nascimento : ", cliente[3])
    print ("Endereço : ", cliente[4])
    print ("Telefone : ", cliente[5])
    print ("Email : ", cliente[6])
    print ("CPF : ", cliente[7])
    print ("RG : ", cliente[8])
    print ("-----------------------")

#------------------------------------------------------
    
def listar_cliente():
    print ("\nListar Clientes \n")
    clientes = cliente.listar_cliente()
    
    for c in clientes:
        imprimir_cliente(c)

        
def remover_cliente():
    print("Removendo cliente por ID")
    id_cliente = str(input("Insira o ID: "))
    
    c = cliente.remover_cliente(id_cliente)
    
    if (c == False):
        print ("Cliente não existente")
    else:
        print ("Cliente removido")

def mostrar_menu():
    run_cliente = True
    menu = ("\n----------------\n"+
             "(1) Adicionar novo Cliente \n" +
             "(2) Remover Cliente \n" +
             "(3) Listar Clientes \n" +
             "(0) Voltar\n"+
            "----------------")
    
    while(run_cliente):
        print (menu)
        op = int(input("Digite sua escolha: "))

        if (op == 1):
            incluir_cliente()
        elif (op == 2):
            remover_cliente()
        elif (op==3):
            listar_cliente()
        elif (op == 0):
            run_cliente = False
