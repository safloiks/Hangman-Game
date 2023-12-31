import pygame
import random
import pygame.time
import time

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True
pygame.font.init()
screen.fill("white")


def face_play():
  pygame.draw.circle(screen, "black", (380, 180), 35)
  pygame.draw.circle(screen, "white", (365, 170), 7)
  pygame.draw.circle(screen, "black", (365, 170), 4)
  pygame.draw.circle(screen, (255, 0, 0), (365, 170), 2)
  pygame.draw.circle(screen, "white", (393, 170), 7)
  pygame.draw.circle(screen, "black", (393, 170), 4)
  pygame.draw.circle(screen, (255, 0, 0), (393, 170), 2)
  pygame.draw.rect(screen, (255, 255, 255), (358, 190, 45, 5))
#Draws face on play screen

def body_play():
  pygame.draw.rect(screen, (0, 0, 0), (362, 230, 36, 135))

  
#Draws body on play screen

def neck_play():
  pygame.draw.rect(screen, (0, 0, 0), (372, 212, 15, 24))

#Draws neck on play screen


def left_arm_play():
  pygame.draw.line(screen, (0, 0, 0), (370, 249), (313, 300), 23)


#Draws left arm on play screen


def right_arm_play():
  pygame.draw.line(screen, (0, 0, 0), (388, 249), (445, 300), 23)


#Draws right arm on play screen


def left_leg_play():
  pygame.draw.line(screen, ((0, 0, 0)), (374, 365), (354, 465), 25)


#Draws left leg on play screen


def right_leg_play():
  pygame.draw.line(screen, (0, 0, 0), (385, 365), (419, 465), 25)

#Draws right leg on play screen


def lighterBackButton1():
  pygame.draw.rect(screen, ("white"), (7, 6, 137, 47))
  screen.blit(
    pygame.font.SysFont("courier new", 35).render("< BACK", True, "black"),
    (11, 8))
  pygame.display.flip()

#Lighter colored version of back button 1


def darkerBackButton1():
  pygame.draw.rect(screen, (100, 100, 100), (7, 6, 137, 47))
  screen.blit(
    pygame.font.SysFont("courier new", 35).render("< BACK", True, "black"),
    (11, 8))
  pygame.display.flip()

#Darker colored version of back button 1

def lighterBackButton2():
  pygame.draw.rect(screen, ("white"), (23, 21, 137, 47))
  screen.blit(
    pygame.font.SysFont("courier new", 35).render("< EXIT", True, "black"),
    (24, 24))
  pygame.display.flip()

#Lighter colored version of back button 2

def darkerBackButton2():
  pygame.draw.rect(screen, (100, 100, 100), (23, 21, 137, 47))
  screen.blit(
    pygame.font.SysFont("courier new", 35).render("< EXIT", True, "black"),
    (24, 24))
  pygame.display.flip()

#Darker colored version of back button 2

def lighterHighlightInstructions():
  pygame.draw.rect(screen, ("white"), (270, 180, 370, 70))
  screen.blit(
    pygame.font.SysFont("courier new", 50).render("INSTRUCTIONS", True,
                                                  "black"), (273, 185))
  pygame.display.flip()

#Lighter colored version of Instructions button

def darkerHighlightInstructions():
  pygame.draw.rect(screen, (100, 100, 100), (270, 180, 370, 70))
  screen.blit(
    pygame.font.SysFont("courier new", 50).render("INSTRUCTIONS", True,
                                                  "black"), (273, 185))
  pygame.display.flip()

#Darker colored version of Instructions button

def lighterHighlightPlay():
  pygame.draw.rect(screen, ("white"), (300, 310, 286, 70))
  screen.blit(
    pygame.font.SysFont("courier new", 50).render("PLAY", True, "black"),
    (374, 315))
  pygame.display.flip()

#Lighter colored version of Play button

def darkerHighlightPlay():
  pygame.draw.rect(screen, (100, 100, 100), (300, 310, 286, 70))
  screen.blit(
    pygame.font.SysFont("courier new", 50).render("PLAY", True, "black"),
    (374, 315))
  pygame.display.flip()

#Darker colored version of Play button
  
