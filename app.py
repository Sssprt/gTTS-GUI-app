import tkinter
from tkinter import filedialog as FD
import customtkinter as ctk

import recorder as REC
import player as PLAY

# Создание окна
app = ctk.CTk()
app.geometry("350x450")
app.title("gTTS-GUI")
ctk.set_appearance_mode('dark')

# Запись аудио
def record_event():
    filepath_txt = FD.askopenfilename(filetypes=[('Text', '.txt')]) # Получение .txt файла
    filepath_mp3 = FD.asksaveasfilename(filetypes=[('Audio', '.mp3')]) # Сохранение .mp3 файла
    REC.record(REC.file_read(filepath_txt), filepath_mp3)
    print(filepath_txt, filepath_mp3)
    
# Воспроизведение аудио
def play_event():
    filepath = FD.askopenfilename(filetypes=[('Audio', '.mp3')]) # Получение .mp3 файла
    PLAY.play(filepath)
    print(filepath)

# Кнопка записи аудио
b_rec = ctk.CTkButton(app, 
                      text="Record .txt file", 
                      command=record_event, 
                      width=150, height=50, 
                      fg_color='green', 
                      corner_radius=15, 
                      anchor='center', 
                      font=('', 15))

# Кнопка воспроизведения аудио
b_play = ctk.CTkButton(app, 
                       text='Play .mp3 file', 
                       command=play_event, 
                       width=150, height=50, 
                       fg_color='green', 
                       corner_radius=15, 
                       anchor='center', 
                       font=('', 15))

b_rec.pack(pady=10)
b_play.pack(pady=10)


# Запуск приложения
app.mainloop()