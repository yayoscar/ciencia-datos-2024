import pygame
import random

# Inicializar pygame
pygame.init()

# Colores
BLANCO = (245, 245, 245)
NEGRO = (0, 0, 0)
VERDE = (0, 200, 0)
AZUL_OSCURO = (0, 0, 128)
ROJO = (200, 0, 0)
NARANJA = (255, 140, 0)

# Tamaño de pantalla
ANCHO = 600
ALTO = 400

# Tamaño de la serpiente y velocidad
bloque = 20
velocidad = 5

# Fuente
fuente = pygame.font.SysFont("Bauhaus 93", 25)

# Crear pantalla y reloj
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Snake Game con Puntos")
reloj = pygame.time.Clock()

# Variable para guardar el récord más alto
record = 0

def mostrar_puntaje(puntos, record):
    texto = fuente.render(f"Puntos: {puntos}   Récord: {record}", True, AZUL_OSCURO)
    pantalla.blit(texto, [10, 10])

def dibujar_serpiente(bloque, lista_serpiente):
    for segmento in lista_serpiente:
        pygame.draw.rect(pantalla, VERDE, [segmento[0], segmento[1], bloque, bloque], border_radius=3)

def juego():
    global record

    x = ANCHO // 2
    y = ALTO // 2
    x_cambio = 0
    y_cambio = 0

    lista_serpiente = []
    largo_serpiente = 1
    puntos = 0

    comida_x = round(random.randrange(0, ANCHO - bloque) / bloque) * bloque
    comida_y = round(random.randrange(0, ALTO - bloque) / bloque) * bloque

    game_over = False
    game_close = False

    while not game_over:

        while game_close:
            pantalla.fill(BLANCO)
            mensaje = fuente.render("Presiona C para continuar, Q para salir", True, ROJO)
            pantalla.blit(mensaje, [ANCHO // 8, ALTO // 3])
            mostrar_puntaje(puntos, record)
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif evento.key == pygame.K_c:
                        return  # Sale del juego actual y vuelve a comenzar

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT and x_cambio == 0:
                    x_cambio = -bloque
                    y_cambio = 0
                elif evento.key == pygame.K_RIGHT and x_cambio == 0:
                    x_cambio = bloque
                    y_cambio = 0
                elif evento.key == pygame.K_UP and y_cambio == 0:
                    y_cambio = -bloque
                    x_cambio = 0
                elif evento.key == pygame.K_DOWN and y_cambio == 0:
                    y_cambio = bloque
                    x_cambio = 0

        x += x_cambio
        y += y_cambio

        if x < 0 or x >= ANCHO or y < 0 or y >= ALTO:
            game_close = True

        pantalla.fill(BLANCO)
        pygame.draw.rect(pantalla, NARANJA, [comida_x, comida_y, bloque, bloque])  # comida

        cabeza = [x, y]
        lista_serpiente.append(cabeza)
        if len(lista_serpiente) > largo_serpiente:
            del lista_serpiente[0]

        for segmento in lista_serpiente[:-1]:
            if segmento == cabeza:
                game_close = True

        dibujar_serpiente(bloque, lista_serpiente)
        mostrar_puntaje(puntos, record)
        pygame.display.update()

        # Comer comida
        if x == comida_x and y == comida_y:
            comida_x = round(random.randrange(0, ANCHO - bloque) / bloque) * bloque
            comida_y = round(random.randrange(0, ALTO - bloque) / bloque) * bloque
            largo_serpiente += 1
            puntos += 1
            if puntos > record:
                record = puntos

        reloj.tick(velocidad)

    pygame.quit()
    quit()

# Bucle principal del juego
while True:
    juego()