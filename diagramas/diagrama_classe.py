import os
from pathlib import Path
from plantuml import PlantUML

plantuml_code_string = """
@startuml

skinparam style strictuml
skinparam Class {
    BackgroundColor white
    BorderColor black
    IconFontSize 0
}

skinparam classAttributeIconSize 0

package "Model" {

class Projeto {
    - Nome: String
    - Orçamento: int
    - OrçamentoP4: int
    - Boleto: int
    - Tarifa: float
    - Energia: float
    - Emissao: float
    - Potencia: int
    --
}

class Painel {
    - EnergiaP: int
    - Quantidade: int
    - Custo: float
    - Taxa: float
    - Lucro: float
    - Meses: int
    - TempoVida: int
    --
    + Payback()
}

class Avaliação {
    - Pontos: int
    --
    + Avaliar()
}

Projeto "1" -r-o "1" Painel
Painel -r- Avaliação

}

@enduml
"""

plantuml = PlantUML(url='http://www.plantuml.com/plantuml/img/')
imagem = plantuml.processes(plantuml_code_string)
diretorioAtual = Path(__file__).resolve().parent
nomeArquivo = diretorioAtual / 'diagrama_classe.png'
with open(nomeArquivo, 'wb') as f:
    f.write(imagem)

print(f"Diagrama salvo com sucesso em: {nomeArquivo}")