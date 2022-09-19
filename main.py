import pygame 
import sys 
from pygame.locals import *

# initializing pygame 
pygame.init()

# setting the screen size
screen = pygame.display.set_mode((900, 600))

# renames the gui's title 
title_caption = "proxress"
pygame.display.set_caption(title_caption)


"""
Fonts 
"""
# loads fonts  
Mainfont = pygame.font.SysFont("dejavusansmono", 20)
smallFont = pygame.font.SysFont("dejavusansmono", 12)

"""
Text 
"""
# main menu text
text1 = Mainfont.render("Main Menu_", True, (238, 165, 165))
# instructions text 
instruc = smallFont.render("press the blue button whenever you want to continue or to select your decision!", True, (239, 165, 167))


# global variable to declare the mouse click to be set to false 
click = False

# music 
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
pygame.mixer.music.load("AdhesiveWombat - 8 Bit Adventure.wav")
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1)
"""
Main Menu 
"""
def main_menu():
  global click 
  click = False

  # event loop
  while True:

      # clears the screen 
      screen.fill((0, 0, 0))

      #reaasigns the new background of the screen 
      screen.fill((222, 222, 222))   

      # displays the "Main Menu" text 
      screen.blit(text1, (100, 120))

      # displays the "Instruct" text 
      screen.blit(instruc, (100, 250))

      # returns the x, y position of the mouse  
      mx, my = pygame.mouse.get_pos()

      # creates rectangle for the button and its dimensions  
      buttonStart = pygame.Rect(100, 200, 75, 30) 

      # renders start text 
      start_text = Mainfont.render("Start", 1, (255, 255, 255))

      # displays start text
      screen.blit(start_text, (100, 175))
    
      # collisions   
      if buttonStart.collidepoint((mx, my)):
        if click:
            firstPrompt()

      #displays the button 
      pygame.draw.rect(screen, (180, 235, 252), buttonStart)

      # to quit the event loop when "x" is pressed
      for event in pygame.event.get():
        if event.type == pygame.QUIT:  
          pygame.quit()
          quit()
        
        # if i have clicked the left button, sets the click variable to true, carries over to next frame 
        if event.type == pygame.MOUSEBUTTONDOWN: 
          if event.button == 1: 
            click = True

        if event.type == pygame.MOUSEBUTTONDOWN: 
          print("going to first prompt")
          print(click)

  
      pygame.display.update()

"""
First Scene Prompt
"""
def firstPrompt():
  global click
  click = False 

  while True: 
    # clears the screen 
    screen.fill((0,0,0))
    
    #reassigns the new background of the screen 
    screen.fill((222, 222, 222))      

    # scene 1 prompt text 
    scene1prompt = Mainfont.render("a strange man you don't know is following you..", True,(255, 255, 0))
    
    # displays the first prompt 
    screen.blit(scene1prompt, (50, 250))

    
    points = smallFont.render("points: ", True, (117, 255, 117))
    screen.blit(points, (600, 40))

    """
    mouse settings 
    """
    # position of the mouse
    mx, my = pygame.mouse.get_pos() 
    
    """
    button settings 
    """
    # continue button creates shape.. (x, y, length, width  < i think? ) 
    buttonCon = pygame.Rect(50, 300, 75, 30) 
    
    #displays the button and colour of the button 
    pygame.draw.rect(screen, (180, 235, 252), buttonCon)

    """
    collisions of the mouse 
    """
    # collisions 
    if buttonCon.collidepoint((mx, my)):
      if click:
        firstScene()
    
    # to quit the event loop when "x" is pressed
    for event in pygame.event.get():
      if event.type == pygame.QUIT:  
        pygame.quit()
        quit()
      # if i have clicked the left button, sets the click variable to true, carries over to next frame 
      if event.type == pygame.MOUSEBUTTONDOWN: 
        if event.button == 1: 
          click = True
    pygame.display.update()


