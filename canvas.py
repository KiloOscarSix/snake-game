import tkinter

from config import COLS, ROWS, TILE_SIZE


class Canvas(tkinter.Canvas):
    def __init__(self, window: tkinter.Tk) -> None:
        super().__init__(
            window,
            bg="black",
            width=TILE_SIZE * ROWS,
            height=TILE_SIZE * COLS,
            borderwidth=0,
            highlightthickness=0,
        )

    def clear(self) -> None:
        self.delete("all")

    def draw(self, game_over: bool, score: int) -> None:
        if game_over:
            self.create_text(
                self.winfo_width() / 2,
                self.winfo_height() / 2,
                font="Arial 20",
                text=f"Game Over: {score}",
                fill="white",
            )
        else:
            self.create_text(
                30, 20, font="Arial 10", text=f"score: {score}", fill="white"
            )
