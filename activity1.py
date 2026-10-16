import pygame, random
pygame.init()

Width, Height = 800, 600
screen = pygame.display.set_mode((Width, Height))
clock = pygame.time.Clock()

CAR_EVENT = pygame.USEREVENT + 1
TRAFFIC_EVENT = pygame.USEREVENT + 2

COLORS = [pygame.Color('red'), pygame.Color('blue'), pygame.Color('orange'), pygame.Color('purple')]
signal_color = pygame.Color('red')

class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((60, 30))
        self.image.fill(random.choice(COLORS))
        self.rect = self.image.get_rect(topleft=(100, 285))
        self.vx = 7

    def update(self):
        self.rect.move_ip(self.vx, 0)
        if self.rect.left <= 0 or self.rect.right >= Width:
            self.vx *= -1
            pygame.event.post(pygame.event.Event(CAR_EVENT))
            pygame.event.post(pygame.event.Event(TRAFFIC_EVENT))

car = Car()
sprites = pygame.sprite.Group(car)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == CAR_EVENT:
            car.image.fill(random.choice(COLORS))
        elif event.type == TRAFFIC_EVENT:
            signal_color = pygame.Color('green') if signal_color == pygame.Color('red') else pygame.Color('red')

    sprites.update()
    screen.fill(pygame.Color('forestgreen'))
    pygame.draw.rect(screen, pygame.Color('gray20'), (0, 200, Width, 200))
    
    for x in range(0, Width, 40):
        pygame.draw.line(screen, pygame.Color('yellow'), (x, 300), (x + 20, 300), 4)

    pygame.draw.rect(screen, pygame.Color('gray'), (700, 50, 10, 150))
    pygame.draw.rect(screen, pygame.Color('black'), (685, 50, 40, 70))
    pygame.draw.circle(screen, signal_color, (705, 85), 15)

    sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