def firstScene(): 
  global click
  click = False
  while True:
    # clears the screen 
    screen.fill((0,0,0))
    
    #reaasigns the new background of the screen 
    screen.fill((222, 222, 222))  
    
    points = smallFont.render("points: ", True, (117, 255, 117))
    screen.blit(points, (600, 40))
    
    """
    text
    """
    # scene 1 prompt text 
    firstAsk = Mainfont.render("do you.. ", True,(255, 255, 0))
    screen.blit(firstAsk, (50, 150))

    # right choice text 
    rightChoice = smallFont.render("try to change your route and see if they're actually following you.",  True, (255, 255, 0))
    screen.blit(rightChoice, (50, 300))

    # wrong choice text 
    wrongChoice = smallFont.render("keep walking the same way ", True, (255, 255, 0))
    screen.blit(wrongChoice, (50, 200))

    
    """
    Mouse settings
    """
    # returns the x, y position of the mouse 
    mx, my = pygame.mouse.get_pos() 

    """
    Choices buttons 
    """
    # creates a rectangle for the box 
    rightButton = pygame.Rect(50, 325, 75, 30)
    wrongButton = pygame.Rect(50, 225, 75, 30)

    #displays the button and colour of the button 
    pygame.draw.rect(screen, (180, 235, 252), rightButton)
    pygame.draw.rect(screen, (180, 235, 252), wrongButton)
    

    # collisions 
    if rightButton.collidepoint((mx, my)):
      if click:
        rightChoice1()
    if wrongButton.collidepoint((mx, my)):  
      if click: 
        wrongChoice1()

    # to quit the event loop when "x" is pressed
    for event in pygame.event.get():
      if event.type == pygame.QUIT:  
        pygame.quit()
        quit()
        
    # if i have clicked the left button, sets the click variable to true, carries over to next frame 
      if event.type == pygame.MOUSEBUTTONDOWN: 
        if event.button == 1: 
          click = True


    # refreshes the screen to display the updates 
    pygame.display.update()



"""
Wrong Choice for the First Scene
"""
def wrongChoice1():
    global click
    click = False 
  

    while True: 
      # clears the screen 
      screen.fill((0,0,0))
    
      #reassigns the new background of the screen 
      screen.fill((222, 222, 222))     

      points = smallFont.render("points: ", True, (117, 255, 117))
      screen.blit(points, (600, 40))

      # scene 1 prompt text 
      explain = smallFont.render("you never know if the person following you is just going the same direction", True,(255, 255, 0))

      explain2 = smallFont.render("so try to change your route and see if its just coincidental. It also allows you to lose them.", True, (255, 255, 0))

      gameOver = smallFont.render("GAME OVER, Try Again!", True, (255, 255, 0))
    
      # displays the first prompt 
      screen.blit(explain, (50, 150))
      screen.blit(explain2,(50, 200))
      screen.blit(gameOver, (50, 250))

      """
      mouse settings 
      """
      # position of the mouse
      mx, my = pygame.mouse.get_pos() 
    
      """
      button settings 
      """
      # continue button creates shape.. (x, y, length, width  < i think? ) 
      buttonCon = pygame.Rect(50, 300, 75, 30) 
    
      #displays the button and colour of the button 
      pygame.draw.rect(screen, (180, 235, 252), buttonCon)

      """
      collisions of the mouse 
      """
      # collisions 
      if buttonCon.collidepoint((mx, my)):
        if click:
          main_menu()
    
      # to quit the event loop when "x" is pressed
      for event in pygame.event.get():
        if event.type == pygame.QUIT:  
          pygame.quit()
          quit()
        # if i have clicked the left button, sets the click variable to true, carries over to next frame 
        if event.type == pygame.MOUSEBUTTONDOWN: 
          if event.button == 1: 
            click = True
      
      pygame.display.update()


"""
Right Choice for the First Scene 
"""
def rightChoice1():
  global click 
  click = False
  
  while True:   
    # clears the screen 
    screen.fill((0,0,0))
    
    #reassigns the new background of the screen 
    screen.fill((222, 222, 222))    

    points = smallFont.render("points: 1", True, (117, 255, 117))
    screen.blit(points, (600, 40))
      
    # scene 1 prompt text 
    explain = smallFont.render(" Good Choice! you never know if the person following you is just going the same direction", True,(255, 255, 0))

    explain2 = smallFont.render("so try to change your route and see if its just coincidental. It also allows you to lose them.", True, (255, 255, 0))
    
    # displays the first prompt 
    screen.blit(explain, (50, 150))
    screen.blit(explain2,(50, 200))

    """
    mouse settings 
    """
    # position of the mouse
    mx, my = pygame.mouse.get_pos() 
    
    """
    button settings 
    """
    # continue button creates shape.. (x, y, length, width  < i think? ) 
    buttonCon = pygame.Rect(50, 300, 75, 30) 
    
    #displays the button and colour of the button 
    pygame.draw.rect(screen, (180, 235, 252), buttonCon)

    """
    collisions of the mouse 
    """
    # collisions 
    if buttonCon.collidepoint((mx, my)):
      if click:
        promptTwo()
 
    for event in pygame.event.get():
      if event.type == pygame.QUIT:  
        pygame.quit()
        quit()
      
        # if i have clicked the left button, sets the click variable to true, carries over to next frame 
      if event.type == pygame.MOUSEBUTTONDOWN: 
        if event.button == 1: 
          click = True
          
    
    pygame.display.update()

