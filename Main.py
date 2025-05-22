import arcade
from arcade import Rect


SQUARE_SCALE = 60
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
        for y in range (ROW_AMOUNT):
            for x in range (COLUMN_AMOUNT):
                if (x  % 2 == 0 and y % 2 == 0) or (x % 2 == 1 and y % 2 == 1):
                    arcade.draw_rect_filled(Rect(left=0, right=0, bottom=0, top=0, width= SQUARE_SCALE, height=SQUARE_SCALE,
                                                 x=x * SQUARE_SCALE + SQUARE_SCALE / 2, y=y * SQUARE_SCALE + SQUARE_SCALE / 2), color=(45, 214, 17))
                else:
                    arcade.draw_rect_filled(Rect(left=0, right=0, bottom=0, top=0, width= SQUARE_SCALE, height=SQUARE_SCALE,
                                                 x=x * SQUARE_SCALE + SQUARE_SCALE / 2, y=y * SQUARE_SCALE + SQUARE_SCALE / 2), color=(32, 156, 12))

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


