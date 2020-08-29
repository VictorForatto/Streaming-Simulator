filmes = []


def incluir_filme(nome_filme, gen_filme, ano_filme, produtora):
    dados_filme = [nome_filme, gen_filme, ano_filme, produtora]
    filmes.append(dados_filme)
    
def listar_filme():
    return filmes

def buscar_filme_nome(nome_filme):
    for n in filmes:
        if (n[0] == nome_filme):
            return n
    return None


def remover_filme(nome_filme):
    for n in filmes:
        if (n[0] == nome_filme):
            filmes.remove(n)
            return True
    return False
    
def iniciar_filme():
    incluir_filme("Senhor dos Anéis","Ação",1998,"Universal")
    incluir_filme("Homem Aranha de Volta ao Lar","Ação",2017,"Marvel Studios")
    incluir_filme("Thor Ragnarok","Ação",2017,"Marvel Studios")
    incluir_filme("Se eu fosse você","Comédia",2012,"Globo Estúdio")
