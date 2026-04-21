import pygame

pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
screen = pygame.display.set_caption("Add Sprites")
display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move(self, x_change, y_change):
        self.rect.x = max(0, min(SCREEN_WIDTH - self.rect.width, self.rect.x + x_change))
        self.rect.y = max(0, min(SCREEN_HEIGHT - self.rect.height, self.rect.y + y_change))

sprite1 = Sprite(pygame.Color('crimson'), 50, 50, 100, 100)
sprite2 = Sprite(pygame.Color('darkblue'), 50, 50, 300, 300)

all_sprites = pygame.sprite.Group()
all_sprites.add(sprite1)
all_sprites.add(sprite2)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        sprite1.move(-5, 0)
    if keys[pygame.K_RIGHT]:
        sprite1.move(5, 0)
    if keys[pygame.K_UP]:
        sprite1.move(0, -5)
    if keys[pygame.K_DOWN]:
        sprite1.move(0, 5)

    display.fill(pygame.Color('white'))
    all_sprites.draw(display)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()