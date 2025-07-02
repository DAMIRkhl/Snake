from random import randint
import arcade
from arcade import Rect


SQUARE_SCALE = 30
ROW_AMOUNT = 17
COLUMN_AMOUNT = 17
SCREEN_WIDTH = COLUMN_AMOUNT * SQUARE_SCALE
SCREEN_HEIGHT = ROW_AMOUNT * SQUARE_SCALE
SCREEN_TITLE = "My snake game"
SNAKE_SPEED = 2


class SpriteSnake(arcade.Sprite):
    def __init__(self,cord_x,cord_y):
        super().__init__("sprite (1).png",scale=SQUARE_SCALE/281.25)
        self.cord_x = cord_x
        self.cord_y = cord_y
        self.change_x = SNAKE_SPEED
        self.where_snake_fasing = 2
        self.Spawn()
    def Spawn(self):
        self.center_x = self.cord_x*SQUARE_SCALE+SQUARE_SCALE/2
        self.center_y = self.cord_y*SQUARE_SCALE+SQUARE_SCALE/2



    def WhereSnakeFasing(self):
        if self.where_snake_fasing == 1:
            self.angle = 90
        if self.where_snake_fasing == 2:
            self.angle = 180
        if self.where_snake_fasing == 3:
            self.angle = -90
        if self.where_snake_fasing == 4:
            self.angle = 0
    def SnakeLogic(self):
        self.center_x += self.change_x
        self.center_y += self.change_y


class SpriteApple(arcade.Sprite):
    def __init__(self):
        super().__init__("apple.png",scale=SQUARE_SCALE/1500,center_x=8*SQUARE_SCALE+SQUARE_SCALE/2,center_y=5*SQUARE_SCALE+SQUARE_SCALE/2)
    def respawn(self):

        self.center_x = randint(0,COLUMN_AMOUNT-1)*SQUARE_SCALE+SQUARE_SCALE/2
        self.center_y = randint(0,ROW_AMOUNT-1)*SQUARE_SCALE+SQUARE_SCALE/2


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.Pause = False
        self.stpos_x,self.stpos_y = 1,7
        self.gamecore = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        ]
        self.gamecore[self.stpos_y][self.stpos_x] = 3
        for row in self.gamecore:
            print(row)

        self.snakehead = SpriteSnake(cord_x=self.stpos_x,cord_y=self.stpos_y)
        self.apple = SpriteApple()
        self.wheretoturn = 0


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
        arcade.draw_sprite(self.apple)

    def on_update(self, delta_time):
        if not self.Pause:
            self.snakehead.SnakeLogic()
            if arcade.check_for_collision(self.snakehead,self.apple):
                self.apple.respawn()
            if self.snakehead.right >= SCREEN_WIDTH or self.snakehead.top >= SCREEN_HEIGHT or self.snakehead.left <= 0 or self.snakehead.bottom <= 0:
                self.Pause = True
                print("you lose")
            if self.wheretoturn == 1:
                print('ВОРКАЕМ =))))')
                print('Snake X: ',self.snakehead.center_x, 'Center:', SQUARE_SCALE/2, 'Result', self.snakehead.change_x%SQUARE_SCALE/2)
                if int(self.snakehead.center_x) % SQUARE_SCALE//2 == 0:
                    self.snakehead.change_x = 0
                    self.snakehead.change_y = SNAKE_SPEED
                    self.snakehead.where_snake_fasing = 1
                    self.wheretoturn = 0
            elif self.wheretoturn == 2:
                if int(self.snakehead.center_x) % SQUARE_SCALE//2 == 0:
                    self.snakehead.change_x = 0
                    self.snakehead.change_y = SNAKE_SPEED
                    self.snakehead.where_snake_fasing = 2
                    self.wheretoturn = 0
            elif self.wheretoturn == 3:
                if int(self.snakehead.center_x) % SQUARE_SCALE//2 == 0:
                    self.snakehead.change_x = 0
                    self.snakehead.change_y = SNAKE_SPEED
                    self.snakehead.where_snake_fasing = 3
                    self.wheretoturn = 0
            elif self.wheretoturn == 4:
                if int(self.snakehead.center_x) % SQUARE_SCALE//2 == 0:
                    self.snakehead.change_x = 0
                    self.snakehead.change_y = SNAKE_SPEED
                    self.snakehead.where_snake_fasing = 4
                    self.wheretoturn = 0



    def on_key_press(self, key, modifiers):
        if self.Pause == False:
            if key == arcade.key.UP and self.snakehead.where_snake_fasing != 3:
                self.wheretoturn = 1

            elif key == arcade.key.RIGHT and self.snakehead.where_snake_fasing != 4:
                self.wheretoturn = 2

            elif key == arcade.key.DOWN and self.snakehead.where_snake_fasing != 1:
                self.wheretoturn = 3

            elif key == arcade.key.LEFT and self.snakehead.where_snake_fasing != 2:
                self.wheretoturn = 4


        if key == arcade.key.P:
            self.Pause = True







        self.snakehead.WhereSnakeFasing()



if __name__ == "__main__":
    game = MyGame()
    game.setup()
    arcade.run()


