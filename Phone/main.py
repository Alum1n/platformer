#!/bin/python

import pygame, sys
pygame.init()

player_gravity = 0
game_active = False
youlost = False
player_score = 0

screen = pygame.display.set_mode((1920,1080), pygame.SCALED|pygame.FULLSCREEN)
pygame.display.set_caption("Platformer")
clock = pygame.time.Clock()

music = pygame.mixer.music.load("Music.mp3")
cat = pygame.image.load("cat-facing-player.png").convert_alpha()
ground = pygame.image.load("ground.png").convert_alpha()
font = pygame.font.Font("font.ttf", 75)
fontbig = pygame.font.Font("font.ttf", 300)
knife = pygame.image.load("knife.png").convert_alpha()
cat_rect = cat.get_rect(midbottom = (750, 777))
knife_rect = knife.get_rect(midbottom = (1920, 750))
lose = fontbig.render("You lost!", True, "Red")
lose_description = font.render("Tap to restart", True, "Black")
cat_large = pygame.image.load("cat-facing-player-large.png").convert_alpha()
start_description = font.render("Tap to start", True, "Black")
name = fontbig.render("Cat Runner", True, "dimgrey")
version = font.render("Alpha v0.2.1", True, "Black")
pygame.mixer.music.play(-1)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if game_active == True:
            if event.type == pygame.MOUSEBUTTONDOWN and cat_rect.bottom >= 777:
                player_gravity = -22
            if event.type == pygame.KEYDOWN and cat_rect.bottom >= 777:
                player_gravity = -22
        else:
            if event.type == pygame.KEYDOWN:
                knife_rect.x = 1920
                player_score = 0
                game_active = True
                youlost = False
                pygame.mixer.music.play(-1)
            if event.type == pygame.MOUSEBUTTONDOWN:
                knife_rect.x = 1920
                player_score = 0
                game_active = True
                youlost = False
                pygame.mixer.music.play(-1)
    if game_active:  
        knife_rect.x = knife_rect.x - 15
        pygame.mixer.music.unpause()
        if cat_rect.colliderect(knife_rect):
            pygame.mixer.music.stop()
            game_active=False
            youlost = True
            crash = pygame.mixer.Sound("died.mp3")
            pygame.mixer.Sound.play(crash)
        player_gravity +=1
        cat_rect.y += player_gravity
        if knife_rect.x < 0:
            knife_rect.x = 1920
        screen.fill((188, 217, 234))
        if cat_rect.bottom >= 777:
            cat_rect.bottom = 777
        screen.blit(cat, cat_rect)
        screen.blit(ground,(0,750))
        player_score +=0.01666666666
        score = font.render(f"Score: {round(player_score)}", True, "Black")
        score_green = font.render(f"Score: {round(player_score)}", True, "chartreuse3")
        screen.blit(score, (825,75))
        screen.blit(knife,knife_rect)
    elif youlost:
        screen.fill((188,217,234))
        screen.blit(lose,(400,0))
        screen.blit(cat_large, (555,300))
        screen.blit(lose_description,(674,825))
        screen.blit(score_green, (795,930))
    else:
        pygame.mixer.music.pause()
        screen.fill((188,217,234))
        screen.blit(name,(225,0))
        screen.blit(cat_large, (555,300))
        screen.blit(start_description,(720,825))
        screen.blit(version, (723,930))
    pygame.display.update()
    clock.tick(60)
