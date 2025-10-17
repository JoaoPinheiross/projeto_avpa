from Projeto import Projeto

def avaliaProjeto(projeto: Projeto) -> str:
    pontos = 0
    if projeto.payback >= Projeto.PAYBACK:
        pontos += 2
    if projeto.geracao >= Projeto.GERACAOENERGIA:
        pontos +=1

    if pontos >= 3:
        return "Um ótimo projeto"
    elif pontos >= 1:
        return "Um projeto mediano"
    else:
        return "Um projeto ruim"

def definiProjeto() -> Projeto:
    nome = input("Digite o nome do projeto: ")
    payback = int(input("Digite o tempo de retorno do projeto: "))
    geracaoEnergia = float(input("Digite a geração de energia do projeto: "))
    projeto = Projeto(nome, payback, geracaoEnergia)
    return projeto

projeto = definiProjeto()
print(avaliaProjeto(projeto))