import os
from pathlib import Path
from plantuml import PlantUML

codigoPlantUML = """
@startuml

skinparam style strictuml
skinparam Class {
    BackgroundColor white
    BorderColor black
    IconFontSize 0
}

skinparam classAttributeIconSize 0

' 1. Definição dos Atores
actor Usuário

' 2. Definição dos Casos de Uso
package "Sistema de avaliação" {
    usecase (UC01 - Inserir dados) as UC1
}

' 3. Relações entre Atores e Casos de Uso
Usuário -r-> UC1

@enduml
"""

plantuml = PlantUML(url='http://www.plantuml.com/plantuml/img/')
imagem = plantuml.processes(codigoPlantUML)
diretorioAtual = Path(__file__).resolve().parent
nomeArquivo = diretorioAtual / 'img_diagrama_uc.png'
with open(nomeArquivo, 'wb') as f:
    f.write(imagem)

print(f"Diagrama salvo com sucesso em: {nomeArquivo}")