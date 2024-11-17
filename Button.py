import pygame

class Button():
    def __init__(self,key:str):
        key_dict = {"1":1}
        self.key=key_dict[key]

    def key_pressed(self):
        return pygame.key.get_pressed()