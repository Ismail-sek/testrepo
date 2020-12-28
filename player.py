import pygame
from projectile import Projectile
# première classe (celle du joueur)
class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 1.7
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount

    def upadate_health_bar(self, surface):

        # dessiner l'arrière plan de la barre de vie
        pygame.draw.rect(surface, (149, 149, 149), [self.rect.x + 50, self.rect.y + 20, self.max_health, 5])
        # dessiner la barre de vie
        pygame.draw.rect(surface, (103, 208, 54), [self.rect.x + 50, self.rect.y + 20, self.health, 5])


    def launch_projectile(self):
        #créer une nouvelle instance de la classe projectile
        self.all_projectiles.add(Projectile(self))


    def move_right(self):
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def  move_left(self):
        self.rect.x -= self.velocity
