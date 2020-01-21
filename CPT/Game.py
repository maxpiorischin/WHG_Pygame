import pygame  # Imports our module pygame, used to draw, track key inputs, and create a window to play on.
import time
import webbrowser

# from time import clock
pygame.init()  # Initializes Pygame

win = pygame.display.set_mode((500, 500))  # Window Size

clock = pygame.time.Clock()  # Clock Counter to track time

pygame.display.set_caption("Worlds Hardest Game")  # Sets window caption

# All these Variables store pictures coming from the file directory
bg0 = pygame.image.load('pics/L0.png').convert_alpha()  # Loads the menu image stored in "pictures" folder
bg1 = pygame.image.load('pics/L1.png').convert_alpha()  # loads the level 1 Background image
bg2 = pygame.image.load('pics/L2.png').convert_alpha()  # Loads the level 2 Background image
bg3 = pygame.image.load('pics/L3.png').convert_alpha()  # Loads the level 2 Background image
bgcongrats = pygame.image.load('pics/thxscreen.png').convert_alpha()  # Loads the final screen background image
turtle = pygame.image.load('pics/player.png').convert_alpha()  # Loads character picture
spikepic = pygame.image.load('pics/spike.png').convert_alpha()  # .. etc-
giveup = pygame.image.load('pics/giveup.png').convert_alpha()
giveupL3 = pygame.image.load('pics/giveupL3.png').convert_alpha()
L1sound = pygame.mixer.Sound('sounds/mario.wav')
L2sound = pygame.mixer.Sound("sounds/not_a_meme.wav")
L3sound = pygame.mixer.Sound("sounds/numanuma.wav")
coingrab = pygame.mixer.Sound("sounds/coingrab.wav")
deathsound = pygame.mixer.Sound("sounds/deathsound.wav")
bruhwin = pygame.mixer.Sound("sounds/bruh.wav")
checkpointsound = pygame.mixer.Sound("sounds/checkpsound.wav")
congratulations = pygame.mixer.Sound("sounds/congratulations.wav")


class Player(object):  # Object Class for our player, and their characteristics
    def __init__(self, x, y, width, height):  # Initializes our character, and their attributes
        self.x = x  # The x value on the grid is whatever the user chooses
        self.y = y  # The y value on the grid is whatever the user chooses
        self.width = width  # Width of character block
        self.height = height  # Height of character block
        self.vel = 14  # How many points the block moves on the grid
        self.hitbox = (self.x, self.y, self.width, self.height)  # hitbox created by coordinates and dimensions

    def draw(self, win):  # Method that draws the player on the screen, redraw function uses this method mainly
        self.hitbox = (self.x, self.y, self.width, self.height)
        pygame.draw.rect(win, (0, 0, 0), (man.x, man.y, man.width, man.height))
        # Draws a rectangle overlap over the turtle
        win.blit(turtle, (man.x - 44, man.y - 45))  # Places turtle picture over where the man is located,
        # under rectangle


class Projectile(object):  # Object Class a projectile, and their characteristics
    def __init__(self, x, y, radius, colour):  # Characteristics
        self.x = x  # The x value on the grid is whatever the user chooses
        self.y = y  # The y value on the grid is whatever the user chooses
        self.radius = radius  # The radius of the projectile on the grid is whatever the user chooses
        self.colour = colour  # The colour of the projectile on the grid is whatever the user chooses
        self.vel = 12  # The velocity of the projectile on the grid is 12.

    def draw(self, win):  # Method that draws a circle indicating a fireball on the screen
        pygame.draw.circle(win, self.colour, (self.x, self.y), self.radius)
        # draws circle using user inputted colour, coords, and radius.


class Spike(object):  # Object Class for a spike, and their characteristics
    def __init__(self, x, y, height, width, colour):  # Characteristics
        self.x = x  # The x value on the grid is whatever the user chooses
        self.y = y  # The y value on the grid is whatever the user chooses
        self.height = height
        self.width = width
        self.vel = 12
        self.colour = colour  # Pygame colour coordinates set by input

    def draw(self, win):
        pygame.draw.ellipse(win, self.colour, (self.x, self.y, self.width, self.height))


