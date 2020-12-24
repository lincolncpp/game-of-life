import pygame

window_width = 640
window_height = 480
square_size = 20
box_width = window_width//square_size
box_height = window_height//square_size
running = True
play = False

rules = [[2, 3], [3]]
generation_ms = 200 
gen_last_time = 0

# False: Cell (x, y) is dead
# True: Cell (x, y) is alive
state = [[False for y in range(0, box_height)] for x in range(0, box_width)]

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode([window_width, window_height])

while running == True:
    screen.fill([20, 20, 20])

    ev = pygame.event.get()
    for event in ev:

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            x = pos[0]//square_size
            y = pos[1]//square_size
            state[x][y] ^= True

        if event.type == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()
            
            if pressed[pygame.K_SPACE]:
                play ^= True

    if pygame.time.get_ticks() >= gen_last_time+generation_ms and play == True:
        gen_last_time = pygame.time.get_ticks()

        up = []
        down = []
        for x in range(0, box_width):
            for y in range(0, box_height):

                alive_neig = 0
                for a in range(-1, 1+1):
                    for b in range(-1, 1+1):
                        if a == 0 and b == 0: continue 
                        if x+a < 0 or x+a >= box_width: continue
                        if y+b < 0 or y+b >= box_height: continue
                        if state[x+a][y+b] == True: alive_neig += 1
                
                if state[x][y] == True:
                    ok = False
                    for val in rules[0]:
                        if alive_neig == val: ok = True
                    if ok == False: down.append([x, y])
                else:
                    for val in rules[1]:
                        if alive_neig == val: up.append([x, y])
        
        for p in up: state[p[0]][p[1]] = True
        for p in down: state[p[0]][p[1]] = False



    for x in range(0, box_width):
        for y in range(0, box_height):
            if state[x][y] == True:
                pygame.draw.rect(screen, [255, 255, 0], (x*square_size, y*square_size, square_size, square_size))    



    clock.tick(60)
    pygame.display.flip();

pygame.quit();
