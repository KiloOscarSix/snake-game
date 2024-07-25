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