class Coin(object):
    def __init__(self, x, y, height, width):  # Characteristics
        self.x = x  # Set to whatever the user chooses
        self.y = y
        self.height = height
        self.width = width
        self.colour = (255, 255, 0)  # Pygame colour coordinates(yellow)

    def draw(self, win):
        pygame.draw.ellipse(win, self.colour, (self.x, self.y, self.width, self.height))


# starting variables
screenwidth = 480  # Variables for backend dimensions(How far all items go)
screenheight = 480
itemhitbox = 15  # Box around items where collision occurs
coinhitbox = 10
lifecounter = 0  # Counter which counts the amount of times the user has died


#  -- Functions that draws the screen on window for each level/process --
def redrawGameWindow0():
    win.blit(bg0, (0, 0))  # pastes background image on window
    pygame.display.update()  # updates display to show background


def redrawGameWindow1():
    global mfireball, fireball  # Activates the variables within the function
    win.blit(bg1, (0, 0))
    man.draw(win)  # Draws character
    for mfireball in morefireballs:  # Refers back to object class, draws circle where fireballs are located
        mfireball.draw(win)
    for fireball in fireballs:
        fireball.draw(win)
    pygame.display.update()  # Updates display


def redrawGameWindow2(counter):
    global fireball, mfireball, tfireball  # activates variables within the function
    win.blit(bg2, (0, 0))  # Displays background
    man.draw(win)  # Draws man
    # Draws fireballs where they are located on window
    for mfireball in morefireballs:
        mfireball.draw(win)
    for fireball in fireballs:
        fireball.draw(win)
    for tfireball in threefireballs:
        tfireball.draw(win)
    spikes[1].draw(win)
    if counter == 0:  # If the coin isn't collected, it gets drawn on the screen
        coinez.draw(win)
    win.blit(spikepic, (-70, -45))  # Display spike picture where the spike is located
    pygame.display.update()  # Updates Display


def redrawGameWindow3(counter, counter1):
    global fireball, mfireball  # activates variables within the function
    win.blit(bg3, (0, 0))  # Displays background
    man.draw(win)
    # Draws fireballs where they are located on window
    for mfireball in morefireballs:
        mfireball.draw(win)
    for fireball in fireballs:
        fireball.draw(win)
    for tfireball in threefireballs:
        tfireball.draw(win)
    for cfireball in squarefireballs:
        cfireball.draw(win)
    for spikepiece in spikes:
        spikepiece.draw(win)
    # If the coin isn't vollected, it gets drawn on the screen
    if counter == 0:
        coinez.draw(win)
    if counter1 == 0:
        coinpz.draw(win)
    # win.blit(spikepic, (-70, -45))
    pygame.display.update()  # Updates Display


def redrawGameWindowcongrats():  # Displays congratulations screen
    win.blit(bgcongrats, (0, 0))
    pygame.display.update()


# ---

def basicmovement():  # This function is used for all levels to control the player movement
    global run, run2, run3, runcongrats, coincounter, coincounter1  # Makes variables available to be used in this function
    keys = pygame.key.get_pressed()  # Sets variable to pygame key detection
    # These commands use pythons key detection to move the player (vel) amount of spaces a direction
    if keys[pygame.K_LEFT] and man.x >= man.vel + man.width:  # layer can only move within the window restrictions
        man.x -= man.vel
    if keys[pygame.K_RIGHT] and man.x <= screenwidth - man.width:
        man.x += man.vel
    if keys[pygame.K_UP] and man.y >= man.vel:
        man.y -= man.vel
    if keys[pygame.K_DOWN] and man.y <= screenheight - man.height:
        man.y += man.vel
    # These commands create cheat codes by making a letter press take the player to a certain next level
    if keys[pygame.K_p]:
        pygame.mixer.Sound.play(bruhwin)  # plays level completion sound
        run = True
        run2 = False
        run3 = False
    if keys[pygame.K_o]:
        pygame.mixer.Sound.play(bruhwin)
        run = False
        run2 = True
        run3 = False
    if keys[pygame.K_i]:
        pygame.mixer.Sound.play(bruhwin)
        run = False
        run2 = False
        run3 = True
    if keys[pygame.K_t]:
        pygame.mixer.Sound.play(bruhwin)
        run = False
        run2 = False
        run3 = False
        runcongrats = True
        pygame.mixer.Sound.stop(L3sound)
    # This command grabs all the coins
    if keys[pygame.K_g]:
        coincounter = True
        coincounter1 = True


