import os.path
import pygame
import pygame.locals as pl
pygame.font.init()


# GUI BUTTON START
class button():
    def __init__(self, color, x, y, width, height, text='', font_color=(0, 0, 0), font_size=25):
        self.color = color
        self.font_size = font_size
        self.font_color = font_color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        if self.text != '':
            font = pygame.font.SysFont('comicsansms', self.font_size)
            self.text = font.render(self.text, 1, font_color)

    def draw(self, win, outline=None):
        if outline:
            pygame.draw.rect(win, outline, (self.x-2, self.y -
                             2, self.width+4, self.height+4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y,
                         self.width, self.height), 0)

        win.blit(self.text, (self.x + (self.width/2 - self.text.get_width()/2),
                             self.y + (self.height/2 - self.text.get_height()/2)))

    def isOver(self, pos):
        if (
            pos[0] > self.x
            and pos[0] < (self.x + self.width)
            and pos[1] > self.y
            and pos[1] < (self.y + self.height)
        ):
            return True

        return False
# GUI BUTTON END


# GUI DISPLAY TEXT START
class display_text:
    def __init__(self, screen, center=False, text="", x=0, y=0, max_width=0, max_height=0, font_family="comicsansms", font_size=17, font_color=(255, 255, 255)):
        self.font_size = font_size
        limit = 3
        flag = 1
        while limit:
            limit -= 1
            try:
                myfont = pygame.font.SysFont(font_family, self.font_size)
                label = myfont.render(text, True, font_color)
                if (label.get_rect().width) < 780:
                    if center:
                        x = (screen.get_size()[0]//2) - \
                            (label.get_rect().width//2)
                        screen.blit(label, (x, y))
                    else:
                        screen.blit(label, (x, y))
                else:
                    pos = (x, y)
                    words = [word.split(' ') for word in text.splitlines()]
                    space = myfont.size(' ')[0]
                    if max_width == 0:
                        max_width = screen.get_size()[0]
                        max_width -= x
                    if max_height == 0:
                        max_height = screen.get_size()[1]

                    for line in words:
                        for word in line:
                            label = myfont.render(word, 0, font_color)
                            word_width, word_height = label.get_size()
                            if x + word_width >= max_width:
                                x = pos[0]  # - (label.get_rect().width//2)
                                y += word_height
                            screen.blit(label, (x, y))
                            x += word_width + space
                        x = pos[0]  # - (label.get_rect().width//2)
                        y += word_height
                flag = 0
                break
            except:
                self.font_size -= 2
        if flag:
            myfont = pygame.font.SysFont(font_family, font_size)
            x, y = 400, 525
            label = myfont.render(
                "Can not load this, Sorry!", True, font_color)
            x = (screen.get_size()[0]//2)-(label.get_rect().width//2)
            screen.blit(label, (x, y))


# GUI DISPLAY TEXT END


# GUI INPUT TEXT START
class input_text:
    def __init__(
            self,
            initial_string="",
            font_family="comicsansms",
            font_size=20,
            antialias=True,
            text_color=(255, 255, 255),
            cursor_color=(0, 0, 1),
            repeat_keys_initial_ms=400,
            repeat_keys_interval_ms=35,
            max_string_length=-1,
            password=False):

        self.antialias = antialias
        self.text_color = text_color
        self.font_size = font_size
        self.max_string_length = max_string_length
        self.password = password
        self.input_string = initial_string

        if not os.path.isfile(font_family):
            font_family = pygame.font.match_font(font_family)

        self.font_object = pygame.font.Font(font_family, font_size)

        self.surface = pygame.Surface((1, 1))
        self.surface.set_alpha(0)

        self.keyrepeat_counters = {}
        self.keyrepeat_intial_interval_ms = repeat_keys_initial_ms
        self.keyrepeat_interval_ms = repeat_keys_interval_ms

        self.cursor_surface = pygame.Surface(
            (int(self.font_size / 20 + 1), self.font_size))
        self.cursor_surface.fill(cursor_color)
        self.cursor_position = len(initial_string)
        self.cursor_visible = True
        self.cursor_switch_ms = 250
        self.cursor_ms_counter = 0
        self.active = False
        self.clock = pygame.time.Clock()

    def update(self, events):
        if self.active:
            for event in events:
                if event.type == pygame.KEYDOWN:
                    self.cursor_visible = True

                    if (
                        event.key not in self.keyrepeat_counters
                        and not event.key == pl.K_RETURN
                    ):
                        self.keyrepeat_counters[event.key] = [
                            0, event.unicode]

                    if event.key == pl.K_BACKSPACE:
                        self.input_string = (
                            self.input_string[:max(
                                self.cursor_position - 1, 0)]
                            + self.input_string[self.cursor_position:]
                        )

                        self.cursor_position = max(self.cursor_position - 1, 0)
                    elif event.key == pl.K_DELETE:
                        self.input_string = (
                            self.input_string[:self.cursor_position]
                            + self.input_string[self.cursor_position + 1:]
                        )

                    elif event.key == pl.K_RETURN:
                        return True

                    elif event.key == pl.K_RIGHT:
                        self.cursor_position = min(
                            self.cursor_position + 1, len(self.input_string))

                    elif event.key == pl.K_LEFT:
                        self.cursor_position = max(self.cursor_position - 1, 0)

                    elif event.key == pl.K_END:
                        self.cursor_position = len(self.input_string)

                    elif event.key == pl.K_HOME:
                        self.cursor_position = 0

                    elif len(self.input_string) < self.max_string_length or self.max_string_length == -1:
                        self.input_string = (
                            self.input_string[:self.cursor_position]
                            + event.unicode
                            + self.input_string[self.cursor_position:]
                        )
                        self.cursor_position += len(event.unicode)

                elif (
                    event.type == pl.KEYUP
                    and event.key in self.keyrepeat_counters
                ):
                    del self.keyrepeat_counters[event.key]

            for key in self.keyrepeat_counters:
                self.keyrepeat_counters[key][0] += self.clock.get_time()

                if self.keyrepeat_counters[key][0] >= self.keyrepeat_intial_interval_ms:
                    self.keyrepeat_counters[key][0] = (
                        self.keyrepeat_intial_interval_ms
                        - self.keyrepeat_interval_ms
                    )

                    event_key, event_unicode = key, self.keyrepeat_counters[key][1]
                    pygame.event.post(pygame.event.Event(
                        pl.KEYDOWN, key=event_key, unicode=event_unicode))

            string = self.input_string
            if self.password:
                string = "*" * len(self.input_string)
            self.surface = self.font_object.render(
                string, self.antialias, self.text_color)

            self.cursor_ms_counter += self.clock.get_time()
            if self.cursor_ms_counter >= self.cursor_switch_ms:
                self.cursor_ms_counter %= self.cursor_switch_ms
                self.cursor_visible = not self.cursor_visible

            if self.cursor_visible:
                cursor_y_pos = self.font_object.size(
                    self.input_string[:self.cursor_position])[0]
                if self.cursor_position > 0:
                    cursor_y_pos -= self.cursor_surface.get_width()
                self.surface.blit(self.cursor_surface, (cursor_y_pos, 0))

            self.clock.tick()
            return False

        return None

    def get_surface(self):
        return self.surface

    def get_text(self):
        return self.input_string

    def get_cursor_position(self):
        return self.cursor_position

    def set_text_color(self, color):
        self.text_color = color

    def set_cursor_color(self, color):
        self.cursor_surface.fill(color)

    def clear_text(self):
        self.input_string = ""
        self.cursor_position = 0
# GUI INPUT TEXT END