def promptTwo():
  print("promptTwo")
  global click
  click = False 

  while True: 
    # clears the screen 
    screen.fill((0,0,0))
    
    #reassigns the new background of the screen 
    screen.fill((222, 222, 222))      
    
    points = smallFont.render("points: 1", True, (117, 255, 117))
    screen.blit(points, (600, 40))

    # scene 1 prompt text 
    scene1prompt = Mainfont.render("turns out he is following you!", True,(255, 255, 0))
    
    # displays the first prompt 
    screen.blit(scene1prompt, (50, 250))

    """
    mouse settings 
    """
    # position of the mouse
    mx, my = pygame.mouse.get_pos() 
    
    """
    button settings 
    """
    # continue button creates shape.. (x, y, length, width  < i think? ) 
    buttonCon = pygame.Rect(50, 300, 75, 30) 
    
    #displays the button and colour of the button 
    pygame.draw.rect(screen, (180, 235, 252), buttonCon)

    """
    collisions of the mouse 
    """
    # collisions 
    if buttonCon.collidepoint((mx, my)):
      if click:
        secondScene()
    
    # to quit the event loop when "x" is pressed
    for event in pygame.event.get():
      if event.type == pygame.QUIT:  
        pygame.quit()
        quit()
      # if i have clicked the left button, sets the click variable to true, carries over to next frame 
      if event.type == pygame.MOUSEBUTTONDOWN: 
        if event.button == 1: 
          click = True
          
    pygame.display.update()

def secondScene():
  global click
  click = False
  while True:
    # clears the screen 
    screen.fill((0,0,0))
    
    #reaasigns the new background of the screen 
    screen.fill((222, 222, 222))  
    
    points = smallFont.render("points: 1", True, (117, 255, 117))
    screen.blit(points, (600, 40))
    
    """
    text
    """
    # scene 1 prompt text 
    firstAsk = Mainfont.render("do you.. ", True,(255, 255, 0))
    screen.blit(firstAsk, (50, 150))

    # right choice text 
    rightChoice = smallFont.render("turn around and make eye contact with them: ",  True, (255, 255, 0))
    screen.blit(rightChoice, (50, 300))

    # wrong choice text 
    wrongChoice = smallFont.render("ignore him: ", True, (255, 255, 0))
    screen.blit(wrongChoice, (50, 200))

    
    """
    Mouse settings
    """
    # returns the x, y position of the mouse 
    mx, my = pygame.mouse.get_pos() 

    """
    Choices buttons 
    """
    # creates a rectangle for the box 
    rightButton = pygame.Rect(50, 325, 75, 30)
    wrongButton = pygame.Rect(50, 225, 75, 30)

    #displays the button and colour of the button 
    pygame.draw.rect(screen, (180, 235, 252), rightButton)
    pygame.draw.rect(screen, (180, 235, 252), wrongButton)
    

    # collisions 
    if rightButton.collidepoint((mx, my)):
      if click:
        rightChoice2()
    if wrongButton.collidepoint((mx, my)):  
      if click: 
        wrongChoice2()

    # to quit the event loop when "x" is pressed
    for event in pygame.event.get():
      if event.type == pygame.QUIT:  
        pygame.quit()
        quit()
        
    # if i have clicked the left button, sets the click variable to true, carries over to next frame 
      if event.type == pygame.MOUSEBUTTONDOWN: 
        if event.button == 1: 
          click = True


    # refreshes the screen to display the updates 
    pygame.display.update()


