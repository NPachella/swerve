import pygame
from random import choice
pygame.init()

screen_width = 1024
screen_height = 673

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Swerve')
bg = pygame.image.load('background.jpg')

options = [pygame.image.load('Mini_truck.png'), pygame.image.load('Ambulance.png'),
		   pygame.image.load('Black_viper.png'), pygame.image.load('Police.png'), ]
them = choice(options)
that = choice(options)

car = pygame.image.load('Car.png')

ex1 = pygame.image.load('ex1 copy.png')
ex2 = pygame.image.load('ex2 copy.png')
ex3 = pygame.image.load('ex3 copy.png')
ex4 = pygame.image.load('ex4.png')
ex5 = pygame.image.load('ex5 copy.png')
ex6 = pygame.image.load('ex6 copy.png')

red = (255,0,0)
myFont = pygame.font.SysFont('monospace', 100)
text = 'You Crashed!'
label = myFont.render(text, 1, red)

class player():
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.vel = 4
		self.hitbox = (self.x + 5, self.y+22, 65, 29)

	def draw(self, screen):
		self.hitbox = (self.x+5, self.y+22, 65, 29)

		if hit == True:
			screen.blit(ex1, (self.x + self.width/2, self.y + self.height/2))
			screen.blit(ex2, (self.x + self.width/2, self.y + self.height/2))
			screen.blit(ex3, (self.x + self.width/2, self.y + self.height/2))
			screen.blit(ex4, (self.x + self.width/2, self.y + self.height/2))
			screen.blit(ex5, (self.x + self.width/2, self.y + self.height/2))
			screen.blit(ex6, (self.x + self.width/2, self.y + self.height/2))
	#pygame.draw.rect(screen, red, self.hitbox, 2)

class enemy():
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.vel = 2
		self.hitbox = (self.x + 5, self.y+22, 65, 30)

	def draw(self, screen):
		self.move()
		screen.blit(them, (self.x, self.y))
		self.hitbox = (self.x + 5, self.y+22, 65, 30)
		#pygame.draw.rect(screen, red, self.hitbox, 2)

	def move(self):
		if self.x > 0 - self.width:
			self.x -= self.vel
		else:
			self.x = 900


class enemy2():
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.vel = 3
		self.hitbox = (self.x + 5, self.y+22, 65, 30)

	def draw(self, screen):
		self.move()
		screen.blit(that, (self.x, self.y))
		self.hitbox = (self.x + 5, self.y+22, 65, 30)
		#pygame.draw.rect(screen, red, self.hitbox, 2)

	def move(self):
		if self.x < 1300 - self.width:
			self.x += self.vel
		else:
			self.x = -10

def redraw():
	if hit == True:
		screen.blit(label, (screen_width/5, screen_height/3),)
	screen.blit(car, (you.x,you.y))
	you.draw(screen)
	for obj in traffic2:
		obj.draw(screen)
	for obj in traffic:
		if t > 50 and t <= 200:
			obj.vel = 4
		if t > 200 and t <= 400:
			obj.vel = 6
		if t > 400 and t <= 600:
			obj.vel = 8
		if t > 600:
			obj.vel = 10
		obj.draw(screen)

	pygame.display.update()

x_list = [250, 400, 600, 800, 1000]
y_list = [270, 305]
z_list = [200, 230]

you = player(50, 280, 40, 60)
traffic = [enemy(choice(x_list), choice(y_list), 40, 60)]
traffic2 = [enemy2(choice(x_list), choice(z_list), 40, 60)]



n = 5
while len(traffic) < n:
	traffic.append(enemy(choice(x_list), choice(y_list), 40, 60))
	for obj in traffic:
		if traffic[-1].x == traffic[-2].x:
		 	traffic[-1].x = choice(x_list)
		# if traffic[-1].y == traffic[-2].y:
		# 	traffic[-1].y = choice(y_list)
while len(traffic2) < n:
	traffic2.append(enemy2(choice(x_list), choice(z_list), 40, 60))
	for obj in traffic2:
		if traffic2[-1].x == traffic2[-2].x:
		 	traffic2[-1].x = choice(x_list)

hit = False
t = 0
while t < 10000:
	screen.blit(bg, (0,0))
	pygame.time.delay(10)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()

	for obj in traffic:
		if you.hitbox[1] < obj.hitbox[1] and you.hitbox[1] + you.hitbox[3] > obj.hitbox[1] or you.hitbox[1] < obj.hitbox[1] + obj.hitbox[3] and you.hitbox[1] + you.hitbox[3] > obj.hitbox[1] + obj.hitbox[3]:
			if you.hitbox[0] < obj.hitbox[0] and you.hitbox[0] + you.hitbox[2] > obj.hitbox[0] or you.hitbox[0] > obj.hitbox[0] and you.hitbox[0] < obj.hitbox[0] + obj.hitbox[2]:
				hit = True
	for obj in traffic2:
		if you.hitbox[1] < obj.hitbox[1] and you.hitbox[1] + you.hitbox[3] > obj.hitbox[1] or you.hitbox[1] < obj.hitbox[1] + obj.hitbox[3] and you.hitbox[1] + you.hitbox[3] > obj.hitbox[1] + obj.hitbox[3]:
			if you.hitbox[0] < obj.hitbox[0] and you.hitbox[0] + you.hitbox[2] > obj.hitbox[0] or you.hitbox[0] > obj.hitbox[0] and you.hitbox[0] < obj.hitbox[0] + obj.hitbox[2]:
				hit = True

	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT] and you.x > you.vel:
		you.x -= you.vel
	if keys[pygame.K_RIGHT] and you.x < screen_width - you.width:
		you.x += you.vel
	if keys[pygame.K_UP] and you.y > 200:
		you.y -= you.vel
	if keys[pygame.K_DOWN] and you.y < 325:
		you.y += you.vel

	t += 1
	redraw()