def Home():
  screen.fill("grey")
  pygame.display.update

  pygame.draw.rect(screen, ((132, 136, 132)), (16, 110, 75, 15))
  pygame.draw.rect(screen, ((132, 136, 132)), (75, 110, 20, 40))
  #hanging pole

  pygame.draw.rect(screen, ((32, 42, 68)), (0, 0, 800, 16))
  pygame.draw.rect(screen, ((32, 42, 68)), (0, 0, 17, 800))
  pygame.draw.rect(screen, ((32, 42, 68)), (0, 585, 800, 17))
  pygame.draw.rect(screen, ((32, 42, 68)), (785, 0, 17, 780))
  #screen frame

  pygame.draw.rect(screen, ("black"), (258, 16, 401, 100))
  pygame.draw.rect(screen, ("gold"), (265, 21, 387, 88))
  #home screen hangman button

  pygame.draw.rect(screen, ("black"), (263, 174, 384, 83))
  pygame.draw.rect(screen, ("white"), (270, 180, 370, 70))
  #home screen instructions button

  pygame.draw.rect(screen, ("black"), (293, 304, 300, 83))
  pygame.draw.rect(screen, ("white"), (300, 310, 286, 70))
  #home screen play button

  pygame.draw.rect(screen, (247, 104, 6), (17, 495, 768, 90))
  screen.blit(
    pygame.font.SysFont("courier new", 90).render("HANGMAN", True, "black"),
    (270, 15))
  screen.blit(
    pygame.font.SysFont("courier new", 50).render("INSTRUCTIONS", True,
                                                  "black"), (273, 185))
  screen.blit(
    pygame.font.SysFont("courier new", 50).render("PLAY", True, "black"),
    (374, 315))

#Words on buttons

  
  pygame.draw.circle(screen, "black", (85, 180), 35)
  pygame.draw.circle(screen, "white", (70, 170), 7)
  pygame.draw.circle(screen, "black", (70, 170), 4)
  pygame.draw.circle(screen, (255, 0, 0), (70, 170), 2)
  pygame.draw.circle(screen, "white", (98, 170), 7)
  pygame.draw.circle(screen, "black", (98, 170), 4)
  pygame.draw.circle(screen, (255, 0, 0), (98, 170), 2)
  pygame.draw.rect(screen, (255, 255, 255), (63, 190, 45, 5))
  #Home screen hangman face

  pygame.draw.rect(screen, (0, 0, 0), (67, 230, 36, 135))
  #Home screen hangman body

  pygame.draw.rect(screen, (0, 0, 0), (77, 212, 15, 24))
  #Home screen hangman neck

  pygame.draw.line(screen, (0, 0, 0), (75, 249), (18, 300), 23)
  #Home screen hangman left arm

  pygame.draw.line(screen, (0, 0, 0), (93, 249), (170, 300), 23)
  #Home screen hangman right arm

  pygame.draw.line(screen, ((0, 0, 0)), (79, 365), (59, 465), 25)
  #Home screen hangman left leg

  pygame.draw.line(screen, (0, 0, 0), (90, 365), (124, 465), 25)
  #Home screen hangman right leg

  pygame.draw.rect(screen, (90, 90, 90), (80, 30, 90, 50))
  pygame.draw.rect(screen, (90, 90, 90), (60, 50, 140, 50))
  #Home screen cloud1 left side

  pygame.draw.rect(screen, (90, 90, 90), (150, 130, 50, 30))
  pygame.draw.rect(screen, (90, 90, 90), (130, 150, 100, 30))
  #Home screen cloud2 left side

  pygame.draw.rect(screen, (90, 90, 90), (175, 215, 35, 30))
  pygame.draw.rect(screen, (90, 90, 90), (160, 235, 80, 30))
  #Home screen cloud3 left side

  pygame.draw.rect(screen, (90, 90, 90), (200, 297, 35, 30))
  pygame.draw.rect(screen, (90, 90, 90), (185, 317, 80, 30))
  #Home screen cloud4 left side

  pygame.draw.rect(screen, (90, 90, 90), (240, 390, 35, 30))
  pygame.draw.rect(screen, (90, 90, 90), (225, 410, 80, 30))
  #Home screen cloud5 left side

  pygame.draw.rect(screen, (247, 130, 20), (400, 535, 50, 15))
  pygame.draw.rect(screen, (247, 130, 20), (270, 510, 50, 15))
  pygame.draw.rect(screen, (247, 130, 20), (600, 550, 50, 15))
  pygame.draw.rect(screen, (247, 130, 20), (200, 515, 50, 15))
  pygame.draw.rect(screen, (247, 130, 20), (100, 560, 50, 15))
  pygame.draw.rect(screen, (247, 130, 20), (650, 515, 50, 15))
  pygame.draw.rect(screen, (247, 130, 20), (310, 545, 50, 15))
  pygame.draw.rect(screen, (247, 130, 20), (520, 525, 50, 15))
  pygame.draw.rect(screen, (247, 130, 20), (80, 505, 50, 15))
  pygame.draw.rect(screen, (247, 60, 20), (40, 550, 50, 15))
  pygame.draw.rect(screen, (247, 60, 20), (170, 540, 50, 15))
  pygame.draw.rect(screen, (247, 60, 20), (320, 515, 50, 15))
  pygame.draw.rect(screen, (247, 60, 20), (570, 560, 50, 15))
  pygame.draw.rect(screen, (247, 60, 20), (380, 550, 50, 15))
  pygame.draw.rect(screen, (247, 60, 20), (430, 530, 50, 15))
  pygame.draw.rect(screen, (247, 60, 20), (60, 520, 50, 15))
  pygame.draw.rect(screen, (247, 60, 20), (680, 567, 50, 15))
  pygame.draw.rect(screen, (247, 60, 20), (240, 555, 50, 15))
  pygame.draw.rect(screen, (247, 60, 20), (707, 510, 50, 15))
  pygame.draw.rect(screen, (254, 222, 23), (557, 505, 50, 15))
  pygame.draw.rect(screen, (254, 222, 23), (480, 549, 50, 15))
  pygame.draw.rect(screen, (254, 222, 23), (180, 559, 50, 15))
  pygame.draw.rect(screen, (254, 222, 23), (450, 501, 50, 15))
  pygame.draw.rect(screen, (254, 222, 23), (150, 506, 50, 15))
  #Home screen lava pool

  pygame.draw.line(screen, (254, 222, 23), (640, 430), (670, 495), 8)
  pygame.draw.line(screen, (254, 222, 23), (660, 430), (670, 495), 8)
  pygame.draw.line(screen, (254, 222, 23), (680, 430), (670, 495), 8)
  pygame.draw.line(screen, (254, 222, 23), (700, 430), (670, 495), 8)
  pygame.draw.line(screen, (254, 222, 23), (720, 430), (670, 495), 8)
  pygame.draw.line(screen, (254, 222, 23), (620, 430), (670, 495), 8)
  #Home screen spark of lava 

  pygame.draw.rect(screen, (90, 90, 90), (665, 300, 50, 30))
  pygame.draw.rect(screen, (90, 90, 90), (630, 320, 110, 30))
  #Home screencloud1 right side

  pygame.draw.rect(screen, (90, 90, 90), (715, 230, 35, 30))
  pygame.draw.rect(screen, (90, 90, 90), (680, 250, 90, 30))
  #Home screen cloud2 right side

  pygame.display.flip()
  

