## desafio-logica-python-c

Desafio de lógica matemática desenvolvido em Python e C para praticar fundamentos de programação.

# Desafio de Lógica — Números Unitários e de Dois Dígitos!

Um exercício de lógica de programação em **Python** para encontrar pares de números que satisfaçam uma condição matemática. O objetivo é praticar laços de repetição, operadores aritméticos e condicionais sem depender de bibliotecas externas.

## O desafio

Encontrar todos os pares de números inteiros `(u, n)` em que:

- `u` é um número unitário, de **1 a 9**;
- `n` é um número de dois dígitos, de **10 a 99**;
- a divisão de `n` por `u` é igual à soma de `u` com os dois algarismos de `n`.

Em outras palavras, se `d` é a dezena e `a` é a unidade de `n`, a condição é:

**n / u = u + d + a**

### Exemplo

Para `u = 3` e `n = 36`:

- Divisão: `36 / 3 = 12`
- Soma: `3 + 3 + 6 = 12`

Como os resultados são iguais, `(3, 36)` é uma solução válida.

## Como a solução funciona

O programa percorre as combinações possíveis de `u` e `n`, separa os algarismos do número de dois dígitos e verifica a igualdade.

Em Python, podemos obter os algarismos de `n` com:

```python
dezena = n // 10
unidade = n % 10
```

Depois, comparamos:

```python
n / u == u + dezena + unidade
```

Se a condição for verdadeira, o par é armazenado como uma solução.

## Como executar

1. Tenha o **Python 3** instalado.
2. Clone o repositório ou baixe o arquivo `.py`.
3. No terminal, execute (ajustando o nome do arquivo, se necessário):

```bash
python desafio.py
```

Não é necessário instalar dependências adicionais.

## Conceitos praticados

- Laços `for` e a função `range()`
- Condicionais `if`
- Divisão inteira (`//`) e resto da divisão (`%`)
- Comparações e operações matemáticas
- Listas e tuplas para armazenar resultados

## Tecnologias

- Python 3
- Biblioteca padrão do Python

## Sobre o projeto

Este exercício foi desenvolvido como parte da prática de fundamentos de programação e resolução de problemas. A proposta é compreender a lógica por trás da solução, em vez de apenas reproduzir o código.

