from PIL.Image import FLIP_LEFT_RIGHT
import arcade
import os
import random
from arcade import color
import arcade.gui
import arcade.application
from arcade.gui import UIManager


# constants here
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 800
GAME_SCREEN_TITLE = "Snails Game by ARK and Zia K."




# section for defining class




"""
Welcome Screen View Here
"""

class WelcomeView(arcade.View):
    def __init__(self):
        super().__init__()
        self.ui_manager = UIManager()

    def on_show(self):
        play_btn = arcade.load_texture("imgs/playBTN.png")
        arcade.set_background_color(arcade.color.ALABAMA_CRIMSON)
    def on_draw(self):
        play_btn = arcade.load_texture("imgs/playBTN.png")
        wlcm_scr_bkgd = arcade.load_texture("imgs/welcome.jpg")
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(
        0, 0, SCREEN_WIDTH, SCREEN_HEIGHT,
        wlcm_scr_bkgd
        )
        arcade.draw_lrwh_rectangle_textured(
            326, 320,
            130, 130,
            play_btn
        )
        arcade.draw_text(
            "Pic Credits: stream.com/",
            0, 790, color=arcade.color.BLACK,
            font_size=9, bold="true",
        )
    # def setup(self):
    #     """ setup window """
    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT:
            if ( x > 326 and x < 456 and y > 320 and y < 450 ):
                welcome_done = InstructionWindow()
                self.window.show_view(welcome_done) 


class InstructionWindow(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.ALMOND)
    def on_draw(self):
        instr_bkg = arcade.load_texture("imgs/instrSCR.png")
        start_btn = arcade.load_texture("imgs/startBTN.png")
        exit_btn = arcade.load_texture("imgs/exitBTN.png")
        guide_btn = arcade.load_texture("imgs/guideBTN.png")
        welcomePNG = arcade.load_texture("imgs/welcome_PNG86.png")
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0,
        SCREEN_HEIGHT, SCREEN_WIDTH, 
        instr_bkg
        )
        # welcome text
        """arcade.draw_text(
            "Welcome to Snails Game",
            start_x=210, start_y=649,
            color=arcade.color.WHITE,
            font_size=20, font_name='Chilanka',
            bold='TRUE'
        )"""
        arcade.draw_lrwh_rectangle_textured(160, 580, 500, 200, welcomePNG)
        arcade.draw_lrwh_rectangle_textured(229, 410, 100, 100, start_btn)
        arcade.draw_lrwh_rectangle_textured(500, 415, 100, 100, guide_btn)
        arcade.draw_lrwh_rectangle_textured(350, 210, 100, 100, exit_btn)


    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT:
            if(x >=229 and x <= 329 and y >= 410 and y <= 510):
                # Start of Game View Here
               print("Play Button Pressed")   
            if( x >= 500 and x <= 600 and y >= 410 and y <= 510):
                # Guide module or View Here
                print("Guide Button Pressed")
            if( x >= 350 and x <= 450 and y >= 210 and y <=310):
                # Exite Module here 
                print(" Button Pressed")
                exit(0)    


#end of classes section

def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, GAME_SCREEN_TITLE)
    welcome_view = WelcomeView()
    window.show_view(welcome_view)
    arcade.run()


if __name__ == "__main__":
    main()
