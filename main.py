#!/bin/python

import pygame, sys
pygame.init()

player_gravity = 0
game_active = True

screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("Platformer")
clock = pygame.time.Clock()

cat = pygame.image.load("Resources/cat-facing-player.png").convert_alpha()
ground = pygame.image.load("Resources/ground.png").convert_alpha()
font = pygame.font.Font("Resources/font.ttf", 50)
fontbig = pygame.font.Font("Resources/font.ttf", 200)
score = font.render("Score: ", True, "Black")
knife = pygame.image.load("Resources/knife.png").convert_alpha()
cat_rect = cat.get_rect(midbottom = (500, 518))
knife_rect = knife.get_rect(midbottom = (1280, 500))
lose = fontbig.render("You lost!", True, "Red")
lose_description = font.render("Press any button to restart", True, "Black")


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if game_active == True:
            if event.type == pygame.MOUSEBUTTONDOWN and cat_rect.bottom >= 518:
                player_gravity = -18
            if event.type == pygame.KEYDOWN and cat_rect.bottom >= 518:
                player_gravity = -18
        else:
            if event.type == pygame.KEYDOWN:
                knife_rect.x = 1280
                game_active = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                knife_rect.x = 1280
                game_active = True
    if game_active:        
        knife_rect.x = knife_rect.x - 12
        if cat_rect.colliderect(knife_rect):
            game_active=False
        player_gravity +=1
        cat_rect.y += player_gravity
        if knife_rect.x < 0:
            knife_rect.x = 1280
        screen.fill((188, 217, 234))
        if cat_rect.bottom >= 518:
            cat_rect.bottom = 518
        screen.blit(cat, cat_rect)
        screen.blit(ground,(0,500))
        screen.blit(score, (550,50))
        screen.blit(knife,knife_rect)
    else:
        screen.blit(lose,(250,200))
        screen.blit(lose_description,(280,420))
    pygame.display.update()
    clock.tick(60)
