import tkinter
#import psycopg2
import customtkinter
from customtkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import speech_recognition as sr
import pyttsx3
import sqlite3
from noticias import *
from main import comando_voz_usuario
from facebook import bot_story
import facebook

audio = sr.Recognizer()
maquina = pyttsx3.init()

class interface(facebook):
    def __init__(self):
        self.janela1 = tkinter.Tk()  #criar janela janela 1
        self.janela1.geometry("400x240")
        self.janela1.title("Login Vivianny")
        self.janela1.iconbitmap(r"C:/vivianny/patas.ico")
        self.janela1.resizable(width=False, height=False)
        text1 = customtkinter.CTkLabel(master=self.janela1,text="Senha",height=20)
        text1.place(relx=0.5,rely=0.1, anchor=tkinter.CENTER)
        self.senha = customtkinter.CTkEntry(master=self.janela1,corner_radius=10,width=150,height=30,show="*")
        self.senha.place(relx=0.5,rely=0.3, anchor=tkinter.CENTER)
        button = customtkinter.CTkButton(master=self.janela1,text="Entrar", corner_radius=10,command=self.verificar)
        button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        button_esqueci = customtkinter.CTkButton(master=self.janela1,text='Esqueceu senha',width=160,height=30,corner_radius=10, command=self.esqueceu)
        button_esqueci.place(relx=0.3, rely=0.7)
    def verificar(self): #codigo de verificação de senha
        if self.senha.get() == '5115':
            messagebox.showinfo('acesso permitido','Seja bem vindo Kauã')
            self.janela1.destroy()
            self.segunda()
        elif self.senha.get() == '2902':
            messagebox.showinfo('acesso permitido','Seja bem vindo Duda')
            self.janela1.destroy()
            self.segunda()
        elif self.senha.get() == '1201':
            messagebox.showinfo('acesso permitido','Seja bem vindo Sullivan')
            self.janela1.destroy()
            self.segunda()
        else:
            messagebox.showwarning('Acesso negado','Tente novamente')
    def esqueceu(self): #janela de recuperação de senha
        self.janelaES = tkinter.Tk()
        self.janela1.destroy()
        self.janelaES.geometry("400x240")
        self.janelaES.title("Recuperar Senha")
        self.janelaES.iconbitmap(r"C:/vivianny/patas.ico")
        self.janelaES.resizable(width=False, height=False)
        self.janelaES.configure(background="#ffffff")
        #criação da janela
        label_pedido = customtkinter.CTkLabel(master=self.janelaES,width=400,height=30,text='Entra com sua cidade natal')
        label_pedido.place(rely=0.2)
        self.entry_pedido = customtkinter.CTkEntry(master=self.janelaES,corner_radius=10,fg_color="#cdd0d6")
        self.entry_pedido.place(relx=0.33, rely=0.5)
        button_pedido = customtkinter.CTkButton(master=self.janelaES,width=150,height=30,text='Recuperar',command=self.esque_recu,corner_radius=5, bg="#cdd0d6")
        button_pedido.place(relx=0.29,rely=0.7)

    def esque_recu(self):
        if 'Resplendor' == self.entry_pedido.get():
            messagebox.showinfo('Acesso a senha','Sua senha é 5115')
            self.janelaES.destroy()
            self.__init__
        elif 'Governador Valadares' == self.entry_pedido.get():
            messagebox.showinfo('Acesso a senha','Sua senha é 2902')
            self.janelaES.destroy()
            self.__init__
        elif 'GV' == self.entry_pedido.get():
            messagebox.showinfo('Acesso a senha','Sua senha é 2902')
            self.janelaES.destroy()
            self.__init__
        else:
            messagebox.showwarning('Acesso negado','Sua informações não batem')
    
    def segunda(self):   #janela 2 o menu
        self.janela2 = tkinter.Tk() #janelas 2, o menu 
        self.janela2.geometry("500x400")
        self.janela2.title("Menu Vivianny")
        self.janela2.iconbitmap(r"C:/vivianny/patas.ico")
        self.janela2.resizable(width=False, height=False)
        self.janela2.configure(background="#ffffff")
        #criando
        label_menu = customtkinter.CTkLabel(master=self.janela2,width=100,height=40,text='Menu',text_color="#00a8ff",text_font=("Arial bold",18),fg_color=None,bg_color=None)     
        label_menu.place(relx=0.1,rely=0)
        #frame jornal
        frame_jornal = customtkinter.CTkFrame(master=self.janela2,width=180,height=80,corner_radius=20,bg_color=None,fg_color="#00a8ff")
        frame_jornal.place(relx=0.1,rely=0.7)
        image_icon = Image.open(r"C:/vivianny/icone/icone_jornal.ico")
        #converter a image
        tk_image = ImageTk.PhotoImage(image_icon)
        icone_jornal = customtkinter.CTkButton(master=frame_jornal,image=tk_image,width=50,height=50,hover_color=None,bg_color=None,fg_color=None)
        icone_jornal.place(relx=0.09,rely=0.2)
        label_jornal = customtkinter.CTkLabel(master=frame_jornal,width=100,height=20,text='Jornal',fg_color=None,bg_color=None,corner_radius=20,text_font=("Arial bold",18))
        label_jornal.place(relx=0.4,rely=0.2)
        button_jornal = customtkinter.CTkButton(master=frame_jornal,width=100,height=20,text='Noticias',hover_color="#00a8ff",fg_color="#ffffff", corner_radius=20,bg_color=None,command=self.noti_cia)
        button_jornal.place(relx=0.4,rely=0.6)
        #frame bot
        frame_bot = customtkinter.CTkFrame(master=self.janela2,width=180,height=80,corner_radius=20,bg_color=None,fg_color="#00a8ff")
        frame_bot.place(relx=0.5,rely=0.7)
        #imagem
        imagem_bot = Image.open(r"C:/vivianny/icone/icone_robot.ico")
        bot_imagem = ImageTk.PhotoImage(imagem_bot)
        icone_bot = customtkinter.CTkButton(master=frame_bot,image=bot_imagem,width=50,height=50,hover_color=None,bg_color=None,fg_color=None)
        icone_bot.place(relx=0.09,rely=0.2)
        label_bot = customtkinter.CTkLabel(master=frame_bot,width=100,height=20,text='Bots',fg_color=None,bg_color=None,text_font=("Arial bold",18))
        label_bot.place(relx=0.4,rely=0.2)
        button_bot = customtkinter.CTkButton(master=frame_bot,width=100,height=20,text='Bot de rede',fg_color="#ffffff",hover_color="#00a8ff",corner_radius=20,bg_color=None,command=bot_story)
        button_bot.place(relx=0.4,rely=0.6)
        #frame ativação
        frame_ativaçao = customtkinter.CTkFrame(master=self.janela2,width=180,height=80,corner_radius=20,bg_color=None,fg_color="#00a8ff")
        frame_ativaçao.place(relx=0.1,rely=0.45)
        imagem_ativação = Image.open(r"C:/vivianny/icone/ativacao.ico")
        imagem_ativar = ImageTk.PhotoImage(imagem_ativação)
        icone_ativar = customtkinter.CTkButton(master=frame_ativaçao,image=imagem_ativar,width=50,height=50,hover_color=None,bg_color=None,fg_color=None)
        icone_ativar.place(relx=0.09,rely=0.2)
        button_ativaçao = customtkinter.CTkButton(master=frame_ativaçao,width=100,height=20,text='Ativar IA',hover_color="#00a8ff",fg_color="#ffffff", corner_radius=20,bg_color=None,command=self.vivizin)
        button_ativaçao.place(relx=0.4,rely=0.6)
        label_ativar = customtkinter.CTkLabel(master=frame_ativaçao,width=100,height=20,text='Ativação',fg_color=None, corner_radius=20,bg_color=None,text_font=("Arial bold",18))
        label_ativar.place(relx=0.4,rely=0.2)
        #frame comando
        imagem_comando = Image.open(r"C:/vivianny/icone/engrenagem.ico")
        imagem_coma = ImageTk.PhotoImage(imagem_comando)
        frame_comando = customtkinter.CTkFrame(master=self.janela2,width=180,height=80,corner_radius=20,bg_color=None,fg_color="#00a8ff")
        frame_comando.place(relx=0.5,rely=0.45)
        icone_comando = customtkinter.CTkButton(master=frame_comando,image=imagem_coma,width=50,height=50,hover_color=None,bg_color=None,fg_color=None)
        icone_comando.place(relx=0.09,rely=0.2)
        button_comando = customtkinter.CTkButton(master=frame_comando,width=100,height=20,text='Comando',hover_color="#00a8ff",fg_color="#ffffff", corner_radius=20,bg_color=None,command=self.comandos_luna)
        button_comando.place(relx=0.4,rely=0.6)
        label_comando = customtkinter.CTkLabel(master=frame_comando,width=100,height=20,text='Comandos',fg_color=None, corner_radius=20,bg_color=None,text_font=("Arial bold",15))
        label_comando.place(relx=0.4,rely=0.2)
        #frame banco de dados
        frame_banco = customtkinter.CTkFrame(master=self.janela2,width=180,height=80,corner_radius=20,bg_color=None,fg_color="#00a8ff")
        frame_banco.place(relx=0.1,rely=0.2)
        imagem_banco = Image.open(r"C:/vivianny/icone/icone_banco.ico")
        imaagem_banco = ImageTk.PhotoImage(imagem_banco)
        icone_banco = customtkinter.CTkButton(master=frame_banco,image=imaagem_banco,width=50,height=50,hover_color=None,bg_color=None,fg_color=None)
        icone_banco.place(relx=0.09,rely=0.2)
        label_banco = customtkinter.CTkLabel(master=frame_banco,width=100,height=20,text='Banco',bg_color=None,fg_color=None,houver_color=None,text_font=("Arial bold",15))
        label_banco.place(relx=0.4,rely=0.2)
        button_banco = customtkinter.CTkButton(master=frame_banco,width=100,height=20,text='Salvar',hover_color="#00a8ff",fg_color="#ffffff", corner_radius=20,bg_color=None,command=self.banco_de_dados)
        button_banco.place(relx=0.4,rely=0.6)

    def noti_cia(self): #janela de noticias
        self.janelano_ti = tkinter.Tk()
        self.janela2.destroy()
        self.janelano_ti.geometry("400x240")
        self.janelano_ti.title("Noticias")
        self.janelano_ti.iconbitmap(r"C:/vivianny/patas.ico")
        self.janelano_ti.resizable(width=False, height=False)
        self.janelano_ti.configure(background="#ffffff")
        frame_noti = customtkinter.CTkFrame(master=self.janelano_ti,width=300,height=220,fg_color="#00a8ff")
        frame_noti.place(relx=0.14,rely=0.05)
        label_noticias_Ps5 = customtkinter.CTkButton(master=frame_noti,width=200,height=30,bg_color=None,fg_color="#ffffff",text='Noticias do Ps5',command=jogos)
        label_noticias_Ps5.place(relx=0.17, rely=0.05)
        button_noticias_Tempo = customtkinter.CTkButton(master=frame_noti,width=200,height=30,bg_color=None,fg_color="#ffffff",text='Noticias do Tempo',command=tempo)
        button_noticias_Tempo.place(relx=0.17,rely=0.2)
        button_noticias_mundo = customtkinter.CTkButton(master=frame_noti,width=200,height=30,fg_color="#ffffff",bg_color=None,text='Noticias sobre Mundo',command=noticia_mundo)
        button_noticias_mundo.place(relx=0.17,rely=0.36)
        button_noticias_futebol = customtkinter.CTkButton(master=frame_noti,width=200,height=30,fg_color="#ffffff",bg_color=None,text='Noticias sobre Anime',command=noticia_animes)
        button_noticias_futebol.place(relx=0.17,rely=0.52)
        label_voltar_noticia = customtkinter.CTkButton(master=frame_noti,width=100,height=30,text='Home',fg_color="#ffffff",bg_color=None,command=self.voltar_noticia)
        label_voltar_noticia.place(relx=0.17,rely=0.8)
    def voltar_noticia(self): #função para voltar ao menu
        self.janelano_ti.destroy()
        self.segunda()
    def vivizin(self):
        janelavv = tkinter.Tk()
        janelavv.geometry("200x100")
        janelavv.title("vivianny")
        janelavv.iconbitmap(r"C:/vivianny/patas.ico")
        janelavv.resizable(width=False, height=False)
        janelavv.configure(background="#ffffff")
        aviso = customtkinter.CTkLabel(master=janelavv,width=200,height=30,text='Vivianny está ativada',bg_color="#00a8ff")
        aviso.place(relx=0,rely=0)
        comando_voz_usuario()
    def comandos_luna(self):  #janela que vai ter a Assistente
        self.janelaCOM = tkinter.Tk()
        self.janela2.destroy()
        self.janelaCOM.geometry("400x600")
        self.janelaCOM.title("Comandos Vivi")
        self.janelaCOM.iconbitmap(r"C:/vivianny/patas.ico")
        self.janelaCOM.resizable(width=False, height=False)
        self.janelaCOM.configure(background="#ffffff")
        #criação da janela
        button_info_comando = customtkinter.CTkLabel(master=self.janelaCOM,width=400,height=40,text='Comandos da Luna')
        button_info_comando.place(rely=0)
        #label musica
        label_musica = customtkinter.CTkLabel(master=self.janelaCOM,width=250,height=30,text="tocar + 'nome da musica' ",fg_color="#00a8ff")
        label_musica.place(relx=0.2,rely=0.1)
        #label pesquisar
        label_pesquisa = customtkinter.CTkLabel(master=self.janelaCOM,width=250,height=30,text="Procure por + 'o que pesquisar' ",fg_color="#00a8ff")
        label_pesquisa.place(relx=0.2,rely=0.2)
        #label hora
        label_horas = customtkinter.CTkLabel(master=self.janelaCOM,width=250,height=30,text="Horas",fg_color="#00a8ff")
        label_horas.place(relx=0.2,rely=0.3)
        #label dia
        label_dia = customtkinter.CTkLabel(master=self.janelaCOM,width=250,height=30,text="hoje é que dia",fg_color="#00a8ff")
        label_dia.place(relx=0.2,rely=0.4)
        #label piada
        label_piada = customtkinter.CTkLabel(master=self.janelaCOM,width=250,height=30,text="conte uma piada",fg_color="#00a8ff")
        label_piada.place(relx=0.2,rely=0.5)
        #traduzir
        label_traduzir = customtkinter.CTkLabel(master=self.janelaCOM,width=250,height=30,text="Traduzir",fg_color="#00a8ff")
        label_traduzir.place(relx=0.2,rely=0.6)
        #label noticia
        label_noticia = customtkinter.CTkLabel(master=self.janelaCOM,width=250,height=30,text="Noticia",fg_color="#00a8ff")
        label_noticia.place(relx=0.2,rely=0.7)
        #label home
        label_voltar_noticia = customtkinter.CTkButton(master=self.janelaCOM,width=100,height=30,text='Home',fg_color="#00a8ff",bg_color=None,command=self.voltar_comando)
        label_voltar_noticia.place(relx=0.17,rely=0.9)
    def voltar_comando(self): #função para voltar ao menu
        self.janelaCOM.destroy()
        self.segunda()

    def banco_de_dados(self):
        self.janela_banco = tkinter.Tk()
        self.janela2.destroy()
        self.janela_banco.geometry("400x350")
        self.janela_banco.title("Banco de dados")
        self.janela_banco.iconbitmap(r"C:/vivianny/patas.ico")
        self.janela_banco.resizable(width=False,height=False)
        self.janela_banco.configure(background="#ffffff")
        
        frame_salvamento = customtkinter.CTkLabel(master=self.janela_banco, text='Salvamento' ,width=300,height=30,bg_color=None,fg_color="#00a8ff")
        frame_salvamento.place(relx=0.12,rely=0.03)
         #frame do email
        frame_email = customtkinter.CTkFrame(master=self.janela_banco,width=300,height=60,bg_color=None,fg_color='#00a8ff',corner_radius=5)
        frame_email.place(relx=0.12,rely=0.14)
        email_app = customtkinter.CTkLabel(master=frame_email,width=200,height=20,bg_color=None,fg_color=None,text='email,id,tag')
        email_app.place(relx=0.15,rely=0.03)
        self.email_pesssoa = customtkinter.CTkEntry(master=frame_email,width=200,height=25,bg_color=None,corner_radius=10,fg_color="#ffffff")
        self.email_pesssoa.place(relx=0.15,rely=0.4)
        #frame do nome da pessoa
        frame_nome = customtkinter.CTkFrame(master=self.janela_banco,width=300,height=60,bg_color=None,fg_color='#00a8ff',corner_radius=5)
        frame_nome.place(relx=0.12,rely=0.34)
        nome_label = customtkinter.CTkLabel(master=frame_nome,width=200,height=20,bg_color=None,fg_color=None,text='Seu Nome')
        nome_label.place(relx=0.15,rely=0.03)
        self.nome_pessoa = customtkinter.CTkEntry(master=frame_nome,width=200,height=25,bg_color=None,corner_radius=10,fg_color="#ffffff")
        self.nome_pessoa.place(relx=0.15,rely=0.4)
        #frame nome do aplicativo
        frame_aplicativo = customtkinter.CTkFrame(master=self.janela_banco,width=300,height=60,bg_color=None,fg_color='#00a8ff',corner_radius=5)
        frame_aplicativo.place(relx=0.12,rely=0.54)
        label_aplica = customtkinter.CTkLabel(master=frame_aplicativo,width=200,height=20,bg_color=None,fg_color=None,text='Nome do app ou site')
        label_aplica.place(relx=0.15,rely=0.03)
        self.aplicativo = customtkinter.CTkEntry(master=frame_aplicativo,width=200,height=25,bg_color=None,corner_radius=10,fg_color="#ffffff")
        self.aplicativo.place(relx=0.15,rely=0.4)
        #senha 
        frame_senha = customtkinter.CTkFrame(master=self.janela_banco,width=300,height=60,bg_color=None,fg_color='#00a8ff',corner_radius=5)
        frame_senha.place(relx=0.12,rely=0.74)
        label_aplica = customtkinter.CTkLabel(master=frame_senha,width=200,height=20,bg_color=None,fg_color=None,text='Senha usada')
        label_aplica.place(relx=0.15,rely=0.03)
        self.senha_usada = customtkinter.CTkEntry(master=frame_senha,width=200,height=25,show="*",bg_color=None,corner_radius=10,fg_color="#ffffff")
        self.senha_usada.place(relx=0.15,rely=0.4)
        button_salvar = customtkinter.CTkButton(master=self.janela_banco,width=100, text='Salvar',corner_radius=5,height=20,fg_color="#00a8ff",bg_color=None,command=self.salvar)
        button_salvar.place(relx=0.36,rely=0.93)
        button_voltar_db = customtkinter.CTkButton(master=self.janela_banco,width=100, text='Home',corner_radius=5,height=20,fg_color="#00a8ff",bg_color=None,command=self.voltar_banco)
        button_voltar_db.place(relx=0.7,rely=0.93)
    #ligamento ao banco de dados
    def salvar(self):
        try:
            banco = sqlite3.connect('dados_salvamento.db')
            cursor = banco.cursor()
            cursor.execute('''INSERT INTO vivianny (email_id,nome,aplicativo,senha)
                        VALUES (? , ? , ? , ?)''',(self.email_pesssoa.get(),self.nome_pessoa.get(),self.aplicativo.get(),self.senha_usada.get()))
            banco.commit()
            maquina.say('Dados foram salvos')
            maquina.runAndWait()
        except:
            maquina.say("os dados não foram salvos")
            maquina.runAndWait()
    #voltar_bacnco_dados
    def voltar_banco(self):
        self.janela_banco.destroy()
        self.segunda()

def chamando():
    jaanela = interface()
    jaanela.janela1.mainloop()

chamando()