import tkinter as tk
import model



# Create the main window
window = tk.Tk()
window.title("PY Note")
window.geometry("700x700")


note_entry = tk.Text(window)
note_entry.place(x=10,y=10,width=680,height=680)


save_button = tk.Button(window, text="Save Note", command=lambda: model.save_note(note_entry.get("1.0", tk.END)))

save_button.place(x=200, y=640, width=135,height=40)




def show_notes():
    print("Viewing")
    notes = model.view_notes()
    view_window = tk.Toplevel(window)
    view_window.title("View Notes")
    view_text = tk.Text(view_window)
    for note in notes:
        view_text.insert(tk.END, note[1] + "\n")
    view_text.pack()

view_button = tk.Button(window, text="View Notes", command=show_notes)

view_button.place(x=345, y=640, width=135,height=40)

window.mainloop()
