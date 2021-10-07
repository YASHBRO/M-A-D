from lyricsgenius import Genius
import requests
import sys
import random
import json
import subprocess
from pytube import YouTube


with open('Assets\\credentials.json', 'r') as f:
    data = json.loads(f.read())

if data["first_run"] is True:
    try:
        subprocess.run("pip install -r Assets\\requirements.txt",
                       shell=True, check=True)
    except:
        subprocess.run("pip install -r requirements.txt",
                       shell=True, check=True)
    data["first_run"] = False
    with open('Assets\\credentials.json', 'w') as f:
        f.write(json.dumps(data))


def download_image(url):
    response = requests.get(url)
    name = "-".join(url.split("/")[2:])
    with open(f"temp\{name}.png", "wb") as f:
        f.write(response.content)
    return name+'.png'


class Anime:
    def random_quotes(self):
        url = "https://animechan.vercel.app/api/random"
        response = requests.get(url)
        cont = response.content.decode()
        return json.loads(cont)

    def quote_by_anime(self, name):
        url = f"https://animechan.vercel.app/api/quotes/anime?title={name}"
        response = requests.get(url)
        cont = response.content.decode()
        return random.choice(json.loads(cont))

    def quote_by_character(self, name):
        url = f"https://animechan.vercel.app/api/quotes/character?name={name}"
        response = requests.get(url)
        cont = response.content.decode()
        return random.choice(json.loads(cont))


class Suggestion:
    def __init__(self):
        self.key = "409313-MAP-WUR9L2ML"

    def similar(self, name, category=''):
        if category == '':
            url = f"https://tastedive.com/api/similar?q={name}&info=1&k={self.key}"
        else:
            url = f"https://tastedive.com/api/similar?q={name}&type={category}&info=1&k={self.key}"
        response = requests.get(url)
        cont = response.content.decode()
        data = json.loads(cont)["Similar"]
        if data['Info'][0]['Type'] == 'unknown':
            return 0
        return data


class Facts:
    def random_facts(self):
        url = "https://uselessfacts.jsph.pl/random.json?language=en"
        response = requests.get(url)
        cont = response.content.decode()
        return json.loads(cont)['text']


class Poem:
    def random_poem(self):
        response = requests.get("https://poetrydb.org/random")
        cont = response.content.decode()
        return json.loads(cont)[0]

    def poem_by_author(self, name):
        response = requests.get(f"https://poetrydb.org/author,random/{name};1")
        cont = response.content.decode()
        return json.loads(cont)[0]

    def poem_by_title(self, name):
        response = requests.get(f"https://poetrydb.org/title,random/{name};1")
        cont = response.content.decode()
        return json.loads(cont)[0]

    def download_poem(self, text):
        with open(text["title"]+".txt", 'w') as f:
            poem_file_text = text["title"]+'\n\t'+'-' + \
                text["author"]+'\n\n'+"\n".join(text["lines"])
            f.write(poem_file_text)


class Lyrics:
    def __init__(self):
        self.genius = Genius(data["geniusAPI"]["token"])

    def searchLyrics(self, name):
        try:
            song, artist = (name.strip()).split(',')
        except:
            song, artist = name.strip(), ""

        self.song = self.genius.search_song(song, artist)
        song_info = {"title": self.song.title, "artist": self.song.artist, "lyrics": self.song.lyrics,
                     "thumbnail": self.song.song_art_image_thumbnail_url, "linecount": (self.song.lyrics).count('\n')}
        return song_info

    def serachSongByLyrics(self, lyr):
        request = self.genius.search_lyrics(lyr)
        ans = []
        for hit in request['sections'][0]['hits']:
            ans.append((hit['result']['full_title']).split(' by'))
        return ans

    def saveLyrics(self, songName, songLyrics):
        with open(f'{songName }.txt', 'w') as f:
            f.write(songLyrics)


class Songs:
    def findLink(self, name):
        url = 'https://www.youtube.com/results?q=' + name
        count = 0
        cont = requests.get(url)
        data = str(cont.content)
        lst = data.split('"')
        for i in lst:
            count += 1
            if i == 'WEB_PAGE_TYPE_WATCH':
                break
        if lst[count-5] == "/results":
            raise Exception("No video found.")
        return "https://www.youtube.com"+lst[count-5]

    def playOnYT(self, name):
        link = Songs().findLink(name)
        subprocess.run(f"start {link}", shell=True, check=True)

    def show_progress_bar(self, stream, _chunk, bytes_remaining):
        current = ((stream.filesize - bytes_remaining)/stream.filesize)
        percent = ('{0:.1f}').format(current*100)
        progress = int(50*current)
        status = '█' * progress + '-' * (50 - progress)
        sys.stdout.write(' ↳ [{bar}] {percent}%\r'.format(
            bar=status, percent=percent))
        sys.stdout.flush()

    def downloadVideo(self, name):
        link = Songs().findLink(name)
        yt = YouTube(link)
        yt.register_on_progress_callback(Songs().show_progress_bar)
        yt.streams.filter(progressive=True).get_highest_resolution().download()
        return yt.title, yt.thumbnail_url

    def downloadAudio(self, name):
        link = Songs().findLink(name)
        yt = YouTube(link)
        yt.register_on_progress_callback(Songs().show_progress_bar)
        yt.streams.get_audio_only().download()
        return yt.title, yt.thumbnail_url


class Advice:
    def gen_advice(self):
        link = 'https://api.adviceslip.com/advice'
        request = requests.get(link)
        return json.loads(request.content.decode())['slip']['advice']


class Quotes:
    def random_quotes(self):
        url = "https://api.quotable.io/random"
        response = requests.get(url)
        cont = response.content.decode()
        return json.loads(cont)


class Joke:
    def get_joke(self):
        link = 'https://icanhazdadjoke.com/slack'
        request = requests.get(link)
        return json.loads(request.content.decode())['attachments'][0]['text']


if __name__ == "__main__":
    pass
