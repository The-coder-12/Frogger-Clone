#Modules
import pygame
import sys
import random

#Initialize pygame
pygame.init()

#Variables
x = 1550
y = 800
white = [255, 255, 255]
green = [88,188,8]
bg = pygame.image.load("bg.jpeg")
bg1 = pygame.transform.scale(bg, (x, y))
black = [0, 0, 0]
score = 0
frog_size = 50
frog_x = x / 2
frog_y = y - 100
frog_speed = 5
car_x = 300
car_y = 168
car_x_change = frog_speed
cars = []
the_car = pygame.image.load("car-removebg-preview.png")
the_car1 = pygame.transform.scale(the_car, (car_x, car_y))
dis = pygame.display.set_mode((x, y))
pygame.display.set_caption("Frogger Clone")
hit = pygame.mixer_music.load("W6UFXTM-human-hit-by-car.mp3")
change = pygame.mixer_music.load("frogs-croaking-46947.mp3")
frogs = [
    pygame.image.load("frog1.jpeg"),
    pygame.image.load("frog2.jpeg"),
    pygame.image.load("frog3.jpg")
]
current_frog_index = 0
frog = pygame.transform.scale(frogs[current_frog_index], (50, 50))

#Create cars
def create_cars():
    car_lane = random.randint(0, y//car_y - 1)
    car_height = car_lane * car_y
    return{"x": x, "y": car_height}

#Clock for maintaining a set speed (in frames per second)
clock = pygame.time.Clock()
#Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.mixer_music.play()
                current_frog_index = (current_frog_index + 1) % len(frogs)
                frog = pygame.transform.scale(frogs[current_frog_index], (50, 50))

    #Controls
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            frog_y = frog_y - frog_speed
        if event.key == pygame.K_DOWN:
            frog_y = frog_y + frog_speed

    #Car creation
    if random.random() < 0.03:
        cars.append(create_cars())

    #For car in cars
    for car in cars:
        car["x"] = car["x"] - car_x_change
        if (frog_x < car["x"] + car_x and frog_x + frog_size > car["x"] and frog_y < car[
            "y"] + car_y and frog_y + frog_size > car["y"]):
            pygame.mixer_music.play()
            frog_y = y - 100
            cars = []
            score = 0
        elif car["x"] == 0:
            cars.remove(car)
            score = score + 1

    #Fill the screen
    dis.fill(white)
    dis.blit(bg1, (0, 0))
    dis.blit(frog, (frog_x, frog_y))
    for car in cars:
        # pygame.draw.rect(dis, black, [car["x"], car["y"], car_x, car_y])
        dis.blit(the_car1, (car["x"], car["y"]))
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Score: {score}", True, black)
    dis.blit(score_text, (100, 10))
    pygame.display.update()
    clock.tick(60)