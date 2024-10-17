from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import speech_recognition as sr
import pyttsx3

audio = sr.Recognizer()
maquina = pyttsx3.init()

class bot():
    def __init__(self,username,password):
        try:
            self._username = username
            self._password = password
            options = webdriver.ChromeOptions()
            options.add_argument("--headless=new")
            self.navegar = webdriver.Chrome()
            self.navegar.get('https://www.instagram.com/')
            sleep(5)
            username_elemento = self.navegar.find_element(By.NAME,'username')
            username_elemento.clear
            username_elemento.send_keys(self._username)
            sleep(3)
            password_elemento = self.navegar.find_element(By.NAME,'password')
            password_elemento.clear
            password_elemento.send_keys(self._password)
            sleep(3)
            entry_elemento = self.navegar.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]/button/div')
            entry_elemento.click()
            #não salvar informaçoes
            sleep(8)
            nao_salvar_info = self.navegar.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div')
            nao_salvar_info.click()
            sleep(10)
            #não ativar notificaçoes
            nao_ativar_notici = self.navegar.find_element(By.XPATH,'/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
            nao_ativar_notici.click()
            sleep(3)
        except:
            maquina.say("Não consegui acessar o seu instagram")
            maquina.runAndWait()
    def direct(self):
        #ver se tem mensagem
        try:
            self.__init__
            responder = self.navegar.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[5]/div/div/div/span/div/a/div/div[1]/div/div[2]/div/span')
            responder.click()
            sleep(2)
            while True:
                tem_msg_ativa = self.navegar.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div[1]/div/div/div/div/div[3]/div/div/span')
                tem_msg_ativa.click()
                sleep(3)
                self.mandar_mensa
        except:
            maquina.say('Não tem mensagem')
            maquina.runAndWait()
    def mandar_mensa(self):
        #mensagem
        try:
            self.direct
            mandar_msg = self.navegar.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]')
            mandar_msg.clear
            mandar_msg.send_keys('dps o kauã te responde')
            sleep(4)
            enviar_msg = self.navegar.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[3]')
            enviar_msg.click()
            sleep(3)
            maquina.say('Respondi o direct')
            maquina.runAndWait()
        except:
            maquina.say('Não tem mensagem no momento')
            maquina.runAndWait()

def direct_msg():
    bot1 = bot('email','senha')
    bot1.mandar_mensa()