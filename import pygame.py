import pygame


pygame.init()

pygame.display.set_caption("Gra w statki")

ROZMIAR_PLANSZY = 45
POZIOMY_MARGINES = ROZMIAR_PLANSZY * 4
PIONOWY_MARGINES = ROZMIAR_PLANSZY 

SZEROKOSC = ROZMIAR_PLANSZY * 10 * 2 + POZIOMY_MARGINES
WYSOKOSC = ROZMIAR_PLANSZY * 10 * 2 + PIONOWY_MARGINES

EKRAN = pygame.display.set_mode((SZEROKOSC, WYSOKOSC))

NIEBIESKI = (176, 196, 222)
SZARY = (112, 128, 144)

#funkcja która rysuje kratkę
def draw_grid(left = 0, top = 0):
    for i in range(100):
        x = left + i % 10 * ROZMIAR_PLANSZY
        y = top + i // 10 * ROZMIAR_PLANSZY
        PLANSZA = pygame.Rect(x, y, ROZMIAR_PLANSZY, ROZMIAR_PLANSZY)
        pygame.draw.rect(EKRAN, SZARY, PLANSZA, width = 3)


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

        #rysowanie ,,szukającej'' planszy
        draw_grid()
        draw_grid(left = (SZEROKOSC-POZIOMY_MARGINES)//2 + POZIOMY_MARGINES, top = (WYSOKOSC-PIONOWY_MARGINES)//2 + PIONOWY_MARGINES)
       
        #rysowanie planszy pozycyjnej
        draw_grid(top = (WYSOKOSC-PIONOWY_MARGINES)//2 + PIONOWY_MARGINES)
        draw_grid(left = (SZEROKOSC-POZIOMY_MARGINES)//2 + POZIOMY_MARGINES)
        








        #update screen

        pygame.display.flip()
