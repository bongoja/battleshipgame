import pygame


pygame.init()

pygame.display.set_caption("Gra w statki")

SQ_SIZE= 45
H_MARGIN = SQ_SIZE * 4
V_MARGIN = SQ_SIZE 

WIDTH = SQ_SIZE * 10 * 2 + H_MARGIN
HEIGHT = SQ_SIZE * 10 * 2 + V_MARGIN

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

NIEBIESKI = (176, 196, 222)
SZARY = (112, 128, 144)

#funkcja która planszę
def draw_grid(left = 0, top = 0):
    for i in range(100):
        x = left + i % 10 * SQ_SIZE
        y = top + i // 10 * SQ_SIZE
        square = pygame.Rect(x, y, SQ_SIZE, SQ_SIZE)
        pygame.draw.rect(SCREEN, SZARY, square, width = 3)


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
            SCREEN.fill(NIEBIESKI)

        #rysowanie ,,szukającej'' planszy
        draw_grid()
        draw_grid(left = (WIDTH-H_MARGIN)//2 + H_MARGIN, top = (HEIGHT-V_MARGIN)//2 + V_MARGIN)
       
        #rysowanie planszy pozycyjnej
        draw_grid(top = (HEIGHT-V_MARGIN)//2 + V_MARGIN)
        draw_grid(left = (WIDTH-H_MARGIN)//2 + H_MARGIN)
        








        #update screen

        pygame.display.flip()
