from pydub import AudioSegment
import os

AudioSegment.converter = r'C:\Users\Денис\Downloads\ffmpeg-4.1-win64-static\bin\ffmpeg.exe'


def start_create_wav(max_time):
    global combined
    sound = AudioSegment.from_wav('music/Empty wav/emp.wav')
    combined = sound + sound
    for i in range(int(max_time) * 3 - 1):
        combined += sound


def sound_all(sound, time):
    global combined
    sound = AudioSegment.from_file(sound)
    combined = combined.overlay(sound, time*1000)


def save_sound(num_of_name):
    global combined
    os.system('mkdir "Save music"')
    combined.export('Save music/Saved file numder {}.wav'.format(num_of_name), format='wav')
