import pygame
import os
import random
import tkinter
from PIL import Image, ImageTk
pygame.init()
#tkinter window settings
root = tkinter.Tk()
root.geometry("1000x680") #window size
root.configure(bg='white') #set background color
root.title("SONIC IN THE DINOSAUR LAND") # Title of window

image1 = Image.open("sonicgame/sonicLogo.png")
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test, bd=0)
label1.image = test
# Position image
label1.pack(anchor='n', pady=(60, 0))

def startGame():
    # Global Constants
    global SCREEN_HEIGHT 
    global SCREEN_WIDTH 
    global SCREEN
    global color
    SCREEN_HEIGHT = 600
    SCREEN_WIDTH = 1100
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    color = (17, 174, 238)
    pygame.init()
    menu(death_count=0)

def exitGame():
    quit()

startButton = tkinter.Button(root, text="Start Game", font="Arial 15", command=startGame,relief=tkinter.RAISED,bd=3, bg="#0157BA", fg="white", height=2, width=14,activebackground="#FDCA0B",activeforeground="black")
startButton.pack(pady=(40, 0)) # set to middle padding from top 40 units

exitButton = tkinter.Button(root, text="Exit", font="Arial 15", command=exitGame,relief=tkinter.RAISED,bd=3, bg="#0157BA", fg="white", height=2, width=14,activebackground="#FDCA0B",activeforeground="black")
exitButton.pack(pady=(40, 0)) # set to middle padding from top 40 units

#this is for running gui
theme_sound = pygame.mixer.Sound("sonicgame/Assets/SoundEffect/sonictheme.mp3")
run_sound = pygame.mixer.Sound("sonicgame/Assets/SoundEffect/runsound.mp3")
jump_sound = pygame.mixer.Sound("sonicgame/Assets/SoundEffect/jumpsound.mp3")
ring_sound = pygame.mixer.Sound("sonicgame/Assets/SoundEffect/ringsound.mp3")
dash_sound = pygame.mixer.Sound("sonicgame/Assets/SoundEffect/dashsound.mp3")
death_sound = pygame.mixer.Sound("sonicgame/Assets/SoundEffect/deathsound.mp3")
potion_sound = pygame.mixer.Sound("sonicgame/Assets/SoundEffect/potionsound.mp3")

# Changing surface color
RUNNING = [pygame.image.load(os.path.join("sonicgame/Assets/Sonic", "SonicStart.png")),
           pygame.image.load(os.path.join("sonicgame/Assets/Sonic", "SonicRun1.png")),
           pygame.image.load(os.path.join("sonicgame/Assets/Sonic", "SonicRun2.png")),
           pygame.image.load(os.path.join("sonicgame/Assets/Sonic", "SonicRun3.png")),
           pygame.image.load(os.path.join("sonicgame/Assets/Sonic", "SonicRun4.png")),
           pygame.image.load(os.path.join("sonicgame/Assets/Sonic", "SonicRun3.png"))]

JUMPING = pygame.image.load(os.path.join("sonicgame/Assets/Sonic", "SonicJump.png"))

DASHING = [pygame.image.load(os.path.join("sonicgame/Assets/Sonic", "SonicDash1.png")),
           pygame.image.load(os.path.join("sonicgame/Assets/Sonic", "SonicDash2.png")),
           pygame.image.load(os.path.join("sonicgame/Assets/Sonic", "SonicDash3.png")),
           pygame.image.load(os.path.join("sonicgame/Assets/Sonic", "SonicDash4.png")),
           pygame.image.load(os.path.join("sonicgame/Assets/Sonic", "SonicDash5.png")),
           pygame.image.load(os.path.join("sonicgame/Assets/Sonic", "SonicDash6.png")),
           pygame.image.load(os.path.join("sonicgame/Assets/Sonic", "SonicDash7.png")),
           pygame.image.load(os.path.join("sonicgame/Assets/Sonic", "SonicDash7.png")),
           pygame.image.load(os.path.join("sonicgame/Assets/Sonic", "SonicDash7.png"))]

SMALL_CACTUS = [pygame.image.load(os.path.join("sonicgame/Assets/Environment", "SmallCactus1.png")),
                pygame.image.load(os.path.join("sonicgame/Assets/Environment", "SmallCactus2.png")),
                pygame.image.load(os.path.join("sonicgame/Assets/Environment", "SmallCactus3.png"))]
LARGE_CACTUS = [pygame.image.load(os.path.join("sonicgame/Assets/Environment", "LargeCactus1.png")),
                pygame.image.load(os.path.join("sonicgame/Assets/Environment", "LargeCactus2.png")),
                pygame.image.load(os.path.join("sonicgame/Assets/Environment", "LargeCactus3.png"))]

CACTUS = [pygame.image.load(os.path.join("sonicgame/Assets/Environment", "cactus.png")),
          pygame.image.load(os.path.join("sonicgame/Assets/Environment", "cactus.png")),
          pygame.image.load(os.path.join("sonicgame/Assets/Environment", "cactus.png"))]

