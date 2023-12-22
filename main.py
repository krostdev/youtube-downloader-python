import asyncio
from pytube import YouTube
import customtkinter
from tkinter.messagebox import *

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()
app.geometry("650x450")

def iniciarDownload():
    yt_link = ytlink.get()

    if yt_link == "":
        showerror(
            title="Insira um link",
            message="Para baixar um video você deve colocar o link no input!"
        )
    else:
        try:
            yt_initializer = YouTube(yt_link, on_progress_callback=progresso, on_complete_callback=completado)
            video = yt_initializer.streams.get_highest_resolution()
            video.download()

            text.configure(text=f"{yt_initializer.title}")

        except:
            showerror(
                title="URL Invalida",
                message="Esta URL não é valida!"
            )

def progresso(stream, chunk, remaing):
    total = stream.filesize
    baixados = total - remaing
    completados = baixados / total * 100
    msgTotal = int(completados)

    span.configure(text=f"{msgTotal}% Baixados")

def completado(stream, chunk):
    showinfo(
        title="Completo",
        message="O video foi salvo na mesma pasta do arquivo!"
    )

text = customtkinter.CTkLabel(app, text="Youtube Downloader com Python", font=("Open Sans", 13))
text.pack(padx=10, pady=10)

ytlink = customtkinter.CTkEntry(app, placeholder_text="Link Do Video", font=("Helvetica", 13), width=300)
ytlink.pack(padx=10, pady=10)

span = customtkinter.CTkLabel(app, text="", font=("Comic Sans", 15))
span.pack(pady=5)

btn_download = customtkinter.CTkButton(app, text="Baixar", command=iniciarDownload).pack(pady=5)

author_label = customtkinter.CTkLabel(app, text="Criado por @krostport | BackEnd Developer", font=("Helvetica", 14)).pack(pady=160)

app.mainloop()