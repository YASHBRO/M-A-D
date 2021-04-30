from assets.GUI_components import *
from assets.main_functions import *
import pygame
import random


def is_over(pos, x, y, width, height):
    if pos[0] > x and pos[0] < (x + width):
        if pos[1] > y and pos[1] < (y + height):
            return True

    return False


class song_page:
    def __init__(self):
        running = True
        clock = pygame.time.Clock()
        search_box = input_text(font_size=17, text_color=(
            0, 0, 0), cursor_color=(0, 0, 10))
        while running:
            mouse_pos = pygame.mouse.get_pos()
            pygame.display.update()
            clock.tick()
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

                screen.fill(BACKGROUND)
                heading_logo = pygame.transform.smoothscale(pygame.image.load(
                    "assets\\favicon_io\\android-chrome-512x512.png").convert_alpha(), (100, 100))
                screen.blit(heading_logo, (350, 0))
                heading = button(color=(19, 0, 166), x=0, y=100,
                                 width=800, height=50, text="SONGS", font_size=30)
                heading.draw(screen, font_color=(255, 255, 255))
                
                back_button=button(color=(52, 196, 0), x=10, y=850, width=75, height=45, text="BACK",font_size=15)
                if event.type == pygame.MOUSEMOTION:
                    if back_button.isOver(mouse_pos):
                        back_button.color = (68, 255, 0)
                    else:
                        back_button.color = (52, 196, 0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if back_button.isOver(mouse_pos):
                        running=False
                back_button.draw(screen, (0, 0, 0))

                display_text(screen, center=True,
                             text="Search here:", x=400, y=250, font_size=25)

                pygame.draw.rect(screen, (255, 255, 255), (100, 350, 600, 40))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if is_over(mouse_pos, 100, 350, 600, 40):
                        search_box.active = True
                    else:
                        search_box.active = False
                search_box.update(events)
                screen.blit(search_box.get_surface(), (105, 355))
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        searched_text = search_box.get_text()
                        if len(searched_text.strip()) == 0:
                            pass
                        else:
                            Songs().playOnYT(searched_text)

                play_on_yt = button(
                    color=(52, 196, 0), x=250, y=460, width=300, height=85, text="Play on YouTube")
                if event.type == pygame.MOUSEMOTION:
                    if play_on_yt.isOver(mouse_pos):
                        play_on_yt.color = (68, 255, 0)
                    else:
                        play_on_yt.color = (52, 196, 0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_on_yt.isOver(mouse_pos):
                        searched_text = search_box.get_text()
                        if len(searched_text.strip()) == 0:
                            pass
                        else:
                            Songs().playOnYT(searched_text)
                play_on_yt.draw(screen, (0, 0, 0))

                download_video = button(
                    color=(52, 196, 0), x=250, y=630, width=300, height=85, text="Download this Video")
                if event.type == pygame.MOUSEMOTION:
                    if download_video.isOver(mouse_pos):
                        download_video.color = (68, 255, 0)
                    else:
                        download_video.color = (52, 196, 0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if download_video.isOver(mouse_pos):
                        searched_text = search_box.get_text()
                        if len(searched_text.strip()) == 0:
                            pass
                        else:
                            Songs().downloadVideo(searched_text)
                download_video.draw(screen, (0, 0, 0))

                download_audio = button(
                    color=(52, 196, 0), x=250, y=800, width=300, height=85, text="Download it's Audio")
                if event.type == pygame.MOUSEMOTION:
                    if download_audio.isOver(mouse_pos):
                        download_audio.color = (68, 255, 0)
                    else:
                        download_audio.color = (52, 196, 0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if download_audio.isOver(mouse_pos):
                        searched_text = search_box.get_text()
                        if len(searched_text.strip()) == 0:
                            pass
                        else:
                            Songs().downloadAudio(searched_text)
                download_audio.draw(screen, (0, 0, 0))


class poems_page:
    def display_poem(self, text):
        pass

    def __init__(self):
        running = True
        clock = pygame.time.Clock()
        search_by_title = input_text(
            font_size=17, text_color=(0, 0, 0), cursor_color=(0, 0, 10))
        search_by_author = input_text(
            font_size=17, text_color=(0, 0, 0), cursor_color=(0, 0, 10))
        while running:
            mouse_pos = pygame.mouse.get_pos()
            pygame.display.update()
            clock.tick()
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

                screen.fill(BACKGROUND)
                heading_logo = pygame.transform.smoothscale(pygame.image.load(
                    "assets\\favicon_io\\android-chrome-512x512.png").convert_alpha(), (100, 100))
                screen.blit(heading_logo, (350, 0))
                heading = button(color=(19, 0, 166), x=0, y=100,
                                 width=800, height=50, text="POEMS", font_size=30)
                heading.draw(screen, font_color=(255, 255, 255))

                back_button=button(color=(52, 196, 0), x=10, y=850, width=75, height=45, text="BACK",font_size=15)
                if event.type == pygame.MOUSEMOTION:
                    if back_button.isOver(mouse_pos):
                        back_button.color = (68, 255, 0)
                    else:
                        back_button.color = (52, 196, 0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if back_button.isOver(mouse_pos):
                        running=False
                back_button.draw(screen, (0, 0, 0))

                random_poem = button(
                    color=(52, 196, 0), x=250, y=250, width=300, height=85, text="Random Peom")
                if event.type == pygame.MOUSEMOTION:
                    if random_poem.isOver(mouse_pos):
                        random_poem.color = (68, 255, 0)
                    else:
                        random_poem.color = (52, 196, 0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if random_poem.isOver(mouse_pos):
                        generated_poem = Poem().random_poem()
                random_poem.draw(screen, (0, 0, 0))


# MAIN SCREEN GUI START
class main_screen:
    def __init__(self, event):
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
        if event.type == pygame.MOUSEBUTTONDOWN:
            if suggestion_button.isOver(mouse_pos):
                render = song_page()
        suggestion_button.draw(screen, font_color=(255, 255, 0))

        # BUTTON 2
        suggestion_button = button(
            color=(14, 14, 192), x=295, y=520, width=210, height=40, text="POEMS")
        if event.type == pygame.MOUSEMOTION:
            if suggestion_button.isOver(mouse_pos):
                suggestion_button.color = (150, 150, 255)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if suggestion_button.isOver(mouse_pos):
                render = poems_page()
        suggestion_button.draw(screen, font_color=(255, 255, 0))

        # BUTTON 3
        suggestion_button = button(
            color=(14, 14, 192), x=290, y=590, width=220, height=40, text="LYRICS")
        if event.type == pygame.MOUSEMOTION:
            if suggestion_button.isOver(mouse_pos):
                suggestion_button.color = (150, 150, 255)
        suggestion_button.draw(screen, font_color=(255, 255, 0))

        # BUTTON 4
        suggestion_button = button(
            color=(14, 14, 192), x=285, y=660, width=230, height=40, text="QUOTES")
        if event.type == pygame.MOUSEMOTION:
            if suggestion_button.isOver(mouse_pos):
                suggestion_button.color = (150, 150, 255)
        suggestion_button.draw(screen, font_color=(255, 255, 0))

        # BUTTON 5
        suggestion_button = button(
            color=(14, 14, 192), x=280, y=730, width=240, height=40, text="SIMILAR")
        if event.type == pygame.MOUSEMOTION:
            if suggestion_button.isOver(mouse_pos):
                suggestion_button.color = (150, 150, 255)
        suggestion_button.draw(screen, font_color=(255, 255, 0))

        # RANDOM TIP
        global main_screen_tip
        display_text(screen, center=True, text=main_screen_tip, x=20, y=800)

# MAIN SCREEN GUI END


def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
            main_screen(event)
        pygame.display.update()
    pygame.quit()


def gen_tip():
    tip_no = random.randint(1, 5)
    # tip_no=3
    if tip_no == 1:
        data = Anime().random_quotes()
        text = (f'" {data["quote"]} "') + \
            (f'  - {data["character"]} (Anime : {data["anime"]})')
    if tip_no == 2:
        data = Quotes().random_quotes()
        text = (f'" {data["content"]} "') + (f" - {data['author']}")
    if tip_no == 3:
        text = "Advice : "+Advice().gen_advice()
    if tip_no == 4:
        text = "~~   " + Joke().get_joke() + "   ~~"
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
    main_screen_tip = gen_tip()
    #  GLOBAL VARIABLES END

    # PYGAME INIT() BASICS START
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_icon(ICON)
    pygame.display.set_caption("M A D")
    # PYGAME INIT() BASICS END

    main()
