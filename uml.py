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

def receberDados():
    time.sleep(0.1)
    registrar("Receber dados do projeto")

def escolherPainel():
    time.sleep(0.1)
    registrar("Escolher tipo de painel")

def avaliar():
    time.sleep(0.1)
    registrar("Avaliar Projeto")

def decisaoAprovar(pontos):
    registrar("Projeto Aprovado?", "decisao_ini")
    meta = 3
    if pontos >= meta:
        return True
    else:
        registrar("", "decisao_senao")
        return False

def descartar():
    registrar("Projeto descartado")

def negociar():
    registrar("Negociar projeto")

def aplicar():
    registrar("Colocar projeto em prática")
    registrar("", "fim")

def gerarUml():
    plantDiagrama = "\n".join(plantumlLog)

    plantuml = PlantUML(url='http://www.plantuml.com/plantuml/img/')
    imagem = plantuml.processes(plantDiagrama)
    diretorioAtual = Path(__file__).resolve().parent
    nomeArquivo = diretorioAtual / 'diagramas' / 'diagrama_avalia_projeto.png'
    with open(nomeArquivo, 'wb') as f:
        f.write(imagem)

    print(f"Diagrama salvo com sucesso em: {nomeArquivo}")

def simularProjeto(pontos):
    plantumlLog = [
    "@startuml",
    "title Diagrama de Atividades: Campanha de Marketing",
    "start"
    ]

    receberDados()
    escolherPainel()
    avaliar()

    # 3. Lógica de decisão que registra corretamente os dois caminhos
    if decisaoAprovar(pontos):
        # Caminho do "Sim" é registrado aqui
        negociar()
        aplicar()
    else:
        # Caminho do "Não" é registrado aqui
        descartar()

    # O 'endif' é chamado APÓS ambos os caminhos terem sido definidos
    registrar("", "decisao_fim")
    gerarUml()