with open("words.txt", 'r') as fp:
  Allwords = (fp.readlines())
for i in range(len(Allwords)):
  Allwords[i] = Allwords[i].strip()

#Creating Allwords variable that contains all the words

stages = [
  face_play(),
  body_play(),
  neck_play(),
  left_arm_play(),
  right_arm_play(),
  left_leg_play(),
  right_leg_play()
]
#Stages of hangman progression


def wincheck(word, guessed_letters):
  for letter in word:
    if letter not in guessed_letters:
      return False
  return True

#Checks if complete word has been guessed


def you_lose():
  
  screen.fill("red")

  pygame.draw.circle(screen, "yellow", (760, 15), 70)
  #sun on loss screen

  pygame.draw.rect(screen, (("black")), (17, 15, 149, 60))
  #exit frame on loss screen


  pygame.draw.rect(screen, ((32, 42, 68)), (0, 0, 800, 16))
  pygame.draw.rect(screen, ((32, 42, 68)), (0, 0, 17, 800))
  pygame.draw.rect(screen, ((32, 42, 68)), (0, 585, 800, 17))
  pygame.draw.rect(screen, ((32, 42, 68)), (785, 0, 17, 780))
  #screen frame on loss screen

  pygame.draw.circle(screen, "black", (380, 490), 35)#+310
  pygame.draw.line(screen,(255,255,255),(370,480),(360,470),5)
  pygame.draw.line(screen,(255,255,255),(370,470),(360,480),5)
  pygame.draw.line(screen,(255,255,255),(397,480),(387,470),5)
  pygame.draw.line(screen,(255,255,255),(397,470),(387,480),5)

  #face of hangman on loss screen
 
  pygame.draw.rect(screen, (247, 104, 6), (17, 495, 768, 90))
  pygame.draw.rect(screen, (247, 130, 20), (400, 535, 50, 15))
  pygame.draw.rect(screen, (247, 130, 20), (270, 510, 50, 15))
  pygame.draw.rect(screen, (247, 130, 20), (600, 550, 50, 15))
  pygame.draw.rect(screen, (247, 130, 20), (200, 515, 50, 15))
  pygame.draw.rect(screen, (247, 130, 20), (100, 560, 50, 15))
  pygame.draw.rect(screen, (247, 130, 20), (650, 515, 50, 15))
  pygame.draw.rect(screen, (247, 130, 20), (310, 545, 50, 15))
  pygame.draw.rect(screen, (247, 130, 20), (520, 525, 50, 15))
  pygame.draw.rect(screen, (247, 130, 20), (80, 505, 50, 15))
  pygame.draw.rect(screen, (247, 60, 20), (40, 550, 50, 15))
  pygame.draw.rect(screen, (247, 60, 20), (170, 540, 50, 15))
  pygame.draw.rect(screen, (247, 60, 20), (320, 515, 50, 15))
  pygame.draw.rect(screen, (247, 60, 20), (570, 560, 50, 15))
  pygame.draw.rect(screen, (247, 60, 20), (380, 550, 50, 15))
  pygame.draw.rect(screen, (247, 60, 20), (430, 530, 50, 15))
  pygame.draw.rect(screen, (247, 60, 20), (60, 520, 50, 15))
  pygame.draw.rect(screen, (247, 60, 20), (680, 567, 50, 15))
  pygame.draw.rect(screen, (247, 60, 20), (240, 555, 50, 15))
  pygame.draw.rect(screen, (247, 60, 20), (707, 510, 50, 15))
  pygame.draw.rect(screen, (254, 222, 23), (557, 505, 50, 15))
  pygame.draw.rect(screen, (254, 222, 23), (480, 549, 50, 15))
  pygame.draw.rect(screen, (254, 222, 23), (180, 559, 50, 15))
  pygame.draw.rect(screen, (254, 222, 23), (450, 501, 50, 15))
  pygame.draw.rect(screen, (254, 222, 23), (150, 506, 50, 15))
  #lava pool in loss screen

  pygame.draw.line(screen, (254, 222, 23), (640, 430), (670, 495), 8)
  pygame.draw.line(screen, (254, 222, 23), (660, 430), (670, 495), 8)
  pygame.draw.line(screen, (254, 222, 23), (680, 430), (670, 495), 8)
  pygame.draw.line(screen, (254, 222, 23), (700, 430), (670, 495), 8)
  pygame.draw.line(screen, (254, 222, 23), (720, 430), (670, 495), 8)
  pygame.draw.line(screen, (254, 222, 23), (620, 430), (670, 495), 8)
  #lava spark in loss screen

  
  pygame.draw.rect(screen,("black"),(140,200,550,190))
  pygame.draw.rect(screen,("white"),(145,207,541,176))
  screen.blit(
  pygame.font.SysFont("courier new", 90).render("YOU LOSE!", True, "black"),
  (175, 225))
