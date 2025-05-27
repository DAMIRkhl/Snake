import arcade
from arcade import Rect


SQUARE_SCALE = 60
ROW_AMOUNT = 11
COLUMN_AMOUNT = 11
SCREEN_WIDTH = COLUMN_AMOUNT * SQUARE_SCALE
SCREEN_HEIGHT = ROW_AMOUNT * SQUARE_SCALE
SCREEN_TITLE = "My snake game"

class SpriteSnake(arcade.Sprite):
    def __init__(self):
        super().__init__("sprite (1).png",scale=0.22,center_x=1*SQUARE_SCALE+SQUARE_SCALE/2,center_y=5*SQUARE_SCALE+SQUARE_SCALE/2)
        self.where_snake_fasing = 2
    def WhereSnakeFasing(self):
        if self.where_snake_fasing == 1:
            self.angle = 90
        if self.where_snake_fasing == 2:
            self.angle = 180
        if self.where_snake_fasing == 3:
            self.angle = -90
        if self.where_snake_fasing == 4:
            self.angle = 0

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
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        ]
        self.snakehead = SpriteSnake()



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

        arcade.draw_sprite(self.snakehead)

    def on_update(self, delta_time):
        pass

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.snakehead.where_snake_fasing = 1
        if key == arcade.key.RIGHT:
            self.snakehead.where_snake_fasing = 2
        if key == arcade.key.DOWN:
            self.snakehead.where_snake_fasing = 3
        if key == arcade.key.LEFT:
            self.snakehead.where_snake_fasing = 4
        self.snakehead.WhereSnakeFasing()
    def on_key_release(self, key, modifiers):
        pass



if __name__ == "__main__":
    game = MyGame()
    game.setup()
    arcade.run()


