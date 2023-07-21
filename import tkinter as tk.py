import tkinter as tk
import webbrowser

def open_browser():
    url = entry.get()
    print("Navigating to:", url)
    webbrowser.open(url)

def create_gui():
    def on_entry_change(*args):
        # This function is called whenever the user changes the entry text.
        # Print the user input in the command prompt.
        user_input = entry.get()
        print("User entered:", user_input)

    root = tk.Tk()
    root.title("Web Browser")

    label = tk.Label(root, text="Enter a URL:")
    label.pack()

    entry = tk.Entry(root)
    entry.pack()
    entry.bind("<KeyRelease>", on_entry_change)  # Bind the entry to the function

    button = tk.Button(root, text="Navigate", command=open_browser)
    button.pack()

    root.mainloop()

if __name__ == "__main__":
    create_gui()
