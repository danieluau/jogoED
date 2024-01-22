import pygame #pip install pygame
import sys
import random

#joguinho feito para demonstrar lista e suas operaçoes

# definindo constantes
largura, altura = 400, 400
tamanho_celula = 20
fps = 10



class JogoDaCobrinha:
    def __init__(self):
        pygame.init()

        # configuração da janela do jogo
        self.tela = pygame.display.set_mode((largura, altura))
        pygame.display.set_caption("snake")

        # relógio para controlar a taxa de atualização
        self.clock = pygame.time.Clock()

        # inicialização da cobra
        self.reiniciarjogo()

    def reiniciarjogo(self):
        self.cobra = [[100, 100], [90, 100], [80, 100]]  # lista de coordenadas dos segmentos da cobra
        self.direcao = 'direita'  # direção inicial da cobra

        # posição inicial da comida e geração da primeira comida
        self.comida = self.gerandocomida()

    def gerandocomida(self):
        # gera uma nova posição para a comida
        comida = [random.randrange(1, (largura // tamanho_celula)) * tamanho_celula,
                  random.randrange(1, (altura // tamanho_celula)) * tamanho_celula]

        # certifica-se de que a comida não está na mesma posição da cobra
        while comida in self.cobra:
            comida = [random.randrange(1, (largura // tamanho_celula)) * tamanho_celula,
                      random.randrange(1, (altura // tamanho_celula)) * tamanho_celula]

        return comida



    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self.atualizar_direcao(event.key)

            self.atualizar()
            self.desenhar()

            pygame.display.flip()
            self.clock.tick(fps)

    def atualizar_direcao(self, key):
        # atualiza a direção da cobra com base na tecla pressionada
        if key == pygame.K_UP and self.direcao != 'baixo':
            self.direcao = 'cima'
        elif key == pygame.K_DOWN and self.direcao != 'cima':
            self.direcao = 'baixo'
        elif key == pygame.K_LEFT and self.direcao != 'direita':
            self.direcao = 'esquerda'
        elif key == pygame.K_RIGHT and self.direcao != 'esquerda':
            self.direcao = 'direita'

    def atualizar(self):
        # atualiza a posição da cabeça da cobra com base na direção
        if self.direcao == 'cima':
            nova_cabeca = [self.cobra[0][0], self.cobra[0][1] - tamanho_celula]
        elif self.direcao == 'baixo':
            nova_cabeca = [self.cobra[0][0], self.cobra[0][1] + tamanho_celula]
        elif self.direcao == 'esquerda':
            nova_cabeca = [self.cobra[0][0] - tamanho_celula, self.cobra[0][1]]
        elif self.direcao == 'direita':
            nova_cabeca = [self.cobra[0][0] + tamanho_celula, self.cobra[0][1]]

        # ajusta as coordenadas para permitir que a cobra atravesse os limites
        nova_cabeca[0] = nova_cabeca[0] % largura
        nova_cabeca[1] = nova_cabeca[1] % altura

        # verifica se a cobra colidiu com o próprio corpo
        if nova_cabeca in self.cobra[1:]:
            self.reiniciarjogo()

        # verifica se a cobra atingiu a posição da comida
        if nova_cabeca == self.comida:
            self.cobra.append(self.comida)  # adiciona a comida à cauda da cobra
            self.comida = self.gerandocomida()  # gera nova comida
        else:
            # remove a cauda se a cobra não comeu
            self.cobra.pop()

        # adiciona a nova cabeça à cobra
        self.cobra.insert(0, nova_cabeca)

    def desenhar(self):
        self.tela.fill((4, 31, 38))  # preenche o fundo com a nova cor verde pastel

        # desenha a cobra
        for i, segmento in enumerate(self.cobra):
            cores_cobra = [(173, 216, 230), (135, 206, 250)]  # cabeça azul pastel, corpo azul claro pastel
            cor_cabeca = cores_cobra[0] if i == 0 else cores_cobra[1]
            pygame.draw.rect(self.tela, cor_cabeca, (segmento[0], segmento[1], tamanho_celula, tamanho_celula))

        # desenha a comida
        cor_comida = (242, 167, 26)  # amarelo
        pygame.draw.rect(self.tela, cor_comida, (self.comida[0], self.comida[1], tamanho_celula, tamanho_celula))



# inicia o jogo
jogo = JogoDaCobrinha()
jogo.run()