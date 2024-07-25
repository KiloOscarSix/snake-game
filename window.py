import tkinter


class Window(tkinter.Tk):
    def __init__(self) -> None:
        super().__init__()

        self.title("Snake")
        self.resizable(False, False)

    def centre(self) -> None:
        window_width: int = self.winfo_width()
        window_height: int = self.winfo_height()

        window_x = int((self.winfo_screenwidth() / 2) - (window_width / 2))
        window_y = int((self.winfo_screenheight() / 2) - (window_height / 2))

        self.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")
