import requests
import customtkinter as ctk
import json
from PIL import Image





app = ctk.CTk()

with open('webhook.json', 'r') as arquivo:
    dados = json.load(arquivo)

WEBHOOK_URL = [dado['url'] for dado in dados][0]


def enviar_para_discord():

    mensagem = {
    'ICAO Partida:': entry_partida.get(),
    'ICAO Chegada:': entry_chegada.get(),
    'Piloto: ': entry_piloto.get(),
    'Aeronave:': entry_aeronave.get(),
    'Distancia:': entry_dist.get(),
    'Tempo:': entry_time.get(),
    'Rota': entry_rota.get('1.0', 'end'),
    'Volanta:': entry_volanta.get()
    }

    if mensagem['ICAO Chegada:'] == '' or mensagem['ICAO Partida:'] == '' or mensagem['Aeronave:'] == '' or mensagem['Distancia:'] == '' or mensagem['Tempo:'] == '':
        label_erro.configure(text='Insira todos os dados com *')
        app.after(5000, lambda: label_erro.configure(text=""))
    
    else:
        mensagem_format = f'🛫 ICAO PARTIDA: {mensagem["ICAO Partida:"]}\n🛬 ICAO CHEGADA: {mensagem["ICAO Chegada:"]}\n👨‍✈️ COMANDANTE: {mensagem['Piloto: ']}\n💺 AERONAVE: {mensagem["Aeronave:"]}\n🌍 DISTANCIA: {mensagem["Distancia:"]} NM\n🕐 TEMPO: {mensagem["Tempo:"]}\n📋 VOLANTA: {mensagem["Volanta:"]}\n🧭 ROTA: {mensagem["Rota"]}'

        payload = {
            "embeds": [
                {
                    "title": '🛫🛫 Registro de Voos',
                    "description": f"```\n{mensagem_format}\n```",
                    "color": 3447003
                }
            ]
        }
        response = requests.post(WEBHOOK_URL, json=payload)
        if response.status_code != 204:
            label_erro_disc.configure(text='Erro ao enviar ao discord, webhook inexistente ou errado\n verifique no arquivo webhook.json')
            app.after(5000, lambda: label_erro.configure(text=""))
        else:
            label_erro_disc.configure(text='Enviado ao discord com sucesso!', text_color = 'green')
            app.after(5000, lambda: label_erro_disc.configure(text=""))



titulo = 'MSFS 2020'



app.geometry('800x600')
app.resizable(False, False)
app._set_appearance_mode('Light')
app.title('Registro de Voos - Microsoft Flight Simulator')
app.configure(fg_color = '#EDF2EF')
app.iconbitmap('icon.ico')

image = ctk.CTkImage(light_image=Image.open("imagem.png"),dark_image=Image.open("imagem.png"),size=(430, 250))

label_img = ctk.CTkLabel(app, image=image, text='')
label_img.place(x=400, y=15)

label_partida = ctk.CTkLabel(app, text='ICAO Partida:* ', font=('Arial', 16, 'bold'), text_color='black')
label_partida.place(x=20, y=30)

label_chegada = ctk.CTkLabel(app, text='ICAO Chegada:* ', font=('Arial', 16, 'bold'), text_color='black')
label_chegada.place(x=240, y=30)

label_piloto = ctk.CTkLabel(app, text='Comandante: ', font=('Arial', 16, 'bold'), text_color='black')
label_piloto.place(x=20, y=80)

label_aeronave = ctk.CTkLabel(app, text='Aeronave:* ', font=('Arial', 16, 'bold'), text_color='black')
label_aeronave.place(x=20, y=130)

label_dist = ctk.CTkLabel(app, text='Distancia (NM):* ', font=('Arial', 16, 'bold'), text_color='black')
label_dist.place(x=20, y=180)

label_dist_info = ctk.CTkLabel(app, text='Apenas números* ', font=('Arial', 11, 'bold'), text_color='red')
label_dist_info.place(x=380, y=180)

label_time = ctk.CTkLabel(app, text='Tempo:* ', font=('Arial', 16, 'bold'), text_color='black')
label_time.place(x=20, y=230)

label_time_info = ctk.CTkLabel(app, text='Formato 00:00:00* ', font=('Arial', 11, 'bold'), text_color='red')
label_time_info.place(x=330, y=230)

label_volanta = ctk.CTkLabel(app, text='Volanta: ', font=('Arial', 16, 'bold'), text_color='black')
label_volanta.place(x=20, y=280)

label_rota = ctk.CTkLabel(app, text='Rota: ', font=('Arial', 16, 'bold'), text_color='black')
label_rota.place(x=20, y=330)

label_cred_1 = ctk.CTkLabel(app, text='Desenvolvido por: ', font=('Arial', 13, 'bold'), text_color='red', bg_color='transparent')
label_cred_1.place(x=20, y=540)

label_dev = ctk.CTkLabel(app, text='AnonymousBR ', font=('Arial', 13, 'bold'), text_color='teal', bg_color= 'transparent')
label_dev.place(x=20, y=560)
label_dev.lower()

label_erro = ctk.CTkLabel(app, text='', font=('Arial', 13, 'bold'), text_color='red')
label_erro.place(x=500, y=530)

label_erro_disc = ctk.CTkLabel(app, text='', font=('Arial', 13, 'bold'), text_color='red')
label_erro_disc.place(x=450, y=550)

entry_partida = ctk.CTkEntry(app, width=100, text_color='black', fg_color='transparent', font=('Arial', 16, 'bold'), border_width=2, border_color='#B8BDB5')
entry_partida.place(x=132, y=30)

entry_chegada = ctk.CTkEntry(app, width=100, text_color='black', fg_color='transparent', font=('Arial', 16, 'bold'), border_width=2, border_color='#B8BDB5')
entry_chegada.place(x=370, y=30)

entry_piloto = ctk.CTkEntry(app, width=300, text_color='black', fg_color='transparent', font=('Arial', 16, 'bold'), border_width=2, border_color='#B8BDB5')
entry_piloto.place(x=135, y=80)

entry_aeronave = ctk.CTkEntry(app, width=220, text_color='black', fg_color='transparent', font=('Arial', 16, 'bold'), border_width=2, border_color='#B8BDB5')
entry_aeronave.place(x=120, y=130)

entry_dist = ctk.CTkEntry(app, width=220, text_color='black', fg_color='transparent', font=('Arial', 16, 'bold'), border_width=2, border_color='#B8BDB5')
entry_dist.place(x=150, y=180)

entry_time = ctk.CTkEntry(app, width=220, text_color='black', fg_color='transparent', font=('Arial', 16, 'bold'), border_width=2, border_color='#B8BDB5')
entry_time.place(x=100, y=230)

entry_volanta = ctk.CTkEntry(app, width=580, text_color='black', fg_color='transparent', font=('Arial', 16, 'bold'), border_width=2, border_color='#B8BDB5')
entry_volanta.place(x=100, y=280)

entry_rota = ctk.CTkTextbox(app, width=580, height=160, text_color='black', border_color='#B8BDB5', border_width=2, font=('Arial', 16, 'bold'), fg_color='transparent')
entry_rota.place(x=100, y=330)

btn_enviar = ctk.CTkButton(app, width=120, text='Enviar', font=('Arial', 14, 'bold'), text_color='white', fg_color='green', cursor='hand2', command=enviar_para_discord)
btn_enviar.place(x=320, y=550)



app.mainloop()


