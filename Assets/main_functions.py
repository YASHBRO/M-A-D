from lyricsgenius import Genius
import requests,webbrowser as web
import sys, random
import json
from pytube import YouTube



with open(r'Assets\Cred.json','r') as f:
    data=json.loads(f.read())



def download_image(url):
    response = requests.get(url)
    name="-".join(url.split("/")[2:-1])
    with open(f"temp\{name}.png","wb") as f:
        f.write(response.content)
    return name



class Anime:
    def random_quotes(self):
        url="https://animechan.vercel.app/api/random"
        response=requests.get(url)
        cont=response.content.decode()
        return json.loads(cont)
    
    def quote_by_anime(self,name):
        url=f"https://animechan.vercel.app/api/quotes/anime?title={name}"
        response=requests.get(url)
        cont=response.content.decode()
        return random.choice(json.loads(cont))
    
    def quote_by_character(self,name):
        url=f"https://animechan.vercel.app/api/quotes/character?name={name}"
        response=requests.get(url)
        cont=response.content.decode()
        return random.choice(json.loads(cont))



class Suggestion:
    def __init__(self):
        self.key="409313-MAP-WUR9L2ML"
    
    def similar(self,name,category):
        url=f"https://tastedive.com/api/similar?q={name}&type={category}&info=1&k={self.key}"
        response=requests.get(url)
        cont=response.content.decode()
        data=json.loads(cont)["Similar"]
        if data['Info'][0]['Type']=='unknown':
            return 0
        return data



class Facts:
    def random_facts(self):
        url="https://uselessfacts.jsph.pl/random.json?language=en"
        response=requests.get(url)
        cont=response.content.decode()
        return json.loads(cont)['text']



class Poem:
    def random_poem(self):
        response=requests.get("https://poetrydb.org/random")
        cont=response.content.decode()
        return json.loads(cont)[0]



class Lyrics:
    def __init__(self):
        super().__init__()
        self.genius = Genius('WzjUkhMwHMY-BeG1T48JOSJKAuu5xR7MljxiM8VRI6GibJ19gDQm2cp7_Q5aLbx2')
    
    def searchSong(self,song,artist=''):
        if artist!='':
            try:
                request = requests.get(f'https://api.lyrics.ovh/v1/{artist}/{song}')
                return (json.loads(request.content.decode())['lyrics'])
            except:
                pass
        self.song = self.genius.search_song(song, artist)
        return song.lyrics
    
    def serachSongByLyrics(self,lyr):
        request = self.genius.search_lyrics(lyr)
        ans=[]
        for hit in request['sections'][0]['hits']:
            ans.append(hit['result']['title'])
        return ans

    def saveLyrics(self,soneName,songLyrics):
        with open(f'{soneName}.txt','w') as f:
            f.write(songLyrics)



class Songs:
    def findLink(self,name):
        url = 'https://www.youtube.com/results?q=' + name
        count = 0
        cont = requests.get(url)
        data = str(cont.content)
        lst = data.split('"')
        for i in lst:
            count+=1
            if i == 'WEB_PAGE_TYPE_WATCH':
                break
        if lst[count-5] == "/results":
            raise Exception("No video found.")
        return "https://www.youtube.com"+lst[count-5]
    
    def playOnYT(self,name):
        link=Songs().findLink(name)
        web.open(link)
    
    def show_progress_bar(self,stream, _chunk, bytes_remaining):
        current = ((stream.filesize - bytes_remaining)/stream.filesize)
        percent = ('{0:.1f}').format(current*100)
        progress = int(50*current)
        status = '█' * progress + '-' * (50 - progress)
        sys.stdout.write(' ↳ [{bar}] {percent}%\r'.format(bar=status, percent=percent))
        sys.stdout.flush()
    
    def downloadVideo(self,name):
        link=Songs().findLink(name)
        yt = YouTube(link)
        yt.register_on_progress_callback(Songs().show_progress_bar)
        yt.streams.filter(progressive=True).get_highest_resolution().download()
        return yt.title,yt.thumbnail_url
                
    
    def downloadAudio(self,name):
        link=Songs().findLink(name)
        yt=YouTube(link)
        yt.register_on_progress_callback(show_progress_bar)
        yt.streams.get_audio_only().download()
        return yt.title,yt.thumbnail_url



class Advice:
    def gen_advice(self):
        link='https://api.adviceslip.com/advice'
        request = requests.get(link)
        return (json.loads(request.content.decode())['slip']['advice'])



class Joke:
    def get_joke(self):
        link='https://icanhazdadjoke.com/slack'
        request = requests.get(link)
        return (json.loads(request.content.decode())['attachments'][0]['text'])

