#!/bin/python

import pygame, sys
pygame.init()

player_gravity = 0
game_active = False
youlost = False
player_score = 0

screen = pygame.display.set_mode((1280,720), pygame.SCALED|pygame.FULLSCREEN)
pygame.display.set_caption("Platformer")
clock = pygame.time.Clock()

music = pygame.mixer.music.load("Resources/Sounds/Music.mp3")
cat = pygame.image.load("Resources/cat-facing-player.png").convert_alpha()
ground = pygame.image.load("Resources/ground.png").convert_alpha()
font = pygame.font.Font("Resources/font.ttf", 50)
fontbig = pygame.font.Font("Resources/font.ttf", 200)
knife = pygame.image.load("Resources/knife.png").convert_alpha()
cat_rect = cat.get_rect(midbottom = (500, 518))
knife_rect = knife.get_rect(midbottom = (1280, 500))
lose = fontbig.render("You lost!", True, "Red")
lose_description = font.render("Press any button to restart", True, "Black")
cat_large = pygame.image.load("Resources/cat-facing-player-large.png").convert_alpha()
start_description = font.render("To start press any key", True, "Black")
name = fontbig.render("Cat Runner", True, "dimgrey")
version = font.render("Alpha v0.2.0", True, "Black")
pygame.mixer.music.play(-1)
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
                player_score = 0
                game_active = True
                youlost = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                knife_rect.x = 1280
                player_score = 0
                game_active = True
                youlost = False
    if game_active:  
        knife_rect.x = knife_rect.x - 12
        pygame.mixer.music.unpause()
        if cat_rect.colliderect(knife_rect):
            pygame.mixer.music.pause()
            game_active=False
            youlost = True
            crash = pygame.mixer.Sound("Resources/Sounds/died.mp3")
            pygame.mixer.Sound.play(crash)
        player_gravity +=1
        cat_rect.y += player_gravity
        if knife_rect.x < 0:
            knife_rect.x = 1280
        screen.fill((188, 217, 234))
        if cat_rect.bottom >= 518:
            cat_rect.bottom = 518
        screen.blit(cat, cat_rect)
        screen.blit(ground,(0,500))
        player_score +=0.01666666666
        score = font.render(f"Score: {round(player_score)}", True, "Black")
        score_green = font.render(f"Score: {round(player_score)}", True, "chartreuse3")
        screen.blit(score, (550,50))
        screen.blit(knife,knife_rect)
    elif youlost:
        screen.fill((188,217,234))
        screen.blit(lose,(270,0))
        screen.blit(cat_large, (370,200))
        screen.blit(lose_description,(300,550))
        screen.blit(score_green, (530,620))
    else:
        pygame.mixer.music.pause()
        screen.fill((188,217,234))
        screen.blit(name,(150,0))
        screen.blit(cat_large, (370,200))
        screen.blit(start_description,(365,550))
        screen.blit(version, (485,620))
    pygame.display.update()
    clock.tick(60)
