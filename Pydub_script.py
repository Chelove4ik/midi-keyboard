from pydub import AudioSegment

AudioSegment.converter = r'C:\Users\Денис\Downloads\ffmpeg-4.1-win64-static\bin\ffmpeg.exe'

#sound1 = AudioSegment.from_file("music/1.wav")
#sound2 = AudioSegment.from_file("music/KYOTO-(SK-16).wav")
#
#combined = sound1.overlay(sound2, 100)
#
#combined = combined.overlay(sound2, 500)
#
#combined.export("combined.wav", format='wav')


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
    combined.export('Save music/Saved file numder {}.wav'.format(num_of_name), format='wav')
