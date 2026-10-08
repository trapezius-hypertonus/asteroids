from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
import pygame
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
         pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def collides_with(self, other):
        if self.position.distance_to(other.position) <=self.radius + other.radius:
            return True
        else:
            return False

    def split(self):
        self.kill()
        if self.radius <=ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            vector1 = self.velocity.rotate(angle)
            vector2 = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            astr1 = Asteroid(self.position.x, self.position.y, new_radius)
            astr2 = Asteroid(self.position.x, self.position.y, new_radius)
            astr1.velocity = vector1 * 1.2
            astr2.velocity = vector2 * 1.2
