import pygame,sys
from pygame.locals import *
from clases import jugador
#Variables
ancho = 480
alto = 700

jgador =  True

nave = jugador.Nave()
# Funcion principal 
pygame.init()
ventana = pygame.display.set_mode((ancho,alto))
fondo = pygame.image.load("imagenes/fondo.png")
pygame.display.set_caption("Mi juego de asteroides")
def main():
    

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    nave.rect.right -= nave.velocidad
                    print("i")
                elif event.key == pygame.K_RIGHT:
                    nave.rect.left += nave.velocidad
                    print("d")
                elif event.key == pygame.K_SPACE:
                    nave.disparar()
                
            
            ventana.blit(fondo, (0,0))
            nave.dibujar(ventana)
            nave.mover()
            pygame.display.update()


main()