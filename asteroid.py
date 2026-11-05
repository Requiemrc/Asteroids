from circleshape import CircleShape
from constants import *
import pygame
from logger import log_state, log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)

    def update(self,dt):
        self.position += self.velocity*dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            random_angle = random.uniform(20,50)
            new_velocity_1 = self.velocity.rotate(random_angle)
            new_velocity_2 =self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            position_x = self.position[0]
            position_y = self.position[1]
            new_a_1 = Asteroid(position_x,position_y, new_radius)
            new_a_1.velocity = new_velocity_1* 1.2
            new_a_2 = Asteroid(position_x,position_y, new_radius)
            new_a_2.velocity = new_velocity_2* 1.2
            
