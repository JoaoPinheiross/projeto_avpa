def recebeBoleto() -> float:
    '''Recebe o valor gasto com energia elétrica pela empresa.
    Args:
        Não possui argumentos.
    Returns:
        float: O valor gasto com energia.
    '''
    while True:
        # Tenta receber o valor gasto
        try:
            boleto: float = float(input("\nInsira o valor do gasto na conta de energia em reais. EX: 200.\nR: "))
            if boleto > 0:
                return boleto # retorna o valor gasto 
            else:
                # Se não for digitado um número maior que zero
                print("O valor gasto precisa ser maior que zero. Tente novamente.\n")
        except ValueError:
            # Caso não for digitado um valor númerico
            print("Tente novamente com um valor númerico.\n")

def recebeNomeProjeto() -> str:
    '''Recebe o nome do projeto a ser avaliado.
    Args:
        Não possui argumentos.
    Returns:
        str: O nome do projeto.
    '''
    while True:
        # Recebe o nome do projeto
        nomeProjeto = input("Insira o nome do projeto/prédio que deseja substituir a energia: ")
        if nomeProjeto == "":
            # Se o nome estiver vazio
            print("Nome da empresa não pode estar vazio. Tente novamente\n")
        else:
            return nomeProjeto

def recebeOrcamento() -> float:
    '''Recebe o orçamento do projeto.
    Args:
        Não possui argumentos.
    Returns:
        flaot: O orçamento do projeto.
    '''
    while True:
        # Tenta receber o orçamento
        try:
            orcamento = float(input("\nValor do orçamento que deseja investir o projeto em reais. EX: 100.\nR: "))
            if orcamento > 0:
                return orcamento
            else:
                # Se não for digitado um número maior que zero
                print("O valor do orçamento precisa ser maior que zero. Tente novamente.\n")
        except ValueError:
            # Caso não for digitado um valor númerico
            print("Tente novamente com um valor númerico.\n")

def recebeTipoPainel() -> int:
    '''Recebe o tipo de painel que irá ser utilizado no projeto.
    Args:
        Não possui argumentos.
    Returns:
        int: O número correspondente ao tipo de painel.
    '''
    while True:
        # Tenta receber o tipo de painel
        try:
            tipoPainel = int(input("\nDigite o tipo de painel a ser utilizado:\n1 - 410w\n2 - 655w\n"))
            if tipoPainel == 1 or tipoPainel == 2:
                return tipoPainel
            else:
                # Se não for digitado nenhum dos dois tipos de painéis
                print("Digite um valor entre 1 e 2.\n")
        except ValueError:
            # Caso não for digitado um valor númerico
            print("Tente novamente com um valor númerico.\n")

def recebePaybackMeta() -> int:
    '''Recebe a Meta de payback definida pela empresa para o projeto.
    Args:
        Não possui argumentos.
    Returns:
        int: A meta de payback.
    '''
    while True:
        # Tenta receber a meta de payback
        try:
            paybackMeta = int(input("\nDigite a meta de payback do projeto: "))
            if paybackMeta > 0:
                return paybackMeta
            else:
                # Se não for digitado um número maior que zero
                print("O valor da meta de payback precisa ser maior que zero. Tente novamente.\n")
        except ValueError:
            # Caso não for digitado um valor númerico
            print("Tente novamente com um valor númerico.\n")