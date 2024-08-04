import tkinter
from tkinter import filedialog as FD
import customtkinter as ctk

import recorder as REC
import player as PLAY

# Создание окна
app = ctk.CTk()
app.geometry("380x480") # Размер окна
app.title("gTTS-GUI")

# Размеры
app.minsize(380, 480) # Минимальный размер окна
app.maxsize(380, 480) # Максимальный размер окна

# Цвета
ctk.set_appearance_mode('dark') # Тема приложения
ctk.set_default_color_theme("green") # Цветовая тема

# 
# Переменные
# 

opt_lang_var = ctk.StringVar(value='ru') # Язык записи
lang = opt_lang_var.get()
txtpath_tk = tkinter.StringVar() # Путь файла для записи TKinter
savepath_tk = tkinter.StringVar() # Путь записи TKinter
savename_tk = tkinter.StringVar() # Имя записи TKinter
filepath_txt: str # Путь файла для записи
savepath: str # Путь записи
savename: str # Имя записи

# 
# Функции
# 

# Запись аудио
def txt_file_event():
    global filepath_txt 
    filepath_txt = FD.askopenfilename(filetypes=[('Text', '.txt')]) # Получение .txt файла
    txtpath_tk.set(value=filepath_txt)
    print(filepath_txt)

# Получение пути сохранения
def file_save_path_event():
    global savepath
    savepath = FD.askdirectory()
    savepath_tk.set(value=savepath)
    print(savepath)

# Воспроизведение аудио
def play_event():
    filepath = FD.askopenfilename(filetypes=[('Audio', '.mp3')]) # Получение .mp3 файла
    PLAY.play(filepath)
    print(filepath)

# Запись аудиофайла
def file_record_event():
    global savename
    savename = savename_tk.get()
    REC.record(REC.file_read(filepath=filepath_txt), filepath=savepath, savename=savename, lang = lang)

# Установка языка записи
def opt_lang_set(choice):
    global lang
    if choice == 'ru':
        lang = 'ru'
    if choice == 'en':
        lang = 'en'
    print(choice)

# 
# Элементы
# 

app_tab = ctk.CTkTabview(master=app)
app_tab.pack(padx=20, pady=20)

# Вкладки
app_tab.add("Настройки")
app_tab.add("Запись")
app_tab.add("Воспроизведение")
app_tab.set("Запись")

# 
# Вкладка настроек
# 

# Фрейм настроек языка
lang_set_frame = ctk.CTkFrame(master=app_tab.tab("Настройки"))
lang_set_frame.pack(pady=10)

# Выбор языка
opt_lang = ctk.CTkOptionMenu(master=lang_set_frame, 
                             values=["ru", "en"],
                             width=50, height=30, 
                             corner_radius=15,
                             dropdown_font=('Montserrat bold', 15),
                             font=('Montserrat bold', 15),
                             variable=opt_lang_var,
                             command=opt_lang_set)
opt_lang.grid(row=1, column=1, padx=5)

# 
# Вкладка записи
# 

# Прокручиваемяй фрейм записи
record_scroll_frame = ctk.CTkScrollableFrame(app_tab.tab("Запись"), width=360, height=400)
record_scroll_frame.pack()

# Разделитель - Фрейм выбора txt файла
label_file_path = ctk.CTkLabel(master=record_scroll_frame,
                               text='Выберите .txt файл',
                               font=('Montserrat bold', 10),
                               anchor='center')
label_file_path.pack(pady=5, padx=10)

# Фрейм выбора txt файла
file_txt_frame = ctk.CTkFrame(master=record_scroll_frame)
file_txt_frame.pack(pady=10)

# Поле ввода пути файла для записи
txt_file_entry = ctk.CTkEntry(master=file_txt_frame, 
                               placeholder_text="",
                               width=190, height=50,
                               font=('Montserrat bold', 15),
                               textvariable=txtpath_tk)
txt_file_entry.grid(row=0, column=0, padx=10)

# Кнопка выбора файла для записи
b_txt_file_select = ctk.CTkButton(master=file_txt_frame,
                            text='Выбрать',
                            width=50, height=50,
                            font=('Montserrat bold', 15),
                            command=txt_file_event)
b_txt_file_select.grid(row=0, column=1)


# Разделитель - Фрейм выбора пути сохранения
label_file_path = ctk.CTkLabel(master=record_scroll_frame,
                               text='Выберите путь сохранения',
                               font=('Montserrat bold', 10),
                               anchor='center')
label_file_path.pack(pady=5, padx=10)

# Фрейм выбора пути сохранения
file_path_frame = ctk.CTkFrame(master=record_scroll_frame)
file_path_frame.pack(pady=5)

# Поле ввода пути для сохранения записи
file_path_entry = ctk.CTkEntry(master=file_path_frame, 
                               placeholder_text="",
                               width=190, height=50,
                               font=('Montserrat bold', 15),
                               textvariable=savepath_tk)
file_path_entry.grid(row=1, column=0, padx=10)

# Кнопка выбора файла для сохранения записи
b_file_select = ctk.CTkButton(master=file_path_frame,
                            text='Выбрать',
                            width=50, height=50,
                            font=('Montserrat bold', 15),
                            command=file_save_path_event)
b_file_select.grid(row=1, column=1)


# Разделитель - Фрейм выбора названия
label_file_name = ctk.CTkLabel(master=record_scroll_frame,
                               text='Выберите название',
                               font=('Montserrat bold', 10),
                               anchor='center')
label_file_name.pack(pady=5, padx=10)

# Фрейм выбора названия
file_name_frame = ctk.CTkFrame(master=record_scroll_frame)
file_name_frame.pack(pady=5)

# Поле ввода имени записи
file_name_entry = ctk.CTkEntry(master=file_name_frame, 
                               placeholder_text="",
                               width=285, height=50,
                               font=('Montserrat bold', 15),
                               textvariable=savename_tk)
file_name_entry.grid(row=1, column=0, padx=10)



# Фрейм записи
file_record_frame = ctk.CTkFrame(master=record_scroll_frame)
file_record_frame.pack(pady=10)

# Кнопка для записи файла
b_file_record = ctk.CTkButton(master=file_record_frame, 
                           text="Записать", 
                           command=file_record_event, 
                           width=285, height=50,
                           anchor='center', 
                           font=('Montserrat bold', 20))
b_file_record.grid(row=0, column=0, padx=10)

# 
# Вкладка воспроизведения
# 

# Кнопка воспроизведения аудио
b_play = ctk.CTkButton(master=app_tab.tab("Воспроизведение"), 
                       text='Воспроизв. .mp3', 
                       command=play_event, 
                       width=230, height=50, 
                       corner_radius=15, 
                       anchor='center', 
                       font=('Montserrat bold', 20))
b_play.pack()

# Запуск приложения
app.mainloop()