import pygame, time, random

pygame.init()
screen = pygame.display.set_mode((1000,400))                           
pygame.display.set_caption("LLAMA GAME")
clock = pygame.time.Clock()

quit_game = False
colors = {"green":(188, 227, 199), "dark_green":(0, 102, 51),
          "blue":(32, 32, 200),"black":(0, 0, 0),"white":(255, 255, 255),
          "lightblue":(176, 197, 245)}

def draw_background():  
    pygame.draw.rect(screen, colors["black"], [0,200,1000,2])
    pygame.draw.rect(screen, colors["green"], [0,202,1000,200])
    pygame.draw.rect(screen, colors["lightblue"], [0,0,1000,200])
    pygame.draw.rect(screen, colors["black"], [168,168,32,32])
    
class Cacti:
    def __init__(self, location, color):
        self.location = location
        self.color = color

    def draw(self):
        pygame.draw.rect(screen, self.color, [self.location,168,32,32])

    def move(self):
        self.location -= 30
        if self.location <= 0:
            self.location = random.randint(1000,1500)

cactus_attrib = [(800,colors["white"]),(900,colors["black"]),
                 (1000,colors["blue"]),(1100,colors["dark_green"]),
                 (1200,colors["green"])]

cacti_list = []
for location, color in cactus_attrib:
    cactus = Cacti(location, color)
    cacti_list.append(cactus)
print(cacti_list)

while quit_game == False:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quit_game = True
    
    draw_background()

    for items in cacti_list:
        items.draw()
        items.move()
        
    pygame.display.update()
    clock.tick(10)
