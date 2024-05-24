import random

import pygame, math, settings
import time
pygame.init()
game_window = pygame.display.set_mode((settings.width, settings.height))
pygame.display.set_caption(f"{settings.title}")
clock = pygame.time.Clock()


def startProgram():
    running = True
    modToggle = False
    center_x, center_y = settings.width // 2, settings.height // 2
    radius = 100
    vertex_count = 5

    vertex_max = 100
    vertex_min = 3

    shape_color = [255, 255, 255]
    rotation = 1
    ## for j in range(0, 61):
    ##    print((j/60) * (2 * math.pi))



    while running:
        #clock.tick(200)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        game_window.fill((0,0,0))

        generateStars(25)

        button_pressed = pygame.key.get_pressed()
        mouseChords = pygame.mouse.get_pos()
        mouseButtonStates = pygame.mouse.get_pressed(num_buttons=3)



        printControls(f"Up Arrow: Increase Vertex Count", 1, settings.size_of_font)
        printControls(f"Down Arrow: Decrease Vertex Count", 2, settings.size_of_font)
        printControls(f"Left Arrow: Decrease Polygon Size", 3, settings.size_of_font)
        printControls(f"Right Arrow: Increase Polygon Size", 4, settings.size_of_font)
        printControls(f"Increase Red Value: 1", 6, settings.size_of_font)
        printControls(f"Decrease Red Value: Q", 7, settings.size_of_font)
        printControls(f"Increase Green Value: 2", 8, settings.size_of_font)
        printControls(f"Decrease Green Value: W", 9, settings.size_of_font)
        printControls(f"Increase Blue Value: 3", 10, settings.size_of_font)
        printControls(f"Decrease Blue Value: E", 11, settings.size_of_font)

        printSats(f"Red: {shape_color[0]}   Green: {shape_color[1]}   Blue: {shape_color[2]}    Vertext Count: {vertex_count}    Size: {radius}", 1, settings.size_of_font)

        vertices = [
            [
                (center_x + radius * math.cos(rotation + (2 * math.pi * i / vertex_count))),
                (center_y + radius * math.sin(rotation + (2 * math.pi * i / vertex_count))),
            ]
            for i in range(vertex_count)
        ]


        pygame.draw.polygon(game_window, shape_color, vertices)






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

        ## Decresse Red
        if button_pressed[pygame.K_q]:
            if shape_color[0] > 30 and shape_color[0] < 256:
                shape_color[0] -= 1

        ## Increase Red
        if button_pressed[pygame.K_1]:
            if shape_color[0] < 255 and shape_color[0] >= 30:
                shape_color[0] += 1

        ## Decrease Green
        if button_pressed[pygame.K_w]:
            if shape_color[1] > 30 and shape_color[1] < 256:
                shape_color[1] -= 1

        ## Increase Green
        if button_pressed[pygame.K_2]:
            if shape_color[1] < 255 and shape_color[1] >= 30:
                shape_color[1] += 1

        ## Decrease Blue
        if button_pressed[pygame.K_e]:
            if shape_color[2] > 30 and shape_color[2] < 256:
                shape_color[2] -= 1

        ## Increase Blue
        if button_pressed[pygame.K_3]:
            if shape_color[2] < 255 and shape_color[2] >= 30:
                shape_color[2] += 1





        # [30,30,30] to [255,255,255]

        rotation += math.pi / 360
        print(rotation)
        time.sleep(1/60)

        pygame.display.flip()

    pygame.quit()

def printControls(text, line, font_size):

    font = pygame.font.Font('freesansbold.ttf', settings.size_of_font)
    input = font.render(text, False, (255, 0, 0), 0)
    inputRect = input.get_rect()
    inputRect.topleft = (0, font_size*(line-1))
    game_window.blit(input, inputRect)

def printSats(text, line, font_size):

    font = pygame.font.Font('freesansbold.ttf', settings.size_of_font)
    input = font.render(text, False, (255, 0, 0), 0)
    inputRect = input.get_rect()
    inputRect.center = (settings.width // 2, settings.height - font_size)
    game_window.blit(input, inputRect)

def generateStars(amount):

    for i in range(amount):
        pygame.draw.circle(game_window, [255, 255, 255], [random.randint(0, settings.width), random.randint(0, settings.height)], 2)



if __name__ == '__main__':
    startProgram()