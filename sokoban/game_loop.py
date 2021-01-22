import pygame

def run():
    pygame.init()
    pygame.key.set_repeat(150)

    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption('Sokoban!!')

    running = True
    while running:  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
        screen.fill((0, 0, 0))
    
        pygame.display.flip()
