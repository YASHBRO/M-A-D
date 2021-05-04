from assets.GUI_components import *
from assets.main_functions import *
import pygame
import random


def is_over(pos, x, y, width, height):
    if pos[0] > x and pos[0] < (x + width):
        if pos[1] > y and pos[1] < (y + height):
            return True
    return False


# MAIN GUI START

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
                                 width=800, height=50, text="SONGS", font_color=(255, 255, 255), font_size=30)
                heading.draw(screen)

                back_button = button(
                    color=(52, 196, 0), x=10, y=850, width=75, height=45, text="BACK", font_size=15)
                if event.type == pygame.MOUSEMOTION:
                    if back_button.isOver(mouse_pos):
                        back_button.color = (68, 255, 0)
                    else:
                        back_button.color = (52, 196, 0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if back_button.isOver(mouse_pos):
                        running = False
                back_button.draw(screen)

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
                    color=(52, 196, 0), x=250, y=460, width=300, height=85, font_color=(255, 255, 255), text="Play on YouTube")
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
                play_on_yt.draw(screen,)

                download_video = button(
                    color=(52, 196, 0), x=250, y=630, width=300, height=85, font_color=(255, 255, 255), text="Download this Video")
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
                download_video.draw(screen,)

                download_audio = button(
                    color=(52, 196, 0), x=250, y=800, width=300, height=85, font_color=(255, 255, 255), text="Download it's Audio")
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
                download_audio.draw(screen,)


