import settings_file
import pygame
from pygame import mixer


def main_menu_music():
    mixer.music.load("assets/Phonothek_Red_Moon.mp3")
    mixer.music.play(-1)


def stop_main_menu_music():
    mixer.music.stop()


class LevelOneMusic:
    pass


def shotgun_sound():
    pass

