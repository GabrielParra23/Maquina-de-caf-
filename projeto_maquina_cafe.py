# TODO 1. importar nossas bibliotecas
from menu import MENU, recursos
from replit import clear

# TODO 2. perguntar ao usuário que tipo de café ele vai querer e seu preço após a escolha


def maquina_cafe():
    jogo = "S"
    print("Bem vindo a maquina de café")
    while jogo == "S":
        escolha = input("Qual café voce ira querer hoje \"Expresso\", \"Latte\" ou \"Cappuccino\"").lower()
        # TODO 3. caso o usuário digite reportar então ira mostrar os recursos que restão
        if escolha == 'reportar':
            print(recursos)
        else:
            cafe = tipos(escolha)
            moedas = moeda()

            print(f"O total de moedas que voce inseriu foi de {moedas:_.2f}")
            # TODO 5. retirar dos recursos os ingredientes necessarios para produzir o café
            if moedas >= MENU[cafe]['custo']:
                if recursos['aguá'] >= MENU[cafe]['ingredientes']['aguá'] and recursos['café'] >= \
                        MENU[cafe]['ingredientes']['café']:
                    recursos['aguá'] -= MENU[cafe]['ingredientes']['aguá']
                    recursos['café'] -= MENU[cafe]['ingredientes']['café']
                    if MENU[cafe] != "expresso":
                        if recursos['leite'] >= MENU[cafe]['ingredientes']['leite']:
                            recursos['leite'] -= MENU[cafe]['ingredientes']['leite']
                    # TODO 6. dar o café para o usuário e diminuir as moedas para zero
                    print(f"Aqui está o seu {cafe}")
                else:
                    print("não é possível fazer o seu café por falta de recursos")
            else:
                print("Voce não colocou dinheiro suficiente, volte outra hora")
            recolocar = input("Deseja recolocar os recursos para fazer o café \"S\" ou \"N\"").lower()
            if recolocar == 's':
                recursos['aguá'] = 300
                recursos['leite'] = 200
                recursos['café'] = 100
        jogo = input("Deseja fazer mais algum café  \"S\" ou \"N\"").lower()


def tipos(decisao):
    if decisao == "expresso":
        print(f"O custo é de {MENU['expresso']['custo']} R$")
        return 'expresso'

    elif decisao == "latte":
        print(f"O custo é de {MENU['latte']['custo']} R$")
        return 'latte'

    elif decisao == "cappuccino":
        print(f"O custo é de {MENU['cappuccino']['custo']} R$")
        return 'cappuccino'

    # TODO 4. adicionar as moedas para pagar o pedido / caso não seja colocado moedas o suficiente o dinheiro seja
    #  reembolsado e terá um aviso de falta de moedas


def moeda():
    moeda1 = float(input("Quantas moedas de 1 centavo quer inserir? ")) * 0.01
    moeda2 = float(input("Quantas moedas de 5 centavos quer inserir? ")) * 0.05
    moeda3 = float(input("Quantas moedas de 10 centavos quer inserir? ")) * 0.10
    moeda4 = float(input("Quantas moedas de 25 centavos quer inserir? ")) * 0.25

    return moeda1 + moeda2 + moeda3 + moeda4


maquina_cafe()

# ALT + SHIFT seleciona para fazer varias coisas ao mesmo tempo