def playerdeath(x, y):  # Function for the players' death, takes players' coordinates as parameters
    global lifecounter, coincounter, coincounter1
    pygame.mixer.Sound.play(deathsound)  # Plays "oof" sound
    if run or run2:
        win.blit(giveup, (0, 0))  # plays smaller give up screen if the first or second level
    if run3:
        win.blit(giveupL3, (0, 0))  # plays bigger give up screen for level 3
    pygame.display.update()
    time.sleep(1)  # shows screen for a second by temporarily stopping time for a second
    man.x = x  # Sets players coordinates according to parameters inputted
    man.y = y
    lifecounter += 1  # Adds 1 to the life counter
    if run2:
        coinez.x = coinezx2  # Sets coins to their locations by setting them to their coordinates
        coinez.y = coinezy2
        coincounter = False
        coincounter1 = False
    if run3 and not checkpointcheck:  # resets coins if checkpoint wasn't hit
        coinez.x = coinezx3
        coinez.y = coinezy3
        coincounter = False  # Sets coin value to not grabbed
        coincounter1 = False
        print(checkpointcheck)
    print("Lives used: " + str(lifecounter))


# This function gets activated when a coin is grabbed
def coingrabbed(a, b, x, y, x2, y2):
    global coincounter, coincounter1
    print("Coin Grabbed")
    if a:  # If the coin is collected, it gets removed off the screen based off the coordinates in parameters
        coincounter = True
        coinez.x = x
        coinez.y = y
        pygame.mixer.Sound.play(coingrab)  # Plays coin grabbing sound
    if b:  # activates if the second coin is collected
        coincounter1 = True
        coinpz.x = x2
        coinpz.y = y2
        pygame.mixer.Sound.play(coingrab)


print("CHEAT CODES")  # prints cheat codes to the console
print("o: Skip to second level")
print("i: Skip to 3rd level")
print("t: Skip to end of game")
print("g: collect all coins")
run0 = True
run = False  # Variables that determine if a level is activated
run2 = False
run3 = False
runcongrats = False
while run0:
    keys = pygame.key.get_pressed()  # Sets variable to what key is pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If player presses red x in corner, it closes the game
            run0 = False
    pygame.event.get()  # Allows events to activate (key presses)
    if keys[pygame.K_SPACE]:  # Pressing space activates the first level
        # print("Yes") # Testing code
        run0 = False
        run = True
    if keys[pygame.K_RETURN]:  # Pressing return opens a link
        webbrowser.open("https://sites.google.com/ycdsbk12.ca/worldshardestgame/game-manual")
        time.sleep(1)
    redrawGameWindow0()  # Draws the window to display
