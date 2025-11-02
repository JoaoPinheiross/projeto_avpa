class Painel:
    # Atributos
    quantidade: int = 0
    geracaoEnergia: float = 0.0
    custo: float = 0.0
    manutencao: float = 0.0
    irradiacao: float = 4.6

    # Construtor
    def __init__(self, potencia: int, eficiencia: float, tempoVida: int) -> None:
        self.potencia: float = potencia
        self.eficiencia = eficiencia
        self.tempoVida = tempoVida

    # Métodos
    def calcularQuantidade(self, gastoEnergia: float) -> None:
        '''Calcula a quantidade de paineis necessários para cobrir o gasto de energia da empresa.
        Args:
            gastoEnergia (float): Gasto de energia da empresa.
        Returns:
            Não possui retornos.
        '''
        self.quantidade =  int(gastoEnergia // self.geracaoEnergia) # gasto de energia // energia gerada pelo painel
        if (self.quantidade == 0):
            self.quantidade += 1

    def calcularGeracaoEnergia(self):
        '''Calcula a geração de energia do painel solar.
        Args:
            Não possui argumentos.
        Returns:
            Não possui retornos.
        '''
        self.geracaoEnergia = self.potencia * self.irradiacao * self.eficiencia * 30 // 1000 # 30 = dias do Mês, 1000 = Tonelada

    def calcularCusto(self):
        '''Calcula o custo de compra dos paineis solares.
        Args:
            Não possui argumentos.
        Returns:
            Não possui retornos.
        '''
        self.custo = self.quantidade * self.potencia * (self.potencia / 100)

    def calcularManutencao(self):
        '''Calcula o custo de manutenção dos paineis.
        Args:
            Não possui argumentos.
        Returns:
            Não possui retornos.
        '''
        self.manutencao = self.potencia // 0.870

class Empresa:
    # Atributos
    tarifa = 0.68

    # Construtor
    def __init__(self, custoEnergia: float) -> None:
        self.custoEnergia: float = custoEnergia
        self.gastoEnergia: float = custoEnergia * self.tarifa
        self.emissaoCo2Kg: float = self.gastoEnergia * 0.289 * 1000 # Gasto de energia(Kws) * fator de emissão * 1000(para transformação em Kg)

class Projeto:
    # Construtor
    def __init__(self, nome: str, orcamento: float, painel: Painel) -> None:
        self.nome: str = nome
        self.orcamento: float = orcamento
        self.orcamento4: float = orcamento // 4
        self.painel: Painel = painel