import speech_recognition as sr
import pyttsx3
import requests
import bs4

audio = sr.Recognizer()
maquina = pyttsx3.init()

def jogos(): #tive que criar uma função para chamar no app noticias
    url = 'https://br.ign.com/ps5'
    requisicao =  requests.get(url)
    pagina = bs4.BeautifulSoup(requisicao.text, "html.parser")
    lista_noticia = pagina.find_all("h3", class_="caption")
    for noticia in lista_noticia:
        noticia2 = noticia
        maquina.say(noticia2.text)
        maquina.runAndWait()
        maquina.say('Proxima')
        maquina.runAndWait()

def tempo():
    url = 'https://www.tempo.com/serra_espirito-santo-l114534.htm'
    requisicao =  requests.get(url)
    pagina = bs4.BeautifulSoup(requisicao.text, "html.parser")
    lista_noticia = pagina.find_all("span", class_="zona-color noche-nuevo row --izq")
    for noticia in lista_noticia:
        noticia4 = noticia
        maquina.say('clima da Serra é' + noticia4.text)
        maquina.runAndWait()

def noticia_mundo():
    url = 'https://www.gazetadopovo.com.br/mundo/'
    requisicao =  requests.get(url)
    pagina = bs4.BeautifulSoup(requisicao.text, "html.parser")
    lista_noticia = pagina.find_all("a", class_="trigger-gtm")
    for noticia in lista_noticia:
        noticia3 = noticia
        maquina.say(noticia3.text)
        maquina.runAndWait()
        maquina.say('Proxima')
        maquina.runAndWait()

def noticia_animes():
    url = 'https://animenew.com.br/noticias/'
    requisicao =  requests.get(url)
    pagina = bs4.BeautifulSoup(requisicao.text, "html.parser")
    lista_noticia = pagina.find_all("a", class_="p-url")
    for noticia in lista_noticia:
        noticia6 = noticia
        maquina.say(noticia6.text)
        maquina.runAndWait()
        maquina.say('Proxima')
        maquina.runAndWait()
