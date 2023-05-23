import pygame
from random import randint
pygame.init()

WIDTH = 400
HEIGHT = 600
result = 0
pausing = False

GREEN = (0,200,0)
BLUE = (0,0,255)
RED = (255,0,0)
BLACK = (255,255,255)
YELLOW = (255,255,0)

pygame.display.set_caption('Flappy Bird')
running = True
screen = pygame.display.set_mode((WIDTH,HEIGHT))

clock = pygame.time.Clock()

font = pygame.font.SysFont('sans', 30)

TUBE_GAP = 150
VELOCITY = 2
TUBE_WIDTH = 50

tube1_x = 0
tube2_x = 200
tube3_x = 400

tube1_height = randint(100,400)
tube2_height = randint(100,400)
tube3_height = randint(100,400)

BIRD_X = 50
bird_y = 400
BIRD_WIDTH = 35
BIRD_HEIGHT = 35
DROP_VEC = 0
GRAVITY = 0.5 

check_tube1 = False
check_tube2 = False
check_tube3 = False

#load the image

background_image = pygame.image.load("background.png")
bird_image = pygame.image.load("bird.png")
bird_image = pygame.transform.scale(bird_image, (BIRD_WIDTH, BIRD_HEIGHT))

while(running):
	clock.tick(60)
	screen.fill(GREEN)
	screen.blit(background_image, (0,0))
	#Draw tube

	tube1 = pygame.draw.rect(screen, BLUE, (tube1_x, 0, TUBE_WIDTH, tube1_height))
	tube2 = pygame.draw.rect(screen, BLUE, (tube2_x, 0, TUBE_WIDTH, tube2_height))
	tube3 = pygame.draw.rect(screen, BLUE, (tube3_x, 0, TUBE_WIDTH, tube3_height))

	#Draw tube in inverse

	tube1_inv = pygame.draw.rect(screen, BLUE, (tube1_x, TUBE_GAP + tube1_height, TUBE_WIDTH, HEIGHT - TUBE_GAP - tube1_height))
	tube2_inv = pygame.draw.rect(screen, BLUE, (tube2_x, TUBE_GAP + tube2_height, TUBE_WIDTH, HEIGHT - TUBE_GAP - tube2_height))
	tube3_inv = pygame.draw.rect(screen, BLUE, (tube3_x, TUBE_GAP + tube3_height, TUBE_WIDTH, HEIGHT - TUBE_GAP - tube3_height))

	#Move tube to the left

	tube1_x = tube1_x - VELOCITY
	tube2_x = tube2_x - VELOCITY
	tube3_x = tube3_x - VELOCITY

	#Generate new tubes

	if tube1_x < -TUBE_WIDTH:
		tube1_x = 550
		tube1_height = randint(100,400)
		check_tube1 = False		
	if tube2_x < -TUBE_WIDTH:
		tube2_x = 550	
		tube2_height = randint(100,400)	
		check_tube2 = False	
	if tube3_x < -TUBE_WIDTH:
		tube3_x = 550
		tube3_height = randint(100,400)
		check_tube3 = False	

	# draw sand
	sand_rect = pygame.draw.rect(screen, YELLOW, (0,550,400,50))

	# draw bird
	bird_rect = screen.blit(bird_image, (BIRD_X, bird_y))
	
	#bird falls. Đoạn này hay!

	bird_y = bird_y + DROP_VEC
	DROP_VEC += GRAVITY

	#count the result

	if tube1_x + TUBE_WIDTH < BIRD_X and check_tube1 == False:
		result += 1
		check_tube1 = True
	if tube2_x + TUBE_WIDTH < BIRD_X and check_tube2 == False:
		result += 1
		check_tube2 = True
	if tube3_x + TUBE_WIDTH < BIRD_X and check_tube3 == False:
		result += 1
		check_tube3 = True

	#Display the result

	text_1 = font.render("Score: " + str(result), True, RED)
	screen.blit(text_1, (60,60))

	#Check collision

	for tube in [tube1, tube2, tube3, tube1_inv, tube2_inv, tube3_inv]:
		if bird_rect.colliderect(tube):
			VELOCITY = 0
			DROP_VEC = 0
			pausing = True
			game_over_txt = font.render("Game over, score: " + str(result), True, BLACK)
			screen.blit(game_over_txt, (100,300))
			press_space_txt = font.render("Press Space to Continue", True, BLACK)
			screen.blit(press_space_txt, (100,400))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				if pausing:
					tube1_x = 600
					tube2_x = 800
					tube3_x = 1000
					VELOCITY = 2
					bird_y = 400
					result = 0
					pausing = False

				DROP_VEC = 0
				DROP_VEC -= 7
		
	pygame.display.flip()

pygame.quit()