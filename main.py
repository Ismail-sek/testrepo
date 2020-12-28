import pygame
import math
from game import Game

pygame.init()
# creation du logo
image = pygame.image.load("assets/icons/player_1.png")

# générer la fenêtre du jeu
pygame.display.set_caption("Comet fall shooter")
pygame.display.set_icon(image)

main_window = pygame.display.set_mode((1080, 720))

# importation du background
background = pygame.image.load('assets/bg.jpg')

#importer le bouton
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(main_window.get_width() / 3.33)
play_button_rect.y = math.ceil(main_window.get_height() / 2)

#Importer la bannière
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(main_window.get_width() / 4)

# Charger le jeu après le chargement du fond

game = Game()

running = True

# boucle de la condition est vraie
while running:

    # afficher l'arrière plan sur la fenêtre
    main_window.blit(background, (0, -200))

    # verification du commencement du jeu
    if game.is_playing:
        # declencher les instructions de la partie
        game.update(main_window)
    #vefifier si le jeu n'a pas commencé
    else:
        #ajoouter mon ecran de bienvenue
        main_window.blit(play_button, play_button_rect)
        main_window.blit(banner, banner_rect)


    #mise à jour de l'écran
    pygame.display.flip()

    # si le joueur ferme la fenêtre
    for event in pygame.event.get():
        # si l'évènement est fermeture de fenêtre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        # détecter si le joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
           game.pressed[event.key] = True

           if event.key == pygame.K_SPACE:
               # détéction du lancement de projectile
               game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
                game.pressed[event.key] = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # verification pour savoir si la spurie clique sur le bouton, du moins si il est en collision
            if play_button_rect.collidepoint(event.pos):
                #mettre le jeu en mode lancé
                game.is_playing = True