def recebeBoleto() -> float:
    '''Recebe o valor gasto com energia elétrica pela empresa.
    Args:
        Não possui argumentos.
    Returns:
        float: O valor gasto com energia.
    '''
    while True:
        try:
            boleto: float = float(input("Insira o valor do gasto na conta de energia em reais. EX: 200.\nR: "))
            if boleto > 0:
                return boleto
            else:
                print("O valor gasto precisa ser maior que zero. Tente novamente.\n")
        except ValueError:
            print("Tente novamente com um valor númerico.\n")

def recebeNomeEmpresa() -> str:
    # Recebe o nome da empresa
    while True:
        nomeEmpresa = input("Insira o nome do projeto/prédio que deseja substituir a energia: ")
        if nomeEmpresa == "":
            print("Nome da empresa não pode estar vazio. Tente novamente\n")
        else:
            return nomeEmpresa

def recebeOrcamento() -> float:
    while True:
        try:
            orcamento = float(input("Valor do orçamento que deseja investir o projeto em reais. EX: 100.\nR: "))
            if orcamento > 0:
                return orcamento
            else:
                print("O valor do orçamento precisa ser maior que zero. Tente novamente.\n")
        except ValueError:
            print("Tente novamente com um valor númerico.\n")

def recebeTipoPainel() -> int:
    while True:
        try:
            tipoPainel = int(input("Digite o tipo de painel a ser utilizado:\n1 - 410w\n2 - 655w\n"))
            if tipoPainel == 1 or tipoPainel == 2:
                return tipoPainel
            else:
                print("Digite um valor entre 1 e 2.\n")
        except ValueError:
            print("Tente novamente com um valor númerico.\n")

def recebePaybackMeta() -> int:
    while True:
        try:
            paybackMeta = int(input("Digite a meta de payback: "))
            if paybackMeta > 0:
                return paybackMeta
            else:
                print("O valor da meta de payback precisa ser maior que zero. Tente novamente.\n")
        except ValueError:
            print("Tente novamente com um valor númerico.\n")