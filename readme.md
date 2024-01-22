# Jogo da cobrinha

### biblioteca necessária

`pip install pygame`

## Introdução

Neste jogo da cobrinha, desenvolvido em Python com a biblioteca pygame, algumas estruturas de dados fundamentais foram usadas para gerenciar o estado do jogo. Aqui está a demonstração de como essas estruturas são aplicadas.

**lista (list):**

*utilização:* na representação da cobra, cada segmento é um elemento na lista. a ordem dos elementos reflete a ordem dos segmentos no corpo da cobra.

**Exemplo:**

`self.cobra = [[100, 100], [90, 100], [80, 100]]`

*lista para coordenadas:*

utilização: para a comida, uma lista de coordenadas é usada. cada elemento contém as coordenadas x e y da comida.

**Exemplo:**

`comida = [random.randrange(1, (largura//tamanho_celula)) * tamanho_celula,
          random.randrange(1, (altura//tamanho_celula)) * tamanho_celula]`

*fila (simulado com inserção e remoção de elementos):*

*utilização*: apesar de não ser explicitamente uma fila, a lógica de inserção (adicionando segmentos da cobra) no fim da lista e remoção (retirando a cabeça) no início simula um comportamento de fila. isso garante que a cobra mantenha seu tamanho correto.

**Exemplo:**

`nova_cabeca = [self.cobra[0][0] + tamanho_celula, self.cobra[0][1]]
self.cobra.insert(0, nova_cabeca)`

## Resumo

Essas estruturas de dados revelaram-se fundamentais para o funcionamento do jogo, desde o rastreamento da posição da cobra até a geração de comida aleatória no tabuleiro. Além disso, a aritmética modular é utilizada para ajustar as posições e permitir que a cobra transponha os limites do tabuleiro. Espero que isso ajude a compreender como as estruturas de dados têm um papel crucial neste jogo.
