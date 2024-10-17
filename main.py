import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import os
import webbrowser
import random
import pyautogui
from translate import Translator
from time import sleep
import sqlite3
from noticias import *
from POO_insta import direct_msg
from facebook import bot_story

audio = sr.Recognizer()
maquina = pyttsx3.init()

def executa_comando():
    comando = ""
    try:
        with sr.Microphone() as source: #import pyaudio para microfone
            audio.adjust_for_ambient_noise(source)
            print("ouvindo...")
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()

            if 'Vivianny' in comando:
                comando = comando.replace('Vivianny','')
                maquina.say(comando)
                maquina.runAndWait()
    except:
        print('Microfone não está funcionando')
    return comando

def comando_voz_usuario():
    while True:
        comando = executa_comando()
        if 'horas' in comando:
            hora = datetime.datetime.now().strftime('%H:%M')
            maquina.say('Agora são' + hora)
            maquina.runAndWait()
        elif 'hoje é que dia' in comando:
            hoje = datetime.datetime.now().day
            maquina.say("hoje é dia" + hoje)
            maquina.runAndWait()
        elif 'qual é o mês' in comando:
           mês = comando
           mês = datetime.datetime.now().month
           maquina.say("estamos no mês" + mês)
           maquina.runAndWait()
    #whatssap
        elif "whatts" in comando:
            resultado = os.open("C:/Users/ADM/Desktop/WhatsApp.lnk")
            maquina.say("aberto")
            maquina.runAndWait()
        elif 'mandar mensagem' in comando:
            if 'foi':
                maquina.say('Mandar para quem?')
                maquina.runAndWait()
                with sr.Microphone() as source:
                   voz = audio.listen(source)
                   fala = audio.recognize_google(voz, language='pt-BR')
                   fala = fala.lower()
                   nome = fala
                maquina.say('Qual mensagem')
                maquina.runAndWait()
                with sr.Microphone() as source:
                   voz = audio.listen(source)
                   fala2 = audio.recognize_google(voz, language='pt-BR')
                   fala2 = fala2.lower()
                   msg = fala2
            sleep(1)
            pyautogui.click(678,750)
            sleep(1)
            pyautogui.press("ctrl" + "f")
            sleep(3)
            pyautogui.write(nome)
            sleep(3)
            pyautogui.press("Tab")
            sleep(3)
            pyautogui.press("enter")
            sleep(3)
            pyautogui.write(msg)
            sleep(3)
            pyautogui.press("enter")
            sleep(3)
            maquina.say('Mensagem enviada')
            maquina.runAndWait()
    #comando de pesquisas
        elif 'procure por' in comando:
            procurar = comando.replace('procure por', '')
            wikipedia.set_lang('pt')
            resultado = wikipedia.summary(procurar,2)
            maquina.say(resultado)
            maquina.runAndWait()
    #programa
        elif 'editor' in comando:
            os.system('C:/Users/ADM/Desktop/CapCut.lnk')
            maquina.say('Editor acessado')
            maquina.runAndWait()
        elif 'Bloco de notas' in comando:
            os.system('%windir%/system32/notepad.exe')
            maquina.say('Bloco de notas aberto')
            maquina.runAndWait()
    #comando para tocar musica
        elif 'tocar' in comando:
            musica = comando.replace('tocar','')
            resultado = pywhatkit.playonyt(musica)
            maquina.say('Tocando musica')
            maquina.runAndWait()
        elif 'toque' in comando:
            musica1 = comando.replace('toque','')
            resultado = pywhatkit.playonyt(musica1)
            maquina.say('Tocando musica')
            maquina.runAndWait()
    #sites do google
        elif 'canal do youtube' in comando:
            canal = comando.replace('canal do youtube', '')
            resultadoCanal = pywhatkit.playonyt(canal)
            maquina.say('Encontrado o canal')
            maquina.runAndWait()
        elif 'rede social' in comando:
            facebook = comando
            resultado = webbrowser.open('https://www.facebook.com/')
            maquina.say('facebook acessado')
            maquina.runAndWait()
        elif 'instagram' in comando:
            instagram = comando
            resultado = webbrowser.open('https://www.instagram.com/')
            maquina.say('instagram acessado')
            maquina.runAndWait()
        elif 'epic games' in comando:
            epic = comando
            resultado = webbrowser.open('https://store.epicgames.com/pt-BR/')
            maquina.say('Loja da Epic Games')
            maquina.runAndWait()
        elif 'steam' in comando:
            steam = comando
            resultado = webbrowser.open('https://store.steampowered.com/?l=portuguese')
            maquina.say('Steam aberta')
            maquina.runAndWait()
        elif 'Youtuber' in comando:
            youtuber = comando
            resultado = webbrowser.open('https://www.youtube.com/')
            maquina.say('Youtuber aberto')
            maquina.runAndWait()
     #musicas,playlist e acesso 
        elif 'playlist brasileira' in comando:
            resultado = webbrowser.open('https://www.youtube.com/watch?v=HjRxaC1lmXI&list=PLiD4JTEjcZ1aWCav2fXEbPoPHVILlQsnG&index=1')
            maquina.say('Playlist Br aberta')
            maquina.runAndWait()
        elif 'playlist inglês' in comando:
            resultado = webbrowser.open('https://www.youtube.com/watch?v=m7Bc3pLyij0&list=PLiD4JTEjcZ1ZrvRDv7NHbiplBIPlJgVzx&index=1')
            maquina.say('Playlist inglês aberta')
            maquina.runAndWait()
        elif 'melhor playlist' in comando:
            resultado = webbrowser.open('https://www.youtube.com/watch?v=vJfLCkf2FZE&list=PLiD4JTEjcZ1b6PIO6jKaRRqfQRnHp411b&index=1')
            maquina.say('Playlist Trap The Fato')
            maquina.runAndWait()
        elif 'conte uma piada' in comando: #piadas
            piada = comando
            piadas = [ 'Qual é o lugar mais certo do Brasil? O sertão' , 'Qual é a comida mais devagar?... A po-lente' ,
                'Você sabe por que a água foi presa?... Porque ela matou a sede' ,
                'Qual a cidade brasileira que não tem táxi?... Uberlândia.' , 'Qual a fórmula da água benta?... H Deus O' , 
                'Qual o contrário de papelada?... Pá vestida' , 'Contei uma piada química... não teve reação' , 
                'Como o Batman conheceu o Robin?... Pelo bat-papo' , 'Você sabe quem é o rei dos queijos?... É o reiqueijão'
                , 'Quem é a mãe do mingau?... A mãe zena' , 'Qual é a parte mais velha do carro?... O vô-lante' ,
                'Qual é o país que mais produz vinho?... Uva-ticano' , 'O que o azeite disse para o vinagre?...“Falo nada, só óleo”'
                , 'Qual é o esporte preferido dos músicos?...Lançamento de disco' , 'Que animal já passou da validade?...O javali'
                , 'O que a lâmpada falou quando a ligaram?...“Tô ligada”' , 'O que o lápis disse para o apontador?...“Estou desapontado”'
                , 'Por que a loja do canivete faliu?...Porque só vendia a-fiado' , 'Qual é a peça de carro que é feita só no Egito?...Os faraóis'
                , 'O que o cadarço falou para o tênis?...“Estou amarradão em você”']
            piada_escolhida = random.choice(piadas)
            maquina.say(piada_escolhida)
            maquina.runAndWait()
        #comandos de fala educadas 
        elif 'boa noite' in comando:
            maquina.say('Boa Noite Kauã')
            maquina.runAndWait()
        elif 'boa tarde' in comando:
            maquina.say('Boa tarde Kauã')
            maquina.runAndWait()
        elif 'bom dia' in comando:
            dia = comando
            maquina.say('Bom Dia Kauã')
            maquina.runAndWait()
        elif 'se apresenta' in comando:
            maquina.say('Sou vivianny,assistente virtual do kauã')
            maquina.runAndWait()
        elif 'desligar' in comando:
            break
        elif 'senha' in comando:
            maquina.say('senha é Haykaua511?')
            maquina.runAndWait()
        elif 'parar' in comando:
            break
        elif 'traduzir' in comando:
                maquina.say('o que quer traduzir para o Ingles')
                maquina.runAndWait()
                with sr.Microphone() as source:
                    voz = audio.listen(source)
                    fala = audio.recognize_google(voz, language='pt-BR')
                    fala = fala.lower()
                s = Translator(from_lang="Pt-Br", to_lang="English")
                resultado = s.translate(fala)
                maquina.say(resultado)
                maquina.runAndWait()
        elif 'noticia' in comando:
            maquina.say('Qual? tenho noticia sobre jogos,sobre o mundo,sobre anime, sobre tempo')
            maquina.runAndWait()
            qual = comando.replace('')
            if 'jogos' 'games' in comando:
                jogos()
            elif 'Tempo' 'previsão do tempo' in comando:
                tempo()
            elif 'mundo' 'planeta' in comando:
                noticia_mundo()
            elif 'animes' in comando:
                noticia_animes()
            else:
                maquina.say('Não entendi')
                maquina.runAndWait()
        elif 'responda o direct' in comando:
            direct_msg()
        elif 'veja o story do facebook' in comando:
            bot_story()
        else:
            maquina.say('')
            maquina.runAndWait()