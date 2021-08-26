from audio_worker import AudioFile
from file_worker import check_exist_directory, create_directory_with_save_voice

import requests
import os
import telebot

token = os.getenv('TOKEN')

bot = telebot.TeleBot(token)

global user_send_data
user_send_data = []

@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('/help', '/изменитьГолос', '/найтиОригинал')
    bot.send_message(message.chat.id, 'Привет, выбери нужную команду!', reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def bot_messages(message):
    bot.send_message(message.chat.id, 'Чтобы зашифровать своё аудио напиши: /code\nЧто-бы расшировать: /encode')

@bot.message_handler(commands=['изменитьГолос', 'code'])
def bot_messages(message):
    global user_send_data
    bot.send_message(message.chat.id, 'Теперь пришли голосовое сообщение')
    user_send_data.append([message.chat.id, 'code'])

@bot.message_handler(commands=['найтиОригинал', 'decode'])
def bot_messages(message):
    global user_send_data
    bot.send_message(message.chat.id, 'Теперь пришли голосовое сообщение')
    user_send_data.append([message.chat.id, 'encode'])

@bot.message_handler(content_types=["voice", 'audio'])
def bot_messages(message):
    number = 0
    for i in user_send_data:
        if i[0] == message.chat.id:
            try:
                file_info = bot.get_file(message.voice.file_id)
            except:
                file_info = bot.get_file(message.audio.file_id)
            file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(token, file_info.file_path))
            src = file_info.file_path[:6] + 'oga' + file_info.file_path[5:]

            src = src.replace('music', 'voice')

            with open(src, 'wb') as f:
                f.write(file.content)

            if src.count('.mp3'):
                src = src.replace('.mp3', '')
            else:
                AudioFile.decode_to_mp3_from_oga(src)

            audio = AudioFile(src+'.mp3', 'mp3')

            if i[1] == 'code':
                audio.code_audio()
                audio.save()
            elif i[1] == 'encode':
                audio.encode_audio()
                audio.save()
            else:
                return False

            bot.send_voice(message.chat.id, voice=open(src+'.mp3', 'rb'))

            user_send_data.pop(number)
            number += 1
            try:
                os.remove(src)
                os.remove(src+'.mp34')
            except FileNotFoundError as e:
                print("Файл для удаления не найден! ", e)
            except PermissionError as e:
                print("Нет прав для удаления файла! ", e)
        break

if __name__ == '__main__':
    if check_exist_directory() == False:
        create_directory_with_save_voice()
    bot.infinity_polling()
