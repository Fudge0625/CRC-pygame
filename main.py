import pygame
import asyncio

async def main():
    BLACK, WHITE = (0, 0, 0), (255, 255, 255)
    FPS = 240
    RES = W, H = 280, 280
    paint_board = (28, 28)
    pixel_w, pixel_h = W / paint_board[0], H / paint_board[1]
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((RES))
    screen.fill(WHITE)
    img = [[0] * paint_board[1] for _ in range(paint_board[0])]
    running = True
    while running:
        clock.tick(FPS)
        pygame.display.set_caption("FPS: {:.2f}".format(clock.get_fps()))
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        if mouse_pressed[0]:
            x, y = int(mouse_pos[0] // pixel_w), int(mouse_pos[1] // pixel_h)
            img[x][y] = 255
            paint = pygame.Rect((x * pixel_w, y * pixel_h), (pixel_w, pixel_h))
            pygame.draw.rect(screen, BLACK, paint)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    screen.fill(WHITE)
                    img = [[0] * paint_board[1] for _ in range(paint_board[0])]
                # if event.key == pygame.K_s:
                    # Save the image by printing it
                    # print("Image saved:", img)
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
        await asyncio.sleep(0)
    pygame.quit()

if __name__ == "__main__":
    asyncio.run(main())