#You lose button in loss screen


  
  pygame.display.flip()


def you_win():
  
  screen.fill("light blue")

  pygame.draw.circle(screen,"yellow", (760, 15), 70)
  #pygame.draw.line(screen, ("yellow"), (693, 32), (640, 55), 8)
  #pygame.draw.line(screen, ("yellow"), (693, 32), (640, 55), 8)
  
  #sun on winning screen
  

  pygame.draw.rect(screen, (("black")), (17, 15, 149, 60))
  #exit button frame on winning screen
  
  pygame.draw.rect(screen, ((32, 42, 68)), (0, 0, 800, 16))
  pygame.draw.rect(screen, ((32, 42, 68)), (0, 0, 17, 800))
  pygame.draw.rect(screen, ((32, 42, 68)), (0, 585, 800, 17))
  pygame.draw.rect(screen, ((32, 42, 68)), (785, 0, 17, 780))
  #screen frame on winning screen
  
  pygame.draw.rect(screen, ("grey"), (17, 495, 768, 90))
  pygame.draw.rect(screen, (132, 136, 132), (17, 536, 768, 10))
  pygame.draw.rect(screen, (132, 136, 132), (17,495, 10, 90))
  pygame.draw.rect(screen, (132, 136, 132), (775,495, 10, 90))
  pygame.draw.rect(screen, (132, 136, 132), (17,495, 768, 10))

  pygame.draw.rect(screen, (132, 136, 132), (17,575, 768, 10))
  pygame.draw.rect(screen, (132, 136, 132), (390,495, 10, 90))
  pygame.draw.rect(screen, (132, 136, 132), (186,495, 10, 90))
  pygame.draw.rect(screen, (132, 136, 132), (576,495, 10, 90))
  #pavement on winning screen


  pygame.draw.rect(screen,("grey"),(260,25,90,50))
  pygame.draw.rect(screen,("grey"),(220,50,200,50))

  pygame.draw.rect(screen,("grey"),(540,75,90,50))
  pygame.draw.rect(screen,("grey"),(500,100,200,50))
  #clouds on winning screen

  pygame.draw.rect(screen,("black"),(140,200,550,190))
  pygame.draw.rect(screen,("white"),(145,207,541,176))
  screen.blit(
  pygame.font.SysFont("courier new", 90).render("YOU WIN!", True, "black"),
  (170, 230))
  #You win button on winning screen
   

  pygame.display.flip()


