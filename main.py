import pygame, settings, tiktaktoe

pygame.init()

screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
clock = pygame.time.Clock()

game = tiktaktoe.tiktaktoe(screen)

while True:
    pos = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()
    dt = clock.tick(settings.FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    game.update(dt, keys, pos)
    game.draw()

    pygame.display.set_caption(f"fps: {round(clock.get_fps())}, player: {game.currentPlayer + 1}")
    pygame.display.update()