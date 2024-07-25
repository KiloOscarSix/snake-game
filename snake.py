import tkinter
from canvas import Canvas
from config import TILE_SIZE
from tile import Tile


class Snake:
    def __init__(self) -> None:
        self.head = Tile(5 * TILE_SIZE, 5 * TILE_SIZE)
        self.body: list[SnakeBody] = []

        self.vel_x: int = 0
        self.vel_y: int = 0

    @property
    def x(self) -> int:
        return self.head.x

    @property
    def y(self) -> int:
        return self.head.y

    def on_key_press(self, e: tkinter.Event[tkinter.Misc]) -> None:
        if e.keysym == "Up" and self.vel_y != 1:
            self.vel_x = 0
            self.vel_y = -1
        elif e.keysym == "Down" and self.vel_y != -1:
            self.vel_x = 0
            self.vel_y = 1
        elif e.keysym == "Left" and self.vel_x != 1:
            self.vel_x = -1
            self.vel_y = 0
        elif e.keysym == "Right" and self.vel_x != -1:
            self.vel_x = 1
            self.vel_y = 0

    def has_self_collision(self) -> bool:
        for tile in self.body:
            if self.head.x == tile.x and self.head.y == tile.y:
                return True

        return False

    def grow(self, x: int, y: int) -> None:
        self.body.append(SnakeBody(x, y))

    def move(self) -> None:
        for i in reversed(range(len(self.body))):
            tile = self.body[i]
            if i == 0:
                tile.x = self.x
                tile.y = self.y
            else:
                prev_tile = self.body[i - 1]
                tile.x = prev_tile.x
                tile.y = prev_tile.y

        self.head.x += self.vel_x * TILE_SIZE
        self.head.y += self.vel_y * TILE_SIZE

    def draw(self, canvas: Canvas) -> None:
        for tile in [self.head] + self.body:
            canvas.create_rectangle(
                tile.x,
                tile.y,
                tile.x + TILE_SIZE,
                tile.y + TILE_SIZE,
                fill="lime green",
            )


SnakeBody = Tile
