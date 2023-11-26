import pygame, sys
pygame.init()

screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("Platformer")
clock = pygame.time.Clock()

test_surface = pygame.Surface((250,250))
test_surface.fill((255,255,255))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(test_surface,(200,100))
    

    pygame.display.update()
    clock.tick(60)
