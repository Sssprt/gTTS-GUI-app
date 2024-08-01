import os
from gtts import gTTS

# Запись .mp3 файла
def record(input_text, filepath):
    tts = gTTS(input_text, lang = 'ru',lang_check=True)
    print('Запись файла начата...')
    tts.save(f'{filepath}')
    print(f'Запись файла завершена\nФайл сохранён в {filepath}')

# Получение текста из .txt файла
def file_read(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        readed_text = file.read()
    return readed_text
