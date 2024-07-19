import tkinter as tk
from pynput import mouse

class MouseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Mouse Coordinates")
        self.label = tk.Label(root, text="Mouse Coordinates: ", font=("Helvetica", 16))
        self.label.pack(pady=20)

        # Create a listener for mouse events
        self.listener = mouse.Listener(on_move=self.on_move)
        self.listener.start()

    def on_move(self, x, y):
        coords = f"Mouse Coordinates: (X {x}, Y {y})"
        self.label.config(text=coords)

# Create the main window
root = tk.Tk()
tracker = MouseTracker(root)

# Run the Tkinter event loop
root.mainloop()
