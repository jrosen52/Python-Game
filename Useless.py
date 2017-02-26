import pygame
import random
import ast
import time

pygame.init()

#RGB color values
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
yellow = (200, 200, 0)
magenta = (255, 0, 255)
dark_red = (200,0,0)
dark_green = (0, 200, 0)
dark_blue = (0, 0, 200)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
bright_blue = (0, 0, 255)
bright_yellow = (255, 255, 0)


class GameOver:

    def __init__(self):
        pygame.init()
        #Creates the screen and the background
        GameOver = True
        screen = pygame.display.set_mode([800, 600])
        pygame.display.set_caption('Useless')
        font1 = pygame.font.Font(None, 36)
        font2 = pygame.font.Font(None, 64)
        background = pygame.Surface(screen.get_size())
        screenheight = pygame.display.get_surface().get_height()
        screenwidth = pygame.display.get_surface().get_width()
        pygame.key.set_repeat(2, 10)
        clock = pygame.time.Clock()
        rgbl = [255, 0, 0]
        random.shuffle(rgbl)

        def game_quit():
            # Quits the game
            pygame.quit
            quit()

        while (GameOver == True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            screen.fill(black)

            title1 = font2.render("The Useless Game", 1, green)
            title1_rect = title1.get_rect()
            title1_rect.center = (screenwidth/2, screenheight/5)

            screen.blit(title1, title1_rect)

            title2 = font1.render("You lose!", 1, red)
            title2_rect = title2.get_rect()
            title2_rect.center = (screenwidth/2, 450)

            screen.blit(title2, title2_rect)

            # Fills the background with white and creates a main menu message in the center
            # of the screen


            def button(text, x, y, width, height, color1, color2, action=None):
                # Button function
                # Recieves the position, width, height, standing color, and the color while the mouse is hovering on the button.
                # Additionally, if the button has a function attached, that can be included
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()

                if x + width > mouse[0] > x and y + height > mouse[1] > y:
                    pygame.draw.rect(screen, color2, (x, y, width, height))
                    if click[0] == 1 and action != None:
                        action()
                else:
                    pygame.draw.rect(screen, color1, (x, y, width, height))

                text_label = font1.render(text, 1, black)
                text_label_rect = text_label.get_rect()
                text_label_rect.center = (x + width/2, y + height/2)

                screen.blit(text_label, text_label_rect)

            # Creates the menu buttons
            button("Retry", 200, 300, 400, 50, dark_green, bright_green, Press1_4)

            pygame.display.update()
            clock.tick(15)

class Intro:

    def __init__(self):
        pygame.init()
        #Creates the screen and the background
        intro = True
        screen = pygame.display.set_mode([800, 600])
        pygame.display.set_caption('Useless')
        font1 = pygame.font.Font(None, 36)
        font2 = pygame.font.Font(None, 64)
        background = pygame.Surface(screen.get_size())
        screenheight = pygame.display.get_surface().get_height()
        screenwidth = pygame.display.get_surface().get_width()
        pygame.key.set_repeat(2, 10)
        clock = pygame.time.Clock()
        rgbl = [255, 0, 0]
        random.shuffle(rgbl)
        self.pressed = 0

        def game_quit():
            # Quits the game
            pygame.quit
            quit()

        while (intro == True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            screen.fill(black)

            title1 = font2.render("The Useless Game", 1, green)
            title1_rect = title1.get_rect()
            title1_rect.center = (screenwidth/2, screenheight/5)

            screen.blit(title1, title1_rect)

            # Fills the background with white and creates a main menu message in the center
            # of the screen


            def button(text, x, y, width, height, color1, color2, action=None):
                # Button function
                # Recieves the position, width, height, standing color, and the color while the mouse is hovering on the button.
                # Additionally, if the button has a function attached, that can be included
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()
                pressed = 0

                if x + width > mouse[0] > x and y + height > mouse[1] > y:
                    pygame.draw.rect(screen, color2, (x, y, width, height))
                    if click[0] == 1 and action != None:
                        action()
                else:
                    pygame.draw.rect(screen, color1, (x, y, width, height))

                text_label = font1.render(text, 1, black)
                text_label_rect = text_label.get_rect()
                text_label_rect.center = (x + width/2, y + height/2)

                screen.blit(text_label, text_label_rect)

            button("Click this useless button", 200, 300, 400, 50, dark_green, bright_green, Press1_1)

            pygame.display.update()
            clock.tick(15)

class Press1_1:

    def __init__(self):
        pygame.init()
        #Creates the screen and the background
        Press1_1 = True
        screen = pygame.display.set_mode([800, 600])
        pygame.display.set_caption('Useless')
        font1 = pygame.font.Font(None, 36)
        font2 = pygame.font.Font(None, 64)
        background = pygame.Surface(screen.get_size())
        screenheight = pygame.display.get_surface().get_height()
        screenwidth = pygame.display.get_surface().get_width()
        pygame.key.set_repeat(2, 10)
        clock = pygame.time.Clock()
        rgbl = [255, 0, 0]
        random.shuffle(rgbl)

        def game_quit():
            # Quits the game
            pygame.quit
            quit()

        while (Press1_1 == True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            screen.fill(black)

            title1 = font2.render("The Useless Game", 1, green)
            title1_rect = title1.get_rect()
            title1_rect.center = (screenwidth/2, screenheight/5)

            screen.blit(title1, title1_rect)

            # Fills the background with white and creates a main menu message in the center
            # of the screen


            def button(text, x, y, width, height, color1, color2, action=None):
                # Button function
                # Recieves the position, width, height, standing color, and the color while the mouse is hovering on the button.
                # Additionally, if the button has a function attached, that can be included
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()

                if x + width > mouse[0] > x and y + height > mouse[1] > y:
                    pygame.draw.rect(screen, color2, (x, y, width, height))
                    if click[0] == 1 and action != None:
                        action()
                else:
                    pygame.draw.rect(screen, color1, (x, y, width, height))

                text_label = font1.render(text, 1, black)
                text_label_rect = text_label.get_rect()
                text_label_rect.center = (x + width/2, y + height/2)

                screen.blit(text_label, text_label_rect)

            # Creates the menu buttons
            button("Click this useless button", 200, 300, 400, 50, dark_green, bright_green, Press1_2)

            pygame.display.update()
            clock.tick(15)

class Press1_2:

    def __init__(self):
        pygame.init()
        #Creates the screen and the background
        Press1_2 = True
        screen = pygame.display.set_mode([800, 600])
        pygame.display.set_caption('Useless')
        font1 = pygame.font.Font(None, 36)
        font2 = pygame.font.Font(None, 64)
        background = pygame.Surface(screen.get_size())
        screenheight = pygame.display.get_surface().get_height()
        screenwidth = pygame.display.get_surface().get_width()
        pygame.key.set_repeat(2, 10)
        clock = pygame.time.Clock()
        rgbl = [255, 0, 0]
        random.shuffle(rgbl)

        def game_quit():
            # Quits the game
            pygame.quit
            quit()

        while (Press1_2 == True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            screen.fill(black)

            title1 = font2.render("The Useless Game", 1, green)
            title1_rect = title1.get_rect()
            title1_rect.center = (screenwidth/2, screenheight/5)

            screen.blit(title1, title1_rect)

            # Fills the background with white and creates a main menu message in the center
            # of the screen


            def button(text, x, y, width, height, color1, color2, action=None):
                # Button function
                # Recieves the position, width, height, standing color, and the color while the mouse is hovering on the button.
                # Additionally, if the button has a function attached, that can be included
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()

                if x + width > mouse[0] > x and y + height > mouse[1] > y:
                    pygame.draw.rect(screen, color2, (x, y, width, height))
                    if click[0] == 1 and action != None:
                        action()
                else:
                    pygame.draw.rect(screen, color1, (x, y, width, height))

                text_label = font1.render(text, 1, black)
                text_label_rect = text_label.get_rect()
                text_label_rect.center = (x + width/2, y + height/2)

                screen.blit(text_label, text_label_rect)

            # Creates the menu buttons
            button("Click this useless button", 200, 300, 400, 50, dark_green, bright_green, Press1_3)

            pygame.display.update()
            clock.tick(15)

class Press1_3:

    def __init__(self):
        pygame.init()
        #Creates the screen and the background
        Press1_3 = True
        screen = pygame.display.set_mode([800, 600])
        pygame.display.set_caption('Useless')
        font1 = pygame.font.Font(None, 36)
        font2 = pygame.font.Font(None, 64)
        background = pygame.Surface(screen.get_size())
        screenheight = pygame.display.get_surface().get_height()
        screenwidth = pygame.display.get_surface().get_width()
        pygame.key.set_repeat(2, 10)
        clock = pygame.time.Clock()
        rgbl = [255, 0, 0]
        random.shuffle(rgbl)

        def game_quit():
            # Quits the game
            pygame.quit
            quit()

        while (Press1_3 == True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            screen.fill(black)

            title1 = font2.render("The Useless Game", 1, green)
            title1_rect = title1.get_rect()
            title1_rect.center = (screenwidth/2, screenheight/5)

            screen.blit(title1, title1_rect)

            # Fills the background with white and creates a main menu message in the center
            # of the screen


            def button(text, x, y, width, height, color1, color2, action=None):
                # Button function
                # Recieves the position, width, height, standing color, and the color while the mouse is hovering on the button.
                # Additionally, if the button has a function attached, that can be included
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()

                if x + width > mouse[0] > x and y + height > mouse[1] > y:
                    pygame.draw.rect(screen, color2, (x, y, width, height))
                    if click[0] == 1 and action != None:
                        action()
                else:
                    pygame.draw.rect(screen, color1, (x, y, width, height))

                text_label = font1.render(text, 1, black)
                text_label_rect = text_label.get_rect()
                text_label_rect.center = (x + width/2, y + height/2)

                screen.blit(text_label, text_label_rect)

            # Creates the menu buttons
            button("Click this useless button", 200, 300, 400, 50, dark_green, bright_green, Press1_4)

            pygame.display.update()
            clock.tick(15)

class Press1_4:

    def __init__(self):
        pygame.init()
        #Creates the screen and the background
        Press1_4 = True
        screen = pygame.display.set_mode([800, 600])
        pygame.display.set_caption('Useless')
        font1 = pygame.font.Font(None, 36)
        font2 = pygame.font.Font(None, 64)
        background = pygame.Surface(screen.get_size())
        screenheight = pygame.display.get_surface().get_height()
        screenwidth = pygame.display.get_surface().get_width()
        pygame.key.set_repeat(2, 10)
        clock = pygame.time.Clock()
        rgbl = [255, 0, 0]
        random.shuffle(rgbl)

        def game_quit():
            # Quits the game
            pygame.quit
            quit()

        while (Press1_4 == True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            screen.fill(black)

            title1 = font2.render("The Useless Game", 1, green)
            title1_rect = title1.get_rect()
            title1_rect.center = (screenwidth/2, screenheight/5)

            screen.blit(title1, title1_rect)

            # Fills the background with white and creates a main menu message in the center
            # of the screen


            def button(text, x, y, width, height, color1, color2, action=None):
                # Button function
                # Recieves the position, width, height, standing color, and the color while the mouse is hovering on the button.
                # Additionally, if the button has a function attached, that can be included
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()

                if x + width > mouse[0] > x and y + height > mouse[1] > y:
                    pygame.draw.rect(screen, color2, (x, y, width, height))
                    if click[0] == 1 and action != None:
                        action()
                else:
                    pygame.draw.rect(screen, color1, (x, y, width, height))

                text_label = font1.render(text, 1, black)
                text_label_rect = text_label.get_rect()
                text_label_rect.center = (x + width/2, y + height/2)

                screen.blit(text_label, text_label_rect)

            # Creates the menu buttons
            button("Click this useless button", 200, 300, 400, 50, dark_green, bright_green, Press1)

            pygame.display.update()
            clock.tick(15)


class Press1:

    def __init__(self):
        pygame.init()
        #Creates the screen and the background
        Press1 = True
        screen = pygame.display.set_mode([800, 600])
        pygame.display.set_caption('Useless')
        font1 = pygame.font.Font(None, 36)
        font2 = pygame.font.Font(None, 64)
        background = pygame.Surface(screen.get_size())
        screenheight = pygame.display.get_surface().get_height()
        screenwidth = pygame.display.get_surface().get_width()
        pygame.key.set_repeat(2, 10)
        clock = pygame.time.Clock()
        rgbl = [255, 0, 0]
        random.shuffle(rgbl)

        def game_quit():
            # Quits the game
            pygame.quit
            quit()

        while (Press1 == True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            screen.fill(black)

            title1 = font2.render("The Useless Game", 1, green)
            title1_rect = title1.get_rect()
            title1_rect.center = (screenwidth/2, screenheight/5)

            screen.blit(title1, title1_rect)

            title2 = font1.render("What are you doing? This game is useless.", 1, red)
            title2_rect = title2.get_rect()
            title2_rect.center = (screenwidth/2, 450)

            screen.blit(title2, title2_rect)

            # Fills the background with white and creates a main menu message in the center
            # of the screen


            def button(text, x, y, width, height, color1, color2, action=None):
                # Button function
                # Recieves the position, width, height, standing color, and the color while the mouse is hovering on the button.
                # Additionally, if the button has a function attached, that can be included
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()

                if x + width > mouse[0] > x and y + height > mouse[1] > y:
                    pygame.draw.rect(screen, color2, (x, y, width, height))
                    if click[0] == 1 and action != None:
                        action()
                else:
                    pygame.draw.rect(screen, color1, (x, y, width, height))

                text_label = font1.render(text, 1, black)
                text_label_rect = text_label.get_rect()
                text_label_rect.center = (x + width/2, y + height/2)

                screen.blit(text_label, text_label_rect)

            # Creates the menu buttons
            button("Click this useless button", 200, 300, 400, 50, dark_green, bright_green, Press2)

            pygame.display.update()
            clock.tick(15)

class Press2:

    def __init__(self):
        pygame.init()
        #Creates the screen and the background
        Press2 = True
        screen = pygame.display.set_mode([800, 600])
        pygame.display.set_caption('Useless')
        font1 = pygame.font.Font(None, 36)
        font2 = pygame.font.Font(None, 64)
        background = pygame.Surface(screen.get_size())
        screenheight = pygame.display.get_surface().get_height()
        screenwidth = pygame.display.get_surface().get_width()
        pygame.key.set_repeat(2, 10)
        clock = pygame.time.Clock()
        rgbl = [255, 0, 0]
        random.shuffle(rgbl)

        def game_quit():
            # Quits the game
            pygame.quit
            quit()

        while (Press2 == True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            screen.fill(black)

            title1 = font2.render("The Useless Game", 1, green)
            title1_rect = title1.get_rect()
            title1_rect.center = (screenwidth/2, screenheight/5)

            screen.blit(title1, title1_rect)

            title2 = font1.render("You're wasting your time.", 1, red)
            title2_rect = title2.get_rect()
            title2_rect.center = (screenwidth/2, 450)

            screen.blit(title2, title2_rect)

            # Fills the background with white and creates a main menu message in the center
            # of the screen


            def button(text, x, y, width, height, color1, color2, action=None):
                # Button function
                # Recieves the position, width, height, standing color, and the color while the mouse is hovering on the button.
                # Additionally, if the button has a function attached, that can be included
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()

                if x + width > mouse[0] > x and y + height > mouse[1] > y:
                    pygame.draw.rect(screen, color2, (x, y, width, height))
                    if click[0] == 1 and action != None:
                        action()
                else:
                    pygame.draw.rect(screen, color1, (x, y, width, height))

                text_label = font1.render(text, 1, black)
                text_label_rect = text_label.get_rect()
                text_label_rect.center = (x + width/2, y + height/2)

                screen.blit(text_label, text_label_rect)

            # Creates the menu buttons
            button("Click this useless button", 200, 300, 400, 50, dark_green, bright_green, Press3)

            pygame.display.update()
            clock.tick(15)

class Press3:

    def __init__(self):
        pygame.init()
        #Creates the screen and the background
        Press3 = True
        screen = pygame.display.set_mode([800, 600])
        pygame.display.set_caption('Useless')
        font1 = pygame.font.Font(None, 36)
        font2 = pygame.font.Font(None, 64)
        background = pygame.Surface(screen.get_size())
        screenheight = pygame.display.get_surface().get_height()
        screenwidth = pygame.display.get_surface().get_width()
        pygame.key.set_repeat(2, 10)
        clock = pygame.time.Clock()
        rgbl = [255, 0, 0]
        random.shuffle(rgbl)

        def game_quit():
            # Quits the game
            pygame.quit
            quit()

        while (Press3 == True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            screen.fill(black)

            title1 = font2.render("The Useless Game", 1, green)
            title1_rect = title1.get_rect()
            title1_rect.center = (screenwidth/2, screenheight/5)

            screen.blit(title1, title1_rect)

            title2 = font1.render("Stop it, this game doesn't do anything.", 1, red)
            title2_rect = title2.get_rect()
            title2_rect.center = (screenwidth/2, 450)

            screen.blit(title2, title2_rect)

            # Fills the background with white and creates a main menu message in the center
            # of the screen


            def button(text, x, y, width, height, color1, color2, action=None):
                # Button function
                # Recieves the position, width, height, standing color, and the color while the mouse is hovering on the button.
                # Additionally, if the button has a function attached, that can be included
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()

                if x + width > mouse[0] > x and y + height > mouse[1] > y:
                    pygame.draw.rect(screen, color2, (x, y, width, height))
                    if click[0] == 1 and action != None:
                        action()
                else:
                    pygame.draw.rect(screen, color1, (x, y, width, height))

                text_label = font1.render(text, 1, black)
                text_label_rect = text_label.get_rect()
                text_label_rect.center = (x + width/2, y + height/2)

                screen.blit(text_label, text_label_rect)

            # Creates the menu buttons
            button("Click this useless button", 200, 300, 400, 50, dark_green, bright_green, Press4)

            pygame.display.update()
            clock.tick(15)

class Press4:

    def __init__(self):
        pygame.init()
        #Creates the screen and the background
        Press4 = True
        screen = pygame.display.set_mode([800, 600])
        pygame.display.set_caption('Useless')
        font1 = pygame.font.Font(None, 36)
        font2 = pygame.font.Font(None, 64)
        background = pygame.Surface(screen.get_size())
        screenheight = pygame.display.get_surface().get_height()
        screenwidth = pygame.display.get_surface().get_width()
        pygame.key.set_repeat(2, 10)
        clock = pygame.time.Clock()
        rgbl = [255, 0, 0]
        random.shuffle(rgbl)

        def game_quit():
            # Quits the game
            pygame.quit
            quit()

        while (Press4 == True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            screen.fill(black)

            title1 = font2.render("The Useless Game", 1, green)
            title1_rect = title1.get_rect()
            title1_rect.center = (screenwidth/2, screenheight/5)

            screen.blit(title1, title1_rect)

            title2 = font1.render("You know what? I'm taking away your useless button privilages.", 1, red)
            title2_rect = title2.get_rect()
            title2_rect.center = (screenwidth/2, 450)

            screen.blit(title2, title2_rect)

            # Fills the background with white and creates a main menu message in the center
            # of the screen


            def button(text, x, y, width, height, color1, color2, action=None):
                # Button function
                # Recieves the position, width, height, standing color, and the color while the mouse is hovering on the button.
                # Additionally, if the button has a function attached, that can be included
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()

                if x + width > mouse[0] > x and y + height > mouse[1] > y:
                    pygame.draw.rect(screen, color2, (x, y, width, height))
                    if click[0] == 1 and action != None:
                        action()
                else:
                    pygame.draw.rect(screen, color1, (x, y, width, height))

                text_label = font1.render(text, 1, black)
                text_label_rect = text_label.get_rect()
                text_label_rect.center = (x + width/2, y + height/2)

                screen.blit(text_label, text_label_rect)

            # Creates the menu buttons
            button("Click this useless button", 200, 300, 400, 50, black, black, Press5)

            pygame.display.update()
            clock.tick(15)

class Press5:

    def __init__(self):
        pygame.init()
        #Creates the screen and the background
        Press5 = True
        screen = pygame.display.set_mode([800, 600])
        pygame.display.set_caption('Useless')
        font1 = pygame.font.Font(None, 36)
        font2 = pygame.font.Font(None, 64)
        background = pygame.Surface(screen.get_size())
        screenheight = pygame.display.get_surface().get_height()
        screenwidth = pygame.display.get_surface().get_width()
        pygame.key.set_repeat(2, 10)
        clock = pygame.time.Clock()
        rgbl = [255, 0, 0]
        random.shuffle(rgbl)

        def game_quit():
            # Quits the game
            pygame.quit
            quit()

        while (Press5 == True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            screen.fill(black)

            title1 = font2.render("The Useless Game", 1, green)
            title1_rect = title1.get_rect()
            title1_rect.center = (screenwidth/2, screenheight/5)

            screen.blit(title1, title1_rect)

            title2 = font1.render("Damn it! How did you do that?", 1, red)
            title2_rect = title2.get_rect()
            title2_rect.center = (screenwidth/2, 450)

            screen.blit(title2, title2_rect)

            # Fills the background with white and creates a main menu message in the center
            # of the screen


            def button(text, x, y, width, height, color1, color2, action=None):
                # Button function
                # Recieves the position, width, height, standing color, and the color while the mouse is hovering on the button.
                # Additionally, if the button has a function attached, that can be included
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()

                if x + width > mouse[0] > x and y + height > mouse[1] > y:
                    pygame.draw.rect(screen, color2, (x, y, width, height))
                    if click[0] == 1 and action != None:
                        action()
                else:
                    pygame.draw.rect(screen, color1, (x, y, width, height))

                text_label = font1.render(text, 1, black)
                text_label_rect = text_label.get_rect()
                text_label_rect.center = (x + width/2, y + height/2)

                screen.blit(text_label, text_label_rect)

            # Creates the menu buttons
            button("Click this useless button", 200, 300, 400, 50, dark_green, bright_green, Press6)

            pygame.display.update()
            clock.tick(15)

class Press6:

    def __init__(self):
        pygame.init()
        #Creates the screen and the background
        Press6 = True
        screen = pygame.display.set_mode([800, 600])
        pygame.display.set_caption('Useless')
        font1 = pygame.font.Font(None, 36)
        font2 = pygame.font.Font(None, 64)
        background = pygame.Surface(screen.get_size())
        screenheight = pygame.display.get_surface().get_height()
        screenwidth = pygame.display.get_surface().get_width()
        pygame.key.set_repeat(2, 10)
        clock = pygame.time.Clock()
        rgbl = [255, 0, 0]
        random.shuffle(rgbl)

        def game_quit():
            # Quits the game
            pygame.quit
            quit()

        while (Press6 == True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            screen.fill(black)

            title1 = font2.render("The Useless Game", 1, green)
            title1_rect = title1.get_rect()
            title1_rect.center = (screenwidth/2, screenheight/5)

            screen.blit(title1, title1_rect)

            title2 = font1.render("You're really getting on my nerves.", 1, red)
            title2_rect = title2.get_rect()
            title2_rect.center = (screenwidth/2, 450)

            screen.blit(title2, title2_rect)

            # Fills the background with white and creates a main menu message in the center
            # of the screen


            def button(text, x, y, width, height, color1, color2, action=None):
                # Button function
                # Recieves the position, width, height, standing color, and the color while the mouse is hovering on the button.
                # Additionally, if the button has a function attached, that can be included
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()

                if x + width > mouse[0] > x and y + height > mouse[1] > y:
                    pygame.draw.rect(screen, color2, (x, y, width, height))
                    if click[0] == 1 and action != None:
                        action()
                else:
                    pygame.draw.rect(screen, color1, (x, y, width, height))

                text_label = font1.render(text, 1, black)
                text_label_rect = text_label.get_rect()
                text_label_rect.center = (x + width/2, y + height/2)

                screen.blit(text_label, text_label_rect)

            # Creates the menu buttons
            button("Click this useless button", 200, 300, 400, 50, dark_green, bright_green, Press7)

            pygame.display.update()
            clock.tick(15)

class Press7:

    def __init__(self):
        pygame.init()
        #Creates the screen and the background
        Press7 = True
        screen = pygame.display.set_mode([800, 600])
        pygame.display.set_caption('Useless')
        font1 = pygame.font.Font(None, 36)
        font2 = pygame.font.Font(None, 64)
        background = pygame.Surface(screen.get_size())
        screenheight = pygame.display.get_surface().get_height()
        screenwidth = pygame.display.get_surface().get_width()
        pygame.key.set_repeat(2, 10)
        clock = pygame.time.Clock()
        rgbl = [255, 0, 0]
        random.shuffle(rgbl)

        def game_quit():
            # Quits the game
            pygame.quit
            quit()

        while (Press7 == True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            screen.fill(black)



            def button(text, x, y, width, height, color1, color2, action=None):
                # Button function
                # Recieves the position, width, height, standing color, and the color while the mouse is hovering on the button.
                # Additionally, if the button has a function attached, that can be included
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()

                if x + width > mouse[0] > x and y + height > mouse[1] > y:
                    pygame.draw.rect(screen, color2, (x, y, width, height))
                    if click[0] == 1 and action != None:
                        action()
                else:
                    pygame.draw.rect(screen, color1, (x, y, width, height))

                text_label = font1.render(text, 1, black)
                text_label_rect = text_label.get_rect()
                text_label_rect.center = (x + width/2, y + height/2)

                screen.blit(text_label, text_label_rect)

            # Creates the menu buttons
            button("Click this useless button", 200, 100, 400, 50, dark_green, bright_green, Press8)

            title1 = font2.render("The Useless Game", 1, black)
            title1_rect = title1.get_rect()
            title1_rect.center = (screenwidth/2, screenheight/5)

            screen.blit(title1, title1_rect)

            title2 = font1.render("OK, try to hit the button now!", 1, red)
            title2_rect = title2.get_rect()
            title2_rect.center = (screenwidth/2, 450)

            screen.blit(title2, title2_rect)

            # Fills the background with white and creates a main menu message in the center
            # of the screen

            pygame.display.update()
            clock.tick(15)

class Press8:

    def __init__(self):
        pygame.init()
        #Creates the screen and the background
        Press8 = True
        screen = pygame.display.set_mode([800, 600])
        pygame.display.set_caption('Useless')
        font1 = pygame.font.Font(None, 36)
        font2 = pygame.font.Font(None, 64)
        background = pygame.Surface(screen.get_size())
        screenheight = pygame.display.get_surface().get_height()
        screenwidth = pygame.display.get_surface().get_width()
        pygame.key.set_repeat(2, 10)
        clock = pygame.time.Clock()
        rgbl = [255, 0, 0]
        random.shuffle(rgbl)

        def game_quit():
            # Quits the game
            pygame.quit
            quit()

        while (Press8 == True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            screen.fill(black)

            title1 = font2.render("The Useless Game", 1, green)
            title1_rect = title1.get_rect()
            title1_rect.center = (screenwidth/2, screenheight/5)

            screen.blit(title1, title1_rect)

            title2 = font1.render("Well that didn't work.", 1, red)
            title2_rect = title2.get_rect()
            title2_rect.center = (screenwidth/2, 450)

            screen.blit(title2, title2_rect)

            # Fills the background with white and creates a main menu message in the center
            # of the screen


            def button(text, x, y, width, height, color1, color2, action=None):
                # Button function
                # Recieves the position, width, height, standing color, and the color while the mouse is hovering on the button.
                # Additionally, if the button has a function attached, that can be included
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()

                if x + width > mouse[0] > x and y + height > mouse[1] > y:
                    pygame.draw.rect(screen, color2, (x, y, width, height))
                    if click[0] == 1 and action != None:
                        action()
                else:
                    pygame.draw.rect(screen, color1, (x, y, width, height))

                text_label = font1.render(text, 1, black)
                text_label_rect = text_label.get_rect()
                text_label_rect.center = (x + width/2, y + height/2)

                screen.blit(text_label, text_label_rect)

            # Creates the menu buttons
            button("Click this useless button", 200, 300, 400, 50, dark_green, bright_green, Press9)

            pygame.display.update()
            clock.tick(15)

class Press9:

    def __init__(self):
        pygame.init()
        #Creates the screen and the background
        Press9 = True
        screen = pygame.display.set_mode([800, 600])
        pygame.display.set_caption('Useless')
        font1 = pygame.font.Font(None, 36)
        font2 = pygame.font.Font(None, 64)
        background = pygame.Surface(screen.get_size())
        screenheight = pygame.display.get_surface().get_height()
        screenwidth = pygame.display.get_surface().get_width()
        pygame.key.set_repeat(2, 10)
        clock = pygame.time.Clock()
        rgbl = [255, 0, 0]
        random.shuffle(rgbl)

        def game_quit():
            # Quits the game
            pygame.quit
            quit()

        while (Press9 == True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            screen.fill(black)

            title1 = font2.render("The Useless Game", 1, green)
            title1_rect = title1.get_rect()
            title1_rect.center = (screenwidth/2, screenheight/5)

            screen.blit(title1, title1_rect)

            title2 = font1.render("Ha! Try to find it now!", 1, red)
            title2_rect = title2.get_rect()
            title2_rect.center = (screenwidth/2, 450)

            screen.blit(title2, title2_rect)

            # Fills the background with white and creates a main menu message in the center
            # of the screen


            def button(text, x, y, width, height, color1, color2, action=None):
                # Button function
                # Recieves the position, width, height, standing color, and the color while the mouse is hovering on the button.
                # Additionally, if the button has a function attached, that can be included
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()

                if x + width > mouse[0] > x and y + height > mouse[1] > y:
                    pygame.draw.rect(screen, color2, (x, y, width, height))
                    if click[0] == 1 and action != None:
                        action()
                else:
                    pygame.draw.rect(screen, color1, (x, y, width, height))

                text_label = font1.render(text, 1, black)
                text_label_rect = text_label.get_rect()
                text_label_rect.center = (x + width/2, y + height/2)

                screen.blit(text_label, text_label_rect)

            # Creates the menu buttons
            button("Click this useless button", 50, 150, 400, 50, dark_green, bright_green)
            button("Click this useless button", 350, 225, 400, 50, dark_green, bright_green)
            button("Click this useless button", 50, 300, 400, 50, dark_green, bright_green)
            button("Click this useless button", 350, 375, 400, 50, dark_green, bright_green, Press10)
            button("Click this useless button", 200, 25, 400, 50, dark_green, bright_green)
            button("Click this useless button", 200, 500, 400, 50, dark_green, bright_green)

            pygame.display.update()
            clock.tick(15)

class Press10:

    def __init__(self):
        pygame.init()
        #Creates the screen and the background
        Press10 = True
        screen = pygame.display.set_mode([800, 600])
        pygame.display.set_caption('Useless')
        font1 = pygame.font.Font(None, 36)
        font2 = pygame.font.Font(None, 64)
        background = pygame.Surface(screen.get_size())
        screenheight = pygame.display.get_surface().get_height()
        screenwidth = pygame.display.get_surface().get_width()
        pygame.key.set_repeat(2, 10)
        clock = pygame.time.Clock()
        rgbl = [255, 0, 0]
        random.shuffle(rgbl)

        def game_quit():
            # Quits the game
            pygame.quit
            quit()

        while (Press10 == True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            screen.fill(black)

            title1 = font2.render("The Useless Game", 1, green)
            title1_rect = title1.get_rect()
            title1_rect.center = (screenwidth/2, screenheight/5)

            screen.blit(title1, title1_rect)

            title2 = font1.render("You're very persistant, aren't you?", 1, red)
            title2_rect = title2.get_rect()
            title2_rect.center = (screenwidth/2, 450)

            screen.blit(title2, title2_rect)

            # Fills the background with white and creates a main menu message in the center
            # of the screen


            def button(text, x, y, width, height, color1, color2, action=None):
                # Button function
                # Recieves the position, width, height, standing color, and the color while the mouse is hovering on the button.
                # Additionally, if the button has a function attached, that can be included
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()

                if x + width > mouse[0] > x and y + height > mouse[1] > y:
                    pygame.draw.rect(screen, color2, (x, y, width, height))
                    if click[0] == 1 and action != None:
                        action()
                else:
                    pygame.draw.rect(screen, color1, (x, y, width, height))

                text_label = font1.render(text, 1, black)
                text_label_rect = text_label.get_rect()
                text_label_rect.center = (x + width/2, y + height/2)

                screen.blit(text_label, text_label_rect)

            # Creates the menu buttons
            button("Click this useless button", 200, 300, 400, 50, dark_green, bright_green, Press11)

            pygame.display.update()
            clock.tick(15)

class Press11:

    def __init__(self):
        pygame.init()
        #Creates the screen and the background
        Press11 = True
        screen = pygame.display.set_mode([800, 600])
        pygame.display.set_caption('Useless')
        font1 = pygame.font.Font(None, 36)
        font2 = pygame.font.Font(None, 64)
        background = pygame.Surface(screen.get_size())
        screenheight = pygame.display.get_surface().get_height()
        screenwidth = pygame.display.get_surface().get_width()
        pygame.key.set_repeat(2, 10)
        clock = pygame.time.Clock()
        rgbl = [255, 0, 0]
        random.shuffle(rgbl)

        def game_quit():
            # Quits the game
            pygame.quit
            quit()

        while (Press11 == True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            screen.fill(black)

            title1 = font2.render("The Useless Game", 1, green)
            title1_rect = title1.get_rect()
            title1_rect.center = (screenwidth/2, screenheight/5)

            screen.blit(title1, title1_rect)

            title2 = font1.render("Alright, do you want a real challenge?", 1, red)
            title2_rect = title2.get_rect()
            title2_rect.center = (screenwidth/2, 450)

            screen.blit(title2, title2_rect)

            # Fills the background with white and creates a main menu message in the center
            # of the screen


            def button(text, x, y, width, height, color1, color2, action=None):
                # Button function
                # Recieves the position, width, height, standing color, and the color while the mouse is hovering on the button.
                # Additionally, if the button has a function attached, that can be included
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()

                if x + width > mouse[0] > x and y + height > mouse[1] > y:
                    pygame.draw.rect(screen, color2, (x, y, width, height))
                    if click[0] == 1 and action != None:
                        action()
                else:
                    pygame.draw.rect(screen, color1, (x, y, width, height))

                text_label = font1.render(text, 1, black)
                text_label_rect = text_label.get_rect()
                text_label_rect.center = (x + width/2, y + height/2)

                screen.blit(text_label, text_label_rect)

            # Creates the menu buttons
            button("Click this useless button", 200, 300, 400, 50, dark_green, bright_green, Press12)

            pygame.display.update()
            clock.tick(15)

class Press12:

    def __init__(self):
        pygame.init()
        #Creates the screen and the background
        Press12 = True
        screen = pygame.display.set_mode([800, 600])
        pygame.display.set_caption('Useless')
        font1 = pygame.font.Font(None, 36)
        font2 = pygame.font.Font(None, 64)
        background = pygame.Surface(screen.get_size())
        screenheight = pygame.display.get_surface().get_height()
        screenwidth = pygame.display.get_surface().get_width()
        pygame.key.set_repeat(2, 10)
        clock = pygame.time.Clock()
        rgbl = [255, 0, 0]
        random.shuffle(rgbl)
        time = 10 #time in seconds
        TIMER = pygame.USEREVENT+1
        pygame.time.set_timer(TIMER, 1000)

        def game_quit():
            # Quits the game
            pygame.quit
            quit()

        while (Press12 == True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == TIMER:
                    time -= 1

            screen.fill(black)

            title1 = font2.render("The Useless Game", 1, green)
            title1_rect = title1.get_rect()
            title1_rect.center = (screenwidth/2, screenheight/5)

            screen.blit(title1, title1_rect)

            title2 = font1.render("You have 10 seconds to find the hidden button", 1, red)
            title2_rect = title2.get_rect()
            title2_rect.center = (screenwidth/2, 450)

            screen.blit(title2, title2_rect)

            # Fills the background with white and creates a main menu message in the center
            # of the screen

            def button(text, x, y, width, height, color1, color2, action=None):
                # Button function
                # Recieves the position, width, height, standing color, and the color while the mouse is hovering on the button.
                # Additionally, if the button has a function attached, that can be included
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()

                if x + width > mouse[0] > x and y + height > mouse[1] > y:
                    pygame.draw.rect(screen, color2, (x, y, width, height))
                    if click[0] == 1 and action != None:
                        action()
                else:
                    pygame.draw.rect(screen, color1, (x, y, width, height))

                text_label = font1.render(text, 1, black)
                text_label_rect = text_label.get_rect()
                text_label_rect.center = (x + width/2, y + height/2)

                screen.blit(text_label, text_label_rect)

            # Creates the menu buttons
            button("Click this useless button", 0, 0, 400, 50, black, black, Press13)

            if(time == 0):
                game = GameOver()

            pygame.display.update()
            clock.tick(60)

class Press13:

    def __init__(self):
        pygame.init()
        #Creates the screen and the background
        Press13 = True
        screen = pygame.display.set_mode([800, 600])
        pygame.display.set_caption('Useless')
        font1 = pygame.font.Font(None, 36)
        font2 = pygame.font.Font(None, 64)
        background = pygame.Surface(screen.get_size())
        screenheight = pygame.display.get_surface().get_height()
        screenwidth = pygame.display.get_surface().get_width()
        pygame.key.set_repeat(2, 10)
        clock = pygame.time.Clock()
        rgbl = [255, 0, 0]
        random.shuffle(rgbl)

        def game_quit():
            # Quits the game
            pygame.quit
            quit()

        while (Press13 == True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            screen.fill(black)

            title1 = font2.render("The Useless Game", 1, green)
            title1_rect = title1.get_rect()
            title1_rect.center = (screenwidth/2, screenheight/5)

            screen.blit(title1, title1_rect)

            title2 = font1.render("Wow you've got quick reflexes. Let's see you're memory skills.", 1, red)
            title2_rect = title2.get_rect()
            title2_rect.center = (screenwidth/2, 450)

            screen.blit(title2, title2_rect)

            # Fills the background with white and creates a main menu message in the center
            # of the screen


            def button(text, x, y, width, height, color1, color2, action=None):
                # Button function
                # Recieves the position, width, height, standing color, and the color while the mouse is hovering on the button.
                # Additionally, if the button has a function attached, that can be included
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()

                if x + width > mouse[0] > x and y + height > mouse[1] > y:
                    pygame.draw.rect(screen, color2, (x, y, width, height))
                    if click[0] == 1 and action != None:
                        action()
                else:
                    pygame.draw.rect(screen, color1, (x, y, width, height))

                text_label = font1.render(text, 1, black)
                text_label_rect = text_label.get_rect()
                text_label_rect.center = (x + width/2, y + height/2)

                screen.blit(text_label, text_label_rect)

            # Creates the menu buttons
            button("Click this useless button", 200, 300, 400, 50, dark_green, bright_green, Press14)

            pygame.display.update()
            clock.tick(15)

class Press14:

    def __init__(self):
        pygame.init()
        #Creates the screen and the background
        Press14 = True
        screen = pygame.display.set_mode([800, 600])
        pygame.display.set_caption('Useless')
        font1 = pygame.font.Font(None, 36)
        font2 = pygame.font.Font(None, 64)
        font3 = pygame.font.Font(None, 18)
        background = pygame.Surface(screen.get_size())
        screenheight = pygame.display.get_surface().get_height()
        screenwidth = pygame.display.get_surface().get_width()
        pygame.key.set_repeat(2, 10)
        clock = pygame.time.Clock()
        rgbl = [255, 0, 0]
        random.shuffle(rgbl)

        def game_quit():
            # Quits the game
            pygame.quit
            quit()

        while (Press14 == True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            screen.fill(black)

            title1 = font2.render("The Useless Game", 1, green)
            title1_rect = title1.get_rect()
            title1_rect.center = (screenwidth/2, screenheight/5)

            screen.blit(title1, title1_rect)

            title2 = font1.render("What was the sixth response I gave?", 1, red)
            title2_rect = title2.get_rect()
            title2_rect.center = (screenwidth/2, 450)

            screen.blit(title2, title2_rect)

            # Fills the background with white and creates a main menu message in the center
            # of the screen


            def button(text, x, y, width, height, color1, color2, action=None):
                # Button function
                # Recieves the position, width, height, standing color, and the color while the mouse is hovering on the button.
                # Additionally, if the button has a function attached, that can be included
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()

                if x + width > mouse[0] > x and y + height > mouse[1] > y:
                    pygame.draw.rect(screen, color2, (x, y, width, height))
                    if click[0] == 1 and action != None:
                        action()
                else:
                    pygame.draw.rect(screen, color1, (x, y, width, height))

                text_label = font3.render(text, 1, black)
                text_label_rect = text_label.get_rect()
                text_label_rect.center = (x + width/2, y + height/2)

                screen.blit(text_label, text_label_rect)

            # Creates the menu buttons
            button("Damn it! How did you do that?", 100, 250, 300, 50, dark_green, bright_green, GameOver)
            button("You're really getting on my nerves.", 450, 250, 300, 50, dark_green, bright_green, Press15)
            button("That's it! You lost you're useless button privilages.", 100, 350, 300, 50, dark_green, bright_green, GameOver)
            button("OK, try to press the button now!", 450, 350, 300, 50, dark_green, bright_green, GameOver)


            pygame.display.update()
            clock.tick(15)

class Press15:

    def __init__(self):
        pygame.init()
        #Creates the screen and the background
        Press15 = True
        screen = pygame.display.set_mode([800, 600])
        pygame.display.set_caption('Useless')
        font1 = pygame.font.Font(None, 36)
        font2 = pygame.font.Font(None, 64)
        background = pygame.Surface(screen.get_size())
        screenheight = pygame.display.get_surface().get_height()
        screenwidth = pygame.display.get_surface().get_width()
        pygame.key.set_repeat(2, 10)
        clock = pygame.time.Clock()
        rgbl = [255, 0, 0]
        random.shuffle(rgbl)

        def game_quit():
            # Quits the game
            pygame.quit
            quit()

        while (Press15 == True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            screen.fill(black)

            title1 = font2.render("The Useless Game", 1, green)
            title1_rect = title1.get_rect()
            title1_rect.center = (screenwidth/2, screenheight/5)

            screen.blit(title1, title1_rect)

            title2 = font1.render("Impressive! You really want this button to do something.", 1, red)
            title2_rect = title2.get_rect()
            title2_rect.center = (screenwidth/2, 450)

            screen.blit(title2, title2_rect)

            # Fills the background with white and creates a main menu message in the center
            # of the screen


            def button(text, x, y, width, height, color1, color2, action=None):
                # Button function
                # Recieves the position, width, height, standing color, and the color while the mouse is hovering on the button.
                # Additionally, if the button has a function attached, that can be included
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()

                if x + width > mouse[0] > x and y + height > mouse[1] > y:
                    pygame.draw.rect(screen, color2, (x, y, width, height))
                    if click[0] == 1 and action != None:
                        action()
                else:
                    pygame.draw.rect(screen, color1, (x, y, width, height))

                text_label = font1.render(text, 1, black)
                text_label_rect = text_label.get_rect()
                text_label_rect.center = (x + width/2, y + height/2)

                screen.blit(text_label, text_label_rect)

            # Creates the menu buttons
            button("Click this useless button", 200, 300, 400, 50, dark_green, bright_green, Press16)

            pygame.display.update()
            clock.tick(15)

class Press16:

    def __init__(self):
        pygame.init()
        #Creates the screen and the background
        Press16 = True
        screen = pygame.display.set_mode([800, 600])
        pygame.display.set_caption('Useless')
        font1 = pygame.font.Font(None, 36)
        font2 = pygame.font.Font(None, 64)
        background = pygame.Surface(screen.get_size())
        screenheight = pygame.display.get_surface().get_height()
        screenwidth = pygame.display.get_surface().get_width()
        pygame.key.set_repeat(2, 10)
        clock = pygame.time.Clock()
        rgbl = [255, 0, 0]
        random.shuffle(rgbl)

        def game_quit():
            # Quits the game
            pygame.quit
            quit()

        while (Press16 == True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            screen.fill(black)

            title1 = font2.render("The Useless Game", 1, green)
            title1_rect = title1.get_rect()
            title1_rect.center = (screenwidth/2, screenheight/5)

            screen.blit(title1, title1_rect)

            title2 = font1.render("How about this: one more challenge, and you get your wish.", 1, red)
            title2_rect = title2.get_rect()
            title2_rect.center = (screenwidth/2, 450)

            screen.blit(title2, title2_rect)

            # Fills the background with white and creates a main menu message in the center
            # of the screen


            def button(text, x, y, width, height, color1, color2, action=None):
                # Button function
                # Recieves the position, width, height, standing color, and the color while the mouse is hovering on the button.
                # Additionally, if the button has a function attached, that can be included
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()

                if x + width > mouse[0] > x and y + height > mouse[1] > y:
                    pygame.draw.rect(screen, color2, (x, y, width, height))
                    if click[0] == 1 and action != None:
                        action()
                else:
                    pygame.draw.rect(screen, color1, (x, y, width, height))

                text_label = font1.render(text, 1, black)
                text_label_rect = text_label.get_rect()
                text_label_rect.center = (x + width/2, y + height/2)

                screen.blit(text_label, text_label_rect)

            # Creates the menu buttons
            button("Click this useless button", 200, 300, 400, 50, dark_green, bright_green, Press17)

            pygame.display.update()
            clock.tick(15)

class Press17:

    def __init__(self):
        pygame.init()
        #Creates the screen and the background
        Press17 = True
        screen = pygame.display.set_mode([800, 600])
        pygame.display.set_caption('Useless')
        font1 = pygame.font.Font(None, 36)
        font2 = pygame.font.Font(None, 64)
        background = pygame.Surface(screen.get_size())
        screenheight = pygame.display.get_surface().get_height()
        screenwidth = pygame.display.get_surface().get_width()
        pygame.key.set_repeat(2, 10)
        clock = pygame.time.Clock()
        rgbl = [255, 0, 0]
        random.shuffle(rgbl)

        def game_quit():
            # Quits the game
            pygame.quit
            quit()

        while (Press17 == True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            screen.fill(black)

            title1 = font2.render("The Useless Game", 1, green)
            title1_rect = title1.get_rect()
            title1_rect.center = (screenwidth/2, screenheight/5)

            screen.blit(title1, title1_rect)

            title2 = font1.render("The button will only be available for a second. Ready?", 1, red)
            title2_rect = title2.get_rect()
            title2_rect.center = (screenwidth/2, 450)

            screen.blit(title2, title2_rect)

            # Fills the background with white and creates a main menu message in the center
            # of the screen


            def button(text, x, y, width, height, color1, color2, action=None):
                # Button function
                # Recieves the position, width, height, standing color, and the color while the mouse is hovering on the button.
                # Additionally, if the button has a function attached, that can be included
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()

                if x + width > mouse[0] > x and y + height > mouse[1] > y:
                    pygame.draw.rect(screen, color2, (x, y, width, height))
                    if click[0] == 1 and action != None:
                        action()
                else:
                    pygame.draw.rect(screen, color1, (x, y, width, height))

                text_label = font1.render(text, 1, black)
                text_label_rect = text_label.get_rect()
                text_label_rect.center = (x + width/2, y + height/2)

                screen.blit(text_label, text_label_rect)

            # Creates the menu buttons
            button("Click this useless button", 200, 300, 400, 50, dark_green, bright_green, Press18)

            pygame.display.update()
            clock.tick(15)

class Press18:

    def __init__(self):
        pygame.init()
        #Creates the screen and the background
        Press18 = True
        screen = pygame.display.set_mode([800, 600])
        pygame.display.set_caption('Useless')
        font1 = pygame.font.Font(None, 36)
        font2 = pygame.font.Font(None, 64)
        background = pygame.Surface(screen.get_size())
        screenheight = pygame.display.get_surface().get_height()
        screenwidth = pygame.display.get_surface().get_width()
        pygame.key.set_repeat(2, 10)
        clock = pygame.time.Clock()
        rgbl = [255, 0, 0]
        random.shuffle(rgbl)
        time = 0 #time in seconds
        TIMER = pygame.USEREVENT+2
        pygame.time.set_timer(TIMER, 750)

        def game_quit():
            # Quits the game
            pygame.quit
            quit()

        while (Press18 == True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == TIMER:
                    time += 1

            screen.fill(black)

            title1 = font2.render("The Useless Game", 1, green)
            title1_rect = title1.get_rect()
            title1_rect.center = (screenwidth/2, screenheight/5)

            screen.blit(title1, title1_rect)

            # Fills the background with white and creates a main menu message in the center
            # of the screen


            def button(text, x, y, width, height, color1, color2, action=None):
                # Button function
                # Recieves the position, width, height, standing color, and the color while the mouse is hovering on the button.
                # Additionally, if the button has a function attached, that can be included
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()

                if x + width > mouse[0] > x and y + height > mouse[1] > y:
                    pygame.draw.rect(screen, color2, (x, y, width, height))
                    if click[0] == 1 and action != None:
                        action()
                else:
                    pygame.draw.rect(screen, color1, (x, y, width, height))

                text_label = font1.render(text, 1, black)
                text_label_rect = text_label.get_rect()
                text_label_rect.center = (x + width/2, y + height/2)

                screen.blit(text_label, text_label_rect)

            # Creates the menu buttons
            #button("Click this useless button", 200, 300, 400, 50, dark_green, bright_green, Intro)

            if(time == 5):
                button("Click this useless button", 300, 50, 400, 50, dark_green, bright_green, Press19)
            elif(time > 7):
                game = GameOver()

            pygame.display.update()
            clock.tick(15)

class Press19:

    def __init__(self):
        pygame.init()
        #Creates the screen and the background
        Press19 = True
        screen = pygame.display.set_mode([800, 600])
        pygame.display.set_caption('Useless')
        font1 = pygame.font.Font(None, 36)
        font2 = pygame.font.Font(None, 64)
        background = pygame.Surface(screen.get_size())
        screenheight = pygame.display.get_surface().get_height()
        screenwidth = pygame.display.get_surface().get_width()
        pygame.key.set_repeat(2, 10)
        clock = pygame.time.Clock()
        rgbl = [255, 0, 0]
        random.shuffle(rgbl)

        def game_quit():
            # Quits the game
            pygame.quit
            quit()

        while (Press19 == True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            screen.fill(black)

            title1 = font2.render("The Useless Game", 1, green)
            title1_rect = title1.get_rect()
            title1_rect.center = (screenwidth/2, screenheight/5)

            screen.blit(title1, title1_rect)

            title2 = font1.render("Wow! That was amazing! Ok, you earned this.", 1, red)
            title2_rect = title2.get_rect()
            title2_rect.center = (screenwidth/2, 450)

            screen.blit(title2, title2_rect)

            # Fills the background with white and creates a main menu message in the center
            # of the screen


            def button(text, x, y, width, height, color1, color2, action=None):
                # Button function
                # Recieves the position, width, height, standing color, and the color while the mouse is hovering on the button.
                # Additionally, if the button has a function attached, that can be included
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()

                if x + width > mouse[0] > x and y + height > mouse[1] > y:
                    pygame.draw.rect(screen, color2, (x, y, width, height))
                    if click[0] == 1 and action != None:
                        action()
                else:
                    pygame.draw.rect(screen, color1, (x, y, width, height))

                text_label = font1.render(text, 1, black)
                text_label_rect = text_label.get_rect()
                text_label_rect.center = (x + width/2, y + height/2)

                screen.blit(text_label, text_label_rect)

            # Creates the menu buttons
            button("Click this useless button", 200, 300, 400, 50, dark_green, bright_green, Press20)

            pygame.display.update()
            clock.tick(15)

class Press20:

    def __init__(self):
        pygame.init()
        #Creates the screen and the background
        Press20 = True
        screen = pygame.display.set_mode([800, 600])
        pygame.display.set_caption('Useless')
        font1 = pygame.font.Font(None, 36)
        font2 = pygame.font.Font(None, 64)
        background = pygame.Surface(screen.get_size())
        screenheight = pygame.display.get_surface().get_height()
        screenwidth = pygame.display.get_surface().get_width()
        pygame.key.set_repeat(2, 10)
        clock = pygame.time.Clock()
        rgbl = [255, 0, 0]
        random.shuffle(rgbl)

        def game_quit():
            # Quits the game
            pygame.quit
            quit()

        while (Press20 == True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            screen.fill(black)

            title1 = font2.render("The Useless Game", 1, green)
            title1_rect = title1.get_rect()
            title1_rect.center = (screenwidth/2, screenheight/5)

            screen.blit(title1, title1_rect)

            title2 = font1.render("There you go. Here is your reward.", 1, red)
            title2_rect = title2.get_rect()
            title2_rect.center = (screenwidth/2, 450)

            screen.blit(title2, title2_rect)

            # Fills the background with white and creates a main menu message in the center
            # of the screen


            def button(text, x, y, width, height, color1, color2, action=None):
                # Button function
                # Recieves the position, width, height, standing color, and the color while the mouse is hovering on the button.
                # Additionally, if the button has a function attached, that can be included
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()

                if x + width > mouse[0] > x and y + height > mouse[1] > y:
                    pygame.draw.rect(screen, color2, (x, y, width, height))
                    if click[0] == 1 and action != None:
                        action()
                else:
                    pygame.draw.rect(screen, color1, (x, y, width, height))

                text_label = font1.render(text, 1, black)
                text_label_rect = text_label.get_rect()
                text_label_rect.center = (x + width/2, y + height/2)

                screen.blit(text_label, text_label_rect)

            # Creates the menu buttons
            button("Click this usefull button", 200, 300, 400, 50, dark_green, bright_green, End)

            pygame.display.update()
            clock.tick(15)

class End:

    def __init__(self):
        pygame.init()
        #Creates the screen and the background
        End = True
        screen = pygame.display.set_mode([800, 600])
        pygame.display.set_caption('Useless')
        font1 = pygame.font.Font(None, 36)
        font2 = pygame.font.Font(None, 64)
        background = pygame.Surface(screen.get_size())
        screenheight = pygame.display.get_surface().get_height()
        screenwidth = pygame.display.get_surface().get_width()
        pygame.key.set_repeat(2, 10)
        clock = pygame.time.Clock()
        rgbl = [255, 0, 0]
        random.shuffle(rgbl)

        def game_quit():
            # Quits the game
            pygame.quit
            quit()

        while (End == True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            screen.fill(black)

            Trophy = pygame.image.load('trophy.png')
            smallTrophy = pygame.transform.scale(Trophy, (400, 300))

            title2 = font1.render("You win!", 1, red)
            title2_rect = title2.get_rect()
            title2_rect.center = (screenwidth/2, 450)

            screen.blit(title2, title2_rect)
            screen.blit(smallTrophy,(200,100))

            # Fills the background with white and creates a main menu message in the center
            # of the screen


            def button(text, x, y, width, height, color1, color2, action=None):
                # Button function
                # Recieves the position, width, height, standing color, and the color while the mouse is hovering on the button.
                # Additionally, if the button has a function attached, that can be included
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()

                if x + width > mouse[0] > x and y + height > mouse[1] > y:
                    pygame.draw.rect(screen, color2, (x, y, width, height))
                    if click[0] == 1 and action != None:
                        action()
                else:
                    pygame.draw.rect(screen, color1, (x, y, width, height))

                text_label = font1.render(text, 1, black)
                text_label_rect = text_label.get_rect()
                text_label_rect.center = (x + width/2, y + height/2)

                screen.blit(text_label, text_label_rect)

            # Creates the menu buttons
            button("Retry", 200, 500, 400, 50, dark_green, bright_green, Press1_4)

            pygame.display.update()
            clock.tick(15)


def main():
    game = Intro()

main()
