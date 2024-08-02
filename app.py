import tkinter
from tkinter import filedialog as FD
import customtkinter as ctk

import recorder as REC
import player as PLAY

# Создание окна
app = ctk.CTk()
app.geometry("350x450")
app.title("gTTS-GUI")

app.minsize(350, 450)
app.maxsize(350, 450)

ctk.set_appearance_mode('dark')
# ctk.set_default_color_theme("green")

# Запись аудио
def record_event():
    filepath_txt = FD.askopenfilename(filetypes=[('Text', '.txt')]) # Получение .txt файла
    t_res_box.configure(text='Файл выбран')
    filepath_mp3 = FD.asksaveasfilename(filetypes=[('Audio', '.mp3')]) # Сохранение .mp3 файла
    t_res_box.configure(text=f'Файл сохранён > {filepath_mp3}.mp3')
    REC.record(REC.file_read(filepath_txt), filepath_mp3, lang)
    print(filepath_txt, filepath_mp3, lang)

# Воспроизведение аудио
def play_event():
    filepath = FD.askopenfilename(filetypes=[('Audio', '.mp3')]) # Получение .mp3 файла
    PLAY.play(filepath)
    print(filepath)

# Кнопка записи аудио
b_rec = ctk.CTkButton(app, 
                      text="Записать .txt файл", 
                      command=record_event, 
                      width=250, height=50, 
                      fg_color='#00522c', 
                      hover_color='#00301a',
                      corner_radius=15, 
                      anchor='center', 
                      font=('', 20))

# Кнопка воспроизведения аудио
b_play = ctk.CTkButton(app, 
                       text='Воспроизв. .mp3 файл', 
                       command=play_event, 
                       width=250, height=50, 
                       fg_color='#00522c', 
                       hover_color='#00301a',
                       corner_radius=15, 
                       anchor='center', 
                       font=('', 20))

res_frame = ctk.CTkScrollableFrame(master=app, width=300, height=100)

t_res_box = ctk.CTkLabel(master=res_frame, text='', fg_color="transparent", font=('', 20))
t_res_box.configure(state='disabled')

t_lang = ctk.CTkLabel(app, text='Язык записи > Русский', fg_color="transparent", font=('', 20))

opt_lang_var = ctk.StringVar(value='ru')

def opt_lang_set(choice):
    if choice == 'ru':
        t_lang.configure(text='Язык записи > Русский')
    if choice == 'en':
        t_lang.configure(text='Язык записи > Английский')

opt_lang = ctk.CTkOptionMenu(app, values=["ru", "en"],
                             fg_color='#00522c',
                             button_color='#00522c',
                             dropdown_hover_color='#00301a',
                             button_hover_color='#00301a',
                             dropdown_fg_color='#00522c',
                             
                             font=('', 20),
                             variable=opt_lang_var,
                             command=opt_lang_set)
lang = opt_lang.get()

opt_lang.pack(pady=10)
b_rec.pack(pady=20)
b_play.pack(pady=0)
t_lang.pack(pady=20)
t_res_box.pack(pady=0)


# Запуск приложения
app.mainloop()