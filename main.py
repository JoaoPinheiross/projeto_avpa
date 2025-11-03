# Importando módulos
from Classes import Projeto, Painel, Empresa
from entradas import recebeBoleto, recebeNomeProjeto, recebeOrcamento, recebeTipoPainel, recebePaybackMeta
from uml import simularProjeto

# Recebendo dados do usuário sobre empresausando o módulo entradas
nomeProjeto: str = recebeNomeProjeto()
orcamento: float = recebeOrcamento()
boleto: float = recebeBoleto()
paybackMeta: int = recebePaybackMeta()

empresa: Empresa = Empresa(boleto, paybackMeta) # Criando a empresa

# Recebendo os dados sobre o tipo
tipoPainel = recebeTipoPainel()
if tipoPainel == 1:
    painel = Painel(410, 0.79, 10, empresa.gastoEnergia, boleto) # Criando Painel com potência 410
else:
    painel = Painel(655, 0.75, 12, empresa.gastoEnergia, boleto) # Criando Painel com potência 655

projeto = Projeto(nomeProjeto, orcamento, painel) # Criando Projeto

# Apresentando dados
print("-- Histórico da empresa --")
print(f"energia gasta: {empresa.gastoEnergia:1.0f}kWh.\nGerando cerca de {empresa.emissaoCo2Kg:.2f}Kg de emissões.\n")

print("-- Quantidade de painéis --")
print(f"{projeto.painel.quantidade:1.0f} painéis de {projeto.painel.potencia}WP\n")

print("-- Gastos do projeto --")
print(f"{projeto.painel.quantidade}x Painel {projeto.painel.potencia}WP = {projeto.painel.custo:1.0f}\n")

print(f"Economia com o projeto = {projeto.painel.economia}\n")

print(f"Payback de {projeto.payback} meses\n")

# Avaliando Projeto
print("-- Avaliação do Projeto --")
print("Entres ambos paineis, com base de 0 a 5 pontos o seu projetos tem:\n")
pontos = projeto.AvaliarProjeto(empresa.custoEnergia, empresa.paybackMeta)

# Gerando UML
print("Gerando diagrama...")
simularProjeto(pontos)