# mainloop 1
winsquarewidth = 405  # Coordinates for where the win square is
winsquareheight = 410
man = Player(40, 40, 10, 10)  # Characteristics of the player
pygame.mixer.Sound.play(L1sound)
# Lists that store the fireball objects
fireballs = []
morefireballs = []
itemhitbox = 15  # Coin hit-boxes
coinhitbox = 5
coincounter = False
spawnx = 40  # Variables that control where the player spawns
spawny = 40
while run:  # Big while loop for the level, while loop ends when level is passed
    seconds = (pygame.time.get_ticks()) / 1000
    pygame.time.delay(100)  # Sets the frame-rate so game isn't running as fast as the computer can process
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If x is pressed, quits the game
            run = False
    if seconds % 2 < 1:  # Displays fireballs after every certain amount of time, depending on how it divides
        fireballs.append(Projectile(370, 1, 5, (255, 0, 0)))
    if seconds % 1.5 < 1:
        morefireballs.append(Projectile(479, 20, 13, (255, 0, 0)))
    if seconds % 3 < 1:
        fireballs.append(Projectile(145, 1, 5, (255, 0, 0)))
    # print(seconds)
    for mfireball in morefireballs:  # Controls every fireball in the list
        if mfireball.x - 15 <= man.x <= mfireball.x + 15:  # Big Fireball collision detection using the hitboxes
            # print("Oye")
            if mfireball.y + 15 >= man.y >= mfireball.y - 15:  # Collision detection
                playerdeath(spawnx, spawny)
        if screenwidth > mfireball.x > 0 and screenheight > mfireball.y > 0:  # if the fireball is in range of the
            # screen, it moves down and left
            mfireball.x -= mfireball.vel
            mfireball.y += mfireball.vel
        else:
            morefireballs.pop(morefireballs.index(mfireball))  # If the fireball is not on the screen, it gets deleted
    for fireball in fireballs:  # Big Fireball collision detection using the hit-boxes
        if fireball.x - itemhitbox <= man.x <= fireball.x + itemhitbox:  # Checks if man is touching fireball hit-box
            # print("Oye")
            if fireball.y + itemhitbox >= man.y >= fireball.y - itemhitbox:
                playerdeath(spawnx, spawny)
        if screenheight > fireball.y > 0:  # Moves fireball if it is still within the screen
            fireball.y += fireball.vel
        else:
            fireballs.pop(fireballs.index(fireball))
    if man.x >= winsquarewidth - man.width and man.y >= winsquareheight - man.height:  # If player is in winning box,
        # next level starts
        pygame.mixer.Sound.stop(L1sound)  # stops L1 music and starts L2 music
        pygame.mixer.Sound.play(bruhwin)
        run = False
        run2 = True  # Runs level 2
        run3 = False
        runcongrats = False
    basicmovement()  # Activates movement function
    """if man.x >= fireball.x - 40 and man.x <= fireball.x + 40:
        print("Oye")
        if man.y <= fireball.y + 40 and man.y >= fireball.y - 40:
           man.x = 40
           man.y = 40"""  # old code

    redrawGameWindow1()  # Draws first level

screenwidth = 480
screenheight = 480  # Setting new window and winning box variables
winsquarewidth = 410
winsquareheight = 100

