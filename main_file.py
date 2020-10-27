from PIL.Image import FLIP_LEFT_RIGHT
import arcade
import os
import random
import math
from arcade import color
from arcade.texture import load_texture

# constants here
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 800
GAME_SCREEN_TITLE = "Snails Game by ARK and Zia K."
SIZE_OF_GRID= 10
CELL_SIZE = math.ceil(SCREEN_HEIGHT - 200) / SIZE_OF_GRID
MARGIN = 100


# section for defining class

"""
Welcome Screen View Here
"""

class WelcomeView(arcade.View):
    def __init__(self):
        super().__init__()

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
        arcade.draw_lrwh_rectangle_textured(229, 410, MARGIN, MARGIN, start_btn)
        arcade.draw_lrwh_rectangle_textured(500, 415, MARGIN, MARGIN, guide_btn)
        arcade.draw_lrwh_rectangle_textured(350, 210, MARGIN, MARGIN, exit_btn)
    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT:
            if(x >=229 and x <= 329 and y >= 410 and y <= 510):
                # Start of Game View Here
               print("Play Button Pressed")
               start_game = MainGame()
               self.window.show_view(start_game)   
            if( x >= 500 and x <= 600 and y >= 410 and y <= 510):
                # Guide module or View Here
                print("Guide Button Pressed")
            if( x >= 350 and x <= 450 and y >= 210 and y <=310):
                # Exite Module here 
                print(" Button Pressed")
                exit(0)    
# main game class here
class MainGame(arcade.View):
    def __init__(self):
        super().__init__()
        self.gameBoard = [[0]*10]*10
        self.initializeBoard()
        self.row = 0
        self.column = 0
        print(self.gameBoard)

    def on_show(self):
        arcade.set_background_color(arcade.color.ALMOND)
    def initializeBoard(self):
        
        self.gameBoard = [ [0]*10 for _ in range(10)]
        self.gameBoard[0][0] = 1
        self.gameBoard[9][9] = 2
    def initializeGrid(self):
        for i in range(SIZE_OF_GRID+1):
            #x-axis
            arcade.draw_line(MARGIN+CELL_SIZE*i, MARGIN, CELL_SIZE*i+MARGIN, SCREEN_HEIGHT - MARGIN, arcade.color.BUBBLES, 3)
            #y-axis
            arcade.draw_line(MARGIN, MARGIN+CELL_SIZE*i, SCREEN_WIDTH - MARGIN, CELL_SIZE*i+MARGIN, arcade.color.BUBBLES, 3)


    def on_draw(self):
        bkg_game = arcade.load_texture("imgs/gameBKG.png")
        snail_p1 = arcade.load_texture("imgs/snail1.png")
        snail_p2 = arcade.load_texture("imgs/snail2.png")
        splash_p1 = arcade.load_texture("imgs/snail1.png")
        splash_p2 = arcade.load_texture("imgs/snail2.png")
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0,
            SCREEN_WIDTH, SCREEN_HEIGHT ,
            bkg_game
        )
        self.initializeGrid()
        snail_to_draw = arcade.texture
        if ( self.gameBoard[self.row][self.column] == 1):
            snail_to_draw = snail_p1
        elif ( self.gameBoard[self.row][self.column] == 2):
            snail_to_draw = snail_p2
        elif ( self.gameBoard[self.row][self.column] == -1):
            snail_to_draw = splash_p1
        elif ( self.gameBoard[self.row][self.column] == -2):
            snail_to_draw = splash_p2   
        start_x = (self.column * CELL_SIZE) + MARGIN
        start_y = (self.row * CELL_SIZE) + MARGIN       
        arcade.draw_lrwh_rectangle_textured(start_x, start_y, CELL_SIZE, CELL_SIZE, snail_to_draw)
    def find_RowCol(self, x, y):
        self.column = int( (x - MARGIN) / CELL_SIZE )
        self.row = int( (y - MARGIN) // CELL_SIZE )

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        if (button == arcade.MOUSE_BUTTON_LEFT):
            self.find_RowCol(x, y)
            print(self.row, self.column)
            
            

#end of classes section

def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, GAME_SCREEN_TITLE)
    welcome_view = WelcomeView()
    window.show_view(welcome_view)
    arcade.run()


if __name__ == "__main__":
    main()
