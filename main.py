from Classes import Projeto, Painel, Empresa
from entradas import recebeBoleto, recebeNomeEmpresa, recebeOrcamento, recebeTipoPainel

boleto: float = recebeBoleto()
empresa: Empresa = Empresa(boleto)

nomeEmpresa = recebeNomeEmpresa()
orcamento = recebeOrcamento()

tipoPainel = recebeTipoPainel()
if tipoPainel == 1:
    painel = Painel(410, 0.79, 10)
else:
    painel = Painel(655, 0.75, 12)

projeto = Projeto(nomeEmpresa, orcamento, painel)