man.x = 45
man.y = 435
coinezx2 = 60  # setting player and item coordinates, new lists for the projectiles
coinezy2 = 60
coinez = Coin(coinezx2, coinezy2, 10, 10)
pygame.mixer.Sound.stop(L1sound)
pygame.mixer.Sound.play(L2sound)
fireballs = []
morefireballs = []  # New empty lists
threefireballs = []
spikes = []
while run2:
    seconds = (pygame.time.get_ticks()) / 1000  # variable for seconds in order to use time
    pygame.time.delay(100)  # Sets frame-rate cap for game

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Pressing x quits the game
            run2 = False
    # These next 8 lines of code create a fireball with characteristics whenever the time condition is met
    if seconds % 2 < 1:
        fireballs.append(Projectile(370, 1, 5, (255, 0, 0)))
    if seconds % 1.75 < 1:
        morefireballs.append(Projectile(479, 100, 13, (255, 0, 0)))
    if seconds % 3 < 1:
        fireballs.append(Projectile(145, 1, 5, (255, 0, 0)))
    if seconds % 1.9 < 1:
        threefireballs.append(Projectile(370, 479, 13, (255, 0, 0)))
    for mfireball in morefireballs:  # For every fireball, there is a movement pattern and possible collision
        if man.x >= mfireball.x - itemhitbox and man.x <= mfireball.x + itemhitbox:  # if coordinates match, player dies
            # print("Oye") Testing
            if man.y <= mfireball.y + itemhitbox and man.y >= mfireball.y - itemhitbox:
                playerdeath(45, 435)
        if mfireball.x < screenwidth and mfireball.y < screenheight and mfireball.y > 0 and mfireball.x > 0:
            mfireball.x -= mfireball.vel
        else:
            morefireballs.pop(morefireballs.index(mfireball))  # Removes fireball if not in window
    for fireball in fireballs:  # Function is same as previous one, just moving differently
        if man.x >= fireball.x - itemhitbox and man.x <= fireball.x:
            # print("Oye")
            if man.y <= fireball.y + itemhitbox and man.y >= fireball.y - itemhitbox:
                playerdeath(45, 435)
        if fireball.y < screenheight and fireball.y > 0:
            fireball.y += fireball.vel
        else:
            fireballs.pop(fireballs.index(fireball))
    for tfireball in threefireballs:  # Function is same as previous one, just moving differently
        if man.x >= tfireball.x - itemhitbox and man.x <= tfireball.x:
            # print("Oye")
            if man.y <= tfireball.y + itemhitbox and man.y >= tfireball.y - itemhitbox:
                playerdeath(45, 435)
        if tfireball.x < screenwidth and tfireball.y < screenheight and tfireball.y > 0 and tfireball.x > 0:
            tfireball.x -= tfireball.vel
            tfireball.y -= tfireball.vel
        else:
            threefireballs.pop(threefireballs.index(tfireball))
    spikes.append(Spike(500 - screenwidth, 200, 5, 340, (40, 40, 40)))  # Adds two spike areas, one as a black hole
    spikes.append(Spike(300, 500 - screenheight, 65, 25, (40, 40, 40)))
    for spikepiece in spikes:  # Every spike has a collision area
        if man.x >= spikepiece.x - spikepiece.width - itemhitbox + 30 and man.x <= spikepiece.x + spikepiece.width + itemhitbox - 10:
            # print("Oye") First collision detection
            if man.y <= spikepiece.y + spikepiece.height + itemhitbox and man.y >= spikepiece.y - spikepiece.height - itemhitbox:
                playerdeath(45, 435)  # if player fits the conditions, a collision occurs
    if man.x >= coinez.x - coinhitbox and man.x <= coinez.x + coinhitbox and not coincounter:  # Coin hitbox conditions
        # print("Oye")
        if man.y <= coinez.y + coinhitbox and man.y >= coinez.y - coinhitbox:
            coingrabbed(True, False, coinezx2, coinezy2, 0, 0)  # If coin collision occurs,
            # the coin grabbing function occurs
    if man.x >= winsquarewidth - man.width and man.y <= winsquareheight - man.height and coincounter:
        pygame.mixer.Sound.play(bruhwin)  # ^ checks if the coin is grabbed and if the user is in the winning area
        run = False
        run2 = False
        run3 = True  # If player fulfills requirements, level 2 stops and level 3 starts
        runcongrats = False

    basicmovement()  # calling the movement and screen drawing function
    redrawGameWindow2(coincounter)

