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

pontos = projeto.AvaliarProjeto(empresa.custoEnergia, empresa.paybackMeta)

simularProjeto(pontos)