class poems_page:
    def __init__(self):
        running = True
        clock = pygame.time.Clock()
        search_by_title = input_text(
            text_color=(0, 0, 0), cursor_color=(0, 0, 10))
        search_by_author = input_text(
            text_color=(0, 0, 0), cursor_color=(0, 0, 10))
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
                                 width=800, height=50, text="POEMS", font_color=(255, 255, 255), font_size=30)
                heading.draw(screen)

                back_button = button(
                    color=(52, 196, 0), x=10, y=850, width=75, height=45, text="BACK", font_size=15)
                if event.type == pygame.MOUSEMOTION:
                    if back_button.isOver(mouse_pos):
                        back_button.color = (68, 255, 0)
                    else:
                        back_button.color = (52, 196, 0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if back_button.isOver(mouse_pos):
                        running = False
                back_button.draw(screen,)

                random_poem = button(
                    color=(52, 196, 0), x=250, y=250, width=300, height=85, font_color=(255, 255, 255), text="Random Peom")
                if event.type == pygame.MOUSEMOTION:
                    if random_poem.isOver(mouse_pos):
                        random_poem.color = (68, 255, 0)
                    else:
                        random_poem.color = (52, 196, 0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if random_poem.isOver(mouse_pos):
                        text = Poem().random_poem()
                        self.display_poem(text)
                random_poem.draw(screen,)

                pygame.draw.rect(screen, (255, 255, 255), (75, 450, 425, 85))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if is_over(mouse_pos, 75, 450, 425, 80):
                        search_by_title.active = True
                    else:
                        search_by_title.active = False
                search_by_title.update(events)
                screen.blit(search_by_title.get_surface(), (80, 480))

                title_search_btn = button(
                    color=(52, 196, 0), x=500, y=450, width=225, height=85, font_color=(255, 255, 255), text="Search by Title")
                if event.type == pygame.MOUSEMOTION:
                    if title_search_btn.isOver(mouse_pos):
                        title_search_btn.color = (68, 255, 0)
                    else:
                        title_search_btn.color = (52, 196, 0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if title_search_btn.isOver(mouse_pos):
                        name = search_by_title.get_text()
                        if len(name.strip()) == 0:
                            pass
                        else:
                            text = Poem().poem_by_title(name)
                            self.display_poem(text)
                title_search_btn.draw(screen,)

                pygame.draw.rect(screen, (255, 255, 255), (75, 650, 425, 85))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if is_over(mouse_pos, 75, 650, 425, 80):
                        search_by_author.active = True
                    else:
                        search_by_author.active = False
                search_by_author.update(events)
                screen.blit(search_by_author.get_surface(), (80, 680))

                author_search_btn = button(
                    color=(52, 196, 0), x=500, y=650, width=225, height=85, font_color=(255, 255, 255), text="Search by Author")
                if event.type == pygame.MOUSEMOTION:
                    if author_search_btn.isOver(mouse_pos):
                        author_search_btn.color = (68, 255, 0)
                    else:
                        author_search_btn.color = (52, 196, 0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if author_search_btn.isOver(mouse_pos):
                        name = search_by_author.get_text()
                        if len(name.strip()) == 0:
                            pass
                        else:
                            text = Poem().poem_by_author(name)
                            self.display_poem(text)
                author_search_btn.draw(screen,)

    def display_poem(self, text):
        self.heading = text["title"]
        font_size_heading = 30
        while True:
            font = pygame.font.SysFont('comicsansms', font_size_heading)
            txt = font.render(self.heading, 1, (0, 0, 0))
            if txt.get_rect().width >= 780:
                font_size_heading -= 2
            else:
                break

        font_size_poem = 20

        scroll = False
        font = pygame.font.SysFont('comicsansms', 20)
        txt = font.render(text["lines"][0], 1, (0, 0, 0))
        if txt.get_rect().height * (int(text["linecount"])) >= 580:
            poem_height = txt.get_rect().height * (int(text["linecount"]))
            scroll = True
        poem_y = 225

        self.author = text["author"]
        font_size_author = font_size_heading-1

        with open("temp\\temp_data.json", 'r') as f:
            file_text = json.loads(f.read())
        with open("temp\\temp_data.json", 'w') as f:
            file_text["poem"] = text
            f.write(json.dumps(file_text))

        self.text = text
        running = True
        clock = pygame.time.Clock()
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

                if scroll:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_DOWN:
                            if poem_y >= -(poem_height-500):
                                poem_y -= 20
                        if event.key == pygame.K_UP:
                            if poem_y <= 225:
                                poem_y += 20
                        if event.key == pygame.K_PAGEDOWN:
                            if poem_y >= -(poem_height-500):
                                poem_y -= 100
                        if event.key == pygame.K_PAGEUP:
                            if poem_y <= 225:
                                poem_y += 100

                display_text(screen, center=False, text="\n".join(
                    text["lines"]), x=30, y=poem_y, font_size=font_size_poem)

                pygame.draw.rect(screen, BACKGROUND, (0, 0, 800, 220))
                pygame.draw.rect(screen, BACKGROUND, (0, 840, 800, 60))

                heading_logo = pygame.transform.smoothscale(pygame.image.load(
                    "assets\\favicon_io\\android-chrome-512x512.png").convert_alpha(), (100, 100))
                screen.blit(heading_logo, (350, 0))
                heading = button(color=(19, 0, 166), x=0, y=100, font_color=(255, 255, 255),
                                 width=800, height=50, text=self.heading, font_size=font_size_heading)
                heading.draw(screen)

                back_button = button(
                    color=(52, 196, 0), x=10, y=850, width=75, height=45, text="BACK", font_size=15)
                if event.type == pygame.MOUSEMOTION:
                    if back_button.isOver(mouse_pos):
                        back_button.color = (68, 255, 0)
                    else:
                        back_button.color = (52, 196, 0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if back_button.isOver(mouse_pos):
                        running = False
                back_button.draw(screen)

                download_button = button(
                    color=(52, 196, 0), x=700, y=850, width=90, height=45, font_color=(255, 255, 255), text="Download", font_size=16)
                if event.type == pygame.MOUSEMOTION:
                    if download_button.isOver(mouse_pos):
                        download_button.color = (68, 255, 0)
                    else:
                        download_button.color = (52, 196, 0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if download_button.isOver(mouse_pos):
                        Poem().download_poem(text)
                download_button.draw(screen)

                display_text(screen, center=False, text='- '+self.author,
                             x=400, y=155, max_width=380, font_size=font_size_author)


class lyrics_page:
    def __init__(self):
        running = True
        clock = pygame.time.Clock()
        search_by_song = input_text(
            text_color=(0, 0, 0), cursor_color=(0, 0, 10))
        search_by_lyrics = input_text(
            text_color=(0, 0, 0), cursor_color=(0, 0, 10))
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
                                 width=800, height=50, text="LYRICS", font_color=(255, 255, 255), font_size=30)
                heading.draw(screen)

                back_button = button(
                    color=(52, 196, 0), x=10, y=850, width=75, height=45, text="BACK", font_size=15)
                if event.type == pygame.MOUSEMOTION:
                    if back_button.isOver(mouse_pos):
                        back_button.color = (68, 255, 0)
                    else:
                        back_button.color = (52, 196, 0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if back_button.isOver(mouse_pos):
                        running = False
                back_button.draw(screen)

                display_text(
                    screen, center=True, text="Get Lyrics by Searching the Name of Song", x=200, y=250, font_size=25)

                pygame.draw.rect(screen, (255, 255, 255), (75, 350, 425, 85))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if is_over(mouse_pos, 75, 350, 425, 85):
                        search_by_song.active = True
                    else:
                        search_by_song.active = False
                search_by_song.update(events)
                screen.blit(search_by_song.get_surface(), (80, 380))

                song_search_btn = button(
                    color=(52, 196, 0), x=500, y=350, width=225, height=85, font_color=(255, 255, 255), text="Search Lyrics", font_size=23)
                if event.type == pygame.MOUSEMOTION:
                    if song_search_btn.isOver(mouse_pos):
                        song_search_btn.color = (68, 255, 0)
                    else:
                        song_search_btn.color = (52, 196, 0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if song_search_btn.isOver(mouse_pos):
                        name = search_by_song.get_text()
                        if len(name.strip()) == 0:
                            pass
                        else:
                            text = Lyrics().searchLyrics(name)
                            self.display_lyrics(text)
                song_search_btn.draw(screen)
                display_text(
                    screen, center=True, text=r'{optional} : mention artist after the song name seperated by ","', x=400, y=445, font_size=17)

                display_text(
                    screen, center=True, text="Search Song Name by writing a part of Lyrics", x=200, y=550, font_size=25)

                pygame.draw.rect(screen, (255, 255, 255), (75, 650, 425, 85))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if is_over(mouse_pos, 75, 650, 425, 85):
                        search_by_lyrics.active = True
                    else:
                        search_by_lyrics.active = False
                search_by_lyrics.update(events)
                screen.blit(search_by_lyrics.get_surface(), (80, 680))

                lyrics_search_btn = button(
                    color=(52, 196, 0), x=500, y=650, width=225, height=85, font_color=(255, 255, 255), text="Search Song Name", font_size=23)
                if event.type == pygame.MOUSEMOTION:
                    if lyrics_search_btn.isOver(mouse_pos):
                        lyrics_search_btn.color = (68, 255, 0)
                    else:
                        lyrics_search_btn.color = (52, 196, 0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if lyrics_search_btn.isOver(mouse_pos):
                        name = search_by_lyrics.get_text()
                        if len(name.strip()) == 0:
                            pass
                        else:
                            text = Lyrics().serachSongByLyrics(name)
                            self.display_song_list(text)
                lyrics_search_btn.draw(screen)

    def display_lyrics(self, text):
        running = True
        clock = pygame.time.Clock()

        self.heading = text["title"]
        font_size_heading = 30
        while True:
            font = pygame.font.SysFont('comicsansms', font_size_heading)
            txt = font.render(self.heading, 1, (0, 0, 0))
            if txt.get_rect().width >= 780:
                font_size_heading -= 2
            else:
                break

        scroll = False
        font = pygame.font.SysFont('comicsansms', 20)
        txt = font.render(text["lyrics"][0:5], 1, (0, 0, 0))
        if txt.get_rect().height * (int(text["linecount"])) >= 580:
            lyrics_height = txt.get_rect().height * (int(text["linecount"]))
            scroll = True
        lyrics_y = 225

        thumbnail=download_image(text['thumbnail'])

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

                if scroll:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_DOWN:
                            if lyrics_y >= -(lyrics_height-500):
                                lyrics_y -= 20
                        if event.key == pygame.K_UP:
                            if lyrics_y <= 225:
                                lyrics_y += 20
                        if event.key == pygame.K_PAGEDOWN:
                            if lyrics_y >= -(lyrics_height-500):
                                lyrics_y -= 100
                        if event.key == pygame.K_PAGEUP:
                            if lyrics_y <= 225:
                                lyrics_y += 100


                song_thumbnail=pygame.transform.smoothscale(pygame.image.load(f"temp\\{thumbnail}").convert_alpha(), (200, 200))
                screen.blit(song_thumbnail, (590, 210))

                display_text(screen, center=False,text=text["lyrics"], x=30, y=lyrics_y, font_size=20)

                pygame.draw.rect(screen, BACKGROUND, (0, 0, 800, 200))
                pygame.draw.rect(screen, BACKGROUND, (0, 840, 800, 60))

                heading_logo = pygame.transform.smoothscale(pygame.image.load(
                    "assets\\favicon_io\\android-chrome-512x512.png").convert_alpha(), (100, 100))
                screen.blit(heading_logo, (350, 0))
                heading = button(color=(19, 0, 166), x=0, y=100,
                                 width=800, height=50, text=text['title'], font_color=(255, 255, 255), font_size=font_size_heading)
                heading.draw(screen)

                display_text(screen, center=False, text='- ' +
                             text['artist'], x=400, y=155, max_width=380, font_size=font_size_heading-5)

                back_button = button(
                    color=(52, 196, 0), x=10, y=850, width=75, height=45, text="BACK", font_size=15)
                if event.type == pygame.MOUSEMOTION:
                    if back_button.isOver(mouse_pos):
                        back_button.color = (68, 255, 0)
                    else:
                        back_button.color = (52, 196, 0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if back_button.isOver(mouse_pos):
                        running = False
                back_button.draw(screen)

                download_button = button(
                    color=(52, 196, 0), x=700, y=850, width=90, height=45, text="Download", font_size=16)
                if event.type == pygame.MOUSEMOTION:
                    if download_button.isOver(mouse_pos):
                        download_button.color = (68, 255, 0)
                    else:
                        download_button.color = (52, 196, 0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if download_button.isOver(mouse_pos):
                        Lyrics().saveLyrics(text['title'],str(text['title']+'\n'+text['artist']+'\n\n'+text['lyrics']))
                download_button.draw(screen)

    def display_song_list(self,text):
        running = True
        clock = pygame.time.Clock()

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
                init_y=250
                for i in range(10):
                    display_text(screen,center=False,text=str(i+1)+'.  '+text[i][0]+'  by '+text[i][1],x=100,y=init_y)
                    init_y+=50
                
                pygame.draw.rect(screen, BACKGROUND, (0, 0, 800, 150))
                pygame.draw.rect(screen, BACKGROUND, (0, 840, 800, 60))

                heading_logo = pygame.transform.smoothscale(pygame.image.load(
                    "assets\\favicon_io\\android-chrome-512x512.png").convert_alpha(), (100, 100))
                screen.blit(heading_logo, (350, 0))
                heading = button(color=(19, 0, 166), x=0, y=100,
                                 width=800, height=50, text="Found these Songs relatable", font_color=(255, 255, 255), font_size=30)
                heading.draw(screen)

                back_button = button(
                    color=(52, 196, 0), x=10, y=850, width=75, height=45, text="BACK", font_size=15)
                if event.type == pygame.MOUSEMOTION:
                    if back_button.isOver(mouse_pos):
                        back_button.color = (68, 255, 0)
                    else:
                        back_button.color = (52, 196, 0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if back_button.isOver(mouse_pos):
                        running = False
                back_button.draw(screen)

                
                






class main_screen:
    def __init__(self, event):
        screen.fill(BACKGROUND)
        mouse_pos = pygame.mouse.get_pos() 
        main_logo = pygame.transform.smoothscale(pygame.image.load(
            "assets\\LOGO.png").convert_alpha(), (400, 400))
        screen.blit(main_logo, (200, 5))

        # BUTTON 1
        song_button = button(
            color=(14, 14, 192), x=300, y=450, width=200, height=40, font_color=(255, 255, 255), text="SONGS")
        if event.type == pygame.MOUSEMOTION:
            if song_button.isOver(mouse_pos):
                song_button.color = (150, 150, 255)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if song_button.isOver(mouse_pos):
                render = song_page()
        song_button.draw(screen)

        # BUTTON 2
        poem_button = button(
            color=(14, 14, 192), x=295, y=520, width=210, height=40, font_color=(255, 255, 255), text="POEMS")
        if event.type == pygame.MOUSEMOTION:
            if poem_button.isOver(mouse_pos):
                poem_button.color = (150, 150, 255)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if poem_button.isOver(mouse_pos):
                render = poems_page()
        poem_button.draw(screen)

        # BUTTON 3
        lyric_button = button(
            color=(14, 14, 192), x=290, y=590, width=220, font_color=(255, 255, 255), height=40, text="LYRICS")
        if event.type == pygame.MOUSEMOTION:
            if lyric_button.isOver(mouse_pos):
                lyric_button.color = (150, 150, 255)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if lyric_button.isOver(mouse_pos):
                render = lyrics_page()
        lyric_button.draw(screen)

        # BUTTON 4
        quote_button = button(
            color=(14, 14, 192), x=285, y=660, width=230, height=40, font_color=(255, 255, 255), text="QUOTES")
        if event.type == pygame.MOUSEMOTION:
            if quote_button.isOver(mouse_pos):
                quote_button.color = (150, 150, 255)
        quote_button.draw(screen)

        # BUTTON 5
        suggestion_button = button(
            color=(14, 14, 192), x=280, y=730, width=240, height=40, font_color=(255, 255, 255), text="SIMILAR")
        if event.type == pygame.MOUSEMOTION:
            if suggestion_button.isOver(mouse_pos):
                suggestion_button.color = (150, 150, 255)
        suggestion_button.draw(screen)

        # RANDOM TIP
        global main_screen_tip
        display_text(screen, center=True, text=main_screen_tip, x=20, y=800)

# MAIN GUI END


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