def rightChoice2():
  global click 
  click = False
  
  while True:   
    # clears the screen 
    screen.fill((0,0,0))
    
    #reassigns the new background of the screen 
    screen.fill((222, 222, 222))     
    
    points = smallFont.render("points: 2", True, (117, 255, 117))
    screen.blit(points, (600, 40))
      
    # scene 1 prompt text 
    explain = smallFont.render("good choice! most perpetrators use the element of surprise so make sure to recognize their face", True,(255, 255, 0))

    explain2 = smallFont.render("and to make eye contact with them. At that point, they'll know you're ", True, (255, 255, 0))

    explain3 = smallFont.render("suspicious of them and ready to react to whatever future actions they'll take.", True, (255, 255, 0))
    
    # displays the first prompt 
    screen.blit(explain, (50, 150))
    screen.blit(explain2,(50, 200))
    screen.blit(explain3, (50, 250))

    """
    mouse settings 
    """
    # position of the mouse
    mx, my = pygame.mouse.get_pos() 
    
    """
    button settings 
    """
    # continue button creates shape.. (x, y, length, width  < i think? ) 
    buttonCon = pygame.Rect(50, 300, 75, 30) 
    
    #displays the button and colour of the button 
    pygame.draw.rect(screen, (180, 235, 252), buttonCon)

    """
    collisions of the mouse 
    """
    # collisions 
    if buttonCon.collidepoint((mx, my)):
      if click:
        thirdScene()
 
    for event in pygame.event.get():
      if event.type == pygame.QUIT:  
        pygame.quit()
        quit()
      
        # if i have clicked the left button, sets the click variable to true, carries over to next frame 
      if event.type == pygame.MOUSEBUTTONDOWN: 
        if event.button == 1: 
          click = True
          
    
    pygame.display.update()
  
def wrongChoice2(): 
    global click
    click = False 

    while True: 
      # clears the screen 
      screen.fill((0,0,0))
    
      #reassigns the new background of the screen 
      screen.fill((222, 222, 222))     
      
      points = smallFont.render("points: 2", True, (117, 255, 117))
      screen.blit(points, (600, 40))

      # scene 1 prompt text 
      explain = smallFont.render("Nice try but most perpetrators use the element of surprise so make sure to recognize their face", True,(255, 255, 0))

      explain2 = smallFont.render("and to make eye contact with them. At that point, they'll know you're ", True, (255, 255, 0))

      explain3 = smallFont.render("suspicious of them and ready to react to whatever future actions they'll take.", True, (255, 255, 0))

      gameOver = smallFont.render("GAME OVER! Try Again!", True, (255, 255, 0))
    
      # displays the first prompt 
      screen.blit(explain, (50, 150))
      screen.blit(explain2,(50, 200))
      screen.blit(explain3, (50, 250))
      screen.blit(gameOver, (50, 275))

      """
      mouse settings 
      """
      # position of the mouse
      mx, my = pygame.mouse.get_pos() 
    
      """
      button settings 
      """
      # continue button creates shape.. (x, y, length, width  < i think? ) 
      buttonCon = pygame.Rect(50, 300, 75, 30) 
    
      #displays the button and colour of the button 
      pygame.draw.rect(screen, (180, 235, 252), buttonCon)

      """
      collisions of the mouse 
      """
      # collisions 
      if buttonCon.collidepoint((mx, my)):
        if click:
          main_menu()
    
      # to quit the event loop when "x" is pressed
      for event in pygame.event.get():
        if event.type == pygame.QUIT:  
          pygame.quit()
          quit()
        # if i have clicked the left button, sets the click variable to true, carries over to next frame 
        if event.type == pygame.MOUSEBUTTONDOWN: 
          if event.button == 1: 
            click = True
      
      pygame.display.update()

  

