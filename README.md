# Mini projeto: Labirinto

Este projeto foi desenvolvido como parte das atividades da disciplina de **Estrutura de Dados** e segue os requisitos estabelecidos pelo professor Ricardo Nunes do Instituto Federal de Alagoas (IFAL).

## Problema

Considere um labirinto representado por uma matriz m × n. O caminho livre é marcado na matriz com " " (sem aspas), enquanto os caminhos ocupados são marcados com "#" (sem aspas). O ratinho está na posição (livre) (1, 0) e quer chegar à posição (livre) (m − 2, n − 1) passando pelo labirinto. Ele pode se mover para uma casa livre que esteja à direita, à esquerda, acima ou abaixo da casa em que está.

## Exemplo de Labirinto

![enter image description here](https://i.ibb.co/rpjVNqv/image.png)

## Gerador de Labirintos

Para facilitar a geração de labirintos de teste, foi disponibilizado o código que gera dinamicamente labiririntos: [Gerador de Labirintos](https://replit.com/@ricardorubens/gera-lab-mp2).

```python
# gera_lab.py
from gera_lab import gera_lab, print_lab

lab = gera_lab(7, 15)  # Gera um labirinto com 7 linhas e 15 colunas
print_lab(lab)  # Imprime o labirinto gerado
```

O uso desse gerador de labirintos simplifica a obtenção de labirintos para testar a implementação e verificar como o algoritmo se comporta em diferentes cenários.

## Comentários

### Abordagem do Algoritmo

Ao enfrentar o desafio de solucionar o problema proposto, o processo de desenvolvimento seguiu uma abordagem passo a passo para garantir uma implementação lógica e eficiente.

### Matriz de Labirinto

Inicialmente, optei por representar o labirinto como uma matriz estática disponibilizada no arquivo atividade.pdf . Essa matriz contém informações sobre os espaços disponíveis, os obstáculos e a posição inicial do rato. A posição inicial foi marcada com um "\*", facilitando a visualização da matriz durante a execução e depuração do código.

### Ordem de Verificação

Para determinar o próximo movimento do rato, elaborei uma ordem de verificação baseada nas direções cardeais. O processo de verificação ocorre da seguinte maneira:

1. Verificar o espaço à direita.
2. Verificar o espaço abaixo.
3. Verificar o espaço acima.
4. Verificar o espaço à esquerda.

Essa abordagem foi escolhida avaliar todas as opções disponíveis para o rato avançar.

### Considerações Especiais

Durante a verificação, levei em consideração duas condições importantes:

1. **Obstáculos:** Verifico se o próximo espaço contém um obstáculo. Caso haja um obstáculo, o rato não pode se mover para esse espaço.

2. **Visitados Anteriormente:** Implementei uma lógica para evitar revisitar espaços pelos quais o rato já passou. Dessa forma, somente os espaços não visitados e sem obstáculos são considerados disponíveis para movimento.

### Utilização de Pilhas

Para manter o controle do movimento do rato e permitir o retorno a espaços anteriores, utilizei uma pilha. Sempre que o rato avança para um novo espaço, o espaço anterior é empilhado. Isso permite que o rato faça um "backtrack" caso não encontre um caminho viável.

### Backtracking

Quando o rato encontra um beco sem saída (nenhum espaço disponível para movimento), ele realiza o processo de backtracking, retornando à posição anterior e revisando as direções restantes. Essa abordagem é repetida até que o rato encontre uma solução ou retorne à posição inicial.

### Resultado e Considerações Finais

Caso o rato não encontre um caminho para o ponto final do labirinto, o algoritmo determina que não existe uma solução possível e retorna a matriz do labirinto com os caminhos percorridos pelo rato, juntamente com o resultado "False". Caso contrario é impresso também o labirinto e o resultado como "True".

## Como Executar

Para executar o projeto, siga as instruções abaixo:

1. Clone este repositório para a sua máquina local.
2. Abra o arquivo main.py em um interpretador Python.
3. Execute o programa.