def update_lives(num_guess):
  pygame.draw.rect(screen, (255, 255, 255),
                   (232, 420, 50, 45))  # Clear the area
  myFont = pygame.font.SysFont("courier new", 48)
  text = f"{7 - num_guess}"
  text_surface = myFont.render(text, True, (0, 0, 0))
  screen.blit(text_surface, (232, 413))
#Updates lives on play screen when letter is guessed wrong


def Play_screen():

  screen.fill("grey")
  clock = pygame.time.Clock()
  message_font = pygame.font.SysFont("courier new", 36)
  
  pygame.draw.rect(screen, ("black"), (16, 16, 150, 60))
  pygame.draw.rect(screen, ("white"), (23, 21, 137, 47))
  screen.blit(
    pygame.font.SysFont("courier new", 35).render("< EXIT", True, "black"),
    (24, 24))
  #exit button on play screen

  
  pygame.draw.rect(screen, ((132, 136, 132)), (16, 110, 370, 15))
  pygame.draw.rect(screen, ((132, 136, 132)), (370, 110, 20, 40))
  #hanging pole on play screen

  pygame.draw.rect(screen, ((32, 42, 68)), (0, 0, 800, 16))
  pygame.draw.rect(screen, ((32, 42, 68)), (0, 0, 17, 800))
  pygame.draw.rect(screen, ((32, 42, 68)), (0, 585, 800, 17))
  pygame.draw.rect(screen, ((32, 42, 68)), (785, 0, 17, 780))
  #screen frame on play screen


  pygame.draw.rect(screen, (247, 104, 6), (17, 495, 768, 90))
  pygame.draw.rect(screen, (247, 130, 20), (400, 535, 50, 15))
  pygame.draw.rect(screen, (247, 130, 20), (270, 510, 50, 15))
  pygame.draw.rect(screen, (247, 130, 20), (600, 550, 50, 15))
  pygame.draw.rect(screen, (247, 130, 20), (200, 515, 50, 15))
  pygame.draw.rect(screen, (247, 130, 20), (100, 560, 50, 15))
  pygame.draw.rect(screen, (247, 130, 20), (650, 515, 50, 15))
  pygame.draw.rect(screen, (247, 130, 20), (310, 545, 50, 15))
  pygame.draw.rect(screen, (247, 130, 20), (520, 525, 50, 15))
  pygame.draw.rect(screen, (247, 130, 20), (80, 505, 50, 15))
  pygame.draw.rect(screen, (247, 60, 20), (40, 550, 50, 15))
  pygame.draw.rect(screen, (247, 60, 20), (170, 540, 50, 15))
  pygame.draw.rect(screen, (247, 60, 20), (320, 515, 50, 15))
  pygame.draw.rect(screen, (247, 60, 20), (570, 560, 50, 15))
  pygame.draw.rect(screen, (247, 60, 20), (380, 550, 50, 15))
  pygame.draw.rect(screen, (247, 60, 20), (430, 530, 50, 15))
  pygame.draw.rect(screen, (247, 60, 20), (60, 520, 50, 15))
  pygame.draw.rect(screen, (247, 60, 20), (680, 567, 50, 15))
  pygame.draw.rect(screen, (247, 60, 20), (240, 555, 50, 15))
  pygame.draw.rect(screen, (247, 60, 20), (707, 510, 50, 15))
  pygame.draw.rect(screen, (254, 222, 23), (557, 505, 50, 15))
  pygame.draw.rect(screen, (254, 222, 23), (480, 549, 50, 15))
  pygame.draw.rect(screen, (254, 222, 23), (180, 559, 50, 15))
  pygame.draw.rect(screen, (254, 222, 23), (450, 501, 50, 15))
  pygame.draw.rect(screen, (254, 222, 23), (150, 506, 50, 15))
  #lava pool on play screen

  pygame.draw.line(screen, (254, 222, 23), (640, 430), (670, 495), 8)
  pygame.draw.line(screen, (254, 222, 23), (660, 430), (670, 495), 8)
  pygame.draw.line(screen, (254, 222, 23), (680, 430), (670, 495), 8)
  pygame.draw.line(screen, (254, 222, 23), (700, 430), (670, 495), 8)
  pygame.draw.line(screen, (254, 222, 23), (720, 430), (670, 495), 8)
  pygame.draw.line(screen, (254, 222, 23), (620, 430), (670, 495), 8)
  #spark of lava on play screen

  pygame.draw.rect(screen, (90, 90, 90), (665, 300, 50, 30))
  pygame.draw.rect(screen, (90, 90, 90), (630, 320, 110, 30))
  #cloud1 on right side of play screen

  pygame.draw.rect(screen, (90, 90, 90), (715, 230, 35, 30))
  pygame.draw.rect(screen, (90, 90, 90), (680, 250, 90, 30))
  #cloud2 on right side of play screen

  pygame.draw.rect(screen, ((32, 42, 68)), (23, 135, 277, 344))
  pygame.draw.rect(screen, (("black")), (27, 140, 267, 333))
  #Frame of all letters in play screen

  alpha_lists = [["A", "B", "C", "D", "E"], ["F", "G", "H", "I", "J"],
                 ["K", "L", "M", "N", "O"], ["P", "Q", "R", "S", "T"],
                 ["U", "V", "W", "X", "Y"], ["Z"]]

  #list of all letters in the alphabet
  x = 33
  y = 145

  for alpha_list in alpha_lists:
    for i in range(len(alpha_list)):
      pygame.draw.rect(screen, ("white"), (x, y, 47, 45))
      screen.blit(
        pygame.font.SysFont("courier new", 48).render(alpha_list[i], True,
                                                      (0, 0, 0)),
        (x + 5, y - 3))
      x = x + 52
    y = y + 55
    x = 33
