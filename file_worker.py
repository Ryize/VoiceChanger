import os

def check_exist_directory():
    if os.listdir().count('voice'):
        return True
    return False

def create_directory_with_save_voice():
    os.makedirs('voice/oga/')