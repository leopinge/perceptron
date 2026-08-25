import random

ARQUIVO = "amostras_1200_lenta.csv"
MAX_EPOCAS = 1000


def ler_arquivo(nome):
    arquivo = open(nome)
    linhas = arquivo.readlines()
    arquivo.close()

    entradas = []
    saidas = []

    for linha in linhas[1:]:
        linha = linha.strip()
        if linha == "":
            continue

        valores = linha.split(",")

        x = []
        for i in range(len(valores) - 1):
            x.append(float(valores[i]))
        entradas.append(x)

        if valores[-1] == "A":
            saidas.append(1)
        else:
            saidas.append(0)

    return entradas, saidas


def sortear_pesos(quantidade):
    pesos = []
    for i in range(quantidade):
        pesos.append(random.uniform(-1, 1))
    return pesos


def calcular_soma(x, pesos, bias):
    soma = pesos[0] * bias
    for i in range(len(x)):
        soma = soma + pesos[i + 1] * x[i]
    return soma


def calcular_saida(x, pesos, bias):
    soma = calcular_soma(x, pesos, bias)

    if soma >= 0:
        return 1
    else:
        return 0


def treinar(entradas, saidas, pesos_iniciais, bias, taxa):
    pesos = list(pesos_iniciais)
    epocas = 0

    while epocas < MAX_EPOCAS:
        erros = 0

        for n in range(len(entradas)):
            x = entradas[n]
            y = calcular_saida(x, pesos, bias)
            erro = saidas[n] - y

            if erro != 0:
                erros = erros + 1
                # regra de aprendizagem: peso = peso + taxa * erro * entrada
                pesos[0] = pesos[0] + taxa * erro * bias
                for i in range(len(x)):
                    pesos[i + 1] = pesos[i + 1] + taxa * erro * x[i]

        epocas = epocas + 1

        if erros == 0:
            break

    return pesos, epocas


def calcular_acuracia(entradas, saidas, pesos, bias):
    acertos = 0
    for n in range(len(entradas)):
        if calcular_saida(entradas[n], pesos, bias) == saidas[n]:
            acertos = acertos + 1
    return acertos / len(entradas) * 100


def mostrar_pesos(titulo, pesos):
    print(titulo)
    for i in range(len(pesos)):
        print("  w" + str(i) + " = " + str(round(pesos[i], 4)))


entradas, saidas = ler_arquivo(ARQUIVO)
qtd_entradas = len(entradas[0])

print("")
print("Amostras lidas:", len(entradas))
print("Entradas por amostra:", qtd_entradas)
print("")

bias = float(input("Valor do bias (ex: -1): "))
taxa = float(input("Taxa de aprendizagem (ex: 0.01): "))

pesos_iniciais = sortear_pesos(qtd_entradas + 1)
pesos, epocas = treinar(entradas, saidas, pesos_iniciais, bias, taxa)
acuracia = calcular_acuracia(entradas, saidas, pesos, bias)

print("")
print("----- RESULTADO DO TREINAMENTO -----")
mostrar_pesos("Pesos iniciais:", pesos_iniciais)
mostrar_pesos("Pesos finais:", pesos)
print("Epocas:", epocas)
print("Acuracia:", str(round(acuracia, 2)) + "%")

print("")
print("----- TESTAR NOVA AMOSTRA -----")

while True:
    print("")
    texto = input("Digite " + str(qtd_entradas) + " valores separados por espaco (ENTER para sair): ")

    if texto.strip() == "":
        break

    valores = texto.split()

    if len(valores) != qtd_entradas:
        print("Voce precisa digitar " + str(qtd_entradas) + " valores.")
        continue

    x = []
    for i in range(len(valores)):
        x.append(float(valores[i]))

    soma = calcular_soma(x, pesos, bias)

    print("")
    print("Conta feita pelo perceptron:")
    print("  bias  : " + str(round(pesos[0], 4)) + " * " + str(bias) + " = " + str(round(pesos[0] * bias, 4)))
    for i in range(len(x)):
        parcela = pesos[i + 1] * x[i]
        print("  x" + str(i + 1) + "    : " + str(round(pesos[i + 1], 4)) + " * " + str(x[i]) + " = " + str(round(parcela, 4)))
    print("  soma  : " + str(round(soma, 4)))
    print("")

    if soma >= 0:
        print("Soma >= 0  ->  Categoria A")
    else:
        print("Soma < 0   ->  Categoria B")