#once moved to the play screen all letters will be displayed in the alphabet frame with a white background
  
  pygame.draw.rect(screen, (("white")), (86, 420, 203, 45))
  screen.blit(
    pygame.font.SysFont("courier new", 40).render("LIVES:", True, (0, 0, 0)),
    (87, 417))

#Draws the text "LIVES" to see how many lives you have left
  
  myFont = pygame.font.SysFont("courier new", 48)
  text_surface = myFont.render("7", True, (255, 0, 0))
  #screen.blit(text_surface, (232, 420))

#making font

  update_lives(0)

  pygame.display.flip()

  #keyboard input
  keys_pressed = set()
  guessed_letters = set()
  while True:
    num_guess = 0
    word = random.choice(Allwords)
    guessed_letters = set()
    while num_guess < 7:
      for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
          pygame.quit()
          #setting everything up for code to work
        if ev.type == pygame.MOUSEBUTTONDOWN:
          mouse = pygame.mouse.get_pos()
          x, y = mouse
          if 23 <= x <= 160 and 21 <= y <= 68:
            Main()
            #Checks if mouse is clicked in the specified area
        
        mouse = pygame.mouse.get_pos()
        x, y = mouse
        #tracks mouses position across the screen
        
        x1 = 177
        if 23 <= x <= 160 and 21 <= y <= 68:
          darkerBackButton2()
        else:
          lighterBackButton2()
        #if mouse is clicked in the specified area darker highlight will appear otherwise the area will stay lighter
        
        for i in range(len(word)):
          pygame.draw.rect(screen, (("black")), (x1, 67, 45, 10))
          x1 += 52
        #Draws a line that resembles "_" at the top of the screen as many times as the amount of characters in the random word
        
        crossX1 = 33
        crossY1 = 145
        crossX2 = 79
        crossY2 = 189
        #sets x and y values for the cross that will appear when a key is pressed
        
        if ev.type == pygame.KEYDOWN:
          guess = ev.unicode
          for i, alpha_list in enumerate(alpha_lists):
            for j ,letter in enumerate(alpha_list):
              if guess.upper() == alpha_list[j]:
                pygame.draw.line(screen, (255, 0, 0), (crossX1 + j * 52, crossY1 + i * 55), (crossX2 + j * 52, crossY2 + i * 55), 8)
                pygame.draw.line(screen, (255, 0, 0), (crossX1 + j * 52 , crossY2 + i * 55), (crossX2 + j * 52 ,crossY1 + i * 55), 8)
            crossX1 = 33
            crossY1 = 145
            crossX2 = 79
            crossY2 = 189
            #When a key is pressed the code above will check for its position and index in the list containing the alphabet and will draw a cross over its position on the alphabet frame
            
            pygame.display.flip()
            
          
          if not str.isalpha(guess):
            screen.blit(pygame.font.SysFont("courier new", 18).render("PLEASE ONLY GUESS LETTERS!", True, "black"), (412,129))
            #checks if guessed input is a letter on the keyboard and sends a message to "PLEASE ONLY GUESS LETTERS!" if it isnt
            
            pygame.display.flip()
            time.sleep(2)
            pygame.draw.rect(screen, ("grey"), (410, 127, 300, 30))
            #will clear the screen of the "PLEASE ONLY GUESS LETTERS!" message after 2 seconds of it appearing
            
            pygame.display.flip()
          elif guess in guessed_letters:
            screen.blit(pygame.font.SysFont("courier new", 18).render("PLEASE ONLY GUESS THE LETTER ONCE!", True, "black"), (410,129))
            #checks if guessed input has already been guessed and sends a message to "PLEASE ONLY GUESS THE LETTER ONCE!" if it has been guessed before
            pygame.display.flip()

            time.sleep(2)
            pygame.draw.rect(screen, ("grey"), (410, 127, 372, 30))
            #will clear the screen of the "PLEASE ONLY GUESS THE LETTER ONCE!" message after 2 seconds of it appearing
            pygame.display.flip()
          else:
            guessed_letters.add(guess)
            # if guessed input hasnt been guessed before it will be added to the gueseed letters set
          if guess not in word and str.isalpha(guess):
            # if guessed input is not in the word it will let you know in console
            num_guess = num_guess + 1
            if num_guess == 1:
              face_play()
            elif num_guess == 2:
              neck_play()
            elif num_guess == 3:
              body_play()
            elif num_guess == 4:
              left_arm_play()
            elif num_guess == 5:
              right_arm_play()
            elif num_guess == 6:
              left_leg_play()
            elif num_guess == 7:
              right_leg_play()
            # for each guessed input that isnt the word the stages of the hangman will appear on the screen aswell as the number of guesses you've used gets added to
            update_lives(num_guess)
            pygame.draw.rect(screen, (255, 255, 255), (232, 420, 50, 45))
            myFont = pygame.font.SysFont("courier new", 48)
            text = f"{7 - num_guess}"
            text_surface = myFont.render(text, True, ("black"))
            screen.blit(text_surface, (232, 413))
            #updates number of lives left on the play screen next to "LIVES"

            pygame.display.flip()
          else:
            #Lets you know if the guessed input is a letter in the random word
            
            guess_indices = [i for i, letter in enumerate(word) if letter == guess]
            for index in guess_indices:
                screen.blit(pygame.font.SysFont("courier new", 48).render(guess.upper(), True, "black"), (177 + index * 53, 15))
            #If guessed input is in the random word the code above will check for the index of the letter in the random word and will draw it at the appropriate position on the screen above the lines/"_" at the top of the screen

          if num_guess == 7:
            pygame.time.wait(500)
            you_lose()
            #checks if guessed input was incorrect 7 times and waits 5 seconds to send you to the loss screen
            pygame.display.flip()
            return
          if wincheck(word, guessed_letters):
            pygame.time.wait(500)
            you_win()
            #checks if all words in the random word have been correctly guessed and sends you to winning screen when word has been completed
            return
    mouse = pygame.mouse.get_pos()
    x, y = mouse
    if 23 <= x <= 160 and 21 <= y <= 68:
      darkerBackButton2()
    else:
      lighterBackButton2()
    #If mouse is clicked in the specified area the color will change to darker and will stay the same if not
    pygame.display.flip()
    clock.tick(60)


