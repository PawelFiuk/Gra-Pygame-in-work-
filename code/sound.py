from pygame import mixer


def main_menu_music():
    #mixer.init()
    mixer.music.load("assets/music/Phonothek_Red_Moon.mp3")
    mixer.music.play(-1)


def stop_main_music():
    mixer.music.stop()


def level_one_first_song():
    pass

def wind_outside_sound():
    wind_sound = mixer.Sound("assets/music/wind-outside-sound-ambient.mp3")
    wind_sound_channel = mixer.Channel(0)
    wind_sound_channel.play(wind_sound, -1)

def shotgun_sound():
    shotgun_soundd = mixer.Sound("assets/music/sound_efects/shotgun_2.mp3")
    shotgun_sound_channel = mixer.Channel(1)
    shotgun_sound_channel.play(shotgun_soundd)

def empty_magazine_sound():
    mixer.music.load("assets/music/sound_efects/empty-gun-shot.mp3")
    mixer.music.play()