def thirdScene():
  global click
  click = False 

  while True: 
    # clears the screen 
    screen.fill((0,0,0))
    
    #reassigns the new background of the screen 
    screen.fill((222, 222, 222))    
    
    points = smallFont.render("points: 2", True, (117, 255, 117))
    screen.blit(points, (600, 40))

    # scene 1 prompt text 
    scene1prompt = smallFont.render("looks like you're not losing them and you start walking a bit faster and they do the same.", True,(255, 255, 0))
    
    # displays the first prompt 
    screen.blit(scene1prompt, (50, 250))

    """
    mouse settings 
    """
    # position of the mouse
    mx, my = pygame.mouse.get_pos() 
    
    """
    button settings 
    """
    # continue button creates shape.. (x, y, length, width  < i think? ) 
    buttonCon = pygame.Rect(50, 300, 75, 30) 
    
    #displays the button and colour of the button 
    pygame.draw.rect(screen, (180, 235, 252), buttonCon)

    """
    collisions of the mouse 
    """
    # collisions 
    if buttonCon.collidepoint((mx, my)):
      if click:
        thirdPrompt()
    
    # to quit the event loop when "x" is pressed
    for event in pygame.event.get():
      if event.type == pygame.QUIT:  
        pygame.quit()
        quit()
      # if i have clicked the left button, sets the click variable to true, carries over to next frame 
      if event.type == pygame.MOUSEBUTTONDOWN: 
        if event.button == 1: 
          click = True
    pygame.display.update()

  
  
def thirdPrompt():
  global click
  click = False
  while True:
    # clears the screen 
    screen.fill((0,0,0))
    
    #reaasigns the new background of the screen 
    screen.fill((222, 222, 222))  
    
    points = smallFont.render("points: 2", True, (117, 255, 117))
    screen.blit(points, (600, 40))
    
    """
    text
    """
    # scene 1 prompt text 
    firstAsk = Mainfont.render("do you.. ", True,(255, 255, 0))
    screen.blit(firstAsk, (50, 150))

    # right choice text 
    rightChoice = smallFont.render("call 911 or ask a stranger for help? ",  True, (255, 255, 0))
    screen.blit(rightChoice, (50, 300))

    # wrong choice text 
    wrongChoice = smallFont.render("think to yourself you're overreacting ", True, (255, 255, 0))
    screen.blit(wrongChoice, (50, 200))

    
    """
    Mouse settings
    """
    # returns the x, y position of the mouse 
    mx, my = pygame.mouse.get_pos() 

    """
    Choices buttons 
    """
    # creates a rectangle for the box 
    rightButton = pygame.Rect(50, 325, 75, 30)
    wrongButton = pygame.Rect(50, 225, 75, 30)

    #displays the button and colour of the button 
    pygame.draw.rect(screen, (180, 235, 252), rightButton)
    pygame.draw.rect(screen, (180, 235, 252), wrongButton)
    

    # collisions 
    if rightButton.collidepoint((mx, my)):
      if click:
        rightChoice3()
    if wrongButton.collidepoint((mx, my)):  
      if click: 
        wrongChoice3()

    # to quit the event loop when "x" is pressed
    for event in pygame.event.get():
      if event.type == pygame.QUIT:  
        pygame.quit()
        quit()
        
    # if i have clicked the left button, sets the click variable to true, carries over to next frame 
      if event.type == pygame.MOUSEBUTTONDOWN: 
        if event.button == 1: 
          click = True


    # refreshes the screen to display the updates 
    pygame.display.update()


  

def wrongChoice3():
    global click
    click = False 

    while True: 
      # clears the screen 
      screen.fill((0,0,0))
    
      #reassigns the new background of the screen 
      screen.fill((222, 222, 222))      
      
      points = smallFont.render("points: 2", True, (117, 255, 117))
      screen.blit(points, (600, 40))

      # scene 1 prompt text 
      explain = smallFont.render("it's better to be safe than sorry!", True,(255, 255, 0))

      explain2 = smallFont.render("make sure to call 911 or an emergency contact as soon as you feel threatened.", True, (255, 255, 0))

      explain3 = smallFont.render("Make sure to send your location to that contact so they can locate you if something happens!", True, (255, 255, 0))

      gameOver = smallFont.render("GAME OVER! Try Again!", True, (255, 255, 0))
    
      # displays the first prompt 
      screen.blit(explain, (50, 150))
      screen.blit(explain2,(50, 200))
      screen.blit(explain3, (50, 250))
      screen.blit(gameOver, (50, 275))

      """
      mouse settings 
      """
      # position of the mouse
      mx, my = pygame.mouse.get_pos() 
    
      """
      button settings 
      """
      # continue button creates shape.. (x, y, length, width  < i think? ) 
      buttonCon = pygame.Rect(50, 300, 75, 30) 
    
      #displays the button and colour of the button 
      pygame.draw.rect(screen, (180, 235, 252), buttonCon)

      """
      collisions of the mouse 
      """
      # collisions 
      if buttonCon.collidepoint((mx, my)):
        if click:
          main_menu()
    
      # to quit the event loop when "x" is pressed
      for event in pygame.event.get():
        if event.type == pygame.QUIT:  
          pygame.quit()
          quit()
        # if i have clicked the left button, sets the click variable to true, carries over to next frame 
        if event.type == pygame.MOUSEBUTTONDOWN: 
          if event.button == 1: 
            click = True
      
      pygame.display.update()

  
  

