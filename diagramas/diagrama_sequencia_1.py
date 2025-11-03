import os
from pathlib import Path
from plantuml import PlantUML

codigoPlantUML = """
@startuml
!theme plain
skinparam style strictuml

title Gerando Projeto

actor Usuário
control Controller

Usuário ++
Usuário -> Controller ++: Inserir dados da empresa
Controller -> Controller ++: Solicitar dados do projeto
Controller --
Controller --
Usuário -> Controller ++: Inserir dados do projeto
Controller -> Controller ++: Solicitar tipo de painel
Controller --
Controller --
Usuário -> Controller ++: Inserir tipo de painel
create participant "painel1: Painel" as painel
Controller -> painel ++: Criar painel: Painel()
painel -> painel ++: Calcula dados do painel
painel --
painel --
create participant "projeto1: Projeto" as projeto
Controller -> projeto ++: Criar projeto: Projeto()
projeto -> projeto ++: calcularPayback()
projeto --
projeto --> Controller: Enviar dados
projeto --
Controller --> Usuário: Enviar relatório do projeto: String
Controller --
Controller --
Usuário --

@enduml
"""

plantuml = PlantUML(url='http://www.plantuml.com/plantuml/img/')
imagem = plantuml.processes(codigoPlantUML)
diretorioAtual = Path(__file__).resolve().parent
nomeArquivo = diretorioAtual / 'img_diagrama_sequencia_1.png'
with open(nomeArquivo, 'wb') as f:
    f.write(imagem)

print(f"Diagrama salvo com sucesso em: {nomeArquivo}")