def Instructions():
  screen.fill("orange")

  pygame.draw.rect(screen, ("black"), (1, 90, 797, 509))
  pygame.draw.rect(screen, ("white"), (8, 96, 784, 496))
  #screen frame in Instructions screen 

  screen.blit(
    pygame.font.SysFont("courier new", 15).render(
      "Guessing the Secret Word: Your goal is to guess a secret word chosen by the computer.",
      True, "black"), (11, 99))
  screen.blit(
    pygame.font.SysFont("courier new", 15).render(
      "The word will be represented by a series of underscores, each representing a letter.",
      True, "black"), (11, 113))

  screen.blit(
    pygame.font.SysFont("courier new", 15).render(
      "Guess One Letter at a Time: Guess a single letter from the alphabet in each turn.",
      True, "black"), (11, 163))
  screen.blit(
    pygame.font.SysFont("courier new", 15).render(
      "Type in the letter you think might be in the word and submit your guess.",
      True, "black"), (11, 177))

  screen.blit(
    pygame.font.SysFont("courier new", 15).render(
      "Correct Guesses: If the letter you guessed is in the word, the underscores that match",
      True, "black"), (11, 227))
  screen.blit(
    pygame.font.SysFont("courier new", 15).render(
      "that letter's position(s) will be replaced with the correct letter.",
      True, "black"), (11, 241))

  screen.blit(
    pygame.font.SysFont("courier new", 15).render(
      "Incorrect Guesses: If the letter you guessed is not in the word, the game will keep",
      True, "black"), (11, 291))
  screen.blit(
    pygame.font.SysFont("courier new", 15).render(
      "track of the incorrect guesses you've made. Additionally, part of a hangman figure",
      True, "black"), (11, 305))
  screen.blit(
    pygame.font.SysFont("courier new", 15).render(
      "will be drawn, showing your progress toward losing the game.", True,
      "black"), (11, 319))

  screen.blit(
    pygame.font.SysFont("courier new", 15).render(
      "Maximum Incorrect Guesses: You have a limit of 7 incorrect guesses before the hangman",
      True, "black"), (11, 369))
  screen.blit(
    pygame.font.SysFont("courier new", 15).render(
      "figure is completely drawn, and the game ends.",
      True, "black"), (11, 383))

  screen.blit(
    pygame.font.SysFont("courier new", 15).render(
      "Winning: If you successfully guess all the letters in the word before the hangman",
      True, "black"), (11, 433))
  screen.blit(
    pygame.font.SysFont("courier new", 15).render(
      "figure is fully drawn, you win! You'll be congratulated on your victory.",
      True, "black"), (11, 447))

  screen.blit(
    pygame.font.SysFont("courier new", 15).render(
      "Losing: If you reach the maximum allowed incorrect guesses and the hangman figure is",
      True, "black"), (11, 497))
  screen.blit(
    pygame.font.SysFont("courier new", 15).render(
      "completed, you lose the game. The game will inform you of your loss.",
      True, "black"), (11, 511))