ROCK =  [pygame.image.load(os.path.join("sonicgame/Assets/Environment", "rock.png")),
        pygame.image.load(os.path.join("sonicgame/Assets/Environment", "rock.png")),
        pygame.image.load(os.path.join("sonicgame/Assets/Environment", "rock.png"))]

MONSTER = [pygame.image.load(os.path.join("sonicgame/Assets/Monster", "amongus.png")),
            pygame.image.load(os.path.join("sonicgame/Assets/Monster", "babyyoda.png")),
            pygame.image.load(os.path.join("sonicgame/Assets/Monster", "trex.png")),
            pygame.image.load(os.path.join("sonicgame/Assets/Monster", "oldman.png")),
            pygame.image.load(os.path.join("sonicgame/Assets/Monster", "agumon.png")),
            pygame.image.load(os.path.join("sonicgame/Assets/Monster", "agumon2.png")),
            pygame.image.load(os.path.join("sonicgame/Assets/Monster", "gangar.png")),
            pygame.image.load(os.path.join("sonicgame/Assets/Monster", "pikachu.png"))]

PURPLE_PTERNODON = [pygame.image.load(os.path.join("sonicgame/Assets/Bird", "purplepter1.png")),
        pygame.image.load(os.path.join("sonicgame/Assets/Bird", "purplepter2.png"))]

GREEN_PTERNODON = [pygame.image.load(os.path.join("sonicgame/Assets/Bird", "greenpter1.png")),
        pygame.image.load(os.path.join("sonicgame/Assets/Bird", "greenpter2.png"))]

RING = [pygame.image.load(os.path.join("sonicgame/Assets/Other", "ring.png")),
        pygame.image.load(os.path.join("sonicgame/Assets/Other", "ring.png"))]

POTION = [pygame.image.load(os.path.join("sonicgame/Assets/Other", "potion.png")),
        pygame.image.load(os.path.join("sonicgame/Assets/Other", "potion.png"))]

CLOUD = pygame.image.load(os.path.join("sonicgame/Assets/Other", "Cloud.png"))

MOUNTAIN = pygame.image.load(os.path.join("sonicgame/Assets/Other", "mountain.png"))

BG = pygame.image.load(os.path.join("sonicgame/Assets/Other", "backgroundsonic2.png"))

class Sonic:
    X_POS = 80
    Y_POS = 300
    Y_POS_DUCK = 310
    JUMP_VEL = 8.5

    def __init__(self):
        self.duck_img = DASHING
        self.run_img = RUNNING
        self.jump_img = JUMPING

        self.sonic_dash = False
        self.sonic_run = True
        self.sonic_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.sonic_rect = self.image.get_rect()
        self.sonic_rect.x = self.X_POS
        self.sonic_rect.y = self.Y_POS

    def update(self, userInput):
        if self.sonic_dash:
            self.duck()
        if self.sonic_run:
            self.run()
        if self.sonic_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

        if userInput[pygame.K_UP] and not self.sonic_jump:
            # pygame.mixer.Sound.play(jump_sound)
            self.sonic_dash = False
            self.sonic_run = False
            self.sonic_jump = True
            pygame.mixer.Sound.play(jump_sound)
            pygame.mixer.Sound.stop(run_sound)
            
        elif userInput[pygame.K_DOWN] and not self.sonic_jump:
            self.sonic_dash = True
            self.sonic_run = False
            self.sonic_jump = False            
            
            pygame.mixer.Sound.play(dash_sound)
            pygame.mixer.Sound.stop(run_sound)
          
        elif not (self.sonic_jump or userInput[pygame.K_DOWN]):
            self.sonic_dash = False
            self.sonic_run = True
            self.sonic_jump = False
            if not pygame.mixer.get_busy():
                pygame.mixer.Sound.play(run_sound)
           
    def duck(self):
        self.image = self.duck_img[self.step_index // 2]
        self.sonic_rect = self.image.get_rect()
        self.sonic_rect.x = self.X_POS
        self.sonic_rect.y = self.Y_POS_DUCK
        self.step_index += 1
        

    def run(self):
        self.image = self.run_img[self.step_index // 2]
        self.sonic_rect = self.image.get_rect()
        self.sonic_rect.x = self.X_POS
        self.sonic_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img
        if self.sonic_jump:
            self.sonic_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < - self.JUMP_VEL:
            self.sonic_jump = False
            self.jump_vel = self.JUMP_VEL

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.sonic_rect.x, self.sonic_rect.y))


class Cloud:
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = CLOUD
        self.width = self.image.get_width()

    def update(self):
        self.x -= game_speed
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))


class Mountain:
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = MOUNTAIN
        self.width = self.image.get_width()

    def update(self):
        self.x -= game_speed
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))


class Obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()
            

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)

class BonusRing:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            rings.pop()
            

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)

