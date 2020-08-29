from logica import cliente
from gui import menu_cliente

from logica import filme
from gui import menu_filmes

from gui import menu_login
    
def inicializar_dados():
    cliente.iniciar_cliente()
    filme.iniciar_filme()

    
def mostrar_menu():
    run_menu = True

    inicializar_dados()
    
    menu = ("\n----------------\n"+
             "(1) Cadastrar Clientes \n" +
             "(2) Cadastrar Filmes \n" +
             "(3) Fazer login e Assistir Filmes \n"+
             "(0) Sair\n"+
            "----------------")
    
    while(run_menu):
        print (menu)
        
        op = int(input("Digite sua escolha: "))

        if (op == 1):
            menu_cliente.mostrar_menu()
        elif(op == 2):
            menu_filmes.mostrar_menu()
        elif (op==3):
            menu_login.mostrar_menu()
        elif (op == 0):
            print ("Você fechou o Programa...")
            run_menu = False
        else:
            print ("Valor inválido !!!!!")

