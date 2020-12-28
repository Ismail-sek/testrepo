import pygame
from player import Player
from monster import Monster


# classe représentant le jeu
class Game:
    def __init__(self):
        # definir si notre jeu a commence ou pas
        self.is_playing = False
        # génerer le joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # groupe de monstre
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_monster()
        self.spawn_monster()

    def update(self, main_window):
        # afficher l'image du player
        main_window.blit(self.player.image, self.player.rect)

        # actuailiser la barre de jeu du joueur
        self.player.upadate_health_bar(main_window)

        # récupérer les projectiles
        for projectiles in self.player.all_projectiles:
            projectiles.move()

        # Récuperer les monstres
        self.all_monsters.draw(main_window)

        # recuperer les monstres (mummy)
        for monster in self.all_monsters:
            monster.forward()
            monster.upadate_health_bar(main_window)

        # afficher les projectiles
        self.player.all_projectiles.draw(main_window)

        # verifier si le joueur souhaite aller à gauche ou à droite et l'empecher de sortit de la fenêtre
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < main_window.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_d) and self.player.rect.x + self.player.rect.width < main_window.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()
        elif self.pressed.get(pygame.K_q) and self.player.rect.x > 0:
            self.player.move_left()
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)