# Voice Changer bot

Telegram-бот для изменения голоса в голосовом сообщении или аудиозаписи, с возможностью возврата зашифрованного голоса к стандартному звучанию. Голос меняется из-за изменения октавы и частоты (при изменении голоса частота уменьшается до 9000).

## Deploy locally:

Клонируйте репозиторий и перейдите в установленную папку:
```
git clone https://github.com/Ryize/voiceChanger.git
cd voiceChanger
```

Установите requirements:
```
pip3 install -r requirements.txt
```

Добавьте свой токен бота в main.py:
```
token = ''
```

Запустите бота:
```
python3 main.py
```

> Технологии, использованные в проекте: Python 3, PyTelegramBotApi, pydub, requests, os.
