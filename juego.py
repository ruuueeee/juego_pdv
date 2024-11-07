import pygame
import math

# Clases----------------------------------------------------------------------|

class Personaje():
    def __init__(self, x, y):
        self.forma = pygame.Rect(0, 0, 20, 20)
        self.forma.center = (x, y)

    def dibujar(self, interfaz):
        pygame.draw.rect(interfaz, (138, 206, 0), self.forma)

    def movimiento(self, delta_x, delta_y):
        self.forma.x += delta_x
        self.forma.y += delta_y


class Enemigo(pygame.sprite.Sprite):  
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 20)) 
        self.image.fill((255, 0, 0))  
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def mover_hacia_jugador(self, jugador_x, jugador_y, velocidad):

        if self.rect.x < jugador_x:
            self.rect.x += velocidad
        elif self.rect.x > jugador_x:
            self.rect.x -= velocidad
        if self.rect.y < jugador_y:
            self.rect.y += velocidad
        elif self.rect.y > jugador_y:
            self.rect.y -= velocidad

# --------------------------------------------------------------------------
ANCHO_VENTANA = 800  
ALTO_VENTANA = 600

jugador = Personaje(50, 50)
enemigo = Enemigo(300, 300)  # Posición inicial del enemigo

def dibujar_grid():
    for x in range(30):
        pygame.draw.line(ventana, (255, 255, 255), (x*40, 0), (x*40, 600))
        pygame.draw.line(ventana, (255, 255, 255), (0, x*40), (800, x*40))

world_data = []





grupo_enemigos = pygame.sprite.Group()
grupo_enemigos.add(enemigo)

pygame.init()
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("JUEGO FINAL")


mover_arriba = False
mover_abajo = False
mover_izquierda = False
mover_derecha = False

# Controlar el frame rate
reloj = pygame.time.Clock()

velocidad_personaje =10
while True:
    reloj.tick(60)
    ventana.fill((0, 0, 20))
    dibujar_grid()

    # Calcular movimiento del jugador
    delta_x = 0
    delta_y = 0
    if mover_derecha:
        delta_x = velocidad_personaje
    if mover_izquierda:
        delta_x = -velocidad_personaje
    if mover_arriba:
        delta_y = -velocidad_personaje
    if mover_abajo:
        delta_y = velocidad_personaje

    #jugador
    jugador.movimiento(delta_x, delta_y)
    jugador.dibujar(ventana)
    #enemigo
    enemigo.mover_hacia_jugador(jugador.forma.centerx, jugador.forma.centery, velocidad=1)
    grupo_enemigos.draw(ventana)

    # Eventos del juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                mover_izquierda = True
            if event.key == pygame.K_d:
                mover_derecha = True
            if event.key == pygame.K_w:
                mover_arriba = True
            if event.key == pygame.K_s:
                mover_abajo = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                mover_izquierda = False
            if event.key == pygame.K_d:
                mover_derecha = False
            if event.key == pygame.K_w:
                mover_arriba = False
            if event.key == pygame.K_s:
                mover_abajo = False

    pygame.display.update()