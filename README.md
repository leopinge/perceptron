# Perceptron

Implementação da rede neural Perceptron em Python

O programa aprende a classificar amostras em duas categorias (A ou B) a partir dos exemplos do arquivo `amostras_1200_lenta.csv`, e depois classifica amostras novas digitadas pelo usuário.

## Clonar o repositório

https://github.com/leopinge/perceptron

```bash
git clone https://github.com/leopinge/perceptron.git
cd perceptron
```

## Como rodar

Precisa apenas do Python 3 instalado. Não há nada para instalar.

```bash
python perceptron.py
```

O programa vai pedir dois valores:

| Pergunta | Valor sugerido |
|---|---|
| Valor do bias | `-1` |
| Taxa de aprendizagem | `0.01` |

## O que aparece na tela

**1. O resultado do treinamento** — os pesos sorteados no início, os pesos aprendidos, quantas épocas foram necessárias e a acurácia:

```
----- RESULTADO DO TREINAMENTO -----
Pesos iniciais:
  w0 = 0.4717
  w1 = 0.4861
  ...
Pesos finais:
  w0 = -2.4183
  w1 = -2.7099
  ...
Epocas: 266
Acuracia: 90.0%
```

**2. O teste de uma amostra nova** — digite 5 valores separados por espaço:

```
Digite 5 valores separados por espaco (ENTER para sair): 5.948 8.0151 0.4773 -6.0567 -6.3841

Conta feita pelo perceptron:
  bias  : -2.234 * -1.0 = 2.234
  x1    : -2.5119 * 5.948 = -14.9409
  x2    : -1.6026 * 8.0151 = -12.845
  x3    : -0.6147 * 0.4773 = -0.2934
  x4    : 3.1497 * -6.0567 = -19.077
  x5    : -2.2467 * -6.3841 = 14.343
  soma  : -30.5793

Soma < 0   ->  Categoria B
```

Dá para testar quantas amostras quiser. Pressione ENTER para encerrar.

## Arquivos

| Arquivo | O que é |
|---|---|
| `perceptron.py` | O programa |
| `amostras_1200_lenta.csv` | 1200 amostras de treinamento (5 entradas + a categoria) |

## Observações

- Os pesos iniciais são aleatórios entre -1 e 1, então cada execução mostra números diferentes e um número diferente de épocas. 
- O treinamento para quando uma época inteira passa sem nenhum erro.
