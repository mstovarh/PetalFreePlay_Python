import pygame, random, sys

pygame.init()

# Aspecto de la ventana del juego
width, height = 1280, 720
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Configurar de la ventana del juego
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("PetalFree")

# Cargar imágenes
def cargar_imagenes():
    images = []
    for i in range(9):
        petal_image = pygame.image.load(f"petal{i}.png")
        images.append(petal_image)
    return images

# Seleccionar palabra aleatoria
def seleccionar_palabra(palabras):
    return random.choice(palabras)

# Dibujar texto en la ventana
def dibujar_texto(texto, font, color, x, y):
    text_surface = font.render(texto, True, color)
    win.blit(text_surface, (x, y))

# Juego principal
def juego():
    # Palabras para adivinar
    palabras = ["orquidea", "rosa", "tulipan", "dalia", "lirio"]

    # Cargar imágenes
    images = cargar_imagenes()

    # Seleccionar palabra aleatoria
    palabra = seleccionar_palabra(palabras)

    # Letras adivinadas
    letras_adiv = []

    # Vidas restantes
    vidas = 8

    # Fuente para el texto
    font = pygame.font.Font(None, 36)

    # Bucle principal del juego
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key >= pygame.K_a and event.key <= pygame.K_z:
                    letter = chr(event.key)
                    letras_adiv.append(letter)
                    if letter not in palabra:
                        vidas -= 1

        # Limpiar la ventana
        win.fill(WHITE)

        # Mostrar la palabra a adivinar
        display_word = ""
        for char in palabra:
            if char in letras_adiv:
                display_word += char + " "
            else:
                display_word += "_ "

        dibujar_texto(display_word, font, BLACK, 50, 50)

        # Mostrar las letras adivinadas
        texto_adiv = "Letras adivinadas: " + ", ".join(letras_adiv)
        dibujar_texto(texto_adiv, font, BLACK, 50, 100)

        # Mostrar la imagen de la flor
        win.blit(images[vidas], (150, 200))

        # Verificar el resultado del jugador
        if all(letter in letras_adiv for letter in palabra):
            dibujar_texto("¡Has ganado!", font, BLACK, 50, 300)
            pygame.display.flip()
            sys.exit()

        if vidas == 0:
            dibujar_texto("¡Has perdido!", font, BLACK, 50, 300)
            pygame.display.flip()
            sys.exit()

        pygame.display.flip()

juego()

pygame.quit
