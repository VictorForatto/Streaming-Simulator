from logica import filme


def incluir_filme():
    nome_filme = str(input("Nome do filme : "))
    gen_filme = str(input("Gênero do filme : "))
    ano_filme = int(input("Ano do filme : "))
    produtora = str(input("Produtora do filme : "))

    filme.incluir_filme(nome_filme, gen_filme, ano_filme, produtora)
    
def buscar_filme_nome():
    print ("\n Buscando Filme por Nome \n")
    nome_filme = str(input("Nome do Filme : "))
    n = filme.buscar_filme_nome(nome_filme)
    if (n == None):
        print ("Nenhum filme com esse Título")
    else:
        print (n)


def remover_filme():
    print ("\n Removendo Filme \n")
    nome_filme = str(input("Nome do Filme: "))
    n = filme.remover_filme(nome_filme)
    if (n == False):
        print ("Nenhum filme encontrado !")
    else:
        print ("Filme removido")

#-----------------------------------------------------------------------------------

def imprimir_filme(dados_filme):
    print ("Nome do filme : ",dados_filme[0])
    print("Gênero do filme :", dados_filme[1])
    print ("Ano do filme :", dados_filme[2])
    print ("Produtora : ", dados_filme[3])
    print ("------------------")

def imprimir_nome_filme(dados_filme):
    print ("Nome do filme : ", dados_filme[0])
    print ("Gênero do filme :", dados_filme[1])
    print ("---------------------------------")

def listar_filme():
    print ("\nListar Filmes \n")
    filmes = filme.listar_filme()
    for f in filmes:
        imprimir_filme(f)
        
def listar_nome_filme():
    print ("\nListar Filmes \n")
    filmes = filme.listar_filme()
    for f in filmes:
        imprimir_nome_filme(f)
        
#----------------------------------------------------------------------------------


def mostrar_menu():
    run_filmes = True
    
    menu = ("\n----------------\n"+
             "(1) Adicionar Novo Filme \n" +
             "(2) Listar Filmes \n" +
             "(3) Buscar Filme por Nome \n" +
             "(4) Remover Filme \n" +
             "(0) Voltar\n"+
            "----------------")
    
    while(run_filmes):
        print (menu)
        op = int(input("Digite sua escolha: "))

        if (op == 1):
            incluir_filme()
        elif(op == 2):
            listar_filme()
        elif(op == 3):       
            buscar_filme_nome()
        elif (op == 4):
            remover_filme()
        elif (op == 0):
            run_filmes = False
            
