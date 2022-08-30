#imports modules needed for the Ultimate Game Of Pong 
import pygame
from pygame import mixer 
import sys 
import time 
import random 

pygame.init()

class Button(): 
    def __init__(self, X_Position, Y_Position, Width_Button, Height_Button, Colour ,Text=""):
        self.X_Position = X_Position
        self.Y_Position = Y_Position
        self.Width_Button = Width_Button
        self.Height_Button = Height_Button
        self.Text = Text
        self.Colour = Colour

    def Draw(self, Display_Surface): 
        pygame.draw.rect(Display_Surface, self.Colour, (self.X_Position, self.Y_Position, self.Width_Button, self.Height_Button), -1) #Chnage the 0 to a -1 for invisable buttons
        Text = font.render(self.Text, True, White)
        Centre_X_Position = self.X_Position + (self.Width_Button/2 - Text.get_width()/2) 
        Centre_Y_Position = self.Y_Position + (self.Height_Button/2 - Text.get_height()/2) 
        Display_Surface.blit(Text, (Centre_X_Position, Centre_Y_Position)) 

def Searching_Algorithm():
    running = False
    

def Main_Menu():
    running = True 

    Background_Image = pygame.image.load("Background_Main_Menu.jpg").convert()
    Display_Surface.blit(Background_Image, (-360, 0))

    pygame.display.set_caption("Ultimate Game Of Pong")
    icon = pygame.image.load("Icon_Image.png")
    pygame.display.set_icon(icon)

    Title = font.render("Ultimate Game Of Pong", True, Green)
    Display_Surface.blit(Title, (201,75))
    pygame.draw.line(Display_Surface, White, [201, 150], [999, 150], 1)
    pygame.draw.line(Display_Surface, White, [201, 80], [999, 80], 1)

    New_Game_Button = Button(450, 250, 300, 50, Red, "Searching Algorithms")
    Instructions = Button(375, 350, 450, 50, Red,"---")
    High_Score = Button(412.5, 450, 375, 50, Red,"Sorting Algorithm")
    Exit_Button = Button(525, 550, 150, 50, Red,"Exit")

    New_Game_Button.Draw(Display_Surface)
    Instructions.Draw(Display_Surface)
    High_Score.Draw(Display_Surface)
    Exit_Button.Draw(Display_Surface)

    pygame.display.update()

    while running:
        for event in pygame.event.get():
 
            if event.type == pygame.QUIT:
                running = False 
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                Mouse_X, Mouse_Y = pygame.mouse.get_pos()
                if 450 < Mouse_X < 750 and 250 < Mouse_Y <300:
                    mixer.music.load("vgmenuselect.ogg")
                    mixer.music.play(1)
                    Searching_Alorithm()

            if event.type == pygame.MOUSEBUTTONDOWN:
                Mouse_X, Mouse_Y = pygame.mouse.get_pos()
                if 375 < Mouse_X < 825 and 350 < Mouse_Y < 400:
                    mixer.music.load("vgmenuselect.ogg")
                    mixer.music.play(1)
                    print("Searching Algorithms")

            if event.type == pygame.MOUSEBUTTONDOWN:
                Mouse_X, Mouse_Y = pygame.mouse.get_pos()
                if 450 < Mouse_X < 750 and 450 < Mouse_Y < 500:
                    mixer.music.load("vgmenuselect.ogg")
                    mixer.music.play(1)
                    print("Sorting Algorithms")

            if event.type == pygame.MOUSEBUTTONDOWN:
                Mouse_X, Mouse_Y = pygame.mouse.get_pos()
                if 525 < Mouse_X < 1075 and 550 < Mouse_Y < 600:
                    time.sleep(0.32)
                    pygame.quit()
                    sys.exit()  

#Define Colours used in the game 
White = (255, 255, 255)
Green = (0, 255, 0)
Blue = (0, 0, 50)
Light_Blue = (0,0,34)
Red = (34,34,5)
Purple = (45,54,54)
Brown = (45,34,65)
Black = (0,0,0)

#Attributes for the Display Surface (Width,Height)
Display_Width = 1200
Display_Height = 800
Display_Surface = pygame.display.set_mode((Display_Width, Display_Height))

#Font used throughout the game
font = pygame.font.SysFont("Courier", 64)

#Runs the game at 60fps (Frames Per Second)
clock = pygame.time.Clock()
clock.tick(60)

#Runs Main Menu Function
Main_Menu()


