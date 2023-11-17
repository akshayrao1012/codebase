import tkinter as tk
from datetime import datetime

class NotepadApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Special Notepad")

        # Text editor box
        self.text_editor = tk.Text(root, height=10, width=40)
        self.text_editor.pack(pady=10)

        # Button to trigger entry to the bottom box
        enter_button = tk.Button(root, text="Enter", command=self.enter_text)
        enter_button.pack()

        # Bottom box to display entries with timestamps
        self.bottom_box = tk.Listbox(root, height=10, width=40)
        self.bottom_box.pack(pady=10)

        # Bind Enter key to enter_text method
        self.root.bind("<Return>", lambda event: self.enter_text())

    def enter_text(self):
        # Get text from the text editor
        entered_text = self.text_editor.get("1.0", "end-1c").strip()

        if entered_text:
            # Get the current timestamp
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Display entry in the bottom box with timestamp
            entry_with_timestamp = f"{timestamp}: {entered_text}"
            self.bottom_box.insert(tk.END, entry_with_timestamp)

            # Clear the text editor for the next entry
            self.text_editor.delete("1.0", tk.END)

            # Save the entry to a text file
            with open("notepad_entries.txt", "a") as file:
                file.write(entry_with_timestamp + "\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = NotepadApp(root)
    root.mainloop()