#displays the games instructions on the instructions screen

  
  pygame.draw.rect(screen, ("black"), (262, 0, 280, 60))
  pygame.draw.rect(screen, ("white"), (269, 6, 267, 47))
  #instructionsframe on instructions screen

  pygame.draw.rect(screen, ("black"), (0, 0, 150, 60))
  pygame.draw.rect(screen, ("white"), (7, 6, 137, 47))
  #backframe on instructions screen

  screen.blit(
    pygame.font.SysFont("courier new", 35).render("INSTRUCTIONS", True,
                                                  "black"), (273, 8))
  screen.blit(
    pygame.font.SysFont("courier new", 35).render("< BACK", True, "black"),
    (11, 8))
  pygame.display.flip()
# displays "INSTRUCTIONS" and "BACK" on the positions of their respective buttons

def Main():
  screen_number = 0
  Home()
  pygame.display.flip()
  while True:
    mouse = pygame.mouse.get_pos()
    x, y = mouse
    for ev in pygame.event.get():
      if ev.type == pygame.QUIT:
        pygame.quit()
      if ev.type == pygame.MOUSEBUTTONDOWN:
        mouse = pygame.mouse.get_pos()
        if screen_number == 0:
          if x >= 300 and x <= 590 and y >= 315 and y <= 380:
            screen_number = 2
            Play_screen()
          #checks if on screen number 0(Home screen) and if mouse is clicked on the specified posistion screen number will change to 2)(Play screen)
          
          if x >= 260 and x <= 650 and y >= 175 and y <= 255:
            screen_number = 1
            Instructions()
        if screen_number == 1:
          if x >= 5 and x <= 142 and y >= 7 and y <= 54:
            Home()
            screen_number = 0
        if screen_number == 2:
          if x >= 17 and x <= 140 and y >= 17 and y <= 65:
            Home()
            screen_number = 0
    if screen_number == 0:
      if x >= 260 and x <= 650 and y >= 175 and y <= 255:
        darkerHighlightInstructions()
      else:
        lighterHighlightInstructions()
      if x >= 300 and x <= 590 and y >= 315 and y <= 380:
        darkerHighlightPlay()
      else:
        lighterHighlightPlay()
    if screen_number == 1:
      if x >= 5 and x <= 142 and y >= 7 and y <= 54:
        darkerBackButton1()
      else:
        lighterBackButton1()
    if screen_number == 2:
      if x >= 17 and x <= 140 and y >= 17 and y <= 65:
        darkerBackButton2()
      else:
        lighterBackButton2()
#checks for current screen number and changes to different screens depending on what screen you're on and what button you click

Main()
