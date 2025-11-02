class Painel:
    # Atributos
    quantidade: int = 0
    geracaoEnergia: float = 0.0
    custo: float = 0.0
    manutencao: float = 0.0
    economia: float = 0.0
    irradiacao: float = 4.6

    # Construtor
    def __init__(self, potencia: int, eficiencia: float, tempoVida: int, gastoEnergia: float, boleto: float) -> None:
        self.potencia: float = potencia
        self.eficiencia = eficiencia
        self.tempoVida = tempoVida
        self.calcularCusto(gastoEnergia)
        self.calcularEconomia(boleto)

    # Métodos
    def calcularQuantidade(self, gastoEnergia: float) -> None:
        '''Calcula a quantidade de paineis necessários para cobrir o gasto de energia da empresa.
        Args:
            gastoEnergia (float): Gasto de energia da empresa.
        Returns:
            Não possui retornos.
        '''
        self.calcularGeracaoEnergia()
        self.quantidade =  int(gastoEnergia // self.geracaoEnergia) # gasto de energia // energia gerada pelo painel
        if (self.quantidade == 0):
            self.quantidade += 1

    def calcularGeracaoEnergia(self) -> None:
        '''Calcula a geração de energia do painel solar.
        Args:
            Não possui argumentos.
        Returns:
            Não possui retornos.
        '''
        self.geracaoEnergia = self.potencia * self.irradiacao * self.eficiencia * 30 // 1000 # 30 = dias do Mês, 1000 = Tonelada

    def calcularCusto(self, gastoEnergia) -> None:
        '''Calcula o custo de compra dos paineis solares.
        Args:
            gastoEnergia (float): Gasto de energia da empresa.
        Returns:
            Não possui retornos.
        '''
        self.calcularQuantidade(gastoEnergia)
        self.custo = self.quantidade * self.potencia * (self.potencia / 1000)

    def calcularManutencao(self) -> None:
        '''Calcula o custo de manutenção dos paineis.
        Args:
            Não possui argumentos.
        Returns:
            Não possui retornos.
        '''
        self.manutencao = self.geracaoEnergia // 0.874

    def calcularEconomia(self, boleto) -> None:
        '''Calcula a economia oriunda dos painéis solares.
        Args:
            boleto (float): Custo com energia elétrica da empresa.
        Returns:
            Não possui retornos.
        '''
        self.calcularManutencao()
        self.economia = boleto - self.manutencao

class Empresa:
    # Atributos
    tarifa = 0.68

    # Construtor
    def __init__(self, custoEnergia: float) -> None:
        self.custoEnergia: float = custoEnergia
        self.gastoEnergia: float = custoEnergia * self.tarifa
        self.emissaoCo2Kg: float = self.gastoEnergia * 0.289 * 1000 # Gasto de energia(Kws) * fator de emissão * 1000(para transformação em Kg)

class Projeto:
    # Atributos
    payback: int = 0

    # Construtor
    def __init__(self, nome: str, orcamento: float, painel: Painel) -> None:
        self.nome: str = nome
        self.orcamento: float = orcamento
        self.orcamento4: float = orcamento // 4
        self.painel: Painel = painel
        self.economiaProjeto: float = self.calcularPayback()
    
    def calcularPayback(self) -> float:
        tempoVida = self.painel.tempoVida
        valorTotal = self.painel.economia
        while valorTotal < self.painel.custo:
            self.payback += 1
            if self.payback % 12 == 0:
                tempoVida -= 1
            valorTotal += self.painel.economia * 2
        return valorTotal
    
    def AvaliarProjeto(self, boleto: float):
        pontos=0

        # Avalia economia
        if self.economiaProjeto > boleto:
            pontos += 1
            print("Conseguiu ter mais dinheiro economizado do que gastava antes")

        # Avalia orçamento
        if self.painel.custo <= self.orcamento4:
            pontos += 3
            print("Orçamento baixo")
        if self.painel.custo <= self.orcamento and self.painel.custo >= self.orcamento4:
            pontos += 2
            print("Orçamento Medio")
        if self.painel.custo > self.orcamento:
            pontos += 1
            print("Orçamento estourado")

        print(f"Você adquiriu {pontos}/5 pontos com a Instalação de {self.painel.potencia}Wp.")