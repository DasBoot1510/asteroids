import pygame
import random
from circleshape import CircleShape
from logger import log_state, log_event
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        newMovement = self.velocity.rotate(angle)
        newNegMovement = self.velocity.rotate(-angle)
        newRadius = self.radius - ASTEROID_MIN_RADIUS
        ast1 = Asteroid(self.position.x, self.position.y, newRadius)
        ast1.velocity = newMovement*1.2
        ast2 = Asteroid(self.position.x, self.position.y, newRadius)
        ast2.velocity = newNegMovement



