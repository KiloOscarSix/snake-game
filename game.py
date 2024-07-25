import tkinter

from canvas import Canvas
from food import Food
from snake import Snake
from window import Window


class Game:
    def __init__(self) -> None:
        self.window = Window()
        self.canvas = Canvas(self.window)

        self.canvas.pack()
        self.window.update()
        self.window.centre()

        self.window.bind("<KeyRelease>", self._on_key_press)

        self.snake = Snake()
        self.food = Food()

        self.score = 0

    @property
    def game_over(self) -> bool:
        if (
            self.snake.x < 0
            or self.snake.x >= self.canvas.winfo_width()
            or self.snake.y < 0
            or self.snake.y >= self.canvas.winfo_height()
        ):
            return True

        if self.snake.has_self_collided():
            return True

        return False

    def _move(self) -> None:
        if self.game_over:
            return

        # Food collision
        if self.snake.x == self.food.x and self.snake.y == self.food.y:
            self.score += 1
            self.snake.grow(self.food.x, self.food.y)
            self.food.create()

        self.snake.move()

    def _draw(self) -> None:
        self._move()

        self.canvas.clear()

        self.food.draw(self.canvas)
        self.snake.draw(self.canvas)

        if self.game_over:
            self.canvas.create_text(
                self.canvas.winfo_width() / 2,
                self.canvas.winfo_height() / 2,
                font="Arial 20",
                text=f"Game Over: {self.score}",
                fill="white",
            )
        else:
            self.canvas.create_text(
                30, 20, font="Arial 10", text=f"score: {self.score}", fill="white"
            )

        self.window.after(100, self._draw)  # 100ms = 1/10 second, 10 frames/second

    def _on_key_press(self, e: "tkinter.Event[tkinter.Misc]") -> None:
        if self.game_over:
            return

        self.snake.on_key_press(e)

    def run(self) -> None:
        self._draw()
        self.window.mainloop()
