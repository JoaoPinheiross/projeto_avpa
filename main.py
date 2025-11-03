from Classes import Projeto, Painel, Empresa
from entradas import recebeBoleto, recebeNomeEmpresa, recebeOrcamento, recebeTipoPainel, recebePaybackMeta
from uml import simularProjeto


nomeEmpresa: str = recebeNomeEmpresa()
orcamento: float = recebeOrcamento()
boleto: float = recebeBoleto()
paybackMeta: int = recebePaybackMeta()
empresa: Empresa = Empresa(boleto, paybackMeta)

tipoPainel = recebeTipoPainel()
if tipoPainel == 1:
    painel = Painel(410, 0.79, 10, empresa.gastoEnergia, boleto)
else:
    painel = Painel(655, 0.75, 12, empresa.gastoEnergia, boleto)

projeto = Projeto(nomeEmpresa, orcamento, painel)

print("-- Histórico da empresa --")
print(f"energia gasta: {empresa.gastoEnergia:1.0f}kWh.\nGerando cerca de {empresa.emissaoCo2Kg:.2f}Kg de emissões.\n")

print("-- Quantidade de painéis --")
print(f"{projeto.painel.quantidade:1.0f} painéis de {projeto.painel.potencia}WP\n")

print("-- Gastos do projeto --")
print(f"{projeto.painel.quantidade}x Painel {projeto.painel.potencia}WP = {projeto.painel.custo:1.0f}\n")

print(f"Economia com o projeto = {projeto.painel.economia}\n")

print(f"Payback de {projeto.payback} meses\n")


print("-- Avaliação do Projeto --")
print("Entres ambos paineis, com base de 0 a 5 pontos o seu projetos tem:")
pontos = projeto.AvaliarProjeto(empresa.custoEnergia, empresa.paybackMeta)
simularProjeto(pontos)