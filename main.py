import tkinter as tk
import model

x_base = 200
button_x_base = 310
window_width = 900
window_height = 900
button_height = 40
pad_left_x = 20
pad_left_y = 10
left_menu_width = 180
button_width=135
button_left_width=170

# Create the main window
window = tk.Tk()
window.title("PY Note")
window.geometry(f"{window_width}x{window_height}")


note_entry = tk.Text(window)
note_entry.place(x=x_base + 10,y=10,width=680,height=window_height-20)


save_button = tk.Button(window, text="Save Note", command=lambda: model.save_note(note_entry.get("1.0", tk.END)))

save_button.place(x=x_base + button_x_base, y = window_height - button_height - 30, width=button_width, height=button_height)




def show_note(note_id):
    print("Viewing")
    print(note_id)
    note = model.view_note(note_id)

    print(note)
    
    view_window = tk.Toplevel(window)
    view_window.title("View Notes")
    view_text = tk.Text(view_window)

    view_text.insert(tk.END, note[0][1] + "\n")

    view_text.pack()




# view_button = tk.Button(window, text="View Notes", command=show_notes)

# view_button.place(x=x_base + button_x_base + 145, y=window_height - button_height - 30, width=button_width,height=button_height)


def show_note_buttons(frame_left):
    print("Adding Left Buttons")
    notes = model.view_notes()
    button_y = button_height + pad_left_y
    for note in notes:
        print(note[0])
        
        view_note_button = tk.Button(frame_left, text=note[1], command=lambda: show_note(note[0]))
        view_note_button.place(x = 0, y = button_y, width = button_left_width, height = button_height)
        button_y += 55



#Add left side label
frame_left = tk.Frame()
label_a = tk.Label(master=frame_left, text="NOTES")
label_a.pack()
frame_left.pack()

frame_left.place(x=pad_left_x, y = pad_left_y, width = left_menu_width, height = window_height-20)

show_note_buttons(frame_left)





window.mainloop()