def rightChoice3(): 
  global click 
  click = False
  
  while True:   
    # clears the screen 
    screen.fill((0,0,0))
    
    #reassigns the new background of the screen 
    screen.fill((222, 222, 222))     
    
    points = smallFont.render("points: 3", True, (117, 255, 117))
    screen.blit(points, (600, 40))
      
    # scene 1 prompt text 
    explain = smallFont.render("good choice! as soon as you feel threatened, make sure to call 911 or an emergency contact that you can rely on.", True,(255, 255, 0))

    explain2 = smallFont.render("Make sure to send your location to that contact so they can locate you if something happens!", True, (255, 255, 0))

    # displays the first prompt 
    screen.blit(explain, (50, 150))
    screen.blit(explain2,(50, 200))

    """
    mouse settings 
    """
    # position of the mouse
    mx, my = pygame.mouse.get_pos() 
    
    """
    button settings 
    """
    # continue button creates shape.. (x, y, length, width  < i think? ) 
    buttonCon = pygame.Rect(50, 300, 75, 30) 
    
    #displays the button and colour of the button 
    pygame.draw.rect(screen, (180, 235, 252), buttonCon)

    """
    collisions of the mouse 
    """
    # collisions 
    if buttonCon.collidepoint((mx, my)):
      if click:
        endScreen()
 
    for event in pygame.event.get():
      if event.type == pygame.QUIT:  
        pygame.quit()
        quit()
      
        # if i have clicked the left button, sets the click variable to true, carries over to next frame 
      if event.type == pygame.MOUSEBUTTONDOWN: 
        if event.button == 1: 
          click = True
          
    
    pygame.display.update()
    

def endScreen():
  global click 
  click = False
  
  while True:   
    # clears the screen 
    screen.fill((0,0,0))
    
    #reassigns the new background of the screen 
    screen.fill((222, 222, 222))      

    points = smallFont.render("points: 3", True, (117, 255, 117))
    screen.blit(points, (600, 40))

    congrats = Mainfont.render("CONGRATS YOU WON!", True, (238, 165, 165))
      
    # scene 1 prompt text 
    explain = smallFont.render("now you're prepped with what to do if you're in a dangerous situation! ", True,(255, 255, 0))

    explain2 = smallFont.render("make sure you always have an emergency contact with you!", True, (255, 255, 0))

    explain3 = smallFont.render("1.sending your location to emergency contacts by a click of a button.", True, (255, 255, 0))
    explain4 = smallFont.render("2.loud alarm 3.fake phone call 4.direct calling to a number by a click of a button", True, (255, 255, 0))

    explain5 = smallFont.render("an app called 'Sekura' is great as it gives you different resources such as:", True, (255, 255, 0))
    
    # displays the first prompt 
    screen.blit(explain, (50, 175))
    screen.blit(explain2,(50, 200))
    screen.blit(explain3, (50, 250))
    screen.blit(congrats, (50, 120))
    screen.blit(explain4, (50, 275))
    screen.blit(explain5, (50, 225))

    """
    mouse settings 
    """
    # position of the mouse
    mx, my = pygame.mouse.get_pos() 
    
    """
    button settings 
    """
    # continue button creates shape.. (x, y, length, width  < i think? ) 
    buttonCon = pygame.Rect(50, 300, 75, 30) 
    
    #displays the button and colour of the button 
    pygame.draw.rect(screen, (180, 235, 252), buttonCon)

    """
    collisions of the mouse 
    """
    # collisions 
    if buttonCon.collidepoint((mx, my)):
      if click:
        pygame.quit()
        quit()
 
    for event in pygame.event.get():
      if event.type == pygame.QUIT:  
        pygame.quit()
        quit()
      
        # if i have clicked the left button, sets the click variable to true, carries over to next frame 
      if event.type == pygame.MOUSEBUTTONDOWN: 
        if event.button == 1: 
          click = True
          
    
    pygame.display.update()
    
main_menu()
