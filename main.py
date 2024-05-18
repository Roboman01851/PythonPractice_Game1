import pygame, math, settings
import time
pygame.init()
game_window = pygame.display.set_mode((settings.width, settings.height))
pygame.display.set_caption(f"{settings.title}")
clock = pygame.time.Clock()

def startProgram():
    running = True

    center_x, center_y = settings.width // 2, settings.height // 2
    radius = 100
    vertex_count = 5

    vertex_max = 100
    vertex_min = 3

    shape_color = [255, 255, 255]
    shape_color[0] -= 1
    print(shape_color)

    while running:
        clock.tick(60)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        game_window.fill((0,0,0))

        printControls(f"Up Arrow: Increase Vertex Count", 1, settings.size_of_font)
        printControls(f"Down Arrow: Decrease Vertex Count", 2, settings.size_of_font)
        printControls(f"Left Arrow: Decrease Polygon Size", 3, settings.size_of_font)
        printControls(f"Right Arrow: Increase Polygon Size", 4, settings.size_of_font)

        vertices = [
            (
                center_x + radius * math.cos(2 * math.pi * i / vertex_count),
                center_y + radius * math.sin(2 * math.pi * i / vertex_count),
            )
            for i in range(vertex_count)
        ]

        pygame.draw.polygon(game_window, shape_color, vertices)

        button_pressed = pygame.key.get_pressed()

        ## Increase Vertex Count
        if vertex_count >= vertex_min and vertex_count < vertex_max:
            if button_pressed[pygame.K_UP]:
                vertex_count += 1
                time.sleep(0.20)

        ## Decrease Vertex Count
        if vertex_count <= vertex_max and vertex_count > vertex_min:
            if button_pressed[pygame.K_DOWN]:
                vertex_count -= 1
                time.sleep(0.20)

        ##  Decrease Radius of Polygon
        if radius >= 1 and radius < 700:
            if button_pressed[pygame.K_LEFT]:
                radius -= 1
                time.sleep(0.1)

        ## Increase Radius of Polygon
        if radius <= 700 and radius > 1:
            if button_pressed[pygame.K_RIGHT]:
                radius += 1
                time.sleep(0.1)


        ## Decrease Red
        if shape_color[0] >= 30 and shape_color[0] < 255:
            if button_pressed[pygame.K_1] and button_pressed[pygame.K_q]:
                ##shape_color[0] -= 1
                pass


        ## Increase Red
        if shape_color[0] <= 255 and shape_color[0] > 30:
            if button_pressed[pygame.K_1]:
                ##shape_color[0] += 1
                pass

        ## Decrease Blue
        if shape_color[1] >= 30 and shape_color[1] < 256:
            if button_pressed[pygame.K_2] and button_pressed[pygame.K_w]:
                shape_color[1] -= 1
                pass

        ## Increase Blue
        if shape_color[1] <= 255 and shape_color[1] > 30:
            if button_pressed[pygame.K_1]:
                shape_color[1] += 1
                pass

        ## Decrease Green
        if shape_color[2] >= 30 and shape_color[2] < 256:
            if button_pressed[pygame.K_3] and button_pressed[pygame.K_e]:
                shape_color[2] -= 1
                pass

        ## Increase Green
        if shape_color[2] <= 255 and shape_color[2] > 30:
            if button_pressed[pygame.K_1]:
                shape_color[2] += 1
                pass

        # [30,30,30] to [255,255,255]

        pygame.display.flip()

    pygame.quit()

def printControls(text, line, font_size):

    font = pygame.font.Font('freesansbold.ttf', settings.size_of_font)
    input = font.render(text, False, (255, 255, 255), 0)
    inputRect = input.get_rect()
    inputRect.topleft = (0, font_size*(line-1))
    game_window.blit(input, inputRect)

if __name__ == '__main__':
    startProgram()