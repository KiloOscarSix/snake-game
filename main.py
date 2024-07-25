import tkinter

from canvas import Canvas
from food import Food
from snake import Snake
from window import Window


window = Window()
canvas = Canvas(window)

canvas.pack()
window.update()
window.centre()

snake = Snake()
food = Food()

game_over = False
score = 0


def on_key_press(e: tkinter.Event[tkinter.Misc]) -> None:
    if game_over:
        return

    snake.on_key_press(e)


def is_game_over(canvas: Canvas, snake: Snake) -> bool:
    if (
        snake.x < 0
        or snake.x >= canvas.winfo_width()
        or snake.y < 0
        or snake.y >= canvas.winfo_height()
    ):
        return True

    if snake.has_self_collision():
        return True

    return False


def move() -> None:
    global game_over, score

    game_over = is_game_over(canvas, snake)
    if game_over:
        return

    # Food collision
    if snake.x == food.x and snake.y == food.y:
        snake.grow(food.x, food.y)
        food.create()
        score += 1

    snake.move()


def draw() -> None:
    move()

    canvas.clear()

    food.draw(canvas)
    snake.draw(canvas)
    canvas.draw(game_over, score)

    window.after(100, draw)  # 100ms = 1/10 second, 10 frames/second


draw()
window.bind("<KeyRelease>", on_key_press)
window.mainloop()
