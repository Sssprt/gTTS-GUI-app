import os
from gtts import gTTS

# Запись .mp3 файла
def record(input_text, filepath, savename, lang):
    tts = gTTS(input_text, lang = lang, lang_check=True)
    tts.save(f'{filepath}/{savename}.mp3')

# Получение текста из .txt файла
def file_read(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        readed_text = file.read()
    return readed_text
