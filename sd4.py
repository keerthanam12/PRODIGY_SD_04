import tkinter as tk
from tkinter import messagebox

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def create_gui(root):
    root.title("Sudoku Solver")
    
    sudoku_frame = tk.Frame(root)
    sudoku_frame.pack(padx=10, pady=10)
    
    sudoku_board = [[None for _ in range(9)] for _ in range(9)]

    for row in range(9):
        for col in range(9):
            entry = tk.Entry(sudoku_frame, width=2, font=("Helvetica", 16))
            entry.grid(row=row, column=col)
            sudoku_board[row][col] = entry

    solve_button = tk.Button(root, text="Solve Sudoku", command=lambda: solve_puzzle(sudoku_board))
    solve_button.pack(pady=10)

def solve_puzzle(sudoku_board):
    board = [[0 for _ in range(9)] for _ in range(9)]
    
    for row in range(9):
        for col in range(9):
            value = sudoku_board[row][col].get()
            if value.isdigit():
                board[row][col] = int(value)
    
    if solve_sudoku(board):
        for row in range(9):
            for col in range(9):
                sudoku_board[row][col].delete(0, tk.END)
                sudoku_board[row][col].insert(0, str(board[row][col]))
    else:
        messagebox.showerror("Error", "No solution exists for the given puzzle.")

if __name__ == "__main__":
    root = tk.Tk()
    create_gui(root)
    root.mainloop()