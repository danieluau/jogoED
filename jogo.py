import pygame
import sys
import random

# definindo constantes
largura, altura = 400, 400
tamanho_celula = 20
fps = 10

class JogoCobrinha:
    def __init__(self):
        pygame.init()

        # configuração da janela do jogo
        self.tela = pygame.display.set_mode((largura, altura))
        pygame.display.set_caption("Jogo da Cobrinha")

        # relógio para controlar a taxa de atualização
        self.clock = pygame.time.Clock()

        # inicialização da cobra
        self.cobra = [[100, 100], [90, 100], [80, 100]]  # lista de coordenadas dos segmentos da cobra
        self.direcao = 'DIREITA'  # direção inicial da cobra

        # posição inicial da comida e geração da primeira comida
        self.comida = self.gerar_comida()

    def gerar_comida(self):
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
        if key == pygame.K_UP and self.direcao != 'BAIXO':
            self.direcao = 'CIMA'
        elif key == pygame.K_DOWN and self.direcao != 'CIMA':
            self.direcao = 'BAIXO'
        elif key == pygame.K_LEFT and self.direcao != 'DIREITA':
            self.direcao = 'ESQUERDA'
        elif key == pygame.K_RIGHT and self.direcao != 'ESQUERDA':
            self.direcao = 'DIREITA'

    def atualizar(self):
        # atualiza a posição da cabeça da cobra com base na direção
        if self.direcao == 'CIMA':
            nova_cabeca = [self.cobra[0][0], self.cobra[0][1] - tamanho_celula]
        elif self.direcao == 'BAIXO':
            nova_cabeca = [self.cobra[0][0], self.cobra[0][1] + tamanho_celula]
        elif self.direcao == 'ESQUERDA':
            nova_cabeca = [self.cobra[0][0] - tamanho_celula, self.cobra[0][1]]
        elif self.direcao == 'DIREITA':
            nova_cabeca = [self.cobra[0][0] + tamanho_celula, self.cobra[0][1]]

        # ajusta as coordenadas para permitir que a cobra atravesse os limites
        nova_cabeca[0] = nova_cabeca[0] % largura
        nova_cabeca[1] = nova_cabeca[1] % altura

        # adiciona a nova cabeça à cobra
        self.cobra.insert(0, nova_cabeca)

        # verifica se a cobra comeu a comida
        if nova_cabeca == self.comida:
            self.comida = self.gerar_comida()  # gera nova comida
        else:
            # remove a cauda se a cobra não comeu
            self.cobra.pop()

    def desenhar(self):
        self.tela.fill((255, 255, 255))  # preenche o fundo com branco

        # desenha a cobra
        for i, segmento in enumerate(self.cobra):
            cor = (0, 255, 0) if i == 0 else (0, 200, 0)  # cabeça verde, corpo verde escuro
            pygame.draw.rect(self.tela, cor, (segmento[0], segmento[1], tamanho_celula, tamanho_celula))

        # desenha a comida
        pygame.draw.rect(self.tela, (255, 0, 0), (self.comida[0], self.comida[1], tamanho_celula, tamanho_celula))

# inicia o jogo
jogo = JogoCobrinha()
jogo.run()
