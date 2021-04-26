import pygame
pygame.font.init()
from Assets.main_functions import *
from Assets.GUI_components import *


#  GLOBAL VARIABLES START
WIDTH,HEIGHT=1000,750
BACKGROUND=(0,16,47)
FPS=60
ICON=pygame.image.load("Assets\\favicon_io\\favicon-32x32.png")
#  GLOBAL VARIABLES END


# PYGAME INIT() BASICS START
pygame.init()
screen= pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_icon(ICON)
pygame.display.set_caption("M A D")
# PYGAME INIT() BASICS END


# MAIN GUI START
def main_screen():
    screen.fill(BACKGROUND)
    pygame.display.update()


def main():
    run = True
    clock=pygame.time.Clock()
    while run:
        clock.tick()
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                run = False
        main_screen()
    pygame.quit()
    
    

# MAIN GUI END



if __name__=="__main__":
    main()