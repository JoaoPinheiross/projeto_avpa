# Importando bibliotecas
import time
from plantuml import PlantUML
from pathlib import Path

plantumlLog = []

def registrar(atividade, tipo="acao"):
    """
    Registra uma etapa do processo na sintaxe PlantUML.

    Args:
        atividade (str): A descrição da atividade.
        tipo (str): O tipo de elemento do diagrama (acao, decisao_ini, etc.).
    """
    if tipo == "acao":
        plantumlLog.append(f":{atividade};")
    elif tipo == "decisao_ini":
        plantumlLog.append(f"if ({atividade}?) then (sim)")
    elif tipo == "decisao_senao":
        plantumlLog.append("else (não)")
    elif tipo == "decisao_fim":
        plantumlLog.append("endif")
    elif tipo == "fork_ini":
        plantumlLog.append("fork")
    elif tipo == "fork_meio":
        plantumlLog.append("fork again")
    elif tipo == "fork_fim":
        plantumlLog.append("end fork")
    elif tipo == "fim":
        plantumlLog.append("stop")
        plantumlLog.append("@enduml")

# Métodos que definem as atividades
def extrairHistórico():
    time.sleep(0.1)
    registrar("Extrair histórico da empresa")

def definirProjeto():
    time.sleep(0.1)
    registrar("Definir parâmetros do projeto")

def escolherPainel():
    time.sleep(0.1)
    registrar("Escolher tipo de painel")

def avaliar():
    time.sleep(0.1)
    registrar("Avaliar Projeto")

def descartar():
    registrar("Projeto descartado")

def negociar():
    registrar("Negociar projeto")

def entregarRelatorio():
    registrar("Realizar relatório")
    registrar("Entregar relatório do projeto")
    registrar("", "fim")

# Decisão de aprovação
def decisaoAprovar(pontos):
    registrar("Projeto Aprovado?", "decisao_ini")
    meta = 3
    if pontos >= meta:
        return True
    else:
        registrar("", "decisao_senao")
        return False

# Gera e salva a UML
def gerarUml():
    plantDiagrama = "\n".join(plantumlLog)

    plantuml = PlantUML(url='http://www.plantuml.com/plantuml/img/')
    imagem = plantuml.processes(plantDiagrama)
    diretorioAtual = Path(__file__).resolve().parent
    nomeArquivo = diretorioAtual / 'diagramas' / 'img_diagrama_avalia_projeto.png'
    with open(nomeArquivo, 'wb') as f:
        f.write(imagem)

    print(f"Diagrama salvo com sucesso em: {nomeArquivo}")

def simularProjeto(pontos: int):
    '''Simula a avaliação do projeto usando uma UML.
    Args:
        pontos (int): Os pontos obtidos na avaliação.
    Returns:
        Não possui retornos.
    '''
    # Simula as atividades
    extrairHistórico()
    definirProjeto()
    escolherPainel()
    avaliar()

    # Lógica de decisão que registra corretamente os dois caminhos
    if decisaoAprovar(pontos):
        # Caminho do "Sim" é registrado aqui
        negociar()
        entregarRelatorio()
    else:
        # Caminho do "Não" é registrado aqui
        descartar()

    # O 'endif' é chamado APÓS ambos os caminhos terem sido definidos
    registrar("", "decisao_fim")

    # Chama o método que gera a uml
    gerarUml()