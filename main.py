import pygame, math, settings


pygame.init()
game_window = pygame.display.set_mode((settings.width, settings.height))
pygame.display.set_caption(f"{settings.title}")
clock = pygame.time.Clock()

def startProgram():
    running = True

    center_x, center_y = settings.width // 2, settings.height // 2
    radius = 100
    vertex_count = 5

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        game_window.fill((0,0,0))

        vertices = [
            (
                center_x + radius * math.cos(2 * math.pi * i / vertex_count),
                center_y + radius * math.sin(2 * math.pi * i / vertex_count),
            )
            for i in range(vertex_count)
        ]

        pygame.draw.polygon(game_window, (255, 255, 255), vertices)

        button_pressed = pygame.key.get_pressed()
        if vertex_count >= 4:
            if button_pressed[pygame.K_UP]:
                vertex_count += 1
            if button_pressed[pygame.K_DOWN]:
                vertex_count -= 1
        print(vertex_count)

        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    startProgram()