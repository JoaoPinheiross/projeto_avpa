# Importando bibliotecas
import os
from pathlib import Path
from plantuml import PlantUML

# Código PlantUML
codigoPlantUML = """
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
    - nome: String
    - orçamento: int
    - orçamentoP4: int
    - painel: Painel
    - economiaProjeto:float
    --
    + Projeto(nome: str, orcamento: float, painel: Painel)
    + calcularPayback(): float
    + avaliarProjeto(boleto: float, paybackMeta: int): int
}

class Painel {
    - potencia: float
    - irradiacao: float
    - eficiencia: float
    - quantidade: int
    - custo: float
    - manutencao: float
    - tempoVida: int
    - economia: float
    - geracaoEnergia: float
    --
    + Painel(potencia: int, eficiencia: float, tempoVida: int, gastoEnergia: float, boleto: float)
    + calcularQuantidade()
    + calcularGeracaoEnergia()
    + calcularCusto()
    + calcularManutencao()
    + calcularEconomia()
}

class Empresa {
    - custoEnergia: float
    - gastoEnergia: float
    - emissaoCo2Kg: float
    - tarifa: float
    - paybackMeta
    --
    + Empresa(custoEnergia: float, paybackMeta: int)
}

Projeto "1" --o "1..*" Painel
Empresa "1" -- "1..*" Projeto

}

@enduml
"""

# Baixando a imagem do diagrama
plantuml = PlantUML(url='http://www.plantuml.com/plantuml/img/')
imagem = plantuml.processes(codigoPlantUML)
try:
    diretorioAtual = Path(__file__).resolve().parent
    nomeArquivo = diretorioAtual / 'img_diagrama_classe.png'
except NameError:
    nomeArquivo = 'img_diagrama_classe.png'
with open(nomeArquivo, 'wb') as f:
    f.write(imagem)

print(f"Diagrama salvo com sucesso em: {nomeArquivo}")