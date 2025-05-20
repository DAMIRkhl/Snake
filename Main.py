import arcade
from arcade import Rect


SQUARE_SCALE = 75
ROW_AMOUNT = 10
COLUMN_AMOUNT = 11
SCREEN_WIDTH = COLUMN_AMOUNT * SQUARE_SCALE
SCREEN_HEIGHT = ROW_AMOUNT * SQUARE_SCALE
SCREEN_TITLE = "My snake"

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.gamecore = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        ]


    def setup(self):
        pass

    def on_draw(self):
        self.clear()
        arcade.draw_rect_filled(Rect(left=0,right=100,bottom=0,top=250,width= 100,height=100,x=0,y=0),color="green")
    def on_update(self, delta_time):
        pass

    def on_key_press(self, key, modifiers):
        pass

    def on_key_release(self, key, modifiers):
        pass



if __name__ == "__main__":
    game = MyGame()
    game.setup()
    arcade.run()