screenwidth = 780
screenheight = 780  # Re-setting variables, this time screen is 800x800 (Slightly less so player isn't at very edge)
winsquarewidth = 730  # new winning square location variables
winsquareheight = 70
itemhitbox = 5  # Two item hit-boxes, one for small items and one for big
bigitemhitbox = 12
win = pygame.display.set_mode((800, 800))  # Creates new window that is 800x800
man.x = 45
man.y = 45  # Variables for where man spawns
spawnx = 45
spawny = 45
checkpointcheck = False  # Variable which represents if checkpoint has been activated
coinezx3 = 185
coinezy3 = 591  # 2 coin spawn location coordinates
coinpzx3 = 575
coinpzy3 = 590
coinez = Coin(coinezx3, coinezy3, 10, 10)  # Creates 2 new coins with their variable spawn points as the coordinates
coinpz = Coin(coinpzx3, coinpzy3, 10, 10)  # width and height for the coin is 10,10
pygame.mixer.Sound.stop(L2sound)  # Stops the level 2 sound
pygame.mixer.Sound.play(L3sound)  # Plays the level 3 sound
coincounter = False  # Sets the coin counters to False
coincounter1 = False
fireballs = []
morefireballs = []
threefireballs = []  # Empty lists that will hold their respective fireballs
squarefireballs = []
spikes = []
sqcounter = 0  # Variable for how many fireballs apart of the square have been sent out
squaretrack = [(740, 440), (440, 740)]  # Array representing the coordinates of the fireball track
while run3:
    seconds = (pygame.time.get_ticks()) / 1000  # variable for seconds in order to use time
    pygame.time.delay(100)  # Sets frame rate cap to not have the game too fast
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If red x is pressed the game is quit
            run3 = False
    # These lines send out fireballs for every certain amount of time
    if seconds % 1.9 < 1:  # if division remainder is less than 1
        fireballs.append(Projectile(0, 100, 5, (0, 0, 255)))
    if seconds % 1.7 < 1:
        fireballs.append(Projectile(0, 200, 5, (0, 0, 255)))
    if seconds % 1.9 < 1:
        fireballs.append(Projectile(0, 300, 5, (0, 0, 255)))
    # if seconds % 1.7 < 1:
    # fireballs.append(projectile(0, 400, 5, (0, 0, 255)))
    if seconds % 1.9 < 1:
        morefireballs.append(Projectile(5, 779, 13, (0, 0, 255)))
    if seconds % 1.9 < 1:
        threefireballs.append(Projectile(375, 779, 13, (0, 0, 255)))
    if seconds % 0.6 < 0.2 and sqcounter != 28:
        squarefireballs.append(Spike(squaretrack[0][0] + 1, 701, 30, 50, (0, 0, 255)))
        sqcounter += 1
    for fireball in fireballs:  # For every fireball there is a collision and movement pattern
        if man.x >= fireball.x - itemhitbox and man.x <= fireball.x + itemhitbox:
            # print("Oye")
            if man.y <= fireball.y + itemhitbox and man.y >= fireball.y - itemhitbox:
                playerdeath(spawnx, spawny)
        if fireball.x < screenwidth:  # moves when still within the screen
            fireball.x += fireball.vel
        else:
            fireballs.pop(fireballs.index(fireball))  # Removes fireballl when off screen using pop function
    for mfireball in morefireballs:  # Same as previous fireball lines
        if man.x >= mfireball.x - bigitemhitbox and man.x <= mfireball.x + bigitemhitbox:
            # print("Oye")
            if man.y <= mfireball.y + bigitemhitbox and man.y >= mfireball.y - bigitemhitbox:
                playerdeath(spawnx, spawny)
        if mfireball.x <= 400 and mfireball.y >= 400 and mfireball.y >= 0 and mfireball.x >= 0:
            mfireball.x += mfireball.vel
            mfireball.y -= mfireball.vel
        else:
            morefireballs.pop(morefireballs.index(mfireball))
    for tfireball in threefireballs:  # Same as previous fireball lines
        if man.x >= tfireball.x - bigitemhitbox and man.x <= tfireball.x + bigitemhitbox:
            # print("Oye")
            if man.y <= tfireball.y + bigitemhitbox and man.y >= tfireball.y - bigitemhitbox:
                playerdeath(spawnx, spawny)
        if tfireball.x < screenwidth and tfireball.y < screenheight and tfireball.x > 20 and tfireball.x:
            tfireball.x -= tfireball.vel
            tfireball.y -= tfireball.vel
        else:
            threefireballs.pop(threefireballs.index(tfireball))
    for sfireball in squarefireballs:  # Lines of code that operate the fireball track moving in a square
        if sfireball.x < squaretrack[0][0] - 20 and sfireball.y > squaretrack[0][1] and sfireball.y > squaretrack[1][1]:
            # ^ testing If fireball is on bottom side
            if sfireball.height != 20 and sfireball.width != 60:  # Changes fireball dimensions to move upwards
                sfireball.y += 10  # Moves fireballs over from the start to make it look less choppy
                sfireball.height = 20  # Changes the dimensions
                sfireball.width = 60
            sfireball.x += sfireball.vel + 1  # Moves fireballs right until condition is not met
        if sfireball.x > squaretrack[0][0] - 20 and sfireball.y > squaretrack[0][1] and sfireball.y > 0:
            # ^ testing If fireball is on right side
            if sfireball.height != 60 and sfireball.width != 20:
                sfireball.x += 20  # Moves fireball right from the start to look less choppy
                sfireball.height = 60
                sfireball.width = 20 +1  # Changing fireball dimensions
            sfireball.y -= sfireball.vel  # Moving fireball up the screen until conditions are not met
        if sfireball.x > squaretrack[1][0] and sfireball.y < squaretrack[0][1] and sfireball.y > 0:
            # ^ testing If fireball is on top side
            if sfireball.height != 20 and sfireball.width != 60:
                sfireball.x -= 20  # Moves fireballs over from the start to make it look less choppy
                sfireball.height = 20
                sfireball.width = 60  # Changing fireball dimensions
                sfireball.x -= 10  # Moving fireball left until conditions are not met
            sfireball.x -= sfireball.vel+1  # Moving fireball left until conditions are not met
        if sfireball.x < squaretrack[1][0] and sfireball.y < squaretrack[1][1] and sfireball.y > 0:
            # ^ testing If fireball is on left side
            if sfireball.height != 60 and sfireball.width != 20:
                sfireball.height = 60
                sfireball.width = 20  # Changing fireball dimensions
            sfireball.y += sfireball.vel +1 # Moving fireball down until conditions are not met
        if man.x >= sfireball.x - bigitemhitbox and man.x <= sfireball.x + bigitemhitbox:
            # print("Oye")
            if man.y <= sfireball.y + bigitemhitbox and man.y >= sfireball.y - bigitemhitbox:
                playerdeath(spawnx, spawny)
    spikes.append(Spike(390, 10, 85, 20, (40, 40, 40)))
    spikes.append(Spike(390, 105, 85, 20, (40, 40, 40)))  # Adding spikes on the screen to 3 different places
    spikes.append(Spike(390, 205, 85, 20, (40, 40, 40)))
    for spikepiece in spikes:  # Every spike has a collision area
        if man.x >= spikepiece.x - spikepiece.width - itemhitbox + 30 and man.x <= spikepiece.x + spikepiece.width + itemhitbox - 10:
            # print("Oye") #First collision detection
            if man.y <= spikepiece.y + spikepiece.height + itemhitbox and man.y >= spikepiece.y - spikepiece.height - itemhitbox:
                playerdeath(spawnx, spawny)  # Death function occurs if collision happens
    if man.x >= coinez.x - coinhitbox and man.x <= coinez.x + coinhitbox and not coincounter:
        # If first coin is grabbed, the coin grabbing function occurs
        if man.y <= coinez.y + coinhitbox and man.y >= coinez.y - coinhitbox:
            coingrabbed(True, False, coinezx3, coinezy3, coinpzx3, coinpzy3)
    if man.x >= coinpz.x - coinhitbox and man.x <= coinpz.x + coinhitbox:
        # If second coin is grabbed, the coin grabbing function occurs
        if man.y <= coinpz.y + coinhitbox and man.y >= coinpz.y - coinhitbox and not coincounter1:
            coingrabbed(False, True, coinezx3, coinezy3, coinpzx3, coinpzy3)
    if 171 <= man.x <= 185 and 745 <= man.y <= 759 and not checkpointcheck:
        pygame.mixer.Sound.play(checkpointsound)
        spawnx = 171
        spawny = 759
        checkpointcheck = True
    if man.x >= winsquarewidth - man.width and man.y <= winsquareheight - man.height and coincounter and coincounter1:
        pygame.mixer.Sound.stop(
            L3sound)  # If player is in the winning square with all the coins, the level ends, sound stops
        pygame.mixer.Sound.play(bruhwin)
        run = False
        run2 = False
        run3 = False
        runcongrats = True  # Congratulations screen runs
    basicmovement()  # Movement and window drawing function is called
    redrawGameWindow3(coincounter, coincounter1)
pygame.mixer.Sound.play(congratulations)
while runcongrats:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Pressing x quits the game
            runcongrats = False
    pygame.event.get()
    if keys[pygame.K_SPACE]:  # Game exits if space is pressed
        # print("Yes")
        runcongrats = False
    redrawGameWindowcongrats()  # window is drawn with background

pygame.quit()  # Pygame quits once every process is finished

# That's it! (If you are Mr Pasutto please give us a 100 <3)
