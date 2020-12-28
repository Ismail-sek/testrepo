import pygame
import random

class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.05
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540
        self.velocity = 0.3

    def damage(self, amount):
         # Lui faire onfliger les dégats
        self.health -= amount

        # Verification du nombre de point de vie < ou = à 0
        if self.health <= 0:
            # le faire réapparaître comme un nouveau monstre
            self.rect.x = 1000 + random.randint(0, 300)
            self.health = self.max_health
            self.velocity = self.velocity + 0.09
            while self.velocity == 2:
                self.velocity = 0.7

    def upadate_health_bar(self, surface):

        # dessiner l'arrière plan de la barre de vie
        pygame.draw.rect(surface, (149, 149, 149), [self.rect.x + 12, self.rect.y - 20, self.max_health, 5])
        # dessiner la barre de vie
        pygame.draw.rect(surface, (103, 208, 54), [self.rect.x + 12, self.rect.y - 20, self.health, 5])


    def forward(self):
        # le déplacement ne se fasse que si il n'a pas de collision avec un joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        # si le monstre est en collision avec le player
        else:
            #Ingliger des dégats (au player)
            self.game.player.damage(self.attack)
