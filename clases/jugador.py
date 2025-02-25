import pygame


class Nave(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagenNave = pygame.image.load("imagenes/nave.png")
        self.rect = self.imagenNave.get_rect()
        self.rect.centerx = 240
        self.rect.centery = 690
        self.velocidad = 50
        self.vida = True
        self.listaDisparo = []
    def mover(self):
        if self.vida == True:
            if self.rect.left <= 0:
                self.rect.left = 0
            elif self.rect.right > 490:
                self.rect.right  = 490
    def disparar(self):
        print("Estoy disparando")
    def dibujar(self, superficie):
        superficie.blit(self.imagenNave, self.rect)