from assets.GUI_components import *
from assets.main_functions import *
import pygame
import random



# MAIN SCREEN GUI START

def main_screen(event):
    screen.fill(BACKGROUND)
    mouse_pos = pygame.mouse.get_pos()
    main_logo = pygame.transform.smoothscale(pygame.image.load(
        "assets\\LOGO.png").convert_alpha(), (400, 400))
    screen.blit(main_logo, (200, 5))

    # BUTTON 1
    suggestion_button = button(
        color=(14, 14, 192), x=300, y=450, width=200, height=40, text="SONGS")
    if event.type == pygame.MOUSEMOTION:
        if suggestion_button.isOver(mouse_pos):
            suggestion_button.color = (150, 150, 255)
    suggestion_button.draw(screen)

    # BUTTON 2
    suggestion_button = button(
        color=(14, 14, 192), x=295, y=520, width=210, height=40, text="POEMS")
    if event.type == pygame.MOUSEMOTION:
        if suggestion_button.isOver(mouse_pos):
            suggestion_button.color = (150, 150, 255)
    suggestion_button.draw(screen)

    # BUTTON 3
    suggestion_button = button(
        color=(14, 14, 192), x=290, y=590, width=220, height=40, text="LYRICS")
    if event.type == pygame.MOUSEMOTION:
        if suggestion_button.isOver(mouse_pos):
            suggestion_button.color = (150, 150, 255)
    suggestion_button.draw(screen)

    # BUTTON 4
    suggestion_button = button(
        color=(14, 14, 192), x=285, y=660, width=230, height=40, text="QOUTES")
    if event.type == pygame.MOUSEMOTION:
        if suggestion_button.isOver(mouse_pos):
            suggestion_button.color = (150, 150, 255)
    suggestion_button.draw(screen)

    # BUTTON 5
    suggestion_button = button(
        color=(14, 14, 192), x=280, y=730, width=240, height=40, text="SIMILAR")
    if event.type == pygame.MOUSEMOTION:
        if suggestion_button.isOver(mouse_pos):
            suggestion_button.color = (150, 150, 255)
    suggestion_button.draw(screen)

    # RANDOM TIP
    global main_screen_tip
    display_text(screen,center=True,text=main_screen_tip,x=400,y=800)

# MAIN SCREEN GUI END


def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        pygame.display.update()
        clock.tick()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            main_screen(event)
    pygame.quit()


def gen_tip():
    tip_no = random.randint(1,5)
    # tip_no=4
    if tip_no == 1:
        data = Anime().random_quotes()
        text = (f'" {data["quote"]} "') + (f'  - {data["character"]} (Anime : {data["anime"]})')
    if tip_no == 2:
        data = Qoutes().random_qoutes()
        text = (f'" {data["content"]} "') + (f" - {data['author']}")
    if tip_no == 3:
        text = "Advice : "+Advice().gen_advice()
    if tip_no == 4:
        text ="~~   " + Joke().get_joke() + "   ~~"
    if tip_no == 5:
        text = 'Fact: '+Facts().random_facts()
    with open("temp\\temp_data.json", 'r') as f:
        file_text = json.loads(f.read())
    with open("temp\\temp_data.json", 'w') as f:
        file_text["main_screen_tip"] = text
        f.write(json.dumps(file_text))
    return text

if __name__ == "__main__":

    #  GLOBAL VARIABLES START
    WIDTH, HEIGHT = 800, 900
    BACKGROUND = (0, 16, 42)
    FPS = 60
    ICON = pygame.image.load("assets\\favicon_io\\favicon-32x32.png")
    main_screen_tip=gen_tip()
    #  GLOBAL VARIABLES END
    
    # PYGAME INIT() BASICS START
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_icon(ICON)
    pygame.display.set_caption("M A D")
    # PYGAME INIT() BASICS END

    main()