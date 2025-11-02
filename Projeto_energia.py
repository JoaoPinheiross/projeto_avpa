#Classe - Empresa
empresa_nome=input("Insira o nome do projeto/prédio que deseja substituir a energia: ")
orcamento=int(input("Valor do orçamento que deseja investir o projeto em reais. EX: 100.\nR: "))
orcamento4=orcamento//4

#Classe - Energia
tarifa=0.68
boleto=int(input("Insira o valor do gasto na conta de energia em reais. EX: 200.\nR: "))
energia_gerada=boleto*tarifa 
energia_emissao=energia_gerada655*0.0289*1000

#Classe - Painel
painel_energia655=655*4.6*0.75*30//1000
painel_energia410=410*4.6*0.79*30//1000
painel_410qtde=(energia_gerada//painel_energia410)
if painel_410qtde==0:
    painel_410qtde+=1
painel_655qtde=(energia_gerada//painel_energia655)
if painel_655qtde==0:
    painel_655qtde+=1
painel_custo410=painel_410qtde*0.65*410
painel_custo655=painel_655qtde*0.65*655
meses41=0
painel_ano41=10
meses65=0
painel_ano65=12
painel_manutencao41=painel_energia410//0.874
painel_manutencao65=painel_energia655//0.874
painel_eco65= boleto-painel_manutencao65
painel_eco41= boleto-painel_manutencao41

print(f"energia gerada: {energia_gerada:1.0f}kWh. acabando gerando cerca de {energia_emissao:.2f}Kg de emissões.")
print("Baseando-se no painel solar de 410Wp e 655Wp, o seu projeto teria como diferença entre os paineis de:")
print(f"{painel_410qtde:1.0f} paineis de 410WP e {painel_655qtde:1.0f} paineis de 655Wp")
print(f"custo de 410Wp:{painel_custo410:1.0f} \nCusto de 655Wp:{painel_custo655:1.0f}")
print(f"economizou entre os paineis[410/655]:\n[{painel_eco41}/{painel_eco65}]")

while painel_eco41<painel_custo410:
    meses41+=1
    if meses41%12==0:
        painel_ano41-=1
    painel_eco41+=painel_eco41
    valor_total41=painel_eco41 #valor total com as economias guardadas

while painel_eco65<painel_custo410:
    meses65+=1
    if meses65%12==0:
        painel_ano41-=1
    painel_eco65+=painel_eco65
    valor_total65=painel_eco65 #valor total com as economias guardadas
print("Payback com os paineis de 410Wp:")
print(f"payback de {meses41} meses, aproveitando o resto de {painel_ano41-1} anos e {12-meses41} meses do tempo de vida dos paineis")
print("Payback com os paineis de 655Wp:")
print(f"payback de {meses65} meses, aproveitando o resto de {painel_ano65-1} anos e {12-meses65} meses do tempo de vida dos paineis")
print("Entres ambos paineis, com base de 0 a 4 pontos o seu projetos tem")

pontos41=0
if valor_total41 > boleto:
    pontos41=pontos41+1
    print("Conseguiu ter mais dinheiro economizado do que gastava antes")

if painel_custo410<=(orcamento4):
    pontos41=pontos41+3
    print("Orçamento baixo")
if painel_custo410<orcamento and painel_custo410 >= orcamento4:
    pontos41=pontos41+2
    print("Orçamento Medio")
if painel_custo410>=orcamento:
    pontos41=pontos41+1
    print("Orçamento estourado")
print(f"Você adquiriu {pontos41}/4 pontos com a Instalação de 410Wp.")

pontos65=0
if valor_total65 > boleto:
    pontos65=pontos65+1
    print("Conseguiu ter mais dinheiro economizado do que gastava antes")
if painel_custo655<=(orcamento4):
    pontos65=pontos65+3
    print("Orçamento baixo")
if painel_custo655<orcamento and painel_custo655 >= orcamento4:
    pontos65=pontos65+2
    print("Orçamento Medio")
if painel_custo655>=orcamento:
    pontos65=pontos65+1
    print("Orçamento estourado")
print(f"Você adquiriu {pontos65}/4 pontos com a instalação de paineis de 655Wp.")