class Potions:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            potions.pop()
            

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)


class SmallCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 325

class LargeCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 300

class Cactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 290

class Rock(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 315

class Monster(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 7)
        super().__init__(image, self.type)
        self.rect.y = 300

class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 240
        self.index = 0

    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index//5], self.rect)
        self.index += 1

class Ring(BonusRing):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 220
        self.index = 0

    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index//5], self.rect)
        self.index += 1

class Potion(Potions):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 220
        self.index = 0

    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index//5], self.rect)
        self.index += 1


def writeFile():
    with open("SonicScores.txt", 'a') as file:
        file.write(str(points) + "\n") 


scoreHistory = []
def readFile():
    with open("SonicScores.txt", 'r') as file:
        for s in file:
            scoreHistory.append(int(ｓ))
        file.close()


def main():
    pygame.mixer.Sound.play(theme_sound)
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles, rings, potions, multiple
    multiple = 1
    with open("SonicScores.txt", 'a') as file:
        file.write("0" + "\n") 
    readFile()
    run = True
    clock = pygame.time.Clock()
    player = Sonic()
    cloud = Cloud()
   
    mountain = Mountain()
    game_speed = 20
    x_pos_bg = 0
    y_pos_bg = 395
    points = 0
    font = pygame.font.Font('freesansbold.ttf', 20)
    obstacles = []
    rings = []
    potions = []
    death_count = 0

    def score():
        global points, game_speed
        points += multiple
        if points % 100 == 0:
            game_speed += 0.5

        text = font.render("SCORES: " + str(points), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (1000, 40)
        SCREEN.blit(text, textRect)

        highScoreText = font.render("HIGH SCORE: " + str(max(scoreHistory)), True, (0, 0, 0))
        highScoreRect = highScoreText.get_rect()
        highScoreRect.center = (800, 40)
        SCREEN.blit(highScoreText, highScoreRect)



    def background():
        global x_pos_bg, y_pos_bg
        image_width = BG.get_width()
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed

    start_ticks = 0

    while run:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        SCREEN.fill(color)
        
        userInput = pygame.key.get_pressed()

        mountain.draw(SCREEN)
        mountain.update()
        player.draw(SCREEN)
        player.update(userInput)

        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(SmallCactus(SMALL_CACTUS))
            elif random.randint(0, 2) == 1:
                obstacles.append(Monster(MONSTER))
            elif random.randint(0, 2) == 0:
                obstacles.append(Rock(ROCK))
            elif random.randint(0, 2) == 1:
                obstacles.append(LargeCactus(LARGE_CACTUS))
            elif random.randint(0, 2) == 1:
                obstacles.append(Cactus(CACTUS))
            elif random.randint(0, 2) == 2:
                obstacles.append(Bird(PURPLE_PTERNODON))
            elif random.randint(0, 2) == 2:
                obstacles.append(Bird(GREEN_PTERNODON))

        if len(rings) == 0:
            if random.randint(0,8) == 0:
                rings.append(Ring(RING))

        for r in rings:
            r.draw(SCREEN)
            r.update()
            if player.sonic_rect.colliderect(r.rect):
                pygame.mixer.Sound.play(ring_sound)
                points += 250
                rings.pop()

        if len(potions) == 0:
            if random.randint(0,1000) == 200:
                potions.append(Potion(POTION)) 
    
        for p in potions:
            p.draw(SCREEN)
            p.update()
            if player.sonic_rect.colliderect(p.rect):
                pygame.mixer.Sound.play(potion_sound)
                start_ticks=pygame.time.get_ticks() #starter tick
                multiple = 100
                
                potions.pop()

        seconds=(pygame.time.get_ticks()-start_ticks)/1000 #calculate how many seconds
       
        if seconds>10: # if more than 10 seconds change multple to 1
            multiple = 1
  
        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update()
            if player.sonic_rect.colliderect(obstacle.rect):
                writeFile()
                pygame.mixer.Sound.play(death_sound)
                pygame.time.delay(1000)
                death_count += 1
                menu(death_count)

      
        background()

        cloud.draw(SCREEN)
        cloud.update()
       
        score()

        clock.tick(30)
        pygame.display.update()


def menu(death_count):
    pygame.mixer.Sound.stop(theme_sound)
    global points
    run = True
    while run:
        SCREEN.fill(color)
        font = pygame.font.Font('freesansbold.ttf', 30)

        if death_count == 0:
            text = font.render("Press any Key to Start", True, (0, 0, 0))
        elif death_count > 0:
            text = font.render("Press any Key to Restart", True, (0, 0, 0))
            score = font.render("Your Score: " + str(points), True, (0, 0, 0))
            scoreRect = score.get_rect()
            scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
            SCREEN.blit(score, scoreRect)
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        SCREEN.blit(text, textRect)
        SCREEN.blit(RUNNING[0], (SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2 - 140))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                main()
    pygame.quit()

root.mainloop() 