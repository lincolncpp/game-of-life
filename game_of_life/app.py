from game_of_life import config
import pygame

# Global running variables
screen = 0
running = False
play = False
gen_last_time = 0
clock = 0

def setup():
    global screen, running, clock

    pygame.init()
    screen = pygame.display.set_mode([config.window_width, config.window_height])

    running = True
    clock = pygame.time.Clock()


def event():
    global running, play

    ev = pygame.event.get()
    for event in ev:

        # Quit game
        if event.type == pygame.QUIT:
            running = False

        # On mouse button down
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            x = pos[0]//config.square_size
            y = pos[1]//config.square_size
            config.state[x][y] ^= True

        # On key down
        if event.type == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()

            # Space key pressed
            if pressed[pygame.K_SPACE]:
                play ^= True


def next_generation():
    up = []
    down = []
    for x in range(0, config.box_width):
        for y in range(0, config.box_height):

            alive_neig = 0
            for a in range(-1, 1+1):
                for b in range(-1, 1+1):
                    if a == 0 and b == 0: continue
                    if x+a < 0 or x+a >= config.box_width: continue
                    if y+b < 0 or y+b >= config.box_height: continue
                    if config.state[x+a][y+b] == True: alive_neig += 1

            if config.state[x][y] == True:
                ok = False
                for val in config.rules[0]:
                    if alive_neig == val: ok = True
                if ok == False: down.append([x, y])
            else:
                for val in config.rules[1]:
                    if alive_neig == val: up.append([x, y])

    for p in up: config.state[p[0]][p[1]] = True
    for p in down: config.state[p[0]][p[1]] = False


def render():
    for x in range(0, config.box_width):
        for y in range(0, config.box_height):
            if config.state[x][y] == True:
                pygame.draw.rect(screen, [255, 255, 0], (x*config.square_size, y*config.square_size, config.square_size, config.square_size))

def run():
    global screen, running, play, gen_last_time, clock

    while running == True:
        screen.fill([20]*3)

        # Handle events
        event()

        # Go to the next generation every 'config.generation_ms' milliseconds
        if play == True and pygame.time.get_ticks() >= gen_last_time+config.generation_ms:
            gen_last_time = pygame.time.get_ticks()
            next_generation()

        # Render generation
        render()

        # Set game fps = 60
        clock.tick(60)

        # Draw
        pygame.display.flip();

    pygame.quit();


def start():
    setup()
    run()
