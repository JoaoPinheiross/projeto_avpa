# Importando bibliotecas
import os
from pathlib import Path
from plantuml import PlantUML

# Código PlantUML
codigoPlantUML = """
@startuml
!theme plain
skinparam style strictuml

title Avaliando Projeto

actor Usuário as user
control Controller
entity Projeto

user ++
Controller ++
Controller -> Projeto++: avaliarProjeto()
Projeto --> Controller: pontos: int
Projeto --
Controller -> user: pontos: int
Controller --
user --

@enduml
"""

# Baixando a imagem do diagrama
plantuml = PlantUML(url='http://www.plantuml.com/plantuml/img/')
imagem = plantuml.processes(codigoPlantUML)
try:
    diretorioAtual = Path(__file__).resolve().parent
    nomeArquivo = diretorioAtual / 'img_diagrama_sequencia_2.png'
except NameError:
    nomeArquivo = 'img_diagrama_sequencia2.png'
with open(nomeArquivo, 'wb') as f:
    f.write(imagem)

print(f"Diagrama salvo com sucesso em: {nomeArquivo}")