# Voice Changer bot

Telegram bot for changing the voice in a voice message or audio recording, with the ability to return the encrypted voice to the standard sound. The voice changes due to changes in the octave and frequency(When the voice changes, the frequency decreases to 9000).

## Deploy locally:

Clone the repository
```
git clone https://github.com/Ryize/voiceChanger.git
```

Install requirements
```
pip3 install -r requirements.txt
```

Add your bot token here in main.py
```
token = ''
```

Run the bot
```
python3 main.py
```

> Technologies used in the project: Python 3, PyTelegramBotApi, pydub, requests, os.
