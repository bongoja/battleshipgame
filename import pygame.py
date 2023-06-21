import pygame


pygame.init()

pygame.display.set_caption("Gra w statki")

SZEROKOSC = 1200
WYSOKOSC = 800

EKRAN = pygame.display.set_mode((SZEROKOSC, WYSOKOSC))

NIEBIESKI = (176, 196, 222)

animating=True
pausing=False
while animating:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            animating = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:

                animating == False

            if event.key == pygame.K_SPACE:

                pausing = not pausing


        if not pausing:
            EKRAN.fill(NIEBIESKI)


        #update screen

        pygame.display.flip()
