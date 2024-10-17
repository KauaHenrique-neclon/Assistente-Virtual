from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import speech_recognition as sr
import pyttsx3

audio = sr.Recognizer()
maquina = pyttsx3.init()

class bot_facebook():
    #entrando no facebook
    def __init__(self,username,password):
            self._username = username
            self._password = password
            options = webdriver.ChromeOptions()
            options.add_argument("--headless=new")
            self.navegar = webdriver.Chrome(options=options)
            self.navegar.get('https://www.facebook.com/')
            sleep(5)
            username_elemento = self.navegar.find_element(By.NAME,'email')
            username_elemento.clear
            username_elemento.send_keys(self._username)
            sleep(3)
            password_elemento = self.navegar.find_element(By.NAME,'pass')
            password_elemento.clear
            password_elemento.send_keys(self._password)
            sleep(3)
            entry_elemento = self.navegar.find_element(By.NAME,'login')
            entry_elemento.click()
            #entrar 
            sleep(10)
            tirar_tela_branca = self.navegar.find_element(By.XPATH,'/html/body/div[5]/div[1]/div/div[2]')
            tirar_tela_branca.click()
            sleep(10)
            maquina.say('Acessei seu facebook')
            maquina.runAndWait()
        #storys
    def story(self):
        try:
            self.__init__
            #ver storys
            ver_story = self.navegar.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div/a/div/div/div[2]/div/div[1]')
            ver_story.click()
            sleep(5)
            story_da_pessoa = self.navegar.find_element(By.CSS_SELECTOR,'#viewer_dialog > div > div > div > div.x1iyjqo2.x1n2onr6 > div > div > div > div.x6s0dn4.x78zum5.xdt5ytf.x5yr21d.xl56j7k.x10l6tqk.x17qophe.x13vifvy.xh8yej3 > div.x6s0dn4.x78zum5.x1q0g3np.x5yr21d.xl56j7k.xh8yej3 > div:nth-child(3) > div > div > div.x1i10hfl.x1ypdohk.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x16tdsg8.x1hl2dhg.xggy1nq.x87ps6o.x1lku1pv.x1a2a7pz.x6s0dn4.x1jx94hy.x1exxf4d.x1y71gwh.x1nb4dca.xu1343h.x14yjl9h.xudhj91.x18nykt9.xww2gxu.x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x178xt8z.xm81vs4.xso031l.xy80clv.x9f619.xi81zsa.x78zum5.xsdox4t.xl56j7k.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x1useyqa')
            sleep(1)
            while True:
                    story_da_pessoa.click()
        except:
            maquina.say('todos os story foram vistos')
            maquina.runAndWait()
        #mensseger
    def mensagem(self):
        try:
            self.__init__
            messenger = self.navegar.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[2]/div[5]/div[1]/div[2]/span/span/div/div[1]')
            messenger.click()
            sleep(2)
            while True:
                tem_msg_ativa = self.navegar.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[2]/div[5]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/div/div/div[1]/div[3]/div/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div/div/div/a/div[1]/div/div[3]/div/div/div/span')
                tem_msg_ativa.click()
                sleep(3)
                self.mandar_mensa
        except:
            maquina.say('Não tem mensagem')
            maquina.runAndWait()
        #mandar mensagem 
    def mandar_mensa(self):
        try:
            self.mensagem
            try:
                while True:
                    escrever_msg = self.navegar.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[5]/div[1]/div[1]/div[1]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div[5]/div/div[1]/div[1]/p')
                    escrever_msg.clear
                    escrever_msg.send_keys('Quando der,Kauã vai te responder')
                    sleep(3)
                    escrever_msg.send_keys(Keys.ENTER)
                    sleep(3)
            except:
                maquina.say('Respondi a caixa de mensagem')
                maquina.runAndWait()
        except:
            maquina.say('Não tem mensagem no momento')
            maquina.runAndWait()

def bot_story():
    bot1 = bot_facebook('email','senha')
    bot1.story()

#ainda não terminado
def bot_mandar_msg():
    bot2 = bot_facebook('email','senha')
    bot2.mandar_mensa()