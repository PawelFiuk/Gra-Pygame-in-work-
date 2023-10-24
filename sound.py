import settings
import pygame
from pygame import mixer


def main_menu_music():
    #mixer.init()
    mixer.music.load("assets/Phonothek_Red_Moon.mp3")
    mixer.music.play(-1)


def stop_main_music():
    mixer.music.stop()


def level_one_first_song():
    pass


def shotgun_sound():
    mixer.music.load("assets/shotgun_2.mp3")
    mixer.music.play()
