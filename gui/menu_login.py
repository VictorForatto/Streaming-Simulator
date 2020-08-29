from logica import cliente

from gui import menu_cliente

from gui import menu_filmes 

from logica import historico

from logica import filme



def fazer_login():
    email_cliente = str(input("Insira email : "))
    senha_cliente = str(input("Insira a senha : "))

    clientes = cliente.listar_cliente()

    for c in clientes:
        if (c[0]==email_cliente) and (c[0]==senha_cliente):
            menu_cliente.imprimir_login(c)
            print (" Login Efetuado ")
    escolha = str(input("Deseja assistir algum filme?"))
    if escolha == 'SIM' or escolha == 'Sim' or escolha =='sim':
        assistir_filme()

def esqueci_senha():
    email_cliente = str(input("Insira email : "))
    
    clientes = cliente.listar_cliente()

    for c in clientes:
        if (c[0]==email_cliente):
            menu_cliente.imprimir_dados(c)

#------------------------------------------------------------------------

def assistir_filme():
    menu_filmes.listar_nome_filme()

    nome_filme = str(input("Insira o nome do filme que quer assistir : "))

    n = filme.buscar_filme_nome(nome_filme)
    
    if (n == None):
        print ("Nenhum filme para assistir com esse título !")
    else:
        historico.incluir_hist(nome_filme)
        print ("Curta bastante o filme !")

def imprimir_hist(filme):
    print ("Nome do filme : ", filme[0])
    print ("------------------")

def listar_hist():
    print ("\n Listando Histórico de Filmes Assistidos \n")
    historicos = historico.listar_hist()
    
    for h in historicos:
        imprimir_hist(h)

#------------------------------------------------------------------------


def mostrar_menu():
    run_login = True
    menu = ("\n----------------\n"+
             "(1) Inserir Email e Senha \n" +
             "(2) Esqueci minha senha \n" +
             "(3) Listar Histórico de Filmes Assistidos \n" +
             "(0) Voltar \n"+
             "----------------")
    
    while(run_login):
        print (menu)
        op = int(input("Digite sua escolha: "))

        if (op == 1):
            fazer_login()
        elif(op == 2):
            esqueci_senha()
        elif(op==3):
            listar_hist()
        elif (op == 0):
            run_login = False
