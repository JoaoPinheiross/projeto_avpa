from Projeto import Projeto

def avaliaProjeto(projeto: Projeto) -> str:
    '''Avalia o projeto de acordo com as metas já propostas pela empresa.
    Args:
        projeto (Projeto): O objeto projeto com todos os seus atributos.
    Returns:
        str: Retorna uma mensagem dizendo a qualidade do projeto.
    '''
    pontos = 0

    # Compara os parâmetros do projeto pelas metas da empresa.
    if projeto.payback >= Projeto.PAYBACK:
        pontos += 1
    if projeto.geracao >= Projeto.GERACAOENERGIA:
        pontos += 1
    if projeto.geracaoCo2 >= Projeto.REDUCAOCO2:
        pontos += 1
    
    # Verifica o nível do projeto
    if pontos >= 3:
        return "Um projeto ótimo"
    elif pontos >= 2:
        return "Um projeto mediano"
    else:
        return "Um projeto ruim"

def definiProjeto() -> Projeto:
    '''Define o projeto com os parâmetros recebidos pelo usuário.
    Args:
        Não possui argumentos.
    Returns:
        Projeto: Retorna o objeto Projeto criado.
    '''
    # Recebe os valores do usúario
    nome = input("Digite o nome do projeto: ")
    payback = int(input("Digite o tempo de retorno do projeto: "))
    geracaoEnergia = float(input("Digite a geração de energia do projeto: "))
    # Cria o objeto do projeto
    projeto = Projeto(nome, payback, geracaoEnergia)
    return projeto

projeto = definiProjeto()
print(avaliaProjeto(projeto))