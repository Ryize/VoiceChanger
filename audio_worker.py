from pydub import AudioSegment
import os

class AudioFile:
    def __init__(self, file_name, format):
        self.file_name = file_name
        self.format = format
        self.sound = AudioSegment.from_file(file_name, format=format)

    def code_audio(self):
        return self.__work_with_sound(octaves=-0.419965, rate=9000)

    def encode_audio(self, sound = None):
        return self.__work_with_sound(octaves=0.419965, rate=41000, sound=sound)

    def save(self):
        os.remove(self.file_name)
        self.hipitch_sound.export(self.file_name, format="mp3")

    def __work_with_sound(self, octaves: float, rate: int, sound=None):
        if sound is None:
            sound = AudioSegment.from_file(self.file_name, self.format)

        new_sample_rate = int(sound.frame_rate * (2.0 ** octaves))

        hipitch_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate})
        hipitch_sound = hipitch_sound.set_frame_rate(rate)

        self.hipitch_sound = hipitch_sound

        return hipitch_sound

    @staticmethod
    def decode_to_mp3_from_oga(file_path):

        sound = AudioSegment.from_ogg(file_path)
        sound.export(file_path + '.mp3', format="mp3")