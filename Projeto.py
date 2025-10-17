class Projeto:
    # Parâmetros definidos pela empresa para comparação
    GERACAO_CO2: float = 784.5
    PAYBACK: int = 3
    CONSUMOENERGIA:float = 50000
    GERACAOENERGIA: float = 50000 * 0.80 # 80% do consumo de energia 
    REDUCAOCO2: float = 1000

    # Construtor
    def __init__(self, nome: str, payback: int, geracaoEnergia: float) -> None:
        self.nome = nome
        self.payback = payback
        self.geracao = geracaoEnergia
        self.geracaoCo2 = geracaoEnergia * 0.035