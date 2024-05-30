import pygame
from Game_assets.button import load_buttons
from Game_assets.slider import Slider
from Game_assets.music import MusicStorage

music_storage = MusicStorage()

class Setting:
    def __init__(self, display, gamestatemanager):
        self.display = display
        self.gamestatemanager = gamestatemanager
        self.music_storage = music_storage
        self.background_image = pygame.image.load('Game Images/Updated Background.png')
        self.text_font_large = pygame.font.Font("Fonts/SuperSalad-qZgvV.ttf", 90)
        self.text_font_small = pygame.font.Font("Fonts/SuperSalad-qZgvV.ttf", 25)

        self.volume_slider = Slider((450, 200), 250, 30, 0, 1, 0.5)

    def run(self):
        self.display.blit(self.background_image, (0, 0))

        volume = self.volume_slider.get_value()
        pygame.mixer.music.set_volume(volume)

        self.back_button = load_buttons('back')[0]

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if self.back_button.is_clicked(pos):
                    self.gamestatemanager.set_state('start')
                elif self.volume_slider.is_clicked(pos):
                    self.volume_slider.dragging = True
            elif event.type == pygame.MOUSEMOTION:
                if self.volume_slider.dragging:
                    pos = pygame.mouse.get_pos()
                    self.volume_slider.update_value(pos)
            elif event.type == pygame.MOUSEBUTTONUP:
                self.volume_slider.dragging = False

        title = self.text_font_large.render("SETTINGS", True, (225, 225, 225))
        self.display.blit(title, (285, 20))
        title = self.text_font_large.render("MUSIC", True, (225, 225, 225))
        self.display.blit(title, (100, 150))
        title = self.text_font_small.render("MAX", True, (225, 225, 225))
        self.display.blit(title, (710, 198))
        title = self.text_font_small.render("Min", True, (225, 225, 225,))
        self.display.blit(title, (415, 198,))

        handle_image_original = pygame.image.load('Game Images/Name Cat.png')
        handle_image_resized = pygame.transform.scale(handle_image_original, (100,100))
        self.volume_slider.draw(self.display, handle_image_resized)

        self.back_button.draw(self.display)