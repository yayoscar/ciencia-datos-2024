import pygame
import random

# Inicializar Pygame
pygame.init()

# Configuración de pantalla
ANCHO = 500
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("🚀 Esquiva Meteoritos")

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)

# Reloj para controlar FPS
clock = pygame.time.Clock()
FPS = 60

# Fuente para puntaje
fuente = pygame.font.SysFont("arial", 30)

# Clase Jugador
class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 40))
        self.image.fill(ROJO)
        self.rect = self.image.get_rect()
        self.rect.centerx = ANCHO // 2
        self.rect.bottom = ALTO - 10
        self.velocidad = 5

    def update(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocidad
        if teclas[pygame.K_RIGHT] and self.rect.right < ANCHO:
            self.rect.x += self.velocidad

# Clase Meteorito
class Meteorito(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill((128, 128, 128))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, ANCHO - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        self.velocidad = random.randint(3, 8)

    def update(self):
        self.rect.y += self.velocidad
        if self.rect.top > ALTO:
            # Cuando se va del todo hacia abajo, lo reseteamos
            self.rect.x = random.randint(0, ANCHO - self.rect.width)
            self.rect.y = random.randint(-100, -40)
            self.velocidad = random.randint(2, 4)
            return True  # Aquí sí pasó el límite
        return False

# Crear grupos de sprites
todos_los_sprites = pygame.sprite.Group()
meteoritos = pygame.sprite.Group()

jugador = Jugador()
todos_los_sprites.add(jugador)

for _ in range(8):
    m = Meteorito()
    todos_los_sprites.add(m)
    meteoritos.add(m)

# Variables de juego
puntuacion = 0
jugando = True

# Bucle principal
while jugando:
    clock.tick(FPS)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False

    # Actualizar
    todos_los_sprites.update()

    # Verificar colisión
    colisiones = pygame.sprite.spritecollide(jugador, meteoritos, False)
    if colisiones:
        jugando = False

    # Aumentar puntuación
    # Actualizar todos los sprites y verificar si alguno reinició
    for m in meteoritos:
        reiniciado = m.update()
        if reiniciado:
            puntuacion += 1

    # Dibujar
    pantalla.fill(NEGRO)
    todos_los_sprites.draw(pantalla)

    texto = fuente.render(f"Puntos: {puntuacion}", True, BLANCO)
    pantalla.blit(texto, (10, 10))

    pygame.display.flip()

pygame.quit()