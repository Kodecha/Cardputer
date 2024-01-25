import os
import tkinter as tk
from PIL import Image, ImageTk

class ChessGame(tk.Tk):
    def __init__(self):
        super().__init__()

        # File paths
        self.piece_image_path = os.path.join("assets", "chesspieces.png")
        self.tile_image_path = os.path.join("assets", "chesstile.png")

        # Board configuration
        self.board_size = 15
        self.tile_size = 15
        self.create_board()

        # Piece images
        self.load_piece_images()

        # Game state
        self.current_player = 'white'  # 'white' or 'black'
        self.move_history = []

        # UI setup
        self.create_widgets()

    def create_board(self):
        self.board = [['empty' for _ in range(self.board_size)] for _ in range(self.board_size)]

    def load_piece_images(self):
        piece_image = Image.open(self.piece_image_path)
        self.piece_images = {}
        for i, piece in enumerate(['P', 'K', 'Q', 'B', 'R', 'N']):
            self.piece_images[piece] = ImageTk.PhotoImage(piece_image.crop((i * 15, 0, (i + 1) * 15, 19)))

        self.tile_image = ImageTk.PhotoImage(Image.open(self.tile_image_path))

    def create_widgets(self):
        self.canvas = tk.Canvas(self, width=self.board_size * self.tile_size, height=self.board_size * self.tile_size)
        self.canvas.pack()

        self.draw_board()

        self.bind("<Button-1>", self.on_click)

    def draw_board(self):
        for row in range(self.board_size):
            for col in range(self.board_size):
                color = "#FFF8E7" if (row + col) % 2 == 0 else "#800020"
                self.canvas.create_image(col * self.tile_size + self.tile_size / 2,
                                         row * self.tile_size + self.tile_size / 2, image=self.tile_image)
                self.canvas.create_rectangle(col * self.tile_size, row * self.tile_size,
                                             (col + 1) * self.tile_size, (row + 1) * self.tile_size,
                                             fill=color, outline="")

        for row in range(self.board_size):
            for col in range(self.board_size):
                piece = self.board[row][col]
                if piece != 'empty':
                    image = self.piece_images[piece]
                    self.canvas.create_image(col * self.tile_size + self.tile_size / 2,
                                             row * self.tile_size + self.tile_size / 2, image=image)

    def on_click(self, event):
        row, col = event.y // self.tile_size, event.x // self.tile_size
        piece = self.board[row][col]

        if piece != 'empty' and piece.isupper() == (self.current_player == 'white'):
            # Valid move
            move = input("Enter your move (e.g., Nhf4): ")
            self.make_move(move)

    def make_move(self, move):
        # Placeholder for move processing
        print(f"Move made: {move}")
        self.move_history.append(move)

        # Placeholder for updating the board state
        # You need to implement logic to update the board based on the move.

        # Switch player
        self.current_player = 'white' if self.current_player == 'black' else 'black'

        # Redraw the board
        self.canvas.delete("all")
        self.draw_board()


if __name__ == "__main__":
    chess_game = ChessGame()
    chess_game.mainloop()
