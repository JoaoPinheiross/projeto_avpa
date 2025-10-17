class Projeto:
    PAYBACK = 3
    CONSUMOENERGIA = 15000
    GERACAOENERGIA = 15000 * 0.80

    def __init__(self, nome: str, payback: int, geracaoEnergia: float) -> None:
        self.nome = nome
        self.payback = payback
        self.geracao = geracaoEnergia