import pygame
import random

pygame.init()
pygame.font.init()

running = True

SCREEN_HEIGHT = 700
SCREEN_WIDTH = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Scuffy bird :)')

gravity_enabled = True

#colors
GREEN = (34, 182, 49)
BLUE = (35, 63, 164)
YELLOW = (255, 255, 102)

#CLASSES

class Bird:
    def __init__(self):
        self.velocity = 0
        self.rect_ = pygame.Rect(25, 60, 35, 35)
    def draw(self):
        pygame.draw.rect(screen, YELLOW, self.rect_)
    def jump(self):
        self.velocity = -10
    def gravity(self):
        self.velocity += 1
        self.rect_.y += self.velocity #calculate and place the bird at the end
    def game_over(self):
        if self.rect_.colliderect(obstacle_.rect1):
            return True
        elif self.rect_.colliderect(obstacle_.rect2):
            return True
        else:
            return False
        
class Obstacle:
    def __init__(self):
        self.distance = 150
        self.length = self.generate_rand_num()
        self.speed = -5
        self.rect1 = pygame.Rect(SCREEN_WIDTH, 0, 50, self.length)
        self.rect2 = pygame.Rect(SCREEN_WIDTH, self.rect1.height + self.distance, 50, 700)
        self.score = 0
        
    def draw(self):
        pygame.draw.rect(screen, GREEN, self.rect1)
        pygame.draw.rect(screen, GREEN, self.rect2)
        
    def generate_rand_num(self):
        return random.randint(150, 600)
    
    def move(self):
        self.rect1.x += self.speed
        self.rect2.x += self.speed
        self.speed -= 0.0000001
        print(self.speed)

    def reset(self):
        if self.rect1.x < 5:
            self.rect1.x = SCREEN_WIDTH
            self.rect2.x = SCREEN_WIDTH
            self.length = self.generate_rand_num()
            self.rect1.height = self.length 
            self.rect2.y = self.rect1.height + self.distance
           
            
    
bird_player = Bird()
obstacle_ = Obstacle()

score = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                #print("space")
                bird_player.jump()
    
    
    
    screen.fill(BLUE)
    
    bird_player.draw()
    bird_player.gravity()

    obstacle_.draw()
    obstacle_.move()
    font = pygame.font.Font("PixelifySans-Medium.ttf ", 50)
    score_text = font.render(f"SCORE: {score}", True, (0, 0, 0 ))
    screen.blit(score_text, ((SCREEN_WIDTH/3, 0)))

    if obstacle_.rect1.x  < 5:
        score += 1

    obstacle_.reset()
    
    if bird_player.game_over():
        running = False             # if collide close window

    pygame.display.update()
    pygame.time.Clock